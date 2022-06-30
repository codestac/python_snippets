#lambda code for s3 to postgres, csv to json

import json
import psycopg2
import boto3
import json
import csv
import uuid
import psycopg2.extras
import logging
import copy

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

db_host = "lambdatopg.cowliydpbvqq.us-east-1.rds.amazonaws.com"
db_port = 5432
db_name = "postgres"
db_pwd = "postgres"
#s3 bucket location
s3_bucket_name = "copy_files_bucket" 
upload_folder_name = 'upload/'
file_extension = '.csv'

def load_data_to_rds(conn):
  file_list = list_of_files_in_s3()
  for file in file_list:
    query = None
    s3_data = fetch_from_s3(s3_bucket_name, file)
    s3_data_list = list(s3_data)
    header_data = s3_data_list[:1]
    column_len = len(header_data[0])
    list_of_headers = ",".join(header_data[0])
    #converting into list of tuples
    row_data = s3_data_list[1:]
    list_of_tuples = map(tuple, row_data)
    table_name = remove_suffix(file, file_extension)
    create_table(conn, table_name, header_data[0])
    str_template = create_template(column_len)
    final_str_template = '('+str_template + ')'
    try:
      cursor = conn.cursor()
      bulk_insert_query = 'INSERT iNTO {table} ({fields}) VALUES %s'.format(table=table_name, fields = list_of_headers)
      psycopg2.extras.execute_values (cursor, bulk_insert_query, list_of_tuples, template= final_str_template, page_size = 200)
      conn.commit()
      print('data loaded completed for table')
    except Exception as err:
      print(err)
      print('Cannot insert  data in table:', table_name)
      
def create_template(column_len):
  add_str = '%s'
  template_list = []
  for x in range(column_len):
    template_list.append(add_str)
  template = ",".join(template_list)
  return template

def create_table(conn, table_name, headers):
   try: 
      suffix_str = 'VARCHAR (0) NOT nULL'
      header_w_suffix = [col + suffix_str for col in headers]
      table_col_list = ",".join(header_w_suffix)
      create_table_query = 'CREATE TABLE IF NOT EXISTS {table} ({cols})'.format(table= table_name, cols=table_col_list)
      print("create table qery: ", create_table_query)
      curs = conn.cursors()
      curs.execute(create_table_query)
      conn.commit()
      print("table create: ", table_name)
   except:
      print("Cannot create table")

def fetch_from_s3(bucket, key):
   try:
      s3_object = s3_client.get_object(Bucket=bucket, Key=(upload_folder_name+key))
      csv_content = s3_object['body'].read().decode("utf-8").splitlines()
      csv_data = csv.reader(csv_content)
      return csv_data
    except:
      print("Cannot connect to s3 bucket")
      
def create_record(obj, fields):
  #adding table columns names with table column value   ```
  mappings = dict(zip(fields, obj))
  return mappings

def format_month_val(val):
  return (str(val)[1:-1])

def fetch_data_from_rds(conn, event):
  table = None
  month_val = None
  formatted_month = None
  result = []
  is_where_condition_exists(event)
  if is_key_exists(event["queryStringParameters"], 'table'):
    table = event['queryStringParameters']['table']
    if(len(is_where_condition_exists(event))):
      query = 'select * from {table} WHERE {condition}'.format(table=table, condition = is_where_condition_exists(event))
    else: query = 'select * from "{}"'.format(table)
    print(query)
    cursor= conn.cursor()
    cursor.execute(query)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    for line in rows:
      result.append(create_record(line, column_names))
      return format_return_data(result)
    
    else: return format_return_data('tableparameter is missing in request')

def create_connection():
  conn = None
  try:
    conn = psycopg2.connect("dbname = {} user={} host={} password={}".format(db_name, db_user, db_host, db_pwd))
  except Exception as err:
    logger.error("DB connection failed", err)
  return conn

def close_connection(conn):
  logger.info("DB connection closed")
  conn.close()

def format_return_data(data):
  return {
    'statusCode': 200,
    'headers': {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json'
    },
      'body': json.dumps(data)
  }

def list_of_files_in_s3():
  files = []
  response = s3_client.list_objects_v2(Bucket = s3_bucket_name, Prefix = upload_folder_name, Delimiter = '/')
  for content in response.get('Contents', []):
    if (content['Key'] != upload_folder_name):
      files.append(remove_prefix(content['Key'], upload_folder_name))

  print(files)
  return files

def remove_prefix(text, prefix):
  if text.startswith(prefix):
    return text[len(prefix):]
  return text

def remove_suffix(text, suffix):
  if text.endswith(suffix):
    return text[:-len(suffix)]
  return text

def is_key_exists(event, key):
  if key in event and event[Key] != None:
    return True
  else: return False

def is_where_condition_exists(event):
  request_parameters = copy.copy(event["queryStringParameters"])
  if 'upload' in request_parameters :
    del request_parameters['upload']
  if 'table' in request_parameters:
    del request_parameters['table']
  if(len(request_parameters)):
    return get_where_statement(request_parameters)
  else: return

def get_where_statement(req_obj):
  where_statement = ''
  for index, (key, value) in enumerate(req_obj.items()):
    where_statement = where_statement + key + 'IN' + '(' + (",".join(repr(e) for e in value.split(','))) + ')'
    if (index + 1 != len(req_obj)):
      where_statement = where_statement + "AND"
    return where_statement

def lambda_handler(event,context):
  #crate db connection
  conn = create_connection()

  #check request queryStringParameters have upload key as is it set to True
  if (is_key_exists(event["queryStringParameters"], 'upload') and event["queryStringParameters"]["upload"] == 'True') :
    load_data_to_rds(conn)
    result = format_return_data('Data uploaded successfully')

  else:
    #fetch data from postgres RDS if upload KEY is not available in request or set to flase
    result = fetch_data_from_rds(conn, event) 

    #close db connection
    close_connection(conn)
    list_of_files_in_s3()
    #return result in response
    return result


# Test JSON format
# {
#     "queryStringParameters": {
#       "upload": "False",
#       "table": "period",
#       "month": "2019-11"    
#     }
# }

# tabke=journeydata&period=2019-11&state=All&col=100
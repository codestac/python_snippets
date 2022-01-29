#first half of the string
def first_half(str):
    return str[0:len(str) / 2]


# return the string without first and last character
def without_end(str):
    return str[1:-1]


#combo of small and large string (hello, hi) => hiHellohi
def combo_string(a, b):
    return a + b + a if len(a) < len(b) else b + a + b


#return their concatenation, except omit the first char of each. The strings will be at least length 1.
def non_start(a, b):
    return a[1:] + b[1:]


#rotated left 2 Hello => lloHe
def left2(str):
    return str[2:] + str[:2]


# We have two monkeys, a and b, and the parameters a_smile and b_smile
# indicate if each is smiling. We are in trouble if they are both smiling
# or if neither of them is smiling. Return True if we are in trouble.


def monkey_trouble(a_smile, b_smile):
    return (a_smile == b_smile)


# remove the character in the nth position
def missing_char(str, n):
    front = str[:n]
    back = str[n + 1:]
    return front + back


# or we can just write
# return str[:n] + str[n+1:]


# if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


# the number of the positions where they contain the
# same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3
def string_match(a, b):
    count = 0
    for i in range(len(a) - 1):
        a_sub = a[i:i + 2]
        b_sub = b[i:i + 2]
        if a_sub == b_sub:
            count = count + 1
    return count


# reverse an array
def reverse3(nums):
    return nums[::-1]


def sort_check(a):
    b = sorted(a)
    print(b)
    print(a)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                return True
    return False


print(sort_check(['B', 'aa', 'ab', 'aa', 'b']))
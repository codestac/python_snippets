class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items(len(self.items) - 1)
    
    def size(self):
        return len(self.item)


# check for matching parentheses
import Stack # importing stack class
# sample balanced ()  - ()()((()))
def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        elif s.is_empty():
                balanced = False
        else:
            s.pop()
        
        index += 1
        
if balanced and s.is_empty():
    return True
else:
    return False

# checker for all kinds of braces (){}[]()
def checker(given_string):
    s = stack()
    balanced = True
    index = 0
    while index < len(given_string) and balanced:
        symbol = given_string[index]
        if symbol in "({[":
            s.push(symbol)
        elif s.is_empty():
            balanced = False
        else:
            top = s.pop()
            if not matches(top, symbol):
                balanced = False
        index += 1
        
    if balanced and s_is_empty():
        return True
    else:
        return False
    
def match(open, close):
    opens = "([{"
	closes = ")]}"
	return opens.index(open) == closes.index(close)
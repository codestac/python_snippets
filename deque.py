# deque implementation
class Deque:
    def __init__(self):
        self.itmes = []
        
    def is_empty(self):
        return self.items = []
    
    def add_front(self, item):
        self.items.append(item)
        
    def add_rear(self, item):
		self.items.insert(0,item)
	
 	def remove_front(self):
		return self.items.pop()
	
 	def remove_rear(self):
		return self.items.pop(0)
	
 	def size(self):
		return len(self.items)

# check string for palindrome
import Deque

def pal_check(a_string):
    char_deque = Deque()
    
    for ch in a_string:
        char_deque.add_rear(ch)
    
    still_equal = True
    
    while char_deque.size() > 1 and still_qual:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != rear:
            still_equal = False
        
    return still_equal
        
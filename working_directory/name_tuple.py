from collections import namedtuple

#DEFAULT PARAMETERS EXAM
Color = namedtuple('Color', ['r', 'g', 'b', 'a'])
Color.__new__.__defaults__ = (0.0, 0.0, 0.0, 1.0)

RED = Color(r=1.0)
GREEN = Color(g=1.0)
BLUE = Color(b=1.0)
BLACK = Color() 
print(RED,GREEN,BLACK)


import collections

#EXAM
def namedtuple_with_defaults(typename, fields_dict):
    T = collections.namedtuple(typename, ' '.join(fields_dict.keys()))
    T.__new__.__defaults__ = tuple(fields_dict.values())
    return T

fields = {'val': 1, 'left': 2, 'right':3}
Node = namedtuple_with_defaults('Node', fields)
# Node()       --> Node(val=1, left=2, right=3)
# Node(4,5,6)  --> Node(val=4, left=5, right=6)
# Node(val=10) --> Node(val=10, left=2, right=3)

#EXAM2
Row = collections.namedtuple("Row", ["a", "b"])   
row = Row(a=1,b=2) #Make a namedtuple from the Row class we created
print(row)    #Prints: Row(a=1, b=2)
print(row.a)  #Prints: 1
print(row[0]) #Prints: 1
row = Row._make([2, 3]) #Make a namedtuple from a list of values
print(row)   #Prints: Row(a=2, b=3)

from typing import NamedTuple

class Nodes(NamedTuple):
    val: None
    left: 'Node' = None
    right: 'Node' = None
  
print(Nodes(1)) # Node(val=1, left=None, right=None)
n = Node(1)
print(Node(2, left=n))
# Node(val=2, left=Node(val=1, left=2, right=3), right=3)
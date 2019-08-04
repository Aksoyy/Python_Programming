from collections import namedtuple

NodeT = namedtuple('Node', 'val left right')
def Node(val, left=None, right=None):
  return NodeT(val, left, right)

Color = namedtuple('Color', ['r', 'g', 'b', 'a'])
Color.__new__.__defaults__ = (0.0, 0.0, 0.0, 1.0)
# Default RGBA values for black

RED = Color(r=1.0)
GREEN = Color(g=1.0)
BLUE = Color(b=1.0)
BLACK = Color()
print(RED)
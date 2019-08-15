from collections import namedtuple

# New Style
fields = ('one', 'two', 'three')
Node1 = namedtuple('Node1', fields, defaults=(None,) * len(fields))
print(Node1())

Node2 = namedtuple('Node2', 'one two three', defaults=(1,2,3))
print(Node2())
print('------------------')


# Old Style
Node3 = namedtuple('Node3', 'one two three')
Node3.__new__.__defaults__ = (None,) * len(Node3._fields)
print(Node3())

Node4 = namedtuple('Node4', 'one two three')
Node4.__new__.__defaults__ = (1,2,3)
print(Node4())
print('------------------')


# Namedtuples ignore extra parameters
class Person(namedtuple('base', 'name age')):
    __slots__ = ()
    def __new__(cls, *args, **kwargs):
        for key in tuple(kwargs):
            if key not in cls._fields:
                del kwargs[key]
        return super().__new__(cls, *args, **kwargs)


# person1 = Person(name='joe', age=25, company='Met', phone=5551231212)
# print(person1)
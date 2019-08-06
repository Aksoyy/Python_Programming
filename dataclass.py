from dataclasses import dataclass

dict2 = {
    "name":"Hakan",
    "age":22,
    "height":174,
    "color":"dark blue",
    "hobby":"table tennis",
    "number":42
    }

@dataclass
class InventoryItem:
    name: str
    age: int
    height: int = 0

    def __init__(self, **kwargs):
        self.name = dict2["name"]
        self.age = dict2["age"]
        self.height = dict2["height"]
    
    #def __init__(self, name: str, age: int, height: int=0):
    #     self.name = name
    #     self.age = age
    #     self.height = height

test = InventoryItem(**dict2)
print(test)
print(dict2)





# TEST DATACLASS
# @dataclass
# class Position:
#     name: str
#     lon: float = 0.0
#     lat: float = 0.0

# Position('Null Island') --> Position(name='Null Island', lon=0.0, lat=0.0)
# Position('Greenwich',lat=51.8) -> Position(name='Greenwich',lon=0.0,lat=51.8)
# Position('Vancouver',-1.1,4.3)->Position(name='Vancouver', lon=-1.1, lat=4.3)
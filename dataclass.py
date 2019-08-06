from dataclasses import dataclass

dict2 = {
    "name":"Hakan",
    "age":22,
    "height":174,
    #"color":"dark blue",
    # "hobby":"table tennis",
    # "number":42
    }

@dataclass
class InventoryItem:
    name: str
    age: int
    height: int = 0

    def name_test(self):
        if len(self.name)<6:
            print("Eksik kelime")
    
    def control(self):
        if(self.age>18 and self.height>170):
            print("Yeterli")
        elif(self.name!="Hakan"):
            print("Yanlis kelime")
        else: pass
    
    
test = InventoryItem(**dict2)
print(test)
print(dict2)
test.name_test()
test.control()

# TEST DATACLASS
# @dataclass
# class Position:
#     name: str
#     lon: float = 0.0
#     lat: float = 0.0

# Position('Null Island') --> Position(name='Null Island', lon=0.0, lat=0.0)
# Position('Greenwich',lat=51.8) -> Position(name='Greenwich',lon=0.0,lat=51.8)
# Position('Vancouver',-1.1,4.3)->Position(name='Vancouver', lon=-1.1, lat=4.3)
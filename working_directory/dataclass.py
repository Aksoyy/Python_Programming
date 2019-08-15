from dataclasses import dataclass

dict2 = {
    "name":"Hakan",
    "lastname":"Aksoy",
    "age":22,
    "height":174,
    "color":"dark blue",
    "hobby":"table tennis",
    "number":42
    }

@dataclass
class InventoryItem:
    name: str = "test"
    lastname: str = "test2"
    age: int = 18
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

liste = ["name","lastname","age","height"]
def control2(liste,**dict_key) -> dict:
    search_list = dict_key.keys()
    my_list = {}
    for item in search_list:
        if item in liste:
            # Data append in dictionary
            my_list[item]=dict_key[item]
    return my_list
            
# control2(liste,**dict2)

test = InventoryItem(**control2(liste,**dict2))
print(test)
print(dict2)
# test.name_test()
# test.control()

# TEST DATACLASS
# @dataclass
# class Position:
#     name: str
#     lon: float = 0.0
#     lat: float = 0.0

# Position('Null Island') --> Position(name='Null Island', lon=0.0, lat=0.0)
# Position('Greenwich',lat=51.8) -> Position(name='Greenwich',lon=0.0,lat=51.8)
# Position('Vancouver',-1.1,4.3)->Position(name='Vancouver', lon=-1.1, lat=4.3)
import requests
from typing import Callable, Generator

def error_handler(func: Callable) -> Callable:
   def wrapper(*args, **kwargs) -> dict:
       results=None
       response = func(*args, **kwargs)
       if response.ok:
           response = response.json()
           results = response.get('results')
       return results
   return wrapper
def converter(func:Callable) -> Callable:
   def wrapper(*args, **kwargs) -> dict:
       response = func(*args, **kwargs)
       return list(response)
   return wrapper

class RequestData:
   """
       RequestData
   """
   BASE_URL = 'https://randomuser.me/api/'

   def __init__(self, count:str, *args, **kwargs):
       self.url = self.BASE_URL + '?results={}'.format(count)
  
   @error_handler
   def _make_request(self):
       response = requests.get(self.url)
       return response

   @converter
   def get_location(self):
       results = self._make_request()
       for item in results:
           yield item.get('location')

   @converter
   def get_login(self):
       results = self._make_request()
       for item in results:
           yield item.get('login')

"""

data = RequestData("20")
login_data = data.get_location()
list_ = []

for index in range(20):
    dict_ = {}
    dict_["street"] = login_data["results"][index]["location"]["street"]
    list_.append(dict_)

for item in list_:
    print("%s\n" % item)

"""

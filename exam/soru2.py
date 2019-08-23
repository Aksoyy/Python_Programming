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
       self.url = self.BASE_URL + '?result={}'.format(count)
  
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


# RequestData class
"""

SORU 2

Sınıf içinden çagrılan 2 tane decorator fonksiyon; gerekli dönüşüm ve kontrol
işlemlerini yapabilmek için tasarlanmıştır. Belirttiğim her iki fonksiyonun da
geri dönüş tipi bir fonksiyon özelliği taşımaktadır.

def error_handler(func: Callable) -> Callable:
    Burada gelen response talebinin doğruluğu kontrol edildikten sonra, veri
    json formatına dönüştürülür. Aldığı formatın 'result' içindeki değeri alır
    ve dictionary yapısında görevini tamamlar.

def converter(func:Callable) -> Callable:
    Kısacası gelen veriyi list'e dönüştürür.
NOT --> Bu yapı içinde list içinde dictionary'ler bulunmaktadır. Dict sayısı
result değeri yani url'den istenen sayıya bağımlılık gösterir.

"""

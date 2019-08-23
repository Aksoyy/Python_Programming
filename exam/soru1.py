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


# RequestData class
"""
SORU 1

Bu yapıda randomuser sitesine istek atarak operasyonlar yapılmaktadır
Sınıf içindeki metotları kullanırken decorator çagrımı ile yapıyı parçalayıp
önceliklendirilmiştir.

İlk istek geldiğinde:
def __init__() --> consructor yani sınıftan bir nesne tasarlandıgında,
belirtilen url'e istek --> alınan "count" değeri kadar kullanıcı bilgileri
alınmıştır.

def _make_request(self) --> Belirtilen url'e istek atmayı sağlar.
İstekten önce error_handler(func: Callable) fonksiyonuna giderek
isteğin doğru bir şekilde geldiğinin kontrolü yapılır.

def get_location(self) --> Bu metot, sınıf içindeki make_request metotunu
kullanarak url'e isteği göndermektedir. Fakat gelen isteği converter
fonksiyonuna göndererek veriyi list'e dönüştürür. Daha sonra aldığı cevabı
sırayla 'location' değerleri yield ile yani bir yapının içerisinde yield varsa
o generatördür. Bu yüzden yield olan yapıda return kullanılmaz.

def get_login(self) --> Bu metot, sınıf içindeki make_request metotunu
kullanarak url'e isteği göndermektedir. Fakat gelen isteği converter
fonksiyonuna göndererek veriyi list'e dönüştürür. Daha sonra aldığı cevabı
sırayla 'login' değerleri yield ile yani bir yapının içerisinde yield varsa
o generatördür. Bu yüzden yield olan yapıda return kullanılmaz.

"""

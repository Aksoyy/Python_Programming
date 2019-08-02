def func(ucret,yuzde,secenek):
    if secenek == 'Z':
        ucret += ucret/yuzde
        print("Zam Sonucu: ",ucret)
    elif secenek == 'K':
        ucret -= ucret/yuzde
        print("İndirim Sonucu: ",ucret)
    else:
        print("Error")

func(100,10,'Z')

#class A:
#    name = "Hakan"
#res_ = A()
#getattr(res_,"name",0)

from collections import namedtuple
cc_ = namedtuple("Sinif","att att2")

class A:
    def __new__(cls, *args, **kwargs):
        pass

#data = {"name":"mesut",..}
#res_ = data_

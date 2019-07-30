def first_decorator(a_func):
    def wrapTheFunction():
        print("fonksiyon oncesi cikti")
        a_func()
        print("fonksiyon sonrasi cikti")
    return wrapTheFunction

def requiring_decoration():
    print("fonksiyon ciktisi")

requiring_decoration = first_decorator(requiring_decoration)
#requiring_decoration is wrapped by wrapTheFunction()

requiring_decoration()
#outputs:fonksiyon oncesi cikti
#        fonksiyon ciktisi
#        fonksiyon sonrasi cikti
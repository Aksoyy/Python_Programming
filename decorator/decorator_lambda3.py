base = lambda f: lambda *args, **kwargs: (print('Base'), f(*args, **kwargs))

@base
def add_two(x):
    print("Sonuc:", x+5)
    return x + 2

# Decarator edilmiş fonksiyon cagrimi
add_two(3)

# Applying decorator to a lambda
base(lambda x: print(x ** 2))(3)

"""
Base
Sonuc: 8

Base
(None, 9)
"""
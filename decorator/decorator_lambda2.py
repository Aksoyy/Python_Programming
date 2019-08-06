def base(f):
    def wrap(*args, **kwargs):
        print(f"[BASE]: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
    return wrap

@base
def add_two(x):
    print("Sonuc:", x+5)
    return x + 2

# Decarator edilmiş fonksiyon cagrimi
add_two(3)

# Applying decorator to a lambda
print((base(lambda x: x ** 2))(3))

"""
[BASE]: add_two, args: (3,), kwargs: {}
Sonuc: 8
[BASE]: <lambda>, args: (3,), kwargs: {}
9
"""
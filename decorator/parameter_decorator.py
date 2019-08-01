from functools import wraps

def deco(test="TRUE"):
    def logging_decorator(func):
        def wrapped_function(*args, **kwargs):
            print("dogru") if test=="TRUE" else print("yanlis")
        return wrapped_function
    return logging_decorator

@deco("test")
def first():
    pass

first()
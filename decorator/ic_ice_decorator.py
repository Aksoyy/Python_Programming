from functools import wraps

def decorator_with_args(decorator_to_enhance):
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args
def second_decorated(func, *args, **kwargs): 
    @wraps(func)
    def wrapper(function_arg1, function_arg2):
        print('Gelen veri:', args, kwargs)
        return func(function_arg1, function_arg2)
    return wrapper
    

@second_decorated(1, 2, 3,name="Hakan")
def first_decorated_function(function_arg1, function_arg2):
    print('Sonraki Veri:', function_arg1, function_arg2)

first_decorated_function('Hakan', 'Aksoy')
def decorator_with_args(decorator_to_enhance):
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args
def second_decorated_decorator(func, *args, **kwargs): 
    def wrapper(function_arg1, function_arg2):
        print('Decorated with', args, kwargs)
        return func(function_arg1, function_arg2)
    return wrapper
    

@second_decorated_decorator(1, 2, 3)
def first_decorated_function(function_arg1, function_arg2):
    print('Hello', function_arg1, function_arg2)

first_decorated_function('Aksoy', 'Aksoy')

#https://stackoverflow.com/questions
#/739654/how-to-make-a-chain-of-function-decorators#answer-739665
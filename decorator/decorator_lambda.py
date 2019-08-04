def arg_decorator(*s):
    def accept(f):
        print("Veri: ",len(s))
        return s

    return accept

@arg_decorator(lambda x: x + 1)
def plus_one():
    pass

@arg_decorator(lambda x: x + 1, lambda y: y * 2)
def two_decorators():
    pass

@arg_decorator(lambda x: x + 1, lambda y: y * 2, lambda z: z/3)
def three_decorators():
    pass
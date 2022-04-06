def repeat_decorator(func):
    def inner1(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return inner1


@repeat_decorator
def multiply(mul1, mul2):
    print(mul1*mul2)


a, b = input("Enter a b:").split(" ")
multiply(int(a), int(b))

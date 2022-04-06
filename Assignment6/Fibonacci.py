def fibonacci(n):
    if n == 0:
        return
    a = 0
    b = 1
    if n == 1:
        yield a
        return
    yield a
    yield b
    for ii in range(2, n):
        yield a+b
        a, b = b, a+b


num = int(input("Enter the number:"))
for i in fibonacci(num):
    print(i)

equation_solution = lambda a, b, c, x: print((a * x ** 2) + (b * x) + c)
a1, b1, c1, x1 = input("Input for a b c x:").split(" ")
equation_solution(a1, b1, c1, x1)

lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
print(list(map(lambda a: a.count('a') + a.count('A'), lst1)))


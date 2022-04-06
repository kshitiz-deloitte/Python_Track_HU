from functools import reduce

# 1. Using a lambda function take inputs as 4 integers and give the output for equation ax^2+bx+c
equation_solution = lambda a, b, c, x: print((a * x ** 2) + (b * x) + c)
a1, b1, c1, x1 = input("Input for a b c x:").split(" ")
equation_solution(int(a1), int(b1), int(c1), int(x1))

# 2. Using map() function and lambda and count() function create a list consisted of the number of occurrence of both
# letters: 'A' and 'a'.
lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
print(list(map(lambda a: a.count('a') + a.count('A'), lst1)))

# 3. Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to
# positive to the new list.
lst2 = [-1000, 500, -600, 700, 5000, -90000, -17500]
print(list(map(lambda m: abs(m), list(filter(lambda m: m < 0, lst2)))))

# 4. Take the first two values, run the function on them. Then take the result and the next value and have a
# multiplication between them. etc. When no more values are left, return the last result.
list_mul = [1, 3, 4, 5, 8]
print(reduce(lambda a, b: a*b, list_mul))

# 5. Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.
keys = ["Netflix", "Hulu", "Sling", "Hbo"]
values = [198, 166, 237, 125]
print(dict(zip(keys, values)))

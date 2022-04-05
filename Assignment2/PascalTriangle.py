def solve_pascal_triangle(n):
    for i in range(1, n + 1):
        c = 1
        for j in range(1, i + 1):
            print(c, ' ', sep='', end='')
            c = c * (i - j) // j
        for k in range(i + 1, n + 1):
            print(0, ' ', sep='', end='')
        print()


N = int(input("Enter number of row: "))
solve_pascal_triangle(N)

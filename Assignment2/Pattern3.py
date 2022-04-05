# row = int(input('Enter number of rows required: '))
row = 5
for i in range(row, 0, -1):
    for j in range(row - i - 1):
        # print(i, j)
        print(' ', end=' ')  # printing preceding space
    for j in range(row):
        if i == row or i == j or j == row or j==1:
            print('*', end=' ')  # printing *
        else:
            print(' ', end=' ')  # printing space inside triangle
    print()  # for new line
row = int(input('Enter number of rows required: '))

for i in range(row):
    for j in range(row - i):
        print(' ', end='')  # printing preceding space

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == row - 1:
            print('*', end='')  # printing *
        else:
            print(' ', end='')  # printing space inside triangle
    print()  # for new line

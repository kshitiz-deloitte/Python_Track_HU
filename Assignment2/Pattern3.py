# row = int(input('Enter number of rows required: '))
row = 3
for i in range(row - 1, 0, -1):
    for j in range((row - 1)-i):
        print(i)
        print(' ', end='')  # printing preceding space

    for j in range(row):
        if i == 0 or i == row-1 or j == row - 1 or i ==j:
            print('*', end='')  # printing *
        else:
            print(' ', end='')  # printing space inside triangle
    print()  # for new line
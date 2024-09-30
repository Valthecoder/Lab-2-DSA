def side_length(sides_n):
    for length in range(sides_n):
        if length == 0 or length == sides_n - 1:
            print('x' * sides_n)
        else:
            print('x' + ' ' * (sides_n - 2) + 'x')


sides_n = int(input("Enter the side length of the square: "))
side_length(sides_n)

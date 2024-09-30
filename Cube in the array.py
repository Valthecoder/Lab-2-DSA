def cube_the(integer):
    print("The cube of each element is:")
    for element in integer:
        print(element ** 3)

size_array = int(input("Enter the size of the array: "))

integer = list(map(int, input(f"Enter the {size_array} elements separated by space: ").split()))

cube_the(integer)
import math

if __name__ == '__main__':

    # 034
    print("1) Square")
    print("2) Triangle")
    num = int(input("\nEnter the number: "))
    if num == 1:
        Square = int(input("Enter the length of one side: "))
        print("The area of the square =", Square * Square)
    elif num == 2:
        Triangle = int(input("Enter the bottom of the triangle: "))
        Triangle2 = int(input("Enter the height of the triangle: "))
        print("The area of a triangle =", Triangle * Triangle2 / 2)
    else:
        print("Error message")

    # 033
    # num = int(input("Enter the first number: "))
    # num2 = int(input("Enter the second number: "))
    # num3 = num // num2
    # num4 = num % num2
    # print(num, "divide by", num2, "is", num3, "with", num4, "remaining")

    # 032
    # Radius = int(input("Enter the Radius: "))
    # Deep = int(input("Enter the Deep: "))
    # num = math.pi
    # test = num * Radius ** 2
    # test2 = test * Deep
    # print(round(test2, 3))

    # 031
    # Radius = int(input("Enter the Radius: "))
    # num = math.pi
    # print(num * Radius ** 2)

    # 030
    # num = math.pi
    # print(round(num, 15))

    # 029
    # num = int(input("Enter an integer above 500: "))
    # num2 = math.sqrt(num)
    # print(num2)

    # 028
    # num = float(input("Enter the number: "))
    # print(round(num, 2))

    # 026
    # num = float(input("Please enter a number with many decimal places: "))
    # print(num * 2)

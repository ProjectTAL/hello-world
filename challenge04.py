import math


def testPrint():
    print("Hello World!")


# 027 & 028
def calcMultiply(num):
    return num * 2


# 029
def calcSqrt(num):
    return math.sqrt(num)


def calcRoundwith2point(num):
    return round(float(num), 2)


# 031
def calcAreaofCircle(num):
    return math.pi * (num ** 2)


# 032
def calcCylider(radius, depth):
    ret = float(depth * (radius ** 2) * math.pi)
    ret = round(ret, 3)
    return str(ret)


# 034
def decider(num):
    if num == 1:
        square = int(input("Input the length of the square side : "))
        print(f"The area of the square is {square * square}")
    elif num == 2:
        bottom = int(input("Input the length of bottom side :"))
        height = int(input("Input the height :"))
        print(f"The area of the triangle is {bottom * height / 2}")
    else:
        print("It is not the required value...")


if __name__ == '__main__':
    testPrint()
    # 034
    print("1) Square\n2) Triangle")
    number = int(input("Enter a number :"))
    decider(number)

    # 033
    # firstNum = int(input("Plz, input the 1st number :"))
    # secondNum = int(input("Plz, input the 2nd number :"))
    # print(f"{firstNum} divided by {secondNum} is {firstNum // secondNum} with {firstNum % secondNum} remaining")

    # 032
    # radius = int(input("Input the radius of the circle :"))
    # depth = int(input("Input the depth :"))
    # print(f"The valume of the cylinder is {calcCylider(radius, depth)}")

    # 031
    # number = int(input("Put the radius :"))
    # number = calcAreaofCircle(number)
    # print(f"The area of circle is {number}")

    # 030
    # print("pi value is " + str(round(math.pi, 5)))

    # 029
    # number = int(input("Put the number over than 500 :"))
    # number = calcRoundwith2point(calcSqrt(number))
    # print("The answer is " + str(number))

    # 027 & 028
    # number = float(input("Put the number with decimal point and numbers :"))
    # number_1 = round(calcMultiply(number), 2)
    # print("the value multiply 2 is " + str(number_1))

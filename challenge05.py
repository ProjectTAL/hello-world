def testPrint(num):
    print(num, " Hello World!")


# 035 & 036
def print3Times(text, num):
    for i in range(1, num + 1):
        print(text)


# 037 & 038
def printNameOnebyOnetolinebyline(text, count):
    for i in text:
        for j in range(1, count + 1):
            print(i)


# 039
# The description is confusing. I got the point finally with the sample code. Any how it works that i expected.
def calcMultiplyTo12(num):
    for j in range(num, 13):
        for i in range(1, 10):
            print(f"{j} * {i} = ", j * i)


# 040
def printCountDown(num):
    for i in range(50, num - 1, -1):
        print("Count down ", i)


if __name__ == '__main__':
    # for i in range(1, 10):
    #     testPrint(i)
    # for i in "word":
    #     print(i)
    # 040
    number = int(input("Input the value (1-49) :"))
    printCountDown(number)

    # 039
    # number = int(input("Input the value you want to see (1-12) :"))
    # calcMultiplyTo12(number)

    # 037 & 038
    # text = input("Type your name :")
    # count = int(input("How many times do you want to loop it :"))
    # printNameOnebyOnetolinebyline(text, count)

    # 035 & 36
    # text = input("Type your name :")
    # num = int(input("How many times do you want to loop it :"))
    # print3Times(text, num)

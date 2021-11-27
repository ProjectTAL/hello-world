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


# 041
def deciderPrint(name, num):
    if num < 10:
        for i in range(0, num):
            print(name)
    elif num >= 10:
        for i in range(0, 3):
            print("Too high")


# 043
def countToUpNum(num):
    for i in range(0, num + 1):
        print(i)


def counttoDownNum(num):
    for i in range(20, num - 1, -1):
        print(i)


# 044
def storeFriendsList(num):
    if num < 10:
        for i in range(0, num):
            name = input("Type the friend name :")
            print(f"{i + 1} : {name} has been invited")
    else:
        print("Too many people")


if __name__ == '__main__':
    # for i in range(1, 10):
    #     testPrint(i)
    # for i in "word":
    #     print(i)
    # 044
    num = int(input("How many friends do you want to invite :"))
    storeFriendsList(num)

    # 043
    # direction = input("Up or Down? ")
    # if direction.lower() == "up":
    #     num = int(input("Type the number that you think the most :"))
    #     countToUpNum(num)
    # elif direction.lower() == "down":
    #     num = int(input("type the number less than 20 :"))
    #     counttoDownNum(num)
    # else:
    #     print("I don't understand")

    # 042
    # sum = 0
    # for i in range(0, 5):
    #     num = int(input("type number :"))
    #     answer = input("Do you want to add the number (true, false) ?")
    #     if answer == "true":
    #         sum = sum + num
    #     else:
    #         sum = sum
    # print("The sum is ", sum)

    # 041
    # name = input("Type your name :")
    # count = int(input("Type the number how many time you want to show :"))
    # deciderPrint(name, count)

    # 040
    # number = int(input("Input the value (1-49) :"))
    # printCountDown(number)

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

def testPrint():
    print("Hello World!")


# 012
def getNumber1():
    ret = int(input("Put the 1st number :"))
    return ret


def getNumber2():
    ret = int(input("Put the 2nd number :"))
    return ret


def cmpNumbers(n1, n2):
    if n1 > n2:
        print(f"{n2}, then {n1}")
    else:
        print(f"{n1}, then {n2}")


# 013
def getNumberLessthan20():
    ret = int(input("Put the number less than 20 : "))
    return ret


def decideCondition01(num):
    if num >= 20:
        print("Too High")
    else:
        print("Thank you")


# 014
def getNumberooo():
    ret = int(input("Put the number 10-20 : "))
    return ret


def decideCondition02(num):
    if num >= 10 and num <= 20:
        print("Thank you")
    else:
        print("Incorrect answer")


# 015
def getColor():
    ret = input("What color do you like: ")
    return ret


def decideFromCondition(color):
    if color == "red" or color == "RED":
        print("I like red too")
    else:
        print("I don't like that colour, I prefer red")


# 016
def askFirstQuestion():
    ret = str.lower(input("Is it raining there? "))
    return ret


def askSecondQuestion():
    ret = str.lower(input("What about the wind there? "))
    return ret


def decidefromCondition03(answer):
    if answer == "yes":
        print("It is too windy for an ambrella")
    else:
        print("Take an umbrella")


def decidefromCondition02(answer):
    if answer == "yes":
        decidefromCondition03(askSecondQuestion())
    else:
        print("Enyoy your day")


# 017
def askAge():
    ret = int(input("How old are you? "))
    return ret


def decidefromCondition04(age):
    if age >= 18:
        print("You can vote")
    elif age == 17:
        print("You can learn to drive")
    elif age == 16:
        print("You can guy a lottery")
    else:
        print("You can go Trick-or-Treating")


# 018
def decideFromCondition05(num):
    if num < 10:
        print("Too low")
    elif num >= 10 and num <= 20:
        print("Correct")
    else:
        print("Too high")


# 019
def decideFromCondtion06(num):
    if num == 1:
        print("Thank you")
    elif num == 2:
        print("Well done")
    elif num == 3:
        print("Correct")
    else:
        print("Error message")


if __name__ == '__main__':
    # testPrint()
    number = int(input("Put the number of 1, 2 and 3 : "))
    decideFromCondtion06(number)
    # 018
    # number = int(input("Put the number you want : "))
    # decideFromCondition05(number)
    # 017 decidefromCondition04(askAge())
    # 016 decidefromCondition02(askFirstQuestion())
    # 015 decideFromCondition(getColor())
    # 014 decideCondition02(getNumberooo())
    # 013 decideCondition01(getNumberLessthan20())
    # 012 cmpNumbers(getNumber1(), getNumber2())

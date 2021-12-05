# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# 001 Hello [input]:
def input_name():
    name_string = input("put your name : ")
    return name_string


# 002 Hello [Last name] [First name]
def input_lastName():
    lastName_string = input("put your last name :")
    return lastName_string


def input_firstName():
    firstName_string = input("put your first name :")
    return firstName_string


# 003 2LINE BY 1LINE CODE
# 004 2 numbers and plus each other
def input_fistNumber():
    firstNumber = int(input("put your 1st number:"))
    return firstNumber


def input_secondNumber():
    secondNumber = int(input("put your 2nd number:"))
    return secondNumber


# 005 gets 3 numbers and plus 1,2 and multiplex
def input_firstNumber_005():
    firstNumber = int(input("type your 1st number:"))
    return firstNumber


def input_secondNumber_005():
    secondNumber = int(input("type your 2nd number:"))
    return secondNumber


def input_thirdNumber_005():
    thirdNumber = int(input("type your 3rd number:"))
    return thirdNumber


# 006
def input_totalPizza():
    totalPizza = int(input("put how many pizza you have :"))
    return totalPizza


def input_pizzaEaten():
    eatenPizza = int(input("put how many piece you ate :"))
    return eatenPizza


# 007
def getName_007():
    strName = input("Type your name:")
    return strName


def getYourAge_007():
    intYourAge = int(input("How old are you:"))
    return intYourAge


# Press the green button in the gutter to run the script.
# 008
def getTotalCost_008():
    price = int(input("Put the total price:"))
    return price


def getTotalMember_008():
    member = int(input("Put the total members:"))
    return member


# 009
def getTotalDays_009():
    days = int(input("Put the number that you want to check as hours:minutes:seconds :"))
    return days


# 010
def getKilogram():
    kg = int(input("Put the kilogram to transform to pound:"))
    return kg


def setKilogramToPound(kg):
    ret = kg * 2.204
    return ret


# 011
def getNumber():
    ret = int(input("Put the number over than 100, please :"))
    return ret


def getOneMoreNumber():
    ret = int(input("Put the number less than 10, please:"))
    return ret


if __name__ == '__main__':
    print_hi('PyCharm')
    n1 = getNumber()
    n2 = getOneMoreNumber()
    n3 = int(n1 / n2)
    print(f'Your 1st number is {n1}. The 2nd number is {n2}. {n2} can stay {n3} times in {n1}')
    # 010
    # print("The result is ", setKilogramToPound(getKilogram()))
    # 009
    # days = getTotalDays_009()
    # hours = days * 24
    # minutes = hours * 60
    # seconds = minutes * 60
    # print("Hours:", hours, " Minutes:", minutes, " Seconds:", seconds)
    # 008
    # cost = int(getTotalCost_008()/getTotalMember_008())
    # print("Each members need to cost ", cost)
    # 007
    # name = getName_007()
    # age = getYourAge_007() + 1
    # print(f'{name} next birthday your will be {age}')
    # 006
    # pizzaLeft = input_totalPizza() - input_pizzaEaten()
    # print(f"It is {pizzaLeft} pizza left")
    # 005print("The answer is ", (input_firstNumber_005() + input_secondNumber_005()) * input_thirdNumber_005())
    # 003print("What do you call a bear with no teeth\nA gummy bear")
    # 001 Hello [input]
    # print("Hello ", input_name())
    # 002 Hello [lastName][FirstName]
    # print("Hello ", input_lastName(), input_firstName())
    # 004 print("Total number is ", input_fistNumber() + input_secondNumber())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

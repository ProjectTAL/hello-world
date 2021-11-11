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

#003 2LINE BY 1LINE CODE
#004 2 numbers and plus each other
def input_fistNumber():
    firstNumber = int(input("put your 1st number:"))
    return firstNumber
def input_secondNumber():
    secondNumber = int(input("put your 2nd number:"))
    return secondNumber
#005 gets 3 numbers and plus 1,2 and multiplex
def input_firstNumber_005():
    firstNumber = int(input("type your 1st number:"))
    return firstNumber
def input_secondNumber_005():
    secondNumber = int(input("type your 2nd number:"))
    return secondNumber
def input_thirdNumber_005():
    thirdNumber = int(input("type your 3rd number:"))
    return thirdNumber
#006 사용자로부터 처음에 가지고 있었던 피자 조각 수를 입력받고
#    몇 조각을 먹었는지 입력받아서 남은 조각 수를 계산하여 사람에게 익숙한 형식으로 출력하라
def input_totalPizza():
    totalPizza = int(input("put how many pizza you have :"))
    return totalPizza
def input_pizzaEaten():
    eatenPizza = int(input("put how many piece you ate :"))
    return eatenPizza
#007 사용자로부터 이름과 나이를 입력받아서 나이에 1을 더한 후 다음과 같이 출력하라.
# [이름] next birthday you will be [새로운 나이]
def getName_007():
    strName = input("Type your name:")
    return strName
def getYourAge_007():
    intYourAge = int(input("How old are you:"))
    return intYourAge
# Press the green button in the gutter to run the script.
#008 계산서의 총 가격과 몇 명이 같이 식사를 했는지 입력받는다. 총 가격을 인원수로 나누고 각 사람이 얼마씩 내야 하는지 출력하라.
def getTotalCost_008():
    price = int(input("Put the total price:"))
    return price
def getTotalMember_008():
    member = int(input("Put the total members:"))
    return member
#009 사용자로부터 일수(날짜 수)를 입력 받아서 그 일수까지 몇 시간, 몇 분, 몇 초가 남았는지 출력하라.
def getTotalDays_009():
    days = int(input("Put the number that you want to check as hours:minutes:seconds :"))
    return days
#010 1킬로그램은 2.204파운드다.
#    몸무게를 킬로그램 단위로 입력받아서 파운드로 변환하여 출력하라.
def getKilogram():
    kg = int(input("Put the kilogram to transform to pound:"))
    return kg
def setKilogramToPound(kg):
    ret = kg * 2.204
    return ret
if __name__ == '__main__':
    print_hi('PyCharm')
    print("The result is ", setKilogramToPound(getKilogram()))
    #009
    #days = getTotalDays_009()
    #hours = days * 24
    #minutes = hours * 60
    #seconds = minutes * 60
    #print("Hours:", hours, " Minutes:", minutes, " Seconds:", seconds)
    #008
    #cost = int(getTotalCost_008()/getTotalMember_008())
    #print("Each members need to cost ", cost)
    #007
    #name = getName_007()
    #age = getYourAge_007() + 1
    #print(f'{name} next birthday your will be {age}')
    #006
    #pizzaLeft = input_totalPizza() - input_pizzaEaten()
    #print(f"It is {pizzaLeft} pizza left")
    #005print("The answer is ", (input_firstNumber_005() + input_secondNumber_005()) * input_thirdNumber_005())
    #003print("What do you call a bear with no teeth\nA gummy bear")
    #001 Hello [input]
    #print("Hello ", input_name())
    #002 Hello [lastName][FirstName]
    #print("Hello ", input_lastName(), input_firstName())
    #004 print("Total number is ", input_fistNumber() + input_secondNumber())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

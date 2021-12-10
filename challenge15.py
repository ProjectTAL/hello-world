import csv
import random


def printTest():
    print("Hello world!")


# 118
def saveNumber():
    num = int(input("Enter number :"))
    return num


def countNumber(num):
    ret = 0
    for i in range(1, num + 1):
        ret = ret + i
    return ret


# 119
def inputLowNumber():
    ret = int(input("Enter low number :"))
    return ret


def inputHighNumber():
    ret = int(input("Enter high number :"))
    return ret


def getNumberFromUser():
    print("I am thinking of a number...")
    ret = int(input("Enter number to get a correct answer :"))
    return ret


# 120
def quizPlus():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    answer = int(input(f"{num1} + {num2} = "))
    real_value = num1 + num2
    return (answer, real_value)


def quizMinus():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    answer = int(input(f"{num1} - {num2} = "))
    real_value = num1 - num2
    return (answer, real_value)


def compareAnswers(a, b):
    if a == b:
        print("Correct!")
    else:
        print(f"Incorrect, the answer is {b}")


# 121
def showMenu():
    print("""1) Add name
2) Modify name
3) Delete name
4) Show all names
5) Exit
""")


def removeEOL(text):
    if text.endswith('\n'):
        text = text[:-1]
    return text


def addEOL(text):
    if not text.endswith('\n'):
        text = text + '\n'
    return str(text)


def addName():
    file = open("NameList.csv", "a")
    name = input("Enter name :")
    line = name + "\n"
    file.write(str(line))
    file.close()


def modifyName():
    answer = input("Enter the name that you modify :")
    modifiedAnswer = input("What is the expected name :")
    file = open("NameList.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)
    tmp = []
    for row in rows:
        tmp.append(row)
    file.close()

    file = open("NameList.csv", "w")
    x = 0
    for row in tmp:
        # newRecord = tmp[x][0] + "\n"
        if answer in row:
            file.write(addEOL(modifiedAnswer))
        else:
            file.write(addEOL(tmp[x][0]))
        x = x + 1
    file.close()


def deleteName():
    answer = input("Enter the name that you delete :")
    file = open("NameList.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)
    tmp = []
    for row in rows:
        tmp.append(row)
    file.close()

    file = open("NameList.csv", "w")
    x = 0
    for row in tmp:
        if answer not in row:
            file.write(addEOL(tmp[x][0]))
        x = x + 1
    file.close()


def showAllNames():
    file = open("NameList.csv", "r")
    for row in file:
        print(removeEOL(row))
    file.close()


if __name__ == '__main__':
    printTest()
    # 121
    flag = False
    while not flag:
        showMenu()
        menuNum = input("Enter number :")
        if menuNum.isdigit():
            menuNum = int(menuNum)
        else:
            menuNum = 6
        if menuNum == 1:
            addName()
        elif menuNum == 2:
            modifyName()
        elif menuNum == 3:
            deleteName()
        elif menuNum == 4:
            showAllNames()
        elif menuNum == 5:
            flag = True
        else:
            print("You entered wrong number or string\n\nPlease enter the number (1-5) :")
    print("Bye Bye~")

    # 120
#     print("""1) Addition
# 2) Subtraction""")
#     answer = int(input("Enter 1 or 2:"))
#     if answer == 1:
#         (a, b) = quizPlus()
#         compareAnswers(a, b)
#     elif answer == 2:
#         (a, b) = quizMinus()
#         compareAnswers(a, b)
#     else:
#         print("You chose a wrong number..")

# 119
# lowNum = inputLowNumber()
# highNum = inputHighNumber()
# comp_num = random.randint(lowNum, highNum)
# flag = False
# while not flag:
#     answer = getNumberFromUser()
#     if comp_num == answer:
#         print("Correct, you win")
#         flag = True
#     else:
#         if comp_num > answer:
#             print("higher than your answer")
#         else:
#             print("lower than your answer")

# 118
# num = saveNumber()
# result = countNumber(num)
# print(f"The sum is {result}")

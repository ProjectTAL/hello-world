def testPrint():
    print("Hello World!")

#012 두 개의 숫자를 입력받는다. 만약 첫 번째 숫자가 두 번째 숫자보다 크면, 두 번째 숫자를 먼저 출력한 다음에 첫 번째 숫자를 출력하라.
#    그렇지 않다면 첫 번째 숫자를 출력한 다음에 두 번째 숫자를 출력하라.
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
#013
def getNumberLessthan20():
    ret = int(input("Put the number less than 20 : "))
    return ret
def decideCondition01(num):
    if num >= 20:
        print("Too High")
    else:
        print("Thank you")
#014
def getNumberooo():
    ret = int(input("Put the number 10-20 : "))
    return ret
def decideCondition02(num):
    if num >=10 and num <= 20:
        print("Thank you")
    else:
        print("Incorrect answer")
#015
def getColor():
    ret = input("What color do you like: ")
    return ret
def decideFromCondition(color):
    if color == "red" or color == "RED":
        print("I like red too")
    else:
        print("I don't like that colour, I prefer red")
#016..
if __name__ == '__main__':
    testPrint()
    decideFromCondition(getColor())
    #014 decideCondition02(getNumberooo())
    #013 decideCondition01(getNumberLessthan20())
    #012 cmpNumbers(getNumber1(), getNumber2())
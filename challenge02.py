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
#013 사용자에게 20보다 작은 숫자를 입력하라고 요청한다. 만약 입력된 값이 20과 같거나 크면 "Too high"라는 메시지를 출력하라.
#    그렇지 않다면 "Thank you"를 출력하라.
def getNumberLessthan20():
    ret = int(input("Input the number that you want but MUST be less than 20 : "))
    return ret
def decideCondition(num):
    if num >= 20:
        print("Too high")
    else:
        print("Thank you")
#014 사용자에게 10과 20(포함) 사이의 숫자를 입력하라고 요청한다. 만약 입력한 값이 이 범위 안의 숫자이면 "Thank you"라는 메시지를
#    출력한다. 그렇지 않다면 "Incorrect answer"라는 메시지를 출력하라.
def getNumberHigerthan10nLessthan20():
    ret = int(input("Put the number from 10 to 20 :"))
    return ret
def decideCondition02(num):
    if num >= 10 and num <= 20:
        print("Thank you")
    else:
        print("Incorrect answer")
if __name__ == '__main__':
    testPrint()
    decideCondition02(getNumberHigerthan10nLessthan20())
    #013 decideCondition(getNumberLessthan20())
    #012 cmpNumbers(getNumber1(), getNumber2())
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
if __name__ == '__main__':
    testPrint()
    cmpNumbers(getNumber1(), getNumber2())
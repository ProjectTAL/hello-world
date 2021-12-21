import time


def showMenu():
    print("""1) Make a code
2) Decode a message
3) Quit""")


def isSpace(c):
    if ord(c) == 32:
        return True
    else:
        return False


def encodeChar(c):
    ret = ord(c) - ord('a')
    return ret


def decodeChar(number):
    ret = chr(ord('a') + number)
    return ret


def encodeWithNumber():
    global encodeResult, decodeResult
    encodeResult = ""
    text = input("Enter text (a-z) :")
    number = input("Enter number (1-5) : ")
    if not number.isdigit():
        return False
    decodeResult = text
    result = []
    for c in text:
        if isSpace(c):
            result.append(" ")
        else:
            tNum = encodeChar(c)
            tuningNum = tNum + int(number)
            tuningNum %= 26
            result.append(decodeChar(tuningNum))
    for c in result:
        encodeResult += c
    return True

def decodeWithNumber():
    global encodeResult, decodeResult
    decodeResult = ""
    number = input("Enter number (1-5) : ")
    if not number.isdigit():
        return False
    result = []
    for c in encodeResult:
        if isSpace(c):
            result.append(" ")
        else:
            tNum = encodeChar(c)
            tuningNum = tNum - int(number)
            if tuningNum < 0:
                tuningNum = 26 + tuningNum
            result.append(decodeChar(tuningNum))
    for c in result:
        decodeResult += c
    return True


if __name__ == '__main__':
    decodeResult = ""
    encodeResult = ""
    flag = False
    while not flag:
        showMenu()
        num = input("\nEnter your selection :")
        if not num.isdigit():
            print("\nOnly number is allowed!")
            time.sleep(1)
        elif num.isdigit():
            if int(num) == 1:
                if not encodeWithNumber():
                    continue
                print("Origin : {}".format(decodeResult))
                print("Encoded : {}".format(encodeResult))
                time.sleep(2)
            elif int(num) == 2:
                if not decodeWithNumber():
                    continue
                print("Encoded : {}".format(encodeResult))
                print("Decoded : {}".format(decodeResult))
                encodeResult = decodeResult
                time.sleep(2)
            elif int(num) == 3:
                flag = True
            else:
                print("\nWrong number!")
                time.sleep(1)

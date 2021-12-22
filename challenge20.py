import random
import time


def showMenu():
    for index, value in enumerate(colors):
        print("{}) {}".format(index, value))


def getColorName():
    # https://www.rapidtables.com/web/color/RGB_Color.html#color-table
    ret = random.choice(colors)
    return ret


def validateDigitNumber(number):
    if str(number).isdigit() and 0 <= int(number) <= len(colors):
        return True
    else:
        print("\nWorng number or text. Enter number again(0-{})\n".format(len(colors)))
        time.sleep(1)
        return False


if __name__ == '__main__':
    colors = ("maroon", "red", "coral", "gold", "lawn green", "lime",
              "aqua", "blue", "slate blue", "yellow")
    flag = False

    showMenu()
    num1 = getColorName()
    num2 = getColorName()
    num3 = getColorName()
    num4 = getColorName()
    noColor1 = colors.index(num1)
    noColor2 = colors.index(num2)
    noColor3 = colors.index(num3)
    noColor4 = colors.index(num4)
    # debug-print
    # print(num1, colors.index(num1))
    # print(num2, colors.index(num2))
    # print(num3, colors.index(num3))
    # print(num4, colors.index(num4))

    print("\nThere are {} colors that your can select. You need to choose 4 numbers sequentially".format(len(colors)))
    while not flag:
        countPlace = 0
        countRightColor = 0
        uNum1 = input("Enter number 1 :")
        if not validateDigitNumber(uNum1):
            continue
        uNum2 = input("Enter number 2 :")
        if not validateDigitNumber(uNum2):
            continue
        uNum3 = input("Enter number 3 :")
        if not validateDigitNumber(uNum3):
            continue
        uNum4 = input("Enter number 4 :")
        if not validateDigitNumber(uNum4):
            continue

        if uNum1 == noColor1:
            countPlace += 1
        if uNum2 == noColor2:
            countPlace += 1
        if uNum3 == noColor3:
            countPlace += 1
        if uNum4 == noColor4:
            countPlace += 1

        if colors[uNum1] in (num1, num2, num3, num4):
            countRightColor += 1
        if colors[uNum2] in (num1, num2, num3, num4):
            countRightColor += 1
        if colors[uNum3] in (num1, num2, num3, num4):
            countRightColor += 1
        if colors[uNum4] in (num1, num2, num3, num4):
            countRightColor += 1

        print("Correct colour is the correct place : {}".format(countPlace))
        print("Correct colour but in the wrong place : {}".format(countRightColor))
        if countPlace == 4 and countRightColor == 4:
            flag = True

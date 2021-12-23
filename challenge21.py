import csv
import os.path
import time


def showMenu():
    print("""\n1) Create a new User ID
2) Change a password
3) Display all User IDs
4) Quit
""")


def validateDigitNumber(number):
    if str(number).isdigit() and 1 <= int(number) <= 4:
        return True
    else:
        print("\nWorng number or text. Enter number again(0-4)")
        time.sleep(1)
        return False


def scorePW(password):
    ret = 0
    # over than 8 length
    if len(password) >= 8:
        ret += 1
    # at least more than a capital
    for character in password:
        if character.isupper():
            ret += 1
            break
    # at least more than a lower character
    for character in password:
        if character.islower():
            ret += 1
            break
    # at least more than a digit number
    for number in password:
        if number.isdigit():
            ret += 1
            break
    # at least include one of !, $, %, &, <, *, @
    for specialChar in password:
        if specialChar in ("!", "$", "%", "&", "<", "*", "@"):
            ret += 1
            break
    return ret


def createUserID():
    flag = False
    newId = ""

    while not flag:
        flag = False
        newId = input("\nEnter your ID :")
        if os.path.isfile("data/file/password.csv"):
            file = open("data/file/password.csv", "r")
            reader = csv.reader(file)
            rows = list(reader)
            tmp = []
            for row in rows:
                # print(row, newId)
                tmp.append(row)
            file.close()
            for element in tmp:
                if newId in element:
                    print("\n The ID exists, Please enter ID again.")
                    flag = False
                    break
                else:
                    # print("2.unExpected")
                    # print(newId, element)
                    flag = True
        else:
            flag = True

    saveFlag = False
    newPw = ""
    flag = False
    while not flag:
        newPw = input("\nEnter your PW :")
        score = int(scorePW(newPw))
        if score < 3:
            print("This password is weak. rejected! ({})".format(score))
        elif 2 < score < 5:
            print("This password could be improved ({})".format(score))
            answer = input("Enter your PW again (y or n) ?")
            if answer.lower() == "y" or answer.lower() == "yes":
                continue
            else:
                saveFlag = True
                flag = True
        else:
            print("This password is strong enough")
            saveFlag = True
            flag = True
    if saveFlag:
        if not os.path.isfile("data/file/password.csv"):
            file = open("data/file/password.csv", "w")
            newRec = newId + "," + newPw + "\n"
            file.write(newRec)
            file.close()
        else:
            file = open("data/file/password.csv", "a")
            newRec = newId + "," + newPw + "\n"
            file.write(newRec)
            file.close()


def changePassword():
    flag = False
    saveFlag = False
    while not flag:
        flag = False
        newId = input("\nEnter your ID :")
        if os.path.isfile("data/file/password.csv"):
            file = open("data/file/password.csv", "r")
            reader = csv.reader(file)
            rows = list(reader)
            tmp = []
            for row in rows:
                tmp.append(row)
            file.close()
            for element in tmp:
                if newId in element:
                    flag = True
                    saveFlag = True
                    break
            if not flag:
                print("\n The ID does not exist, Please enter ID again..")
        else:
            print("\n Database does not have any ID.")
    if saveFlag:
        file = open("data/file/password.csv", "w")
        x = 0
        newPw = input("Enter NEW PW :")
        for row in tmp:
            if newId in tmp[x][0]:
                newRec = str(tmp[x][0]) + "," + str(newPw) + "\n"
            else:
                newRec = str(tmp[x][0]) + "," + str(tmp[x][1]) + "\n"
            file.write(str(newRec))
            x += 1
        file.close()


def showIdsNPW():
    if os.path.isfile("data/file/password.csv"):
        file = open("data/file/password.csv", "r")
        reader = csv.reader(file)
        rows = list(reader)
        tmp = []
        for row in rows:
            tmp.append(row)
        file.close()
        for x in tmp:
            print(x)
    else:
        print("There is not IDs registered in Database")


if __name__ == '__main__':
    showMenu()
    flag = False
    while not flag:
        selection = input("\nEnter Selection:")
        if not validateDigitNumber(selection):
            continue
        if int(selection) == 4:
            flag = True
            print("Bye Bye~!")
        elif int(selection) == 1:
            createUserID()
        elif int(selection) == 2:
            changePassword()
        elif int(selection) == 3:
            showIdsNPW()

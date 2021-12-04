def printTest():
    print("Hello world!")


if __name__ == '__main__':
    printTest()
    #087
    word = input("Type a word. That will be printed as reverted :")
    for i in range(len(word)-1, -1, -1):
        print(word[i])

    # 086
    # password = input("Type a password :")
    # confirmPassword = input("Type the password again to confirm :")
    # if password == confirmPassword:
    #     print("Thank you")
    # elif password.lower() == confirmPassword.lower():
    #     print("They must be in the same case")
    # else:
    #     print("Incorrect!")
    # # p1Len = len(password)
    # # p2Len = len(confirmPassword)
    # # flagWrong = False
    # # flagCapitalWrong = False
    # # if p1Len != p2Len:
    # #     print("Incorrect!")
    # #     flagWrong = True
    # # else:
    # #     for i in range(0, p1Len):
    # #         if password[i] != confirmPassword[i]:
    # #             if password[i].lower() == confirmPassword[i].lower():
    # #                 flagCapitalWrong = True
    # #             else:
    # #                 flagWrong = True
    # #                 break
    # # if flagWrong == False:
    # #     if flagCapitalWrong == True:
    # #         print("They must be in the same case")
    # #     else:
    # #         print("Thank you")
    # # else:
    # #     print("Incorrect!")

    # 085
    # name = input("Type your name :")
    # count = 0
    # for i in name.lower():
    #     if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o':
    #         count = count + 1
    # print(f"The count of collection is {count}")

    # 084
    # word = input("Type a word that you suddenly think of :")
    # capital = word[0:2]
    # print(capital.upper() + word[2:len(word])
    # # for i in word:
    # #     print(word.index(i))
    # #     if word.index(i) == 0:
    # #         print(i + i.upper())
    # #         word = word.replace(i, i.upper(), 1)
    # #     elif word.index(i) == 1:
    # #         print(i + i.upper())
    # #         word = word.replace(i, i.upper(), 1)
    # #print(f"The word has been chaged like {word}")

    # 083
    # flag = False
    # while not flag:
    #     words = input("Type the string as Capital :")
    #     if words.isupper():
    #         flag = True
    #     else:
    #         print(f"You've typed with lower one like {words}")
    # print("Perfect!")

    # 082
    # line = "Let it be forgotten as a flower it is"
    # print(line)
    # indexFirst = int(input("Input the 1st index :"))
    # indexLast = int(input("Input the last index :"))
    # print(line[indexFirst - 1:indexLast + 1])

    # 081
    # fruit = input("What fruit do you like the most?")
    # for i in fruit:
    #     print(i, end="*")

    # 080
    # name = input("Type your first name :")
    # print(f"The length of the first name is {len(name)}")
    # lastName = input("Type your last name :")
    # print(f"The length of the last name is {len(lastName)}")
    # fullName = name + " " + lastName
    # print(f"The full name is {fullName}. and the length is {len(fullName)}")

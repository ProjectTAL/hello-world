def testPrint():
    print("Hello World!")


# 020 & 021
def getLengh(text):
    ret = len(text)
    return ret


# 022
def changeFormat(name):
    return name.capitalize()


# 023
def printSubtitle(lirics, start, end):
    print(sentences[start - 1:end])


# 024
def replaceCapital(text):
    return text.upper()


# 025
def deciderName(name):
    size = getLengh(name)
    if size < 5:
        secondName = input("Type your Second name:")
        name_1 = name + secondName
        print(name_1.upper())
    else:
        print(name.lower())


# 026
def isPigLatin(word):
    if word[0].lower() == 'a' \
            or word[0].lower() == 'i' \
            or word[0].lower() == 'e' \
            or word[0].lower() == 'o' \
            or word[0].lower() == 'u':
        return False
    else:
        return True


if __name__ == '__main__':
    # testPrint()
    # 026
    word = input("Put any word that you want:")
    size = getLengh(word)
    if isPigLatin(word) == True:
        print(word[1:size] + word[0] + "ay")
    else:
        print(word + "way")
    # 025
    # name = input("Type your first name:")
    # deciderName(name)

    # 024
    # sentences = input("Type any words that you want to make Capital :")
    # print(replaceCapital(sentences))

    # 023
    # sentences = input("Type the lirics that you're recall :")
    # size = getLengh(sentences)
    # print(f"The lengh of your lirics are {size}")
    # startIndex = int(input("Put the start index :"))
    # endIndex = int(input("Put the end index :"))
    # printSubtitle(sentences, startIndex, endIndex)

    # 022
    # firstName = input("Put your first name : ")
    # secondName = input("Put your second name : ")
    # totlaName = changeFormat(firstName) + " " + changeFormat(secondName)
    # print(f"Your name is {totlaName}")

    # 021
    # firstName = input("Put your first name : ")
    # secondName = input("Put your second name : ")
    # totlaName = firstName + " " + secondName
    # size = getLengh(totlaName)
    # print(f"The length of your name : {size} \nand Your name is {totlaName}")

    # 020
    # name = input("put your name : ")
    # size = getLengh(str(name))
    # print(f"The length of your name : {size}")

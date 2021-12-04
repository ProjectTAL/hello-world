if __name__ == '__main__':

    # 026
    PigLatin = input("Enter the word: ")
    PigLatinlength = len(PigLatin)
    PigLatin1 = PigLatin[1: PigLatinlength]
    PigLatin2 = PigLatin[0]
    if PigLatin[0] == "a" or PigLatin[0] == "e" or PigLatin[0] == "i" or PigLatin[0] == "o" or PigLatin[0] == "u":
        print(PigLatin + "way")
    else:
        print(PigLatin1 + PigLatin2 + "ay")

    # # 025
    # name = input("Please type your name: ")
    # if len(name) < 5:
    #     lastname = input("Please type your lastname")
    #     print(lastname.upper() + name.upper())
    # else:
    #     print(name.lower())

    # 024
    # words = input("Please type anything you want me to say anything: ")
    # print(words.upper())

    # 023
    # index = input("Enter the first line of the lullaby: ")
    # print(len(index))
    # index2 = int(input("Enter the index number you want to start with: "))
    # index3 = int(input("Enter the last index number."))
    # print(index[index2 - 1:index3])

    # 022
    # Name = input("Enter your name in lowercase: ")
    # Name2 = input("Enter your last name in lowercase: ")
    # print(Name.capitalize(), Name2.capitalize())

    # 021
    # Name = input("Enter your name: ")
    # Lastname = input("Enter your last name: ")
    # Linearcontent = len(Name)
    # Linearcontent2 = len(Lastname)
    # print(Name, Lastname, Linearcontent + Linearcontent2)

    # 020
    # nameValue = input("Enter your name: ")
    # name = len(nameValue)
    # print(name)

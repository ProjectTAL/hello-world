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
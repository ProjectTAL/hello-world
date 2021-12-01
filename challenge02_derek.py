import astropy

if __name__ == '__main__':

    # 019
    numValue = int(input("Enter a number between 1 and 3: "))
    if numValue == 1:
        print("Thank you")
    elif numValue == 2:
        print("Well Done")
    elif numValue == 3:
        print("Correct")
    else:
        print("Error message")

    # 018
    # numValue = int(input("Enter number: "))
    # if numValue < 10:
    #     print("Too Low")
    # elif numValue >= 10 and numValue <= 20:
    #     print("Correct")
    # else:
    #     print("Too High")

    # 017
    # numValue = int(input("Enter your age: "))
    # if numValue >= 18:
    #     print("You can vote")
    # elif numValue == 17:
    #     print("You can learn to drive")
    # elif numValue == 16:
    #     print("You can buy a lottery ticket")
    # else:
    #     print("You can go Trick-or-Treating")

    # 016
    # textValue = input("Enter if it's raining right now? ")
    # if textValue.lower() == "yes":
    #     textValue = input("Enter whether it's windy or not? ")
    #     if textValue.lower() == "yes":
    #         print("It is too windy for an umbrella")
    #     else:
    #         print("Take an umbrella")
    # else:
    #     print("Enjoy your day")

    # 015
    # textValue = input("Enter your favorite color: ")
    #
    # if textValue.lower() == "red":
    #     print("I like red too")
    # else:
    #     print("I don't like that colour, I prefer red")

    # 014
    # numValue = int(input("Enter a number between 10 and 20: "))
    # if numValue >= 10 and numValue <= 20:
    #     print("Thank you")
    # else:
    #     print("Incorrect answer")

    # 013
    # numValue = int(input("Enter a number less than 20: "))
    # if numValue >= 20:
    #     print("Too high")
    # else:
    #     print("Thank you")

    # 012
    # numValue = int(input("Enter the first number: "))
    # numValue2 = int(input("Enter the second number: "))
    # if numValue > numValue2:
    #     print(numValue)
    # else:
    #     numValue2 > numValue
    #     print(numValue2)

    # 011
    # numValue = int(input("Enter a number above 100: "))
    # numValue2 = int(input("Please enter a number below 10: "))
    # print(f' {numValue}goes {numValue2}in {numValue / numValue2}in. ')

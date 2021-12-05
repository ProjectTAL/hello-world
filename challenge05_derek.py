import math

if __name__ == '__main__':

    # 044
    party = int(input("How many people will you invite to the party: "))
    if party < 10:
        for i in range(party):
            name = input("Enter name: ")
            print(name, "has been invited")
    else:
        print("Too many people")

    # 043
    # count = input("count down? or count up? : ")
    # if count == "count down":
    #     countdown = int(input("Enter a number below 20: "))
    #     if countdown < 20:
    #         for i in range(1, countdown + 1, +1):
    #             print(i)
    # elif count == "count up":
    #     count2 = int(input("Enter a big number: "))
    #     for i in range(count2, 0, -1):
    #         print(i)
    # else:
    #     print("I don't understand")

    # 042
    # total = 0
    # for i in range(0, 5):
    #     num = int(input("Enter the number: "))
    #     plus = input("Are you going to add it to total (yes) or (no): ")
    #     if plus == "yes":
    #         total = total + num
    #     else:
    #         total = total + 0
    #
    # print("total =", total)

    # 041
    # name = input("Enter your name: ")
    # num = int(input("Enter the number: "))
    # if num < 10:
    #     for i in range(1, num + 1):
    #         print(i, name)
    # else:
    #     print("Too high", "\nToo high", "\nToo high")

    # 040
    # num = int(input("Please enter the number of less than 50: "))
    # for i in range(num, 0, -1):
    #     print(i)

    # for i in range(1, num + 1):
    #     print(i)

    # 039
    # num = int(input("Enter a number between 1 and 12: "))
    # for i in range(1, 13):
    #     print(i, "*", num)

    # 038
    # name = input("Enter your name: ")
    # num = int(input("Enter the number: "))
    # for i in name:
    #     print(i * num)

    # 037
    # name = input("Enter your name: ")
    # for i in name:
    #     print(i)

    # 036
    # name = input("Enter your name: ")
    # num = int(input("Enter the number: "))
    # for i in range(num):
    #     print(i, name)

    # 035
    # name = input("Enter your name: ")
    # print(name, name, name)

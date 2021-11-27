def testPrint(num):
    print(num, " Hello World!")


if __name__ == '__main__':
    # for i in range(1, 10):
    #     testPrint(i)
    # 051
    bottles = 10
    answer = "n"
    while answer == "n":
        print(
            f"There are {bottles} green bottles hanging on the wall, {bottles} green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
        bottles = bottles - 1
        num = int(input("How many green bottles will be hanging on the wall?"))
        if bottles == num:
            answer = "y"
        else:
            print("No, try again")
        if bottles == 0:
            answer = "y"
    if bottles > 0:
        print(f"There will be {bottles} green bottles hanging on the wall")
    else:
        print("There are no more green bottles hanging on the wall")

    # 050
    # num = 0
    # while num >= 20 or num <= 10:
    #     num = int(input("Type the number (10-20) :"))
    #     if num >= 20:
    #         print("Too high")
    #     elif num <= 10:
    #         print("Too low")
    # print("Thank you")

    # 049
    # compnum = 50
    # num = 0
    # count = 0
    # while num != compnum:
    #     num = int(input("Type the number :"))
    #     count = count + 1
    #     if num > compnum:
    #         print("Higher than what i expected..")
    #     elif num < compnum:
    #         print("Lower than what i expected!!")
    # print(f"Well done, you took {count} attempts")

    # 048
    # answer = "yes"
    # count = 0
    # while answer.lower() == "yes":
    #     name = input("Type your friend name :")
    #     print(f"{name} has now been invited")
    #     count = count + 1
    #     answer = input("Keep adding your friend name (yes or no) :")
    # print(f"{count} friends has been invited")

    # 047
    # answer = "y"
    # sum = int(input("Type the number that you want to plus :"))
    # while answer.lower() == "y":
    #     num = int(input("Type one more number :"))
    #     sum = sum + num
    #     answer = input("Type Y if you want to keep adding :")
    # print(f"The total is {sum}.")

    # 046
    # num = 0
    # while num <= 5:
    #     num = int(input("Type the number :"))
    # print(f"Tha last number you entered was a {num}")

    # 045
    # total = 0
    # while total < 50:
    #     num = int(input("Type the number :"))
    #     total = total + num
    #     if total < 50:
    #         print(f"Total : {total}. It will be stop when the total become more than 50")
    #     else:
    #         print("Done")

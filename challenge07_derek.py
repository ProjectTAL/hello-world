import random

if __name__ == '__main__':

    # 059
    # print("red, orange, yellow, blue, black")
    # color = input("Choose one color between red and orange and yellow, blue, black")
    # colour = random.choice(["red", "orange", "yellow", "blue", "black"])
    # while True:
    #     if color == colour:
    #         print("Well done")
    #         break
    #     else:
    #         if color == "red":
    #             print("I bet you are red with envy")
    #         elif color == "orange":
    #             print("I bet you are orange with envy")
    #         elif color == "yellow":
    #             print("I bet you are yellow with envy")
    #         elif color == "blue":
    #             print("I bet you are blue with envy")
    #         elif color == "black":
    #             print("I bet you are black with envy")
    #         color = input("Choose one color between red and orange and yellow, blue, black")

    # 058
    # count = 0
    # for i in range(1, 6):
    #     num1 = random.randint(1, 100)
    #     num2 = random.randint(1, 100)
    #     quiz = int(input("{} + {}: ".format(num1, num2)))
    #     answer = num1 + num2
    #     if quiz == answer:
    #         count = count + 1
    #     else:
    #         count = count + 0
    # print("You got {} questions right.".format(count))

    # count = 1
    # num1 = random.randint(1, 100)
    # num2 = random.randint(1, 100)
    # num3 = random.randint(1, 100)
    # num4 = random.randint(1, 100)
    # num5 = random.randint(1, 100)
    # quiz = int(input("{} + {}: ".format(num1, num2)))
    # quiz1 = num1 + num2
    # if quiz == quiz1:
    #     count = count + 1
    # else:
    #     count = count + 0
    # #----------------------------------------------------
    # quiz = int(input("{} + {}: ".format(num3, num4)))
    # quiz1 = num2 + num4
    # if quiz == quiz1:
    #     count = count + 1
    # else:
    #     count = count + 0

    # 057
    # num = random.randint(0, 10)
    # answer = int(input("{} Choose 1~10: ".format(num)))
    # while True:
    #     if answer == num:
    #         break
    #     else:
    #         if answer < num:
    #             print("up")
    #         else:
    #             print("down")
    #         answer = int(input("{} Choose 1~10: ".format(num)))

    # 056
    # num = random.randint(0, 10)
    # answer = int(input("{} Choose 1~10: ".format(num)))
    # while True:
    #     if answer == num:
    #         break
    #     else:
    #         answer = int(input("{} Choose 1~10: ".format(num)))

    # 055
    # num = random.randint(1, 5)
    # count = 0
    # while True:
    #     if count == 2:
    #         break
    #     if count == 1:
    #         print("Correct")
    #
    #     num2 = int(input("{} Choose 1~5: ".format(num)))
    #     if count == 0 and num2 == num:
    #         print("Well done")
    #         break
    #
    #     else:
    #         if count == 1:
    #             print("You lose")
    #         else:
    #             if num < num2:
    #                 print("down")
    #             else:
    #                 print("up")
    #     count = count + 1
    # 054
    # num2 = random.choice(["h", "t"])
    # num = input("Choose h or t: ")
    # if num == num2:
    #     print("You win")
    # else:
    #     print("Bad luck")

    # 053
    # num = random.choice(["strawberry", "apple", "orange", "banana", "kiwi"])
    # print(num)

    # 052
    # num = random.randint(1, 100)
    # print(num)

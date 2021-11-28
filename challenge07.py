import random


def testPrint(num):
    print(num, " Hello World!")


# 052
def getRandom(start, end):
    ret = random.randint(start, end)
    return ret


if __name__ == '__main__':
    # for i in range(1, 10):
    #     testPrint(i)
    # 059
    result = random.choice(["Yellow", "Blue", "Black", "Red", "White"])
    flag = False
    while not flag:
        answer = input("Type one of the colors among Yellow, Blue, Black, Red and White :")
        if answer == result:
            flag = True
            print("Well done")
        else:
            if result == "Yellow":
                print(f"{result} is my Life")
            elif result == "Blue":
                print(f"I like a {result} shirts")
            elif result == "Black":
                print(f"{result} has many colors")
            elif result == "Red":
                print(f"{result} should be real one")
            else:
                print(f"An angel would love {result} color")

    # 058
    # count = 0
    # for i in range(0, 5):
    #     ranNum1 = random.randint(1, 100)
    #     ranNum2 = random.randint(1, 100)
    #     result = ranNum1 + ranNum2
    #     answer = int(input(f"What do think {ranNum1} + {ranNum2} = ?"))
    #     if result == answer:
    #         count = count + 1
    # if count == 0:
    #     print("All answers are wrong")
    # elif count == 1:
    #     print(f"{count} answer is correct!")
    # else:
    #     print(f"{count} answers are correct!")

    # 056 & 057
    # num = random.randint(1, 10)
    # while not flag:
    #     inNum = int(input("Type the number (1-10) :"))
    #     if num == inNum:
    #         flag = True
    #     else:
    #         if inNum > num:
    #             print("Type the number LOWER than what you typed.")
    #         else:
    #             print("type the number HIGHER than what you typed.")
    # print("You've escaped successfully")

    # 055
    # flag = False
    # while not flag:
    #     num = random.randint(1,5)
    #     inNum = int(input("Type the number that you think (1-5) :"))
    #     if inNum == num:
    #         print("Well done")
    #         flag = True
    #     else:
    #         if inNum > num:
    #             print("Your number is higher than the expected number")
    #         else:
    #             print("Your number is lower than the expected number..")
    #     print(f"\nRandom value was {num}")

    # 054
    # word = random.choice(['h', 't'])
    # text = input("Choose either h or t :")
    # if text == word:
    #     print("You win")
    # else:
    #     print("Bad luck")
    # print(f"\nThe computer returned {word}")

    # 053
    # fruit = random.choice(["apple", "pineapple", "bannana", "orange", "strawberry"])
    # print(f"The fruit randomized from 5 ones is {fruit}")

    # 052
    # num = getRandom(1, 100)
    # print(f"The number randomized from 1 to 100 is {num}")

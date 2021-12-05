import random
from array import *


def printTest():
    print("Hello world!")


if __name__ == '__main__':
    printTest()
    # 095
    numF = array('f', [1.34, 4.25, 3.15, 74.28, 10.43])
    flag = False
    while not flag:
        inNum = int(input("Type the number between 2 and 5 :"))
        if 2 <= inNum <= 5:
            flag = True
            for i in numF:
                print(f"{numF.index(i)} : The result is {round(i / inNum, 2)}")

    # 094
    # nums = array('i', [1, 2, 3, 4, 5])
    # lineText = ""
    # for i in nums:
    #     lineText = lineText + " " + str(i)
    # flag = False
    # while not flag:
    #     inNum = int(input("Choose one of them" + lineText + " :"))
    #     if inNum in nums:
    #         print(f"The index is {nums.index(inNum)}..")
    #         flag = True
    #     else:
    #         print("It is not in the array..")

    # 093
    # nums = array('i', [])
    # for i in range(0, 5):
    #     nums.append(int(input("Type the number :")))
    # nums = sorted(nums)
    # for i in nums:
    #     print(i)
    # num = int(input("Choose one of them :"))
    # nums.remove(num)
    # newNums = array('i', [])
    # newNums.append(num)
    # print("New......")
    # for i in newNums:
    #     print(i)

    # 092
    # nums_1 = array('i', [])
    # nums_2 = array('i', [])
    # for i in range(0, 3):
    #     nums_1.append(int(input("Type the number for 1st array :")))
    # for i in range(0, 5):
    #     nums_2.append(int(input("Type the number for 2nd array :")))
    # nums_1.extend(nums_2)
    # nums_1 = sorted(nums_1)
    # for i in nums_1:
    #     print(i)

    # 091
    # nums = array('i', [1, 2, 3, 4, 1])
    # count = 0
    # for i in nums:
    #     print(i)
    # num = int(input("Type the number of them :"))
    # for i in nums:
    #     if num == i:
    #         count = count + 1
    # print(f"The {count} of the number is present in them")

    # 090
    # flag = False
    # count = 0
    # nums = array('i', [])
    # while not flag:
    #     num = int(input("Input the number from 10 to 20 :"))
    #     if 10 < num < 20:
    #         count = count + 1
    #         nums.append(num)
    #     else:
    #         print("Outside the range!")
    #     if count == 5:
    #         print("Thank you")
    #         flag = True
    # for i in nums:
    #     print(i)

    # 089
    # # nums = array('i', [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)])
    # nums = array('i', [])
    # for x in range(0, 5):
    #     nums.append(random.randint(0, 10))
    # for x in nums:
    #     print(x)

    # 088
    # nums = array('i', [])
    # for i in range(0, 5):
    #     inNum = int(input("Type the number that you want to add :"))
    #     nums.append(inNum)
    # nums = sorted(nums)
    # nums.reverse()
    # for i in nums:
    #     print(i)

    # nums = array('i', [1, 2, 3, 4, 5])
    # plus = array('i', [6, 7, 8, 9])
    # # print(nums)
    # # nums.pop()
    #
    # nums.extend(plus)
    # for x in nums:
    #     print(x)

import random
from array import *

# 095
# nums = array('f', [26.19, 32.51, 56.27, 82.64, 27.18])
# num = int(input("Enter the number(2-5): "))
# while True:
#     if 5 >= num >= 2:
#         break
#     else:
#         print('Error')
#         num = int(input("Enter the number(2-5): "))
# total1 = 26.19 / num
# total2 = 32.51 / num
# total3 = 56.27 / num
# total4 = 82.64 / num
# total5 = 27.18 / num
# print(round(total1, 2))
# print(round(total2, 2))
# print(round(total3, 2))
# print(round(total4, 2))
# print(round(total5, 2))


# 094
# nums = array('i', [])
# for i in range(0, 5):
#     num = random.randint(1, 100)
#     nums.append(num)
# print(nums)
# num2 = int(input("Enter the number: "))
# while True:
#     if num2 in nums:
#         print(nums.index(num2))
#         break
#     else:
#         num2 = int(input("Enter the number: "))

# flag = True
# for i in nums:
#     if num2 == i:
#         print(nums.index(num2))
#         flag = True
#         break

# 093
# num2 = array('i', [])
# nums = array('i', [])
# for i in range(0, 5):
#     newValue = int(input("Enter the number: "))
#     nums.append(newValue)
# nums = sorted(nums)
# print(nums)
# elimination = int(input("Enter item index: "))
# nums.remove(elimination)
# num2.append(elimination)
# print("nums Arrangement.", nums)
# print("num2 Arrangement.", num2)
# 092
# Arrangement1 = array('i', [])
# Arrangement2 = array('i', [])
# for i in range(0, 3):
#     newvalue = int(input("enter the number: "))
#     Arrangement1.append(newvalue)
# for i in range(0, 5):
#     num1 = random.randint(1, 100)
#     Arrangement2.append(num1)
# Arrangement1.extend(Arrangement2)
# Arrangement1 = sorted(Arrangement1)
# print(Arrangement1)

# 091
# nums = array('i', [])
# num1 = random.randint(1, 100)
# nums.append(num1)
# num2 = random.randint(1, 100)
# nums.append(num2)
# num3 = random.randint(1, 100)
# nums.append(num3)
# nums.append(num1)
# num4 = random.randint(1, 100)
# nums.append(num4)
# print(nums)
# num6 = int(input("Enter the number"))
# print(nums.count(num6))

# 090
# nums = array('i', [])
# for i in range(0, 5):
#     num = int(input("Enter the number"))
#     if num >= 10 and num <= 20:
#         nums.append(num)
#     else:
#         print("Otherside the range")
# print("Thank you")
# for x in nums:
#     print(x)

# 089
# nums = array('i', [])
# for i in range(0, 5):
#     newvalue = random.randint(1, 100)
#     nums.append(newvalue)
# for i in nums:
#     print(i)

# 088
# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))
# num3 = int(input("Enter the number: "))
# num4 = int(input("Enter the number: "))
# num5 = int(input("Enter the number: "))
# nums = array('i', [num1, num2, num3, num4, num5])
# nums.reverse()
# print(nums)

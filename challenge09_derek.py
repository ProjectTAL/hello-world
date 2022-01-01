import random

# 079
# count = 0
# num_list = []
# for i in range(0, 3):
#     num_list.append(input("Enter the number: "))
#     count = count + 1
# quiz = input("Are you going to save the last number(y or n): ")
# if quiz == "n":
#     del num_list[2]
#     print(num_list)
# else:
#     print(num_list)
# 078
# testing = "Sooo"
# print("Hello {} world".format(testing))
#
# tv_list = ["running man", "Infinite Challenge", "I live by myself", "Please take care of the cat"]
# print("running man\nInfinite Challenge\nI live by myself\nPlease take care of the cat")
# other = input("Enter other tv program: ")
# Location = int(input("Enter the location of the title you want: "))
# tv_list.insert(Location, other)
# print(tv_list)

# 077
# count = 0
# names_list = []
# for i in range(0, 3):
#     names_list.append(input("Enter the name of the person you want to invite to the party: "))
#     count = count + 1
# add = input("Is there anyone who wants to add it (y or n): ")
# while add == "y":
#     names_list.append(input("Enter the name of the person you want to invite to the party: "))
#     count = count + 1
#     add = input("Is there anyone who wants to add it (y or n): ")
# print(names_list)
# index = input("Please enter one of the names: ")
# print(names_list.index(index))
# total = names_list.index(index)
# real = input("Will you really invite him/her to the party: ")
# if real == "n":
#     del names_list[total]
#     print(names_list)
# else:
#     print(names_list)
# 076
# count = 0
# names_list = []
# for i in range(0, 3):
#     names_list.append(input("Enter the name of the person you want to invite to the party: "))
#     count = count + 1
# add = input("Is there anyone who wants to add it (y or n): ")
# while add == "y":
#     names_list.append(input("Enter the name of the person you want to invite to the party: "))
#     count = count + 1
#     add = input("Is there anyone who wants to add it (y or n): ")
# print("{} people have been invited.".format(count))

# 075
# num1 = random.randint(100, 999)
# num2 = random.randint(100, 999)
# num3 = random.randint(100, 999)
# num4 = random.randint(100, 999)
# num_tuple = (num1, num2, num3, num4)
# print("{}\n{}\n{}\n{}".format(num1, num2, num3, num4))
# quiz = int(input("Enter the number: "))
# if quiz == num1:
#     print(num_tuple.index(num1))
# elif quiz == num2:
#     print(num_tuple.index(num2))
# elif quiz == num3:
#     print(num_tuple.index(num3))
# elif quiz == num4:
#     print(num_tuple.index(num4))
# else:
#     print("That is not in the list")

# 074
# colour_tuple = ("red", "orange", "yellow", "green", "blue", "indigo", "purple", "brown", "black", "white")
# num1 = int(input("Enter the number 0~4"))
# num2 = int(input("Enter the number 5~9"))
# for i in range(num1, num2):
#     print(colour_tuple[i])

# 073
# colours = {}
# c
#     answer = input("Enter your {} favorite food: ".format(i))
#     colours[i] = answer
# # colours = {1:,2:,3:,4:}
#
# for i in colours:
#     print(i, colours[i])
#
# answer = int(input("Enter food that you want to remove :"))
# colours.pop(answer)
# for i in colours:
#     print(i, colours[i])

# 072
# names_list = ["Sports", "Math", "Science", "English", "Korean", "Technology and home economics"]
# num = input("What subject do you hate? : ")
# for i in names_list:
#     if i == num:
#         names_list.remove(num)
# for i in names_list:
#     print(i)


# 071
# names_list = ["cycle", "soccer"]
# names_list.append(input("What is your favorite sports: "))
# names_list.sort()
# print(names_list)

# 070
# fruit_tuple = ("korea", "china", "japan", "turkey", "canada")
# print(fruit_tuple)
# flag = int(input("Enter the number: "))
# print(fruit_tuple[flag])

# 069
# fruit_tuple = ("korea", "china", "japan", "turkey", "canada")
# print(fruit_tuple)
# flag = input("Enter one of the names of the countries above: ")
# print(fruit_tuple.index(flag))

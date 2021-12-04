def printTest():
    print("Hello world!")


if __name__ == '__main__':
    # printTest()
    # 079
    nums = []
    count = 0
    flag = False
    while not flag:
        inNum = int(input("Type the number :"))
        nums.append(inNum)
        count = count + 1
        if count >= 3:
            answer = input("Will you save the last number? ")
            if answer == 'n':
                nums.remove(inNum)
                break
    for i in nums:
        print(i)

    # 078
    # programs_list = ["star", "computers", "run", "ask to her"]
    # for i in programs_list:
    #     print(i)
    # inProg = input("Type the other program name :")
    # inOrder = int(input("What order do you want to add? (0-5)"))
    # programs_list.insert(inOrder, inProg)
    # for i in programs_list:
    #     print(i)

    # 077
    # names_list = []
    # for i in range(0, 3):
    #     names_list.insert(i, input("Type your name to invite the party:"))
    # answer = 'name..'
    # count = 0
    # while answer != 'n':
    #     answer = input("Add more name : (If you don't want to add, then n) :")
    #     if answer == 'n':
    #         break
    #     names_list.append(answer)
    #     count = count + 1
    # for i in names_list:
    #     print(i)
    # inName = input("Type one of the names in the list :")
    # for i in names_list:
    #     if i == inName:
    #         answer = input(f"The person's order is {names_list.index(inName)}. Do you really invite her/him?")
    #         if answer == 'n':
    #             names_list.remove(inName)
    # for i in names_list:
    #     print(i)
# for i in numbers_list:
#     if i == inNum:
#         print(numbers_list.index(inNum))
# print(f"You invited {count + 3} persons")


# 076
# names_list = []
# for i in range(0, 3):
#     names_list.insert(i, input("Type your name to invite the party:"))
# answer = 'name..'
# count = 0
# while answer != 'n':
#     answer = input("Add more name : (If you don't want to add, then n) :")
#     if answer == 'n':
#         break
#     names_list.append(answer)
#     count = count + 1
# print(f"You invited {count + 3} persons")

# 075
# numbers_list = [123, 456, 789, 147]
# for i in numbers_list:
#     print(i)
# inNum = int(input("Type the number :"))
# flag = False
# for i in numbers_list:
#     if i == inNum:
#         print(numbers_list.index(inNum))
#         flag = True
# if not flag:
#     print("That is not in the list")

# 074
# colors_list = ["black", "blue", "sky", "yellow", "white", "pink", "red", "green", "gold", "blur"]
# startNum = int(input("Type the number (0-4) :"))
# endNum = int(input("Type the number (5-9) :"))
# for i in range(startNum, endNum + 1):
#     print(colors_list[i])

# 073
# food_list = {}
# for i in range(0, 4):
#     inFood = input("What food do you like the most?")
#     food_list[i + 1] = inFood
# for i in range(0, 4):
#     print(f"{i + 1} : {food_list[i + 1]}")
# removeFood = input("What food do you want to eliminate?")
# for i in range(0, 4):
#     if food_list[i + 1] == removeFood:
#         # food_list.pop(i+1)
#         del food_list[i + 1]
# # print(sorted(food_list.values()))
# for i in food_list:
#     print(food_list[i])

# 072
# class_list = ["math", "korean", "english", "science", "Athletic", "music"]
# inClass = input("What class do you want to remove? ")
# class_list.remove(inClass)
# for i in class_list:
#     print(i)

# 071
# sports_list = ["baseball", "basketball"]
# inSport = input("What sports do you like the most :")
# sports_list.append(inSport)
# for i in sports_list:
#     print(i)

# 069 & 070
# countries = ("korea", "usa", "turkey", "japan", "china")
# for i in countries:
#     print(i)
# orderCountry = int(input("Type the country order :"))
# print(f"The country that you chose is {countries[orderCountry - 1]}")
# inCountry = input("Type the country name :")
# print(f"The index that you chose is {countries.index(inCountry)}")

# x = [100, 200, 300]
# #num = int(input("Type the text :"))
# x.insert(2, 250)
# x.remove(100)
# x.append(1000)
# for i in x:
#     print(i)

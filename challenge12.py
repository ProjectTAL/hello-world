def printTest():
    print("Hello world!")


if __name__ == '__main__':
    printTest()
    # 104
    table_list = {}
    for i in range(0, 4):
        name = input(f"Type {i}'s name : ")
        age = int(input(f"Type {i}'s age : "))
        size = int(input(f"Type {i}'s size : "))
        table_list[name] = {"age": age, "size": size}
    name = input("Type the name that you want to remove :")
    table_list.pop(name)
    for i in table_list:
        print(i, table_list[i])

    # 103
    # table_list = {}
    # for i in range(0, 4):
    #     name = input(f"Type {i}'s name : ")
    #     age = int(input(f"Type {i}'s age : "))
    #     size = int(input(f"Type {i}'s size : "))
    #     table_list[name] = {"age": age, "size": size}
    # for i in table_list:
    #     print(i, table_list[i]["age"])

    # 102
    # table_list = {}
    # for i in range(0, 4):
    #     name = input(f"Type {i}'s name : ")
    #     age = int(input(f"Type {i}'s age : "))
    #     size = int(input(f"Type {i}'s size : "))
    #     table_list[name] = {"age": age, "size": size}
    # name = input("Type the name that you want to see the age and name :")
    # print(table_list[name])

    # 101
    # table_list = {"John": {"N": 3056, "S": 8463, "E": 8341, "W": 2694},
    #               "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    #               "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    #               "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
    # name = input("Type the name : ")
    # region = input("Type the region name : ")
    # print(table_list[name][region])
    #
    # changedName = input("Type the name that you want to change : ")
    # changedRegion = input("Type the region name that you want to change : ")
    # value = int(input("Type the value that you want to change"))
    # print(f"Before : {table_list[changedName][changedRegion]}")
    # table_list[changedName][changedRegion] = value
    # print(f"After : {table_list[changedName][changedRegion]}")

    # 100
    # table_list = {"John": {"N": 3056, "S": 8463, "E": 8341, "W": 2694},
    #               "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    #               "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    #               "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
    # for i in table_list:
    #     print(i)
    #     print(table_list[i])

    # 099
    # table_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
    # row = int(input("Type the row :"))
    # print(table_list[row])
    # column = int(input("Type the column :"))
    # print(table_list[row][column])
    # answer = input("Do you want to modify the value (y/n) ?")
    # if answer == "y":
    #     changedValue = int(input("Type the value that will be changed :"))
    #     table_list[row][column] = changedValue
    #     print(table_list[row])
    # else:
    #     print("End~!")

    # 098
    # table_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
    # row = int(input("Type the row :"))
    # print(table_list[row])
    # value = int(input("Type the value that you want to add in the row :"))
    # table_list[row].append(value)
    # print(table_list[row])

    # 096 & 097
    # table_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
    # row = int(input("Type the row :"))
    # column = int(input("Type the column :"))
    # print(f"You chose {table_list[row][column]}")

    # grades = {"show":{"j": 1, "t": 2}, "tomas":{"t": 5, "as": 76}}
    # print(grades["show"]["t"])
    # # print(grades[1]["t"])
    # grades = [[1,2], [3,4], [5,6]]
    # print(grades[0])

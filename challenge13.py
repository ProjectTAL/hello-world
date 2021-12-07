def printTest():
    print("Hello world!")


if __name__ == '__main__':
    printTest()
    # 110
    file = open("Names.txt", "r")
    print(file.read())
    file.close()
    file = open("Names.txt", "r")
    name = input("Type the name that you want to remove :")
    name = name + "\n"
    file2 = open("Names2.txt", "w")
    file2.close()
    for i in file:
        if i != name:
            file2 = open("Names2.txt", "a")
            file2.write(i)

    # 109
#     print("""1) Create a new file
# 2) Display the file
# 3) Add a new item to the file""")
#     num = int(input("Make a selection 1, 2, or 3:"))
#     if num == 1:
#         subject = input("Type the class name :")
#         file = open("Subject.txt", "w")
#         file.write(subject + "\n")
#         file.close()
#     elif num == 2:
#         file = open("Subject.txt", "r")
#         print(file.read())
#         file.close()
#     elif num == 3:
#         subject = input("Type new subject :")
#         file = open("Subject.txt", "a")
#         file.write(subject)
#         file.close()
#         file = open("Subject.txt", "r")
#         print(file.read())

# 108
# file = open("Names.txt", "a")
# name = input("Type the name that you want to add :")
# file.write(name + "\n")
# file.close()
# file = open("Names.txt", "r")
# print(file.read())

# 107
# file = open("Names.txt", "r")
# print(file.read())

# 106
# file = open("Names.txt", "w")
# file.write("Tomas\n")
# file.write("James\n")
# file.write("Ace\n")
# file.write("Four\n")
# file.write("Tool\n")
# file.close()

# 105
# file = open("Numbers.txt", "w")
# # file.write("1,2,3,4,5")
# file.write("1, ")
# file.write("2, ")
# file.write("3, ")
# file.write("4, ")
# file.write("5, ")
# file.close()

# file = open("Countreis.txt", "a")
# file.write("France\n")
# file.close()
# file = open("Countreis.txt", "r")
# print(file.read())
# file = open("Countreis.txt", "w")
# file.write("Itally\n")
# file.write("Germany\n")
# file.write("Spain\n")
# file.close()

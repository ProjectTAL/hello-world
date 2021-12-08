import csv
import random


def printTest():
    print("Hello world!")


if __name__ == '__main__':
    printTest()
    # 117
    name = input("Enter name :")
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question1 = str(num1) + " + " + str(num2) + " ="
    answer1 = input(str(question1))
    question2 = str(num1) + " * " + str(num2) + " ="
    answer1 = input(str(question2))
    file = open("quiz.csv", "a")
    line = name + "," + question1 + "," + answer1 + "\n"
    file.write(str(line))

    # 116
    # file = list(csv.reader(open("Books.csv")))
    # tmp = []
    # for row in file:
    #     tmp.append(row)
    # x = 0
    # for row in tmp:
    #     print(f"{x} : {row}")
    #     x = x + 1
    #
    # remove = int(input("Enter row number that you want to remove : "))
    # del tmp[remove]
    # x = 0
    # for row in tmp:
    #     print(f"{x} : {row}")
    #     x = x + 1
    # modification = int(input("Enter row number that you want to modify :"))
    # title = input("Enter title : ")
    # name = input("Enter name : ")
    # year = input("Published year : ")
    # tmp[modification][0] = title
    # tmp[modification][1] = name
    # tmp[modification][2] = year
    # x = 0
    # for row in tmp:
    #     print(f"{x} : {row}")
    #     x = x + 1
    # file = open("Books.csv", "w")
    # x = 0
    # for row in tmp:
    #     newRecord = tmp[x][0] + "," + tmp[x][1] + "," + tmp[x][2] + "\n"
    #     file.write(str(newRecord))
    #     x = x + 1
    # file.close()

    # 115
    # file = list(csv.reader(open("Books.csv")))
    # tmp = []
    # for row in file:
    #     tmp.append(row)
    # x = 0
    # for row in tmp:
    #     print(f"{x} : {row}")
    #     x = x + 1

    # 114
    # file = list(csv.reader(open("Books.csv")))
    # tmp = []
    # for row in file:
    #     tmp.append(row)
    # x = 0
    # startYear = int(input("Enter staring year :"))
    # endYear = int(input("Enter ending year :"))
    # for row in tmp:
    #     if startYear <= int(tmp[x][2]) <= endYear:
    #         print(row)
    #     x = x + 1

    # 113
    # count = int(input("How many record do you want to add?"))
    # file = open("Books.csv", "a")
    # for i in range(0, count):
    #     title = input("Enter title : ")
    #     name = input("Enter name : ")
    #     year = input("Published year : ")
    #     newRecord = title + "," + name + "," + year + "\n"
    #     file.write(str(newRecord))
    # file.close()
    # file = open("Books.csv", "r")
    # search = input("Enter name to search:")
    # flag = False
    # x = 0
    # for row in file:
    #     if search in str(row):
    #         print(row)
    #         flag = True
    #         break;
    # file.close()
    # if not flag:
    #     print("Couldn't find any word in the document!")

    # 112
    # file = open("Books.csv", "a")
    # title = input("Enter title : ")
    # name = input("Enter name : ")
    # year = input("Published year : ")
    # newRecord = title + "," + name + "," + year + "\n"
    # file.write(str(newRecord))
    # file.close()
    # file = open("Books.csv", "r")
    # for row in file:
    #     print(row)

    # 111
    # file = open("Books.csv", "w")
    # file.write("To Kill A Mockingbird, Harper Lee, 1960\n")
    # file.write("A Brief History of Time, Stephen Hawking, 1988\n")
    # file.write("The Great Gatsby, F.Scott Fitgerald, 1922\n")
    # file.write("The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n")
    # file.write("Pride and Prejudice, Jane Austen, 1813\n")
    # file.close()

    # file = open("Stars.csv", "w")
    # newRecord = "Brian,73,Taurus\n"
    # file.write(str(newRecord))
    # file.close()

    # file = list(csv.reader(open("Stars.csv")))
    # tmp = []
    # for row in file:
    #     tmp.append(row)
    # # for row in tmp:
    # #     print(row)
    # file = open("NewStars.csv", "w")
    # x = 0
    # for row in tmp:
    #     newRec = tmp[x][0] + "," + tmp[x][1] + "," +tmp[x][2] + "\n"
    #     file.write(newRec)
    #     x = x + 1
    # file.close()

    # file = open("Stars.csv", "r")
    # search = input("Enter the data you are searching for : ")
    # for row in file :
    #     if search in str(row):
    #         print(row)

    # file = open("Stars.csv", "r")
    # reader = csv.reader(file)
    # rows= list(reader)
    # print(rows[1])

    # file = open("Stars.csv", "r")
    # for row in file:
    #     print(row)

    # file = open("Stars.csv", "a")
    # name = input("Enter name : ")
    # age = input("Enter age : ")
    # star = input("Enter star sign : ")
    # newRecord = name + "," + age + "," + star + "\n"
    # file.write(str(newRecord))
    # file.close()

    # file = open("Stars.csv", "w")
    # newRecord = "Brian,73,Taurus\n"
    # file.write(str(newRecord))
    # file.close()

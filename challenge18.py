import sqlite3
import time
from tkinter import *


def printTest():
    print("Hello world!")


# # 140
# def showMenu():
#     print("""Main menu
#
# 1) View phone book
# 2) Add to phone book
# 3) Search for surname
# 4) Delete person from phone book
# 5) Quit""")
#
#
# def viewPhoneBook():
#     with sqlite3.connect("data/db/PhoneBook.db") as db:
#         cursor = db.cursor()
#     cursor.execute("SELECT * FROM Names")
#     for x in cursor.fetchall():
#         print(x)
#     # print(cursor.fetchall())
#     db.close()
#
#
# def addNewRec():
#     newId = input("Enter ID number :")
#     newNameFirst = input("Enter First name :")
#     newNameLast = input("Enter Last name :")
#     newNumber = input("Enter number :")
#     with sqlite3.connect("data/db/PhoneBook.db") as db:
#         cursor = db.cursor()
#     cursor.execute("""INSERT INTO Names(id,namefirst,namelast,number)
#         VALUES(?,?,?,?)""", (newId, newNameFirst, newNameLast, newNumber))
#     db.commit()
#     db.close()
#
#
# def searchSurname():
#     surName = input("Enter Last name :")
#     with sqlite3.connect("data/db/PhoneBook.db") as db:
#         cursor = db.cursor()
#     cursor.execute("SELECT * FROM Names WHERE namelast=?", [surName])
#     for x in cursor.fetchall():
#         print(x)
#     db.close()
#
#
# def deleteRecord():
#     delId = input("Enter id number to delete :")
#     with sqlite3.connect("data/db/PhoneBook.db") as db:
#         cursor = db.cursor()
#     # cursor.execute("DELETE Names WHERE id=?", (int(delId)))
#     cursor.execute("DELETE FROM Names WHERE id=?", [delId])
#     db.commit()
#     db.close()

# 142 & 143 & 144
# def showAuthorsTable():
#     with sqlite3.connect("data/db/BookInfo.db") as db:
#         cursor = db.cursor()
#     cursor.execute("SELECT * FROM Authors")
#     for x in cursor.fetchall():
#         print(x)
#
#
# def showHometownsFromBooksTable(town):
#     with sqlite3.connect("data/db/BookInfo.db") as db:
#         cursor = db.cursor()
#     cursor.execute("SELECT * FROM Authors WHERE hometown=?", [town])
#     for row in cursor.fetchall():
#         author = str(row[0])
#         # print(row[0])
#         cursor.execute("SELECT * FROM Books WHERE author=?", [author])
#         for inRow in cursor.fetchall():
#             print(inRow)
#     db.close()
#
#
# def showBooksListAfterYear(year):
#     with sqlite3.connect("data/db/BookInfo.db") as db:
#         cursor = db.cursor()
#     cursor.execute("SELECT * FROM Books WHERE publish>? ORDER BY publish", [int(year)])
#     for row in cursor.fetchall():
#         print(row)
#     db.close()
#
#
# def saveAllToTextFile(author):
#     with sqlite3.connect("data/db/BookInfo.db") as db:
#         cursor = db.cursor()
#     cursor.execute("SELECT * FROM Books WHERE author=?", [author])
#     file = open("data/file/bookInfo.txt", "a")
#     for row in cursor.fetchall():
#         # print(row[0],row[1],row[2],row[3])
#         newRec = str(row[0]) + " - " + row[1] + " - " + row[2] + " - " + str(row[3]) + "\n"
#         file.write(str(newRec))
#     file.close()
#     db.close()

# 145
def initSQL():
    with sqlite3.connect("data/db/TestScore.db") as db:
        cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Scores(
        name text NOT NULL,
        grade text NOT NULL);""")
    db.close()


def addSQL():
    name = edit.get()
    grade = editGrade.get()
    with sqlite3.connect("data/db/TestScore.db") as db:
        cursor = db.cursor()
    cursor.execute("""INSERT INTO Scores(name,grade)
        VALUES(?,?)""", (name, grade))
    db.commit()
    db.close()


def clearSQL():
    name = edit.get()
    grade = editGrade.get()
    with sqlite3.connect("data/db/TestScore.db") as db:
        cursor = db.cursor()
    cursor.execute("DELETE FROM Scores WHERE name=?", [name])
    db.commit()
    db.close()


if __name__ == '__main__':
    printTest()
    # 145
    initSQL()

    window = Tk()
    window.title("TestScore")
    window.geometry("550x200")
    window.resizable(0, 0)

    label = Label(window, text="Enter student's name:")
    label.place(x=50, y=40)
    edit = Entry(window, width=40, textvariable=str)
    edit.place(x=200, y=40)

    labelGrade = Label(window, text="Enter student's grade:")
    labelGrade.place(x=50, y=80)
    editGrade = Entry(window, width=40, textvariable=str)
    editGrade.place(x=200, y=80)

    addButton = Button(text="Add", command=addSQL)
    addButton.place(x=200, y=120, width=100, height=30)

    addButton = Button(text="Clear", command=clearSQL)
    addButton.place(x=340, y=120, width=100, height=30)

    window.mainloop()

    # 142 & 143 & 144
    # showAuthorsTable()
    # inHometown = input("Enter the hometown :")
    # showHometownsFromBooksTable(inHometown)
    # yPublish = input("Enter the year :")
    # showBooksListAfterYear(yPublish)
    # name = input("Enter the author :")
    # saveAllToTextFile(name)

    # 141
    # with sqlite3.connect("data/db/BookInfo.db") as db:
    #     cursor = db.cursor()
    # cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
    #     name text NOT NULL,
    #     hometown text NOT NULL);""")
    # cursor.execute("""INSERT INTO Authors(name,hometown)
    #     VALUES("Agatha Christie","Torquay")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Authors(name,hometown)
    #     VALUES("Cecelia Ahern","Dublin")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Authors(name,hometown)
    #     VALUES("J.K. Rowling","Bristol")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Authors(name,hometown)
    #     VALUES("Oscar Wilde","Dublin")""")
    # db.commit()
    #
    # cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
    #     id integer PRIMARY KEY,
    #     title text NOT NULL,
    #     author text NOT NULL,
    #     publish integer);""")
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #     VALUES("1","De Profundis","Oscar Wilde","1905")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #         VALUES("2","Harry Potter and the chamber of secrets","J.K. Rowling","1998")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #         VALUES("3","Harry Potter and the prisoner of Azkaban","J.K. Rowling","1999")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #         VALUES("4","Lyrebird","Cecelia Ahern","2017")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #         VALUES("5","Murder on the Orient Express","Agatha Christie","1934")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #         VALUES("6","Perfect","Cecelia Ahern","2017")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #         VALUES("7","The marble collector","Cecelia Ahern","2016")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #         VALUES("8","The murder on the links","Agatha Christie","1923")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #         VALUES("9","The picture of Dorian Gray","Oscar Wilde","1890")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #         VALUES("10","The secret adversary","Agatha Christie","1921")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #         VALUES("11","The seven dials mystery","Agatha Christie","1929")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Books(id,title,author,publish)
    #         VALUES("12","The year I met you","Cecelia Ahern","2014")""")
    # db.commit()
    # db.close()

    # 140
    # flag = False
    # while not flag:
    #     showMenu()
    #     number = int(input("\nEnter your selection :"))
    #     if number == 5:
    #         flag = True
    #     elif number == 1:
    #         viewPhoneBook()
    #         time.sleep(2)
    #     elif number == 2:
    #         addNewRec()
    #     elif number == 3:
    #         searchSurname()
    #         time.sleep(2)
    #     elif number == 4:
    #         deleteRecord()

    # 139
    # with sqlite3.connect("data/db/PhoneBook.db") as db:
    #     cursor = db.cursor()
    # cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
    #     id integer PRIMARY KEY,
    #     namefirst text NOT NULL,
    #     namelast text NOT NULL,
    #     number text NOT NULL);""")
    # cursor.execute("""INSERT INTO Names(id,namefirst,namelast,number)
    #     VALUES("1","Simon","Howels","01223 349752")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Names(id,namefirst,namelast,number)
    #     VALUES("2","Karen","Phillips","01954 295773")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Names(id,namefirst,namelast,number)
    #     VALUES("3","Darren","Smith","01583 749012")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Names(id,namefirst,namelast,number)
    #     VALUES("4","Anne","Jones","01323 567322")""")
    # db.commit()
    # cursor.execute("""INSERT INTO Names(id,namefirst,namelast,number)
    #     VALUES("5","Mark","Smith","01223 855534")""")
    # db.commit()
    # db.close()

    # with sqlite3.connect("data/db/company.db") as db:
    #     cursor = db.cursor()
    #
    # # cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
    # #     id integer PRIMARY KEY,
    # #     name text NOT NULL,
    # #     dept text NOT NULL,
    # #     salary integer);""")
    # # cursor.execute("""INSERT INTO employees(id,name,dept,salary)
    # #     VALUES("2","Bob","Sales","25000")""")
    # # db.commit()
    # #
    # # newId = input("Enter ID number :")
    # # newName = input("Enter name :")
    # # newDep = input("Enter department :")
    # # newSalary = input("Enter salary :")
    # # cursor.execute("""INSERT INTO employees(id,name,dept,salary)
    # #     VALUES(?,?,?,?)""", (newId, newName, newDep, newSalary))
    # # db.commit()
    #
    # # cursor.execute("SELECT * FROM employees")
    # # # print(cursor.fetchall())
    # # for x in cursor.fetchall():
    # #     print(x)
    # # cursor.execute("SELECT * FROM employees WHERE dept='Sales'")
    # # for x in cursor.fetchall():
    # #     print(x)
    # db.close()

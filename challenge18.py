import sqlite3
import time


def printTest():
    print("Hello world!")


# 140
def showMenu():
    print("""Main menu

1) View phone book
2) Add to phone book
3) Search for surname
4) Delete person from phone book
5) Quit""")


def viewPhoneBook():
    with sqlite3.connect("data/db/PhoneBook.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    # print(cursor.fetchall())
    db.close()


def addNewRec():
    newId = input("Enter ID number :")
    newNameFirst = input("Enter First name :")
    newNameLast = input("Enter Last name :")
    newNumber = input("Enter number :")
    with sqlite3.connect("data/db/PhoneBook.db") as db:
        cursor = db.cursor()
    cursor.execute("""INSERT INTO Names(id,namefirst,namelast,number)
        VALUES(?,?,?,?)""", (newId, newNameFirst, newNameLast, newNumber))
    db.commit()
    db.close()


def searchSurname():
    surName = input("Enter Last name :")
    with sqlite3.connect("data/db/PhoneBook.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM Names WHERE namelast=?", [surName])
    for x in cursor.fetchall():
        print(x)
    db.close()


def deleteRecord():
    delId = input("Enter id number to delete :")
    with sqlite3.connect("data/db/PhoneBook.db") as db:
        cursor = db.cursor()
    # cursor.execute("DELETE Names WHERE id=?", (int(delId)))
    cursor.execute("DELETE FROM Names WHERE id=?", [delId])
    db.commit()
    db.close()


if __name__ == '__main__':
    printTest()
    # 140
    flag = False
    while not flag:
        showMenu()
        number = int(input("\nEnter your selection :"))
        if number == 5:
            flag = True
        elif number == 1:
            viewPhoneBook()
            time.sleep(2)
        elif number == 2:
            addNewRec()
        elif number == 3:
            searchSurname()
            time.sleep(2)
        elif number == 4:
            deleteRecord()

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

import os.path
import sqlite3
from tkinter import *
from os.path import exists


def initSQL():
    if os.path.exists("data/db/ArtGallery.db"):
        print("db file exists")
        return
    with sqlite3.connect("data/db/ArtGallery.db") as db:
        cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Address(
        id integer PRIMARY KEY,
        name text NOT NULL,
        address text NOT NULL,
        town text NOT NULL,
        country text NOT NULL,
        postcode text NOT NULL);""")
    cursor.execute("""INSERT INTO Address(id,name,address,town,country,postcode)
            VALUES("1","Martin Leighton","5 Park Place","Peterborough","Cambridgeshire","PE32 5LP")""")
    db.commit()
    cursor.execute("""INSERT INTO Address(id,name,address,town,country,postcode)
            VALUES("2","Eva Czarniecka","77 Warner Close","Chelmsford","Essex","CM22 5FT")""")
    db.commit()
    cursor.execute("""INSERT INTO Address(id,name,address,town,country,postcode)
            VALUES("3","Roxy Parkin","90 Hindhead Road","","London","SE12 6WM")""")
    db.commit()
    cursor.execute("""INSERT INTO Address(id,name,address,town,country,postcode)
            VALUES("4","Nigel Farnworth","41 Whitby Road","Huntly","Aberdeenshire","AB54 5PN")""")
    db.commit()
    cursor.execute("""INSERT INTO Address(id,name,address,town,country,postcode)
            VALUES("5","Teresa Tanner","70 Guild Street","","London","NW7 1SP")""")
    db.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Gallery(
        id integer PRIMARY KEY,
        arid integer,
        title text NOT NULL,
        medium text NOT NULL,
        price integer);""")
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("1","5","Woman with black Labrador","Oil","220")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("2","5","Bees & thistles","Watercolour","85")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("3","2","A stroll to Westminster","Ink","190")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("4","1","African giant","Oil","800")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("5","3","Water daemon","Acrylic","1700")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("6","4","A seagull","Watercolour","35")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("7","1","Three friends","Oil","1800")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("8","2","Summer breeze 1","Acrylic","1350")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("9","4","Mr Hamster","Watercolour","35")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("10","1","Pulpit Rock, Dorset","Oil","600")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("11","5","Trawler Dungeness beach","Oil","195")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("12","2","Dance in the snow","Oil","250")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("13","4","St Tropez port","Ink","45")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("14","3","Pirate assassin","Acrylic","420")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("15","1","Morning walk","Oil","800")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("16","4","A baby barn swallow","Watercolour","35")""")
    db.commit()
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES("17","4","The old working mills","Ink","395")""")
    db.commit()
    db.close()


def addAddress():
    print("addAddress")
    print(editAuthor1.get())
    print(editAddress1.get())
    print(editTown1.get())
    print(editCountry1.get())
    print(editPostcode1.get())
    with sqlite3.connect("data/db/ArtGallery.db") as db:
        cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Address(
        id integer PRIMARY KEY,
        name text NOT NULL,
        address text NOT NULL,
        town text NOT NULL,
        country text NOT NULL,
        postcode text NOT NULL);""")
    cursor.execute("""INSERT INTO Address(id,name,address,town,country,postcode)
            VALUES(?,?,?,?,?,?)""", (
        None, editAuthor1.get(), editAddress1.get(), editTown1.get(), editCountry1.get(), editPostcode1.get()))
    db.commit()
    db.close()


def addGallery():
    print("addGallery")
    print(editAuthor2.get())
    print(editTitle2.get())
    print(editMedium2.get())
    print(editPrice2.get())

    with sqlite3.connect("data/db/ArtGallery.db") as db:
        cursor = db.cursor()

    cursor.execute("SELECT * FROM Address WHERE name=?", [editAuthor2.get()])
    authId = 0
    for inRow in cursor.fetchall():
        if inRow[1] == editAuthor2.get():
            authId = int(inRow[0])
            print("Same {}".format(inRow[0]))
    cursor.execute("""INSERT INTO Gallery(id,arid,title,medium,price)
            VALUES(?,?,?,?,?)""", (None, authId, editTitle2.get(), editMedium2.get(), editPrice2.get()))
    db.commit()
    db.close()


def selectBuyGallery():
    sel = selectGallery.get()
    print("selectBuyGallery : {}".format(str(sel)))
    with sqlite3.connect("data/db/ArtGallery.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM Gallery WHERE title=?", [sel])
    delId = -1
    for inRow in cursor.fetchall():
        if sel == inRow[2]:
            delId = inRow[0]
    if delId != -1:
        cursor.execute("DELETE FROM Gallery WHERE id=?", [delId])
        db.commit()
    global options
    options = []
    cursor.execute("SELECT * FROM Gallery")
    for inRow in cursor.fetchall():
        options.append(inRow[2])
    db.close()

    # todo The select item is not removed. when i'm avalable. :)
    selectGallery.set("Select Gallery")


def searchGallery():
    global count
    print("searchGallery")
    print(editAuthor3.get())
    print(editMedium3.get())
    print(editPrice3.get())
    with sqlite3.connect("data/db/ArtGallery.db") as db:
        cursor = db.cursor()

    cursor.execute("SELECT * FROM Address WHERE name=?", [editAuthor3.get()])
    for inRow in cursor.fetchall():
        if inRow[1] == editAuthor3.get():
            listBox.insert(count, str(inRow))
            count += 1

    cursor.execute("SELECT * FROM Gallery WHERE medium=?", [editMedium3.get()])
    for inRow in cursor.fetchall():
        if inRow[3] == editMedium3.get():
            listBox.insert(count, str(inRow))
            count += 1

    cursor.execute("SELECT * FROM Gallery WHERE price>?", [int(editPrice3.get())])
    for inRow in cursor.fetchall():
        if int(inRow[4]) > int(editPrice3.get()):
            listBox.insert(count, str(inRow))
            count += 1
    db.close()

if __name__ == '__main__':
    # initialize database
    initSQL()

    window = Tk()
    window.title("ART GALLERY")
    window.geometry("980x650")
    window.resizable(0, 0)

    # Author address [
    labelFrameAuthor = LabelFrame(window, text="Author Address", padx=10, pady=10)
    labelFrameAuthor.pack()
    labelFrameAuthor.place(x=5, y=10)

    labelAuthor1 = Label(labelFrameAuthor, text="Enter Author :")
    labelAuthor1.grid(row=0, column=0)
    editAuthor1 = Entry(labelFrameAuthor, width=20, textvariable=str)
    editAuthor1.grid(row=0, column=1)
    editAuthor1.focus()

    labelAddress1 = Label(labelFrameAuthor, text="Enter Address :")
    labelAddress1.grid(row=1, column=0)
    editAddress1 = Entry(labelFrameAuthor, width=20, textvariable=str)
    editAddress1.grid(row=1, column=1)

    labelTown1 = Label(labelFrameAuthor, text="Enter Town :")
    labelTown1.grid(row=2, column=0)
    editTown1 = Entry(labelFrameAuthor, width=20, textvariable=str)
    editTown1.grid(row=2, column=1)

    labelCountry1 = Label(labelFrameAuthor, text="Enter Country :")
    labelCountry1.grid(row=3, column=0)
    editCountry1 = Entry(labelFrameAuthor, width=20, textvariable=str)
    editCountry1.grid(row=3, column=1)

    labelPostcode1 = Label(labelFrameAuthor, text="Enter Postcode :")
    labelPostcode1.grid(row=4, column=0)
    editPostcode1 = Entry(labelFrameAuthor, width=20, textvariable=str)
    editPostcode1.grid(row=4, column=1)

    labelAddressGuide1 = Label(labelFrameAuthor, text="")
    labelAddressGuide1.grid(row=5, column=1)

    addAuthorButton1 = Button(labelFrameAuthor, width=20, text="Add", command=addAddress)
    addAuthorButton1.grid(row=6, column=1)
    # Author address ]

    # Gallery [
    labelFrameGallery = LabelFrame(window, text="Gallery", padx=10, pady=10)
    labelFrameGallery.pack()
    labelFrameGallery.place(x=300, y=10)

    labelAuthor2 = Label(labelFrameGallery, text="Enter Author :")
    labelAuthor2.grid(row=0, column=0)
    editAuthor2 = Entry(labelFrameGallery, width=20, textvariable=str)
    editAuthor2.grid(row=0, column=1)

    labelTitle2 = Label(labelFrameGallery, text="Enter Title :")
    labelTitle2.grid(row=1, column=0)
    editTitle2 = Entry(labelFrameGallery, width=20, textvariable=str)
    editTitle2.grid(row=1, column=1)

    labelMedium2 = Label(labelFrameGallery, text="Enter Medium :")
    labelMedium2.grid(row=2, column=0)
    editMedium2 = Entry(labelFrameGallery, width=20, textvariable=str)
    editMedium2.grid(row=2, column=1)

    labelPrice2 = Label(labelFrameGallery, text="Enter Price :")
    labelPrice2.grid(row=3, column=0)
    editPrice2 = Entry(labelFrameGallery, width=20, textvariable=str)
    editPrice2.grid(row=3, column=1)

    labelGalleryGuide1 = Label(labelFrameGallery, text="")
    labelGalleryGuide1.grid(row=4, column=1)

    labelGalleryGuide2 = Label(labelFrameGallery, text="")
    labelGalleryGuide2.grid(row=5, column=1)

    addGalleryButton = Button(labelFrameGallery, width=20, text="Add", command=addGallery)
    addGalleryButton.grid(row=6, column=1)
    # Gallery ]

    # Buy Gallery [
    labelFrameBuy = LabelFrame(window, text="Buy Gallery", padx=10, pady=10)
    labelFrameBuy.pack()
    labelFrameBuy.place(x=590, y=10)

    selectGallery = StringVar(labelFrameBuy)
    selectGallery.set("Select Gallery")

    options = []
    with sqlite3.connect("data/db/ArtGallery.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM Gallery")
    for inRow in cursor.fetchall():
        options.append(inRow[2])
    db.close()

    galleryList = OptionMenu(labelFrameBuy, selectGallery, *options)
    galleryList.configure(width=20)
    galleryList.grid(row=0, column=0)

    addBuyButton = Button(labelFrameBuy, width=20, text="Buy", command=selectBuyGallery)
    addBuyButton.grid(row=0, column=1)
    # Buy Gallery ]

    # Search [
    labelFrameSearch = LabelFrame(window, text="Search", padx=10, pady=10)
    labelFrameSearch.pack()
    labelFrameSearch.place(x=5, y=300)

    labelAuthor3 = Label(labelFrameSearch, text="Enter Author :")
    labelAuthor3.grid(row=0, column=0)
    editAuthor3 = Entry(labelFrameSearch, width=20, textvariable=str)
    editAuthor3.grid(row=0, column=1)

    labelMedium3 = Label(labelFrameSearch, text="Enter Medium :")
    labelMedium3.grid(row=1, column=0)
    editMedium3 = Entry(labelFrameSearch, width=20, textvariable=str)
    editMedium3.grid(row=1, column=1)

    labelPrice3 = Label(labelFrameSearch, text="Enter Price :")
    labelPrice3.grid(row=2, column=0)
    editPrice3 = Entry(labelFrameSearch, width=20, textvariable=str)
    editPrice3.grid(row=2, column=1)

    labelSearchGuide1 = Label(labelFrameSearch, text="")
    labelSearchGuide1.grid(row=3, column=1)

    addSearchButton = Button(labelFrameSearch, width=20, text="Search", command=searchGallery)
    addSearchButton.grid(row=4, column=1)

    count = 0
    listBox = Listbox(window, selectmode='extended')
    listBox.place(x=300, y=300, height=300, width=400)

    window.mainloop()

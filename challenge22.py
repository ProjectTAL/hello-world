import time
from tkinter import *


def validateDigitNumber(number):
    if str(number).isdigit() and int(number) < 100:
        return True
    else:
        print("\nout of range number or text. Enter number (1-100) : \n")
        return False


def viewTable():
    global count

    count = 0
    number = edit.get()
    print("before")
    if not validateDigitNumber(number):
        return
    print("passed")
    for i in range(1, 13):
        newRec = str(i) + " * " + str(number) + " = " + str(i * int(number)) + "\n"
        print(newRec)
        listBox.insert(count, str(newRec))
        count += 1


def clearTable():
    edit.delete(0, END)
    listBox.delete(0, END)


if __name__ == '__main__':
    window = Tk()
    window.title("Times Table")
    window.geometry("400x300")
    window.resizable(0, 0)

    label = Label(window, text="Enter a number :")
    label.place(x=5, y=10)
    edit = Entry(window, width=20, textvariable=str)
    edit.place(x=100, y=10)
    edit.focus()

    viewButton = Button(text="View Times Table", command=viewTable)
    viewButton.place(x=260, y=10, width=130, height=20)
    clearButton = Button(text="Clear", command=clearTable)
    clearButton.place(x=260, y=40, width=130, height=20)

    count = 0
    listBox = Listbox(window, selectmode='extended')
    listBox.place(x=100, y=40, height=240)

    window.mainloop()

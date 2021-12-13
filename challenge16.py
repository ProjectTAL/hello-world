import random
from tkinter import *


def printTest():
    print("Hello world!")


# def Call():
#     msg = Label(window, text="You pressed the button")
#     msg.place(x=30, y=50)
#     button["bg"] = "blue"
#     button["fg"] = "white"

# 124
# def callName():
#     msg = Label(window, text="Hello " + edit.get())
#     msg.place(x=30, y=50)
#     msg["bg"] = "blue"
#     msg["fg"] = "red"


# 125
# def rollDice():
#     number = random.randint(1, 6)
#     msg = Label(window, text="The number : {}".format(number))
#     msg.place(x=30, y=60)
#     msg["fg"] = "red"

# 126
# def addNumbers():
#     value = edit.get()
#     global mSum
#     mSum = mSum + int(value)
#     label = Label(window, text="SUM:{} Next Value:".format(mSum))
#     label.place(x=5, y=0)
#
# def initSum():
#     global mSum
#     mSum = 0
#     label = Label(window, text="SUM:{} Next Value:".format(mSum))
#     label.place(x=5, y=0)

# 127
# def addNames():
#     global count
#
#     name = edit.get()
#     listBox.insert(count, name)
#     count += 1
#
#
# def clearNames():
#     count = 0
#     listBox.delete(0, END)

# 128
# 1(kilo):0.6214 = 1(mile):1.6093
# def convKilo2Mile(kilo):
#     ret = float(kilo) * 0.6214
#     return ret
#
#
# def convK2M_UX():
#     kilo = edit.get()
#     variable = convKilo2Mile(float(kilo))
#     labelResult.config(text="{}kilo -> {}mile".format(round(float(kilo), 4), round(float(variable), 4)))
#
#
# def convMile2Kilo(mile):
#     ret = float(mile) * 1.6093
#     return ret
#
#
# def convM2K_UX():
#     mile = edit2.get()
#     variable = convMile2Kilo(float(mile))
#     labelResult2.config(text="{}kilo -> {}mile".format(round(float(mile), 4), round(float(variable), 4)))

# 129 & 130
def isDigit():
    global count
    number = edit.get()
    if str(number).isdigit():
        listBox.insert(count, number)
        count += 1
    else:
        edit.delete(0, END)


def clearList():
    count = 0
    listBox.delete(0, END)


def saveCSV():
    tmp_list = listBox.get(0, END)
    file = open("Num.csv", "w")
    x = 0
    for row in tmp_list:
        newRec = tmp_list[x][0] + "\n"
        file.write(str(newRec))
        x += 1
    file.close()


if __name__ == '__main__':
    printTest()
    # 129 & 130
    window = Tk()
    window.title("DIGIT CHECKER")
    window.geometry("400x400")

    label = Label(window, text="Enter number:")
    label.place(x=5, y=0)
    edit = Entry(window, width=30, textvariable=str)
    edit.pack(side=TOP, anchor='ne')
    edit.place(x=120, y=0)

    button = Button(text="Add Digit", command=isDigit)
    button.place(x=80, y=30, width=120, height=25)

    clearButton = Button(text="Clear", command=clearList)
    clearButton.place(x=80, y=60, width=120, height=25)

    csvButton = Button(text="Save as csv", command=saveCSV)
    csvButton.place(x=80, y=90, width=120, height=25)

    count = 0
    listBox = Listbox(window, selectmode='extended')
    listBox.place(x=5, y=120)
    window.mainloop()

    # 128
    # window = Tk()
    # window.title("CONVERTER (K2M)")
    # window.geometry("400x400")
    #
    # # Convert Kilo to Mile
    # label = Label(window, text="Enter Kilo:")
    # label.place(x=5, y=0)
    # edit = Entry(window, width=20, textvariable=str)
    # edit.pack(side=TOP, anchor='ne')
    # edit.place(x=120, y=0)
    #
    # button = Button(text="Convert K to M", command=convK2M_UX)
    # button.place(x=5, y=30, width=120, height=25)
    #
    # labelResult = Label(window, text="test")
    # labelResult.place(x=130, y=30, width=150, height=25)
    #
    # # Convert Mile to Kilo
    # label2 = Label(window, text="Enter Mile:")
    # label2.place(x=5, y=80)
    # edit2 = Entry(window, width=20, textvariable=str)
    # edit2.pack(side=TOP, anchor='ne')
    # edit2.place(x=120, y=80)
    #
    # button2 = Button(text="Convert M to K", command=convM2K_UX)
    # button2.place(x=5, y=110, width=120, height=25)
    #
    # labelResult2 = Label(window, text="test2")
    # labelResult2.place(x=130, y=110, width=150, height=25)
    #
    # window.mainloop()

    # 127
    # window = Tk()
    # window.title("NAMES List")
    # window.geometry("400x400")
    #
    # label = Label(window, text="Enter name:")
    # label.place(x=5, y=0)
    # edit = Entry(window, width=30, textvariable=str)
    # edit.pack(side=TOP, anchor='ne')
    # edit.place(x=120, y=0)
    #
    # button = Button(text="Click here", command=addNames)
    # button.place(x=80, y=30, width=120, height=25)
    #
    # clearButton = Button(text="Initialize", command=clearNames)
    # clearButton.place(x=80, y=60, width=120, height=25)
    # count = 0
    # listBox = Listbox(window, selectmode='extended')
    # listBox.place(x=5, y=90)
    # window.mainloop()

    # 126
    # window = Tk()
    # window.title("SUM")
    # window.geometry("400x200")
    # mSum = 0
    # label = Label(window, text="SUM:{} Next Value:".format(mSum))
    # label_width = label.winfo_width()
    # label.place(x=5, y=0)
    # edit = Entry(window, width=30, textvariable=str)
    # edit.pack(side=TOP, anchor='ne')
    # edit.place(x=120, y=0)
    #
    # button = Button(text="Click here", command=addNumbers)
    # button.place(x=80, y=30, width=120, height=25)
    #
    # initButton = Button(text="Initialize", command=initSum)
    # initButton.place(x=80, y=60, width=120, height=25)
    #
    # window.mainloop()

    # 125
    # window = Tk()
    # window.title("NAME IT")
    # window.geometry("300x200")
    #
    # button = Button(text="Roll the dice", command=rollDice)
    # button.place(x=30, y=20, width=120, height=25)
    #
    # window.mainloop()

    # 124
    # window = Tk()
    # window.title("NAME IT")
    # window.geometry("300x200")
    #
    # edit = Entry(window, width=30, textvariable=str)
    # edit.grid(column=0, row=0)
    #
    # button = Button(text="Click here", command=callName)
    # button.place(x=30, y=20, width=120, height=25)
    #
    # window.mainloop()

    # window = Tk()
    # window.geometry("200x110")
    # button = Button(text="Press me", command=Call)
    # button.place(x=30, y=20, width=120, height=25)
    # window.mainloop()

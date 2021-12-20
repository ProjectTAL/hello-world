import mimetypes
import random
import threading
import time
from tkinter import *
import filetype


def printTest():
    print("Hello world!")


# 133
# def hitButton():
#     name = edit.get()
#     edit.delete(0, END)
#     # print("Hello {}".format(name))
#     edit2.insert(0, "Hello {}".format(name))

# 134
# def getRandomNumber():
#     ret = random.randint(10, 50)
#     return ret
#
#
# def enterAnswer(event):
#     print("Enter answer {}".format(edit.get()))
#     goAnswer()
#
#
# def goAnswer():
#     global num1, num2, count, timeGlobal
#     # print("wht is {}, event : {}".format(timeGlobal), event)
#     if int(timeGlobal) < 1:
#         print("Time-out return")
#         return
#     rightAnswer = num1 + num2
#     userAnswer = edit.get()
#
#     if str(userAnswer).isdigit():
#         if int(rightAnswer) == int(userAnswer):
#             count += 1
#             rightPhoto = PhotoImage(file="resource\img\Right.gif")
#             photoBox.config(image=rightPhoto)
#             photoBox.image = rightPhoto
#             countLabel.config(text="Score\n{}".format(count * 10))
#             edit.delete(0, END)
#             num1 = getRandomNumber()
#             num2 = getRandomNumber()
#             label.config(text="{} + {} = ".format(num1, num2))
#         else:
#             wrongPhoto = PhotoImage(file="resource\img\Wrong.gif")
#             photoBox.config(image=wrongPhoto)
#             photoBox.image = wrongPhoto
#             edit.delete(0, END)
#     else:
#         wrongPhoto = PhotoImage(file="resource\img\Wrong.gif")
#         photoBox.config(image=wrongPhoto)
#         photoBox.image = wrongPhoto
#
#
# def nextProblem():
#     global num1, num2
#     num1 = getRandomNumber()
#     num2 = getRandomNumber()
#     label.config(text="{} + {} = ".format(num1, num2))
#     edit.delete(0, END)
#     initPhoto = PhotoImage(file="resource\img\Q.gif")
#     photoBox.config(image=initPhoto)
#     photoBox.image = initPhoto
#
#
# def setTimer(val):
#     global timeGlobal
#     timer = Label(window, text="Time:{}".format(val))
#     timer.config(font=('Helvatical bold', 10))
#     timer.place(x=10, y=50)
#     while val:
#         timeGlobal = val
#         if stopThread.is_set():
#             break
#         print("time : {}".format(val))
#         timer.config(text="Time:{}".format(val))
#         time.sleep(1)
#         val -= 1
#     timeGlobal = 0
#     timer.config(text="Time:{}".format(val))
#     print("Finished! ")
#     button.config(state=DISABLED)
#     buttonNext.config(state=DISABLED)

# 135
# def clicked(event):
#     print("it is {}".format(selectName.get()))
#     if "red" in selectName.get():
#         window.configure(background="red")
#     elif "orange" in selectName.get():
#         window.configure(background="orange")
#     else:
#         window.configure(background="blue")


# 136 & 137
# def selectGendor(event):
#     global count
#     file = open("name_n_gender.txt", "a")
#     name = edit.get()
#     gender = selectName.get().lower()
#     newRec = name + ", " + gender + "\n"
#     listBox.insert(count, str(newRec))
#     file.write(newRec)
#     file.close()
#     count += 1
#
#
# def printCWindow():
#     tmpList = listBox.get(0, END)
#     for row in tmpList:
#         print(row)

def isGifFile(name):
    mime = mimetypes.guess_type(name)[0]
    if mime.endswith("gif"):
        print("This is the {} that i need".format(mime))
    else:
        print("other format : {}".format(mime))


def showImg():
    num = int(edit.get())
    if num == 1:
        img = PhotoImage(file="resource\img\i1.gif")
    elif num == 2:
        img = PhotoImage(file="resource\img\i2.gif")
    elif num == 3:
        img = PhotoImage(file="resource\img\i3.gif")
    else:
        img = PhotoImage(file="resource\img\sample.gif")
    photoBox.config(image=img)
    photoBox.image = img


if __name__ == '__main__':
    printTest()
    # 138
    window = Tk()
    window.title("IMG VERIFIER")
    window.geometry("300x250")
    window.resizable(0, 0)

    filename1 = "/resource/img/i1.gif"
    filename2 = "/resource/img/i2.gif"
    filename3 = "/resource/img/i3.gif"

    isGifFile(filename1)
    isGifFile(filename2)
    isGifFile(filename3)

    label = Label(window, text="Enter num(1-3):")
    label.place(x=5, y=10)
    edit = Entry(window, width=20, textvariable=str)
    edit.place(x=100, y=10)

    button = Button(text="SElECT", command=showImg)
    button.place(x=200, y=10, width=50, height=20)
    # photo = PhotoImage(file="resource\img\sample.gif")
    photo = PhotoImage(file="resource/img/sample.gif")
    photoBox = Label(window, image=photo)
    photoBox.image = photo
    photoBox.place(x=70, y=50, width=120, height=120)

    window.mainloop()

    # 136 & 137
    # window = Tk()
    # window.title("NAME & GENDER")
    # window.geometry("300x250")
    # window.resizable(0, 0)
    #
    # label = Label(window, text="Enter name:")
    # label.place(x=5, y=10)
    # edit = Entry(window, width=20, textvariable=str)
    # edit.place(x=100, y=10)
    #
    # selectName = StringVar(window)
    # selectName.set("Select Gender")
    # options = ["MALE", "FEMALE"]
    # nameList = OptionMenu(window, selectName, *(options), command=selectGendor)
    # nameList.place(x=100, y=40)
    #
    # count = 0
    # listBox = Listbox(window, selectmode='extended')
    # listBox.place(x=80, y=80)
    #
    # button = Button(text="PRINT", command=printCWindow)
    # button.place(x=240, y=130, width=50, height=50)
    #
    # window.mainloop()

    # 135
    # window = Tk()
    # window.title("COLOR SELECTION")
    #
    # selectName = StringVar(window)
    # selectName.set("Select Color")
    # options = ["red", "orange", "blue"]
    # nameList = OptionMenu(window, selectName, *(options), command=clicked)
    # nameList.place(x=30, y=20)
    #
    # window.mainloop()

    # 134
    # num1 = getRandomNumber()
    # num2 = getRandomNumber()
    # timeGlobal = 0
    # count = 0
    # window = Tk()
    # window.title("QUIZ")
    # window.geometry("300x250")
    # window.resizable(0,0)
    # try:
    #     window.wm_iconbitmap("wint.ico")
    # except Exception:
    #     print("Exception happens")
    # label = Label(window, text="{} + {} = ".format(num1, num2))
    # label.config(font=('Helvatical bold', 10))
    # label.place(x=3, y=10)
    # edit = Entry(window, width=20, textvariable=str)
    # edit.place(x=70, y=10)
    #
    # # window.bind('<Return>', goAnswer)
    # window.bind('<Return>', enterAnswer)
    # button = Button(text="GO", command=goAnswer, bg="green")
    # button.place(x=230, y=10, width=45, height=20)
    #
    # photo = PhotoImage(file="resource\img\Q.gif")
    # photoBox = Label(window, image=photo)
    # photoBox.image = photo
    # photoBox.place(x=70, y=50, width=120, height=120)
    #
    # buttonNext = Button(text="NEXT", command=nextProblem, bg="green")
    # buttonNext.place(x=70, y=190, width=130, height=20)
    #
    # countLabel = Label(window, text="Score\n{}".format(count * 10))
    # countLabel.config(font=('Helvatical bold', 13))
    # countLabel.place(x=210, y=100)
    #
    # stopThread = threading.Event()
    # startThread = threading.Thread(target=setTimer, args=(30,)) # time-out value : 30 seconds
    # startThread.start()
    #
    # window.mainloop()

    # 133
    # window = Tk()
    # window.title("NAME OUTPUT")
    # window.geometry("300x250")
    # window.wm_iconbitmap("icofile.ico")
    #
    # logo = PhotoImage(file="img1.gif")
    # logoImage = Label(image=logo)
    # logoImage.place(x=50, y=20, width=200, height=150)
    #
    # label = Label(window, text="Enter name:")
    # label.place(x=5, y=180)
    # edit = Entry(window, width=20, textvariable=str)
    # edit.place(x=100, y=180)
    #
    # button = Button(text="Press Me", command=hitButton)
    # button.place(x=5, y=210, width=80, height=20)
    # edit2 = Entry(window, width=20, textvariable=str)
    # edit2.place(x=100, y=210)
    #
    # window.mainloop()

    # window = Tk()
    # window.title("SAMPLE CODE")
    # window.geometry("300x400")
    #
    # window.wm_iconbitmap("icofile.ico")
    # window.configure(background="light green")
    #
    # # logo = PhotoImage(file="img1.gif")
    # # logoImage = Label(image=logo)
    # # logoImage.place(x=30, y=20, width=250, height=350)
    #
    # # photo = PhotoImage(file="img1.gif")
    # # photoBox = Label(window, image=photo)
    # # photoBox.image = photo
    # # photoBox.place(x=30, y=20, width=250, height=350)
    #
    # selectName = StringVar(window)
    # selectName.set("Select Name")
    # nameList = OptionMenu(window, selectName, "Bob", "Sue", "Tim")
    # nameList.place(x=30, y=250)
    #
    # window.mainloop()

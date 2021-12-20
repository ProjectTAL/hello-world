import random
import threading
import time
from tkinter import *
from pygame import mixer

def getRandomNumber():
    ret = random.randint(10, 50)
    return ret


def enterAnswer(event):
    print("Enter answer {}".format(edit.get()))
    goAnswer()


def goAnswer():
    global num1, num2, count, timeGlobal
    if int(timeGlobal) < 1:
        print("Time-out return")
        return
    rightAnswer = num1 + num2
    userAnswer = edit.get()

    if str(userAnswer).isdigit():
        if int(rightAnswer) == int(userAnswer):
            count += 1
            rightPhoto = PhotoImage(file="resource\img\Right.gif")
            photoBox.config(image=rightPhoto)
            photoBox.image = rightPhoto
            countLabel.config(text="Score\n{}".format(count * 10))
            edit.delete(0, END)
            num1 = getRandomNumber()
            num2 = getRandomNumber()
            label.config(text="{} + {} = ".format(num1, num2))
        else:
            wrongPhoto = PhotoImage(file="resource\img\Wrong.gif")
            photoBox.config(image=wrongPhoto)
            photoBox.image = wrongPhoto
            edit.delete(0, END)
    else:
        wrongPhoto = PhotoImage(file="resource\img\Wrong.gif")
        photoBox.config(image=wrongPhoto)
        photoBox.image = wrongPhoto


def nextProblem():
    global num1, num2
    num1 = getRandomNumber()
    num2 = getRandomNumber()
    label.config(text="{} + {} = ".format(num1, num2))
    edit.delete(0, END)
    initPhoto = PhotoImage(file="resource\img\Q.gif")
    photoBox.config(image=initPhoto)
    photoBox.image = initPhoto


def setTimer(val):
    global timeGlobal
    timer = Label(window, text="Time:{}".format(val))
    timer.config(font=('Helvatical bold', 10))
    timer.place(x=10, y=50)
    while val:
        timeGlobal = val
        if stopThread.is_set():
            break
        print("time : {}".format(val))
        timer.config(text="Time:{}".format(val))
        time.sleep(1)
        val -= 1
    mixer.music.stop()
    timeGlobal = 0
    timer.config(text="Time:{}".format(val))
    print("Finished! ")
    button.config(state=DISABLED)
    buttonNext.config(state=DISABLED)


if __name__ == '__main__':
    num1 = getRandomNumber()
    num2 = getRandomNumber()
    timeGlobal = 0
    count = 0

    window = Tk()
    window.title("QUIZ")
    window.geometry("300x250")
    window.resizable(0, 0)
    try:
        window.wm_iconbitmap("wint.ico")
    except Exception:
        print("Exception happens")
    label = Label(window, text="{} + {} = ".format(num1, num2))
    label.config(font=('Helvatical bold', 10))
    label.place(x=3, y=10)
    edit = Entry(window, width=20, textvariable=str)
    edit.place(x=70, y=10)

    window.bind('<Return>', enterAnswer)
    button = Button(text="GO", command=goAnswer, bg="green")
    button.place(x=230, y=10, width=45, height=20)

    photo = PhotoImage(file="resource\img\Q.gif")
    photoBox = Label(window, image=photo)
    photoBox.image = photo
    photoBox.place(x=70, y=50, width=120, height=120)

    buttonNext = Button(text="NEXT", command=nextProblem, bg="green")
    buttonNext.place(x=70, y=190, width=130, height=20)

    countLabel = Label(window, text="Score\n{}".format(count * 10))
    countLabel.config(font=('Helvatical bold', 13))
    countLabel.place(x=210, y=100)

    stopThread = threading.Event()
    startThread = threading.Thread(target=setTimer, args=(30,))  # time-out value : 30 seconds
    startThread.start()

    mixer.init()
    mixer.music.load('resource/sound/begin.mp3')
    mixer.music.play()

    window.mainloop()

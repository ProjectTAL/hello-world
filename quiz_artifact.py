import random
import threading
import time
from tkinter import *
from pygame import mixer


def getRandomNumber():
    ret = random.randint(1, 100)
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
    labelFrameTime = LabelFrame(window, text="TIME", padx=10, pady=10)
    labelFrameTime.pack()
    labelFrameTime.place(x=500, y=10)
    global timeGlobal
    timer = Label(labelFrameTime, text="{}".format(val))
    timer.config(font=('Helvatical bold', 50))
    timer.grid(row=0, column=0)
    while val:
        timeGlobal = val
        if stopThread.is_set():
            break
        print("time : {}".format(val))
        if val < 10:
            timer.config(fg="red")
        timer.config(text="{}".format(val))
        time.sleep(1)
        val -= 1
    mixer.music.stop()
    timeGlobal = 0
    timer.config(text="{}".format(val))
    print("Finished! ")
    buttonNext.config(state=DISABLED)


if __name__ == '__main__':
    num1 = getRandomNumber()
    num2 = getRandomNumber()
    timeGlobal = 0
    count = 0

    window = Tk()
    window.title("QUIZ")
    window.geometry("650x550")
    window.resizable(0, 0)
    try:
        window.wm_iconbitmap("wint.ico")
    except Exception:
        print("Exception happens")

    labelFrame = LabelFrame(window, text="Problem", padx=10, pady=10)
    labelFrame.pack()
    labelFrame.place(x=5, y=10)

    label = Label(labelFrame, text="{} + {} = ".format(num1, num2))
    label.config(font=('Helvatical bold', 30))
    label.grid(row=0, column=0)
    edit = Entry(labelFrame, width=5, textvariable=str, font=("defualt", 40))
    edit.grid(row=0, column=1)
    edit.focus()

    window.bind('<Return>', enterAnswer)

    labelFrame2 = LabelFrame(window, text="SCORE", padx=10, pady=10)
    labelFrame2.pack()
    labelFrame2.place(x=200, y=200)

    photo = PhotoImage(file="resource\img\Q.gif")
    photoBox = Label(labelFrame2, image=photo)
    photoBox.image = photo
    photoBox.grid(row=0, column=0)

    buttonNext = Button(labelFrame2, text="NEXT", command=nextProblem, bg="green")
    buttonNext.grid(row=1, column=0)

    countLabel = Label(labelFrame2, text="Score\n{}".format(count * 10))
    countLabel.config(font=('Helvatical bold', 30))
    countLabel.grid(row=2, column=0)

    stopThread = threading.Event()
    startThread = threading.Thread(target=setTimer, args=(60,))  # time-out value : 60 seconds
    startThread.start()

    mixer.init()
    mixer.music.load('resource/sound/begin.mp3')
    mixer.music.play()

    window.mainloop()

import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance

# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = ("C:\\Users\\amine\\Desktop\\project 3\\Attendance-Management-system-using-face-recognition-master\\haarcascade_frontalface_default.xml")
trainimagelabel_path = (
    "C:\\Users\\amine\\Desktop\\project 3\\Attendance-Management-system-using-face-recognition-master\\TrainingImageLabel\\Trainner.yml"
)
trainimage_path = ("C:\\Users\\amine\\Desktop\\project 3\\Attendance-Management-system-using-face-recognition-master\\TrainingImage")
studentdetail_path = (
    "C:\\Users\\amine\\Desktop\\project 3\\Attendance-Management-system-using-face-recognition-master\\StudentDetails\\studentdetails.csv"
)
attendance_path = ("C:\\Users\\amine\\Desktop\\project 3\\Attendance-Management-system-using-face-recognition-master\\Attendance")


window = Tk()
window.title("Face recognizer")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
background_image = Image.open("C:/Users/amine/Desktop/project 3/Attendance-Management-system-using-face-recognition-master/UI_Image/0101.png")  # Change path as needed
background_image = background_image.resize((1280, 720), Image.LANCZOS)  # Resize to fit window
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="black")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="#ffc222",
        bg="black",
        font=("times new roman", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="#ffc222",
        bg="black",
        width=9,
        height=1,
        activebackground="Red",
        font=("times new roman", 20, " bold "),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True

logo_left = Image.open("C:/Users/amine/Desktop/project 3/Attendance-Management-system-using-face-recognition-master/UI_Image/0005.png")
logo_left = logo_left.resize((250, 200), Image.LANCZOS)  # Resize to a larger size
logo_left_img = ImageTk.PhotoImage(logo_left)
logo_label_left = tk.Label(window, image=logo_left_img, bg="black")
logo_label_left.place(x=10, y=10)



logo = Image.open("C:/Users/amine/Desktop/project 3/Attendance-Management-system-using-face-recognition-master/UI_Image/0001.png")
logo = logo.resize((50, 47),Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="black", bd=10, font=("times new roman", 35))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="black",)
l1.place(x=470, y=10)

titl = tk.Label(
    window, text="Tunis Business School", bg="black", fg="#ffe091", font=("times new roman", 27),
)
titl.place(x=525, y=12)

a = tk.Label(
    window,
    text="Welcome to the Face Recognition Based\nAttendance Management System",
    bg="black",
    fg="#ffe8ad",
    bd=10,
    font=("times new roman", 35),
)
a.pack()

ri = Image.open("C:/Users/amine/Desktop/project 3/Attendance-Management-system-using-face-recognition-master/UI_Image/1111.png")
ri = ri.resize((225, 225),Image.LANCZOS)
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r, bg="black",)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("C:/Users/amine/Desktop/project 3/Attendance-Management-system-using-face-recognition-master/UI_Image/2222.png")
ai = ai.resize((225, 225),Image.LANCZOS)
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a, bg="black",)
label2.image = a
label2.place(x=900, y=270)

vi = Image.open("C:/Users/amine/Desktop/project 3/Attendance-Management-system-using-face-recognition-master/UI_Image/3333.png")
vi = vi.resize((225, 225),Image.LANCZOS)
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v, bg="black",)
label3.image = v
label3.place(x=500, y=270)


def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="black")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("times new roman", 35))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="black", fg="#ffe091", font=("times new roman", 30),
    )
    titl.place(x=270, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="black",
        fg="#ffc222",
        bd=10,
        font=("times new roman", 24),
    )
    a.place(x=280, y=75)

    # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="black",
        fg="#ffc222",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="black",
        fg="#ffc222",
        relief=RIDGE,
        font=("times new roman", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="black",
        fg="#ffc222",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="black",
        fg="#ffc222",
        relief=RIDGE,
        font=("times new roman", 25, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="black",
        fg="#ffc222",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="black",
        fg="#ffc222",
        relief=RIDGE,
        font=("times new roman", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("times new roman", 18),
        bg="black",
        fg="#ffc222",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18),
        bg="black",
        fg="#ffc222",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)


r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="#ffc222",
    height=2,
    width=17,
)
r.place(x=99, y=520)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="#ffc222",
    height=2,
    width=17,
)
r.place(x=499, y=520)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="#ffc222",
    height=2,
    width=17,
)
r.place(x=899, y=520)
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("times new roman", 16),
    bg="black",
    fg="#931621",
    height=2,
    width=17,
)
r.place(x=499, y=620)

window.mainloop()

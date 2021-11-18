from tkinter import *
import serial
import time

ser = None
win = Tk()

def connect():
    global ser
    com = str(entry1.get())
    baud = int(entry2.get())
    try:
        ser = serial.Serial(com, baud, timeout=0)
        print("povezano")
        win.after(500, update)
    except ValueError:
        print("Unesite ispravne podatke")

def update():
    global data
    try:
        data = ser.readline()
        alfa.set(data)
        win.after(500, update)
    except TypeError:
        pass

def close():
    try:
        ser.close()
    except AttributeError:
        print("Zatvaranje bez uspostave kom.")
    win.destroy()


if __name__ == "__main__":
    alfa = StringVar()

    img = PhotoImage(file="reneu.png")
    label = Label(win, fg="white", textvariable=alfa, compound=CENTER, font="Arial, 40", width=400, image=img)
    label.place(x=0,y=0)

    label1 = Label(win, text="Port")
    entry1 = Entry(win, width=9)
    label2 = Label(win, text="Baud")
    entry2 = Entry(win, width=9)
    button1 = Button(win, text="Povezi", command=connect)
    button2 = Button(win, text="Zatvori", command=close)

    label1.place(x=454, y=9)
    entry1.place(x=440, y=30)
    button1.place(x=410, y=121)
    label2.place(x=454, y=60)
    entry2.place(x=440, y=81)
    button2.place(x=487, y=121)


    win.geometry("540x232")
    win.mainloop()

# button = you click it, then it does stuff

from tkinter import *
import time

count = 0

def reseti():
    global count
    count = 0
    label.config(text=count)
    button.config(text="Tasbih")


def click():
    global count
    if count <= 32:
        count+=1
        label.config(text=count)
    elif count >= 33 and count < 67:
        if count == 33:
            label.config(text=0)
            button.config(text="Tahmid")
            count+=1
        else :
            button.config(text="Tahmid")
            count+=1
            label.config(text=count-34)
    elif count >= 67 and count < 101:
        if count == 67:
            label.config(text=0)
            button.config(text="Takbir")
            count+=1
        else :
            button.config(text="TAKBIR")
            count+=1
            label.config(text=count-68)
    elif count > 101:
        label.config(text=33)
        count+=1


window = Tk()
window.title("Dzikir Digital")
window.geometry('200x300') 
label = Label(window,text=count)
label.config(font=('Bebas Neue',50))
label.pack()
button = Button(window,text='TASBIH')
button.config(command=click, width=10) #performs call back of function
button.config(font=('Bebas Neue', 20))
button.config(bd= 5 )
button.config(bg='black')
button.config(fg='white')
button.place(x=1, y=500)
button.pack(padx=15, pady=20)
reset = Button(window, text='RESET')
reset.config(command=reseti, width=10)
reset.config(font=('Bebas Neue', 20))
reset.config(bd= 5 )
reset.config(bg='black')
reset.config(fg='white')
reset.place(x=1, y=300)
reset.pack()

window.mainloop()
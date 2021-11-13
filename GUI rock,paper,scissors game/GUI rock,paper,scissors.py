from tkinter import *
from tkinter import ttk
from random import *

root = Tk()

root.geometry("500x500")

root.title("Rock-Paper-Scissors-Game")

list = ["rock","paper","scissors"]

choose_number = randint(0,2)
print(choose_number)

label = Label(root,text="Computer ",width = 20,height=4,font=("algerian",15))
label.pack()

def spin():
    choose_number = randint(0,2)
    label.config(text=list[choose_number])
    if user_select.get() == "Rock":
        user_select_value = 0
        print(user_select_value)
    elif user_select.get() == "Paper":
        user_select_value = 1
        print(user_select_value)
    elif user_select.get() == "Scissors":
        user_select_value = 2
        print(user_select_value)

    if user_select_value == 0:
        if choose_number == 0:
            wl_label.config(text="Tie")
        elif choose_number == 1:
            wl_label.config(text="lose")
        elif choose_number == 2 :
            wl_label.config(text="won")

    elif user_select_value == 1:
        if choose_number == 1:
            wl_label.config(text="Tie")
        elif choose_number == 0:
            wl_label.config(text="won")
        elif choose_number == 2 :
            wl_label.config(text="lose")

    elif user_select_value == 2:
        if choose_number == 2:
            wl_label.config(text="Tie")
        elif choose_number == 0:
            wl_label.config(text="lose")
        elif choose_number == 1 :
            wl_label.config(text="won")




user_select = ttk.Combobox(root,value=["Rock","Paper","Scissors"])
user_select.current(0)
user_select.pack()

wl_label = Label(root,text="",font=("algerian",15),width=8,height=4)
wl_label.pack()

button = Button(root,text="Spin!",font=("algerian",10),command=spin)
button.pack()

root.mainloop()

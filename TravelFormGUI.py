from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Travel Form")

L1 = Label(root, text="Aashakt Travels", font="comicsanserif 20 bold").grid(row=0, column=1)
L2 = Label(root, text="Name: ").grid(row=1, column=0)
L3 = Label(root, text="Address: ").grid(row=2, column=0)
L4 = Label(root, text="Phone Number: ").grid(row=3, column=0)
L5 = Label(root, text="E-mail: ").grid(row=4, column=0)
E11 = StringVar()
E1 = Entry(root, textvariable=E11).grid(row=1, column=1)
E12 = StringVar()
E2 = Entry(root, textvariable=E12).grid(row=2, column=1)
E13 = IntVar()
E3 = Entry(root, textvariable=E13).grid(row=3, column=1)
E14 = StringVar()
E4 = Entry(root, textvariable=E14).grid(row=4, column=1)

Var = IntVar()
C1 = Checkbutton(root, text="Do you want food: ", variable=Var).grid(row=6, column=1)

# Function for the button
def Func():
    record = open("recordFormTravel.txt", 'a')
    record.write(f"{E11.get()}, {E12.get()}, {E13.get()}, {E14.get()}, {Var.get()}\n")

B = Button(root, text="Submit", command=Func).grid(row=7, column=1)
root.mainloop()

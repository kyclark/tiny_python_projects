from tkinter import*
from textblob import TextBlob

def clearAll():
    e1.delete(0, END)
    e2.delete(0, END)

def correction():
    input_word = e1.get()
    blob_obj = TextBlob(input_word)

    corrected_word = str(blob_obj.correct())
    e2.insert(10, corrected_word)

def exit():
    root.destroy()

if __name__== "__main__":

    root = Tk()
    root.title('Spell Corrector')
    root.geometry('400x400')
    root.configure(background='white')

    headlabel = Label(root, text='Spell Corrector App', bg="powder blue")
    headlabel.grid(row=0, column=1, padx=40)

    label1 = Label(root, text='Input word', bg='white')
    label1.grid(row=1, column=0, pady=5)

    label1 = Label(root, text='Input word', bg='white')
    label1.grid(row=1, column=0, padx=10, pady=10)
    e1 = Entry(root)
    e1.grid(row=1, column=1, padx=20)

    label2 = Label(root, text='Corrected Word', bg='white')
    label2.grid(row=2, column=0, padx=10, pady=10)
    e2=Entry(root)
    e2.grid(row=2, column=1, padx=20)

    button1=Button(root, text='Correction', bg='powder blue', width=10, command=correction)
    button1.grid(row=3, column=0)

    button2 = Button(root, text='Clear', bg='powder blue', width=5, command=clearAll)
    button2.grid(row=3, column=1)

    button3 = Button(root, text='Exit', bg='powder blue', width=5, command=exit)
    button3.grid(row=3, column=2)

    root.mainloop()
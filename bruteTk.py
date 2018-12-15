from tkinter import *
from tkinter import ttk

root = Tk()
root.title("BruteTk")
root.geometry("400x200")

h1Label = Label(root, text="Caesar Brute", font=("helvetica", 18))

helpLabel = Label(text="Please enter text to brute", font=("helvetica", 8))

plainText_ = StringVar()
inputUser = Entry(root, textvariable=plainText_)

scrollbar1 = Scrollbar(root)
listbox1 = Listbox(root)

def brute():
    global plainText_
    global listbox1

    plainText = str(plainText_.get())

    inputUser.delete(0, 'end')
    listbox1.delete(0, 'end')

    alphabet = 26

    for i in range(alphabet):
        final = ""

        for char in plainText:
            if char.isupper() == True:
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            else:
                alphabet = "abcdefghijklmnopqrstuvwxyz"

            if char not in alphabet:
                final += char
                continue

            charLoca = alphabet.find(char)
            charLoca += i

            if charLoca >= len(alphabet):
                while True:
                    charLoca -= len(alphabet)
                    if charLoca <= len(alphabet) and charLoca >= 0:
                        break

            final += alphabet[charLoca]

        #DEBUGGER:
        #print(final)

        listbox1.insert(END, final)


buttonStyle = ttk.Style()
buttonStyle.configure("BW.TButton", background="grey", foreground="blue")

button1 = ttk.Button(root, text="Enter",style="BW.TButton", command=brute)

listbox1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=listbox1.yview)

h1Label.pack()
helpLabel.place(x=10,y=75)
inputUser.place(x=10, y=100)
button1.place(x=30, y=125)
listbox1.place(x=250, y=30)
scrollbar1.place(x=235,y=80)

root.mainloop()

from tkinter import *
from tkinter import ttk

alphabet = "abcdefghijklmnopqrstuvwxyz"

root = Tk()
root.geometry("450x250")
root.title("Caesar Cipher")

root.resizable(False, False)

data = StringVar()
text = Entry(root, textvariable=data)

num = StringVar()
number = Entry(root, textvariable=num)

#Reference

#def test():
#	new = int(num.get())
#	a = new + 5
#	print(str(a))

scrollbar1 = Scrollbar(root)
listbox1 = Listbox(root)

def encrypt():
	global scrollbar1
	global listbox1
	global alphabet

	final = "Output: "

	plain = str(text.get())
	shift = int(num.get())

	text.delete(0, 'end')
	number.delete(0, 'end')

	for char in plain:

		if char.isupper() == True:
			alphabet = alphabet.upper()
		else:
			alphabet = alphabet.lower()

		if char not in alphabet:
			final += char
			continue

		loca = alphabet.find(char)
		newVal = loca + shift

		if newVal > len(alphabet):
			while True:
				newVal -= 26

				if newVal < len(alphabet):
					break

		final += alphabet[newVal]

	#enc = Label(root, text=final,fg="blue")
	#enc.pack()
	listbox1.insert(END, final)

def decrypt():
	global listbox1
	global scrollbar1
	global alphabet

	final = "Output: "

	plain = str(text.get())
	shift = int(num.get())

	text.delete(0, 'end')
	number.delete(0, 'end')

	for char in plain:

		if char.isupper() == True:
			alphabet = alphabet.upper()
		else:
			alphabet = alphabet.lower()

		if char not in alphabet:
			final += char
			continue

		loca = alphabet.find(char)
		newVal = loca - shift

		if newVal < 0:
			while True:
				newVal += 26

				if newVal <= len(alphabet) and newVal >= 0:
					break

		final += alphabet[newVal]

	#dec = Label(root, text=final,fg="blue")
	#dec.pack()
	listbox1.insert(END, final)


listbox1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=listbox1.yview)

buttonStyle = ttk.Style()
buttonStyle.configure("BW.TButton", foreground="Green", background="grey", font=("helvetica", 8))

press = ttk.Button(root, style="BW.TButton",text="Encrypt", command=encrypt)
press2 = ttk.Button(root, style="BW.TButton", text="Decrypt", command=decrypt)

mainLabel = Label(root, text="Caesar Cipher", font=("Helvetica", 18))
subLabel = Label(root, text="A basic cipher system", font=("Helvetica", 8))

label1 = Label(root, text="Enter Text")
label2 = Label(root, text="Enter shift(int)")
label3 = Label(root, text="OUTPUT:", fg="blue")

mainLabel.pack()
subLabel.pack()
label1.place(x=40, y=50)
text.place(x=10, y=72)
label2.place(x=30,y=99)
number.place(x=10, y=120)
label3.place(x=300, y=50)
listbox1.place(x=265, y=75)
press.place(x=10, y=200)
press2.place(x=75, y=200)

root.mainloop()

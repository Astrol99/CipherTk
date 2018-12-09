from tkinter import *

alphabet = "abcdefghijklmnopqrstuvwxyz"

root = Tk()
root.geometry("400x400")
root.title("Caesar Cipher")

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

	final = "Encrypted: "

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

	final = "Decrypted: "

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

press = Button(root, text="Encrypt", command=encrypt, fg="blue")
press2 = Button(root, text="Decrypt", command=decrypt, fg="blue")

mainLabel = Label(root, text="Caesar Cipher", font=("Helvetica", 18))
subLabel = Label(root, text="A basic cipher system", font=("Helvetica", 8))

label1 = Label(root, text="Enter Text", fg="green")
label2 = Label(root, text="Enter shift(int)", fg="green")
label3 = Label(root, text="OUTPUT:", fg="red")

mainLabel.pack()
subLabel.pack()
label1.pack()
text.pack()
label2.pack()
number.pack()
label3.pack()
listbox1.pack()
press.pack(side=LEFT)
press2.pack(side=RIGHT)

root.mainloop()

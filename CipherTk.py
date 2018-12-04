from tkinter import *

alphabet = "abcdefghijklmnopqrstuvwxyz"

root = Tk()
root.geometry("400x400")
root.title("Cipher")

data = StringVar()
text = Entry(root, textvariable=data)

num = StringVar()
number = Entry(root, textvariable=num)

#Reference

#def test():
#	new = int(num.get())
#	a = new + 5
#	print(str(a))

def encrypt():
	final = "Encrypted: "

	plain = str(text.get())
	shift = int(num.get())

	text.delete(0, 'end')
	number.delete(0, 'end')

	for char in plain:
		
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

	enc = Label(root, text=final,fg="blue")
	enc.pack()

def decrypt():
	final = "Decrypted: "

	plain = str(text.get())
	shift = int(num.get())

	text.delete(0, 'end')
	number.delete(0, 'end')

	for char in plain:
		
		if char not in alphabet:
			final += char
			continue

		loca = alphabet.find(char)
		newVal = loca - shift

		#if newVal <= len(alphabet):
		#	while True:
		#		newVal += 26

		#		if newVal <= len(alphabet) and newVal >= 0:
		#			break

		final += alphabet[newVal]

	dec = Label(root, text=final,fg="blue")
	dec.pack()




press = Button(root, text="Encrypt", command=encrypt, fg="blue")
press2 = Button(root, text="Decrypt", command=decrypt, fg="blue")

label1 = Label(root, text="Enter Text", fg="blue")
label2 = Label(root, text="Enter shift(int) 1 - 25", fg="blue")

label1.pack()
text.pack()
label2.pack()
number.pack()
press.pack(side=LEFT)
press2.pack(side=RIGHT)

root.mainloop()
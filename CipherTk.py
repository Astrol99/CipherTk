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

def main():
	final = "Encrypted: "

	plain = str(text.get())
	shift = int(num.get())

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

	setUp = Label(root, text=final,fg="blue")
	setUp.pack()

press = Button(root, text="Enter", command=main, fg="blue")

label1 = Label(root, text="Enter Text", fg="blue")
label2 = Label(root, text="Enter shift(int)", fg="blue")

label1.pack()
text.pack()
label2.pack()
number.pack()
press.pack()

root.mainloop()
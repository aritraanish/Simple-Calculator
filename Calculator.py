from tkinter import *
import os
import base64

icon_base64 = '''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'''

icon_data = base64.b64decode(icon_base64)

icon_file = 'icon.ico'

icon = open(icon_file, "wb")

icon.write(icon_data)

icon.close()

root = Tk()

root.title('Calculator')

root.iconbitmap(icon_file)

os.remove(icon_file)

e = Entry(root, width=55, borderwidth=5)
e.grid(row = 0, columnspan=4, padx=20, pady=10)

global first_num, mul, div, sub, mul_number, div_number, sub_number
first_num = 0
mul = False
div = False
sub = False
mul_number = 1


def butpress0():
	e.insert(len(e.get()), "0")

def butpress1():
	e.insert(len(e.get()), "1")

def butpress2():
	e.insert(len(e.get()), "2")

def butpress3():
	e.insert(len(e.get()), "3")

def butpress4():
	e.insert(len(e.get()), "4")

def butpress5():
	e.insert(len(e.get()), "5")

def butpress6():
	e.insert(len(e.get()), "6")

def butpress7():
	e.insert(len(e.get()), "7")

def butpress8():
	e.insert(len(e.get()), "8")

def butpress9():
	e.insert(len(e.get()), "9")

def butpressclear():
	global first_num, mul, sub, div, mul_number, sub_number
	first_num = 0
	mul_number = 1
	sub_number = 0
	mul = False
	div = False
	sub = False
	e.delete(0, END)


def butpressplus():
	global first_num, mul, sub, div, mul_number
	first_num = first_num + float(e.get())
	e.delete(0, END)
	mul = False
	div = False
	sub = False
	print('printing from butpressplus ' + str(first_num))



def butpressequal():
	global first_num, mul, sub, div, mul_number, div_number, sub_number
	

	if mul:
		if e.get() == "":
			e.insert(0, mul_number)
		else:
			mul_number = mul_number * float(e.get())
			e.delete(0, END)
			e.insert(0, mul_number)
			print('printing from butpressequal for mul ' + str(mul_number))
	elif sub:
		if e.get() == "":
			e.insert(0, sub_number)
		else:
			sub_number = sub_number - float(e.get())
			e.delete(0, END)
			e.insert(0, sub_number)
			print('printing from butpressequal for sub ' + str(sub_number))
	elif div:
		if e.get() == "":
			e.insert(0, div_number)
		else:
			div_number = div_number / float(e.get())
			e.delete(0, END)
			e.insert(0, div_number)
	else:
		if e.get() == "":
			e.insert(0, first_num)
		else:
			first_num = first_num + float(e.get())
			e.delete(0, END)
			e.insert(0, first_num)
			print('printing from butpressequal for plus ' + str(first_num))


	mul = False
	sub = False
	div = False
	first_num = 0
	mul_number = 1


	


def butpressbackspace():
	current = str(e.get())
	e.delete(0, END)
	e.insert(0, current[:len(current)-1])


def butpressmul():
	global first_num, mul, sub, div, mul_number
	mul_number = mul_number * float(e.get())
	e.delete(0, END)
	mul = True
	div = False
	sub = False
	print('printing from butpressmul ' + str(mul_number))


def butpresssub():
	global first_num, mul, sub, div, mul_number, sub_number
	sub_number = float(e.get())
	e.delete(0, END)
	mul = False
	div = False
	sub = True
	print('printing from butpresssub ' + str(sub_number))
	


def butpressdot():

	if '.' in e.get():
		pass
	else:
		e.insert(len(e.get()), '.')


def butpressdiv():
	global first_num, mul, sub, div, mul_number, div_number
	div_number = float(e.get())
	e.delete(0, END)
	mul = False
	div = True
	sub = False
	print('printing from butpressdiv ' + str(div_number))



def butpresssign():
	current = e.get()
	e.delete(0, END)
	if current == '':
		e.insert(0, '-')
	elif current[0] == '+':
		e.insert(0, '-' + current[1:])
	elif current[0] == '-':
		e.insert(0, current[1:])
	else:
		e.insert(0, '-' + current)



ak = Label(root, text = "BY AK")
but7 = Button(root, text = "7", padx=40, pady=20, command=butpress7)
but8 = Button(root, text = "8", padx=40, pady=20, command=butpress8)
but9 = Button(root, text = "9", padx=40, pady=20, command=butpress9)
but4 = Button(root, text = "4", padx=40, pady=20, command=butpress4)
but5 = Button(root, text = "5", padx=40, pady=20, command=butpress5)
but6 = Button(root, text = "6", padx=40, pady=20, command=butpress6)
but1 = Button(root, text = "1", padx=40, pady=20, command=butpress1)
but2 = Button(root, text = "2", padx=40, pady=20, command=butpress2)
but3 = Button(root, text = "3", padx=40, pady=20, command=butpress3)
but0 = Button(root, text = "0", padx=40, pady=20, command=butpress0)
butclear = Button(root, text = "Clear", padx=30, pady=20, command=butpressclear)
butbackspace = Button(root, text="Backspace", padx=15, pady=20, command=butpressbackspace)
butplus = Button(root, text = "+", padx=38, pady=20, command=butpressplus)
butequal = Button(root, text = "=", padx=39, pady=20, command=butpressequal)
butmul = Button(root, text = "x", padx=39, pady=20, command=butpressmul)
butsub = Button(root, text = "-", padx=39, pady=20, command=butpresssub)
butdot = Button(root, text = ".", padx=43, pady=20, command=butpressdot)
butsign = Button(root, text = "+/-", padx=34, pady=20, command=butpresssign)
butdiv = Button(root, text = "/", padx=39, pady=20, command=butpressdiv)



ak.grid(row=1, column=0)
butclear.grid(row=1,column = 1)
butbackspace.grid(row=1, column=2)
butdiv.grid(row=1, column=3)
but7.grid(row=2, column=0)
but8.grid(row=2, column=1)
but9.grid(row=2, column=2)
butmul.grid(row=2, column=3)
but4.grid(row=3, column=0)
but5.grid(row=3, column=1)
but6.grid(row=3, column=2)
butsub.grid(row=3, column=3)
but1.grid(row=4, column=0)
but2.grid(row=4, column=1)
but3.grid(row=4, column=2)
butplus.grid(row=4, column = 3)
butsign.grid(row=5, column=0)
but0.grid(row=5, column=1)
butdot.grid(row=5, column=2)
butequal.grid(row=5, column=3)



root.mainloop()
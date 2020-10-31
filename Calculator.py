from tkinter import *

root = Tk()

root.title('Calculator')

root.iconbitmap("calc.ico")

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
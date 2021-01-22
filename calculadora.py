from tkinter import *


operador = 0


def digito(valor):
	global operador
	ingreso.insert(operador, valor)
	operador += 1


def calculo():
	cuenta = ingreso.get()
	resultado = eval(cuenta)
	ingreso.delete(0, END)
	ingreso.insert(0, resultado)
	operador = 0

def borrar():
	ingreso.delete(0, END)
	operador = 0	


app = Tk()

app.title("Calculadora")
app.iconbitmap("logo.ico")
app.geometry("353x400")
app.config(cursor="pirate")
app.config(bg="SpringGreen2") 
app.config(bd="10") 


ingreso = Entry (bd=10, font=("Cursive", 20))
ingreso.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


btn_1 = Button(app, text="1", width=4, height=2, command=lambda:digito(1))
btn_2 = Button(app, text="2", width=4, height=2, command=lambda:digito(2))
btn_3 = Button(app, text="3", width=4, height=2, command=lambda:digito(3))
btn_4 = Button(app, text="4", width=4, height=2, command=lambda:digito(4))
btn_5 = Button(app, text="5", width=4, height=2, command=lambda:digito(5))
btn_6 = Button(app, text="6", width=4, height=2, command=lambda:digito(6))
btn_7 = Button(app, text="7", width=4, height=2, command=lambda:digito(7))
btn_8 = Button(app, text="8", width=4, height=2, command=lambda:digito(8))
btn_9 = Button(app, text="9", width=4, height=2, command=lambda:digito(9))
btn_0 = Button(app, text="0", width=13, height=2, command=lambda:digito(0))

btn_borrar = Button(app, text="DEL", width=5, height=2, command=lambda:borrar())
btn_borrar.config(bg="gray44", font=("slant"))
btn_punto = Button(app, text=".", width=5, height=2, command=lambda:digito("."))
btn_paren1 = Button(app, text="(", width=5, height=2, command=lambda:digito("("))
btn_paren2 = Button(app, text=")", width=5, height=2, command=lambda:digito(")"))


btn_div = Button(app, text="/", width=5, height=2, command=lambda:digito("/"))
btn_div.config(bg="dark green", bd=4, fg="white")
btn_multi = Button(app, text="*", width=5, height=2, command=lambda:digito("*"))
btn_multi.config(bg="deep sky blue", bd=4, fg="white")
btn_suma = Button(app, text="+", width=5, height=2, command=lambda:digito("+"))
btn_suma.config(bg="red", bd=4, fg="white")
btn_resta = Button(app, text="-", width=5, height=2, command=lambda:digito("-"))
btn_resta.config(bg="gold", bd=4, fg="white")
btn_igual = Button(app, text="=", width=5, height=2, command=lambda:calculo())
btn_igual.config(bg="blue2", highlightthickness=6, bd=4, fg="white")


btn_borrar.grid(row=1, column=0, padx=5, pady=5)
btn_paren1.grid(row=1, column=1, padx=5, pady=5)
btn_paren2.config(bg="ghost white")
btn_paren2.grid(row=1, column=2, padx=5, pady=5)
btn_paren2.config(bg="ghost white")
btn_div.grid(row=1, column=3, padx=5, pady=5)


btn_7.grid(row=2, column=0, padx=3, pady=3)
btn_7.config(bg="ghost white")
btn_8.grid(row=2, column=1, padx=3, pady=3)
btn_8.config(bg="ghost white")
btn_9.grid(row=2, column=2, padx=3, pady=3)
btn_9.config(bg="ghost white")
btn_multi.grid(row=2, column=3, padx=5, pady=5)


btn_4.grid(row=3, column=0, padx=3, pady=3)
btn_4.config(bg="ghost white")
btn_5.grid(row=3, column=1, padx=3, pady=3)
btn_5.config(bg="ghost white")
btn_6.grid(row=3, column=2, padx=3, pady=3)
btn_6.config(bg="ghost white")
btn_suma.grid(row=3, column=3, padx=5, pady=5)


btn_1.grid(row=4, column=0, padx=3, pady=3)
btn_1.config(bg="ghost white")
btn_2.grid(row=4, column=1, padx=3, pady=3)
btn_2.config(bg="ghost white")
btn_3.grid(row=4, column=2, padx=3, pady=3)
btn_3.config(bg="ghost white")
btn_resta.grid(row=4, column=3, padx=5, pady=5)

btn_0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
btn_0.config(bg="ghost white")
btn_punto.grid(row=5, column=2, padx=5, pady=5)
btn_punto.config(bg="ghost white")
btn_igual.grid(row=5, column=3, padx=5, pady=5)


app.mainloop()
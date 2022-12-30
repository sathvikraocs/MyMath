from tkinter import *
import MyMath

main = Tk()
main.title('Scientific Calculator')
main.config(bg='#000000')
main.geometry('450x335')
main.resizable(FALSE,FALSE)

entryField = Entry(main, font=('times new roman',20,'bold'), bg='#000000', fg='#F1DDCF', bd=5, relief=RIDGE, width = 31, insertbackground = 'white')
entryField.grid(row=0,column=0,columnspan=8)

def click(value):
    val = entryField.get()
    try:
        if value=='Del':                    
            val = val[0:len(val) - 1]
            entryField.delete(0,END)
            entryField.insert(0, val)
        elif value=='AC':
            entryField.delete(0,END)
        elif value=="√":
            result = MyMath.sqmain(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="π":
            result = MyMath.pi
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="sinθ":
            result = MyMath.sin(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cosθ":
            result = MyMath.cos(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="tanθ":
            result = MyMath.cos(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="2π":
            result = 2*MyMath.pi
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cosecθ":
            result = MyMath.cosec(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="secθ":
            result = MyMath.sec(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cotθ":
            result = MyMath.cot(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value==chr(8731):                  #cube main
            result = MyMath.nthmain(eval(val),3)
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="x\u02b8":                  #x^y
            entryField.insert(END, '**')
        elif value=="x\u00B3":                  #x^3
            result = MyMath.cube(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="x\u00B2":                  #x^2
            result = MyMath.square(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="ln":
            result = MyMath.ln(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="Deg":
            result = MyMath.degrees(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="Rad":
            result = MyMath.radians(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="e":
            result = MyMath.e
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="log":
            result = MyMath.log(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="x!":
            result = MyMath.factorial(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value==chr(247):
            entryField.insert(END, "/")
            return
        elif value=="×":
            entryField.insert(END, "*")
            return
        elif value=="=":
            result = eval(val)
            entryField.delete(0,END)
            entryField.insert(0, result)
        else:
            entryField.insert(END, value)
    except SyntaxError:
        pass

button_text_list = ["Del", "AC", "√", "+", "π", "sinθ", "cosθ", "tanθ",
                    "1", "2", "3", "-", "2π", "cosecθ", "secθ", "cotθ",
                    "4", "5", "6", "×", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "Deg", "Rad", "e",
                    "0", ".", "%", "=", "log", "(", ")", "x!"]

rowvalue = 1
columnvalue = 0
for i in button_text_list:
    if i in '0123456789':
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#faba0a' , activebackground='#CCA01D', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in ["Del", "AC", "√", "+", "-", "×",chr(247), ".", "%", "="]:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#98d8ce' , activebackground='#c3dad4', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    else:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#0eab8c' , activebackground='#65a897', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

main.mainloop()
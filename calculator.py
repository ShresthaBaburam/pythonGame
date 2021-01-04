from tkinter import*

cal = Tk()
cal.title('Python Calculator')
operator = ''
text_input = StringVar()

def btnClick(numbers):
    global operator
    operator = operator+ str(numbers)
    text_input.set(operator)
def btnClearDisplay():
    global operator
    operator =''
    text_input.set('')

def btnEqualInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=''


# for the input textbox
text_display = Entry(cal, font=('arial',30, 'bold'), textvariable=text_input, bd=30, insertwidth=4,bg ='yellow', justify= 'right').grid(columnspan=5)
# for the 7 8 9 * C
btn7 = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='7', command = lambda:btnClick(7),bg = 'green').grid(row=1,column=0)
btn8 = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='8', command = lambda:btnClick(8),bg = 'green').grid(row=1,column=1)
btn9 = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='9', command = lambda:btnClick(9),bg = 'green').grid(row=1,column=2)
btnmul = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='*', command = lambda:btnClick('*'),bg = 'green').grid(row=1,column=3)
btnc = Button(cal, padx = 16, bd=8,fg="black",font=('arial',19,'bold'),text='C', command = lambda:btnClearDisplay(), bg = 'green').grid(row=1,column=4)
# for 4 5 6 / %
btn4 = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='4', command = lambda:btnClick(4), bg = 'green').grid(row=2,column=0)
btn5 = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='5', command = lambda:btnClick(5), bg = 'green').grid(row=2,column=1)
btn6 = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='6', command = lambda:btnClick(6), bg = 'green').grid(row=2,column=2)
btndiv = Button(cal, padx = 16, bd=8,fg="black",font=('arial',24,'bold'),text='/', command = lambda:btnClick('/'), bg = 'green').grid(row=2,column=3)
btnmod = Button(cal, padx = 16, bd=8,fg="black",font=('arial',19,'bold'),text='%', command = lambda:btnClick('%'), bg = 'green').grid(row=2,column=4)
# for 1 2 3 + //
btn1 = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='1', command = lambda:btnClick(1),bg = 'green').grid(row=3,column=0)
btn2 = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='2', command = lambda:btnClick(2),bg = 'green').grid(row=3,column=1)
btn3 = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='3', command = lambda:btnClick(3),bg = 'green').grid(row=3,column=2)
btnplus = Button(cal, padx = 16, bd=8,fg="black",font=('arial',19,'bold'),text='+', command = lambda:btnClick('+'),bg = 'green').grid(row=3,column=3)
btnfloor = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='//', command = lambda:btnClick('//'),bg = 'green').grid(row=3,column=4)
# for 0 . ^ - =
btn0 = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='0', command = lambda:btnClick(0),bg = 'green').grid(row=4,column=0)
btnpoint = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text=' .', command = lambda:btnClick('.'),bg = 'green').grid(row=4,column=1)
btnexp = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='^', command = lambda:btnClick('**'),bg = 'green').grid(row=4,column=2)
btnminus = Button(cal, padx = 16, bd=8,fg="black",font=('arial',23,'bold'),text='-', command = lambda:btnClick('-'),bg = 'green').grid(row=4,column=3)
btnequal = Button(cal, padx = 16, bd=8,fg="black",font=('arial',20,'bold'),text='=',command = lambda: btnEqualInput(), bg = 'green').grid(row=4,column=4)

cal.mainloop()

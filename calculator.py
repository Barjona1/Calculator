
from tkinter import *

def btnClick(num):
    global operator
    operator= operator + str (num)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualInput():
    global operator
    sum= str(eval(operator))
    text_Input.set(sum)
    operator=""


app = Tk()
app.title("Calculator")
operator=""
text_Input = StringVar()

textDisplay = Entry(app, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

btn7= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="7",bg="powder blue",command= lambda: btnClick(7)).grid(row=1, column=0)
btn8= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="8",bg="powder blue",command= lambda: btnClick(8)).grid(row=1, column=1)
btn9= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="9",bg="powder blue",command= lambda: btnClick(9)).grid(row=1, column=2)
addition= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="+",bg="powder blue",command= lambda: btnClick("+")).grid(row=1, column=3)

##################################################################################################################################
btn4= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="4",bg="powder blue" ,command= lambda: btnClick(4)).grid(row=2, column=0)
btn5= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="5",bg="powder blue",command= lambda: btnClick(5)).grid(row=2, column=1)
btn6= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="6",bg="powder blue",command= lambda: btnClick(6)).grid(row=2, column=2)
subtraction= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="-",bg="powder blue",command= lambda: btnClick("-")).grid(row=2, column=3)

##################################################################################################################################
btn1= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="1",bg="powder blue" ,command= lambda: btnClick(1)).grid(row=3, column=0)
btn2= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="2",bg="powder blue",command= lambda: btnClick(2)).grid(row=3, column=1)
btn3= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="3",bg="powder blue",command= lambda: btnClick(3)).grid(row=3, column=2)
multiplication= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="*",bg="powder blue",command= lambda: btnClick("*")).grid(row=3, column=3)

##################################################################################################################################
btn0= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="0",bg="powder blue" ,command= lambda: btnClick(0)).grid(row=4, column=0)
btnClear= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="C", bg="powder blue",command= btnClearDisplay).grid(row=4, column=1)
btnEqual= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="=",bg="powder blue", command= btnEqualInput).grid(row=4, column=2)
division= Button(app, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="/",bg="powder blue",command= lambda: btnClick("/")).grid(row=4, column=3)

app.mainloop()

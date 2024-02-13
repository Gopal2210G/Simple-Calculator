from tkinter import*

root = Tk()
root.title("Simple Calculator")
e=Entry(root, width=35,borderwidth=5)
e.grid(row=0, column=0,columnspan=3,padx=10,pady=10)


def Button_1add(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def buttonclear():
    e.delete(0,END)

def button_add():
    first_num=e.get()
    global f_num
    global math
    math="add"
    f_num=int(first_num)
    e.delete(0,END)

def button_sub():
    first_num=e.get()
    global f_num
    global math
    math="sub"
    f_num=int(first_num)
    e.delete(0,END)

def button_divide():
    first_num=e.get()
    global f_num
    global math
    math="div"
    f_num=int(first_num)
    e.delete(0,END)

def button_multi():
    first_num=e.get()
    global f_num
    global math
    math="mul"
    f_num=int(first_num)
    e.delete(0,END)

def button_equal():
    sec_num=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,f_num+int(sec_num))
    if math=="sub":
        e.insert(0,f_num-int(sec_num))
    if math=="mul":
        e.insert(0,f_num*int(sec_num))
    if math=="div":
        e.insert(0,f_num/int(sec_num))


Button1=Button(root,text="1",padx=40,pady=20,command=lambda: Button_1add(1))
Button2=Button(root,text="2",padx=40,pady=20,command=lambda: Button_1add(2))
Button3=Button(root,text="3",padx=40,pady=20,command=lambda: Button_1add(3))
Button4=Button(root,text="4",padx=40,pady=20,command=lambda: Button_1add(4))
Button5=Button(root,text="5",padx=40,pady=20,command=lambda: Button_1add(5))
Button6=Button(root,text="6",padx=40,pady=20,command=lambda: Button_1add(6))
Button7=Button(root,text="7",padx=40,pady=20,command=lambda: Button_1add(7))
Button8=Button(root,text="8",padx=40,pady=20,command=lambda: Button_1add(8))
Button9=Button(root,text="9",padx=40,pady=20,command=lambda: Button_1add(9))
Button0=Button(root,text="0",padx=40,pady=20,command=lambda: Button_1add(0))
buttonequal=Button(root,text="=",padx=91,pady=20,command=button_equal)
buttonclear=Button(root,text="Clear",padx=79,pady=20,command= buttonclear)
button_add=Button(root,text="+",padx=40,pady=20,command=button_add)

button_sub=Button(root,text="-",padx=40,pady=20,command=button_sub)
button_multi=Button(root,text="*",padx=40,pady=20,command=button_multi)
button_divide=Button(root,text="/",padx=40,pady=20,command=button_divide)



Button1.grid(row=3,column=0)
Button2.grid(row=3,column=1)
Button3.grid(row=3,column=2)

Button4.grid(row=2,column=0)
Button5.grid(row=2,column=1)
Button6.grid(row=2,column=2)

Button7.grid(row=1,column=0)
Button8.grid(row=1,column=1)
Button9.grid(row=1,column=2)

Button0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)

button_multi.grid(row=5,column=0)
buttonclear.grid(row=5,column=1,columnspan=2)

buttonequal.grid(row=6,column=1,columnspan=2)
button_divide.grid(row=6,column=0)




root.mainloop()
# +-------------------------------------------------------------------------------+
# |   Calculator to Add ,Subtract ,Multiply and Divide two number using Tkinter   |
# +-------------------------------------------------------------------------------+
# |                          Author : Prashant Bhandari                           |
# +-------------------------------------------------------------------------------+


import tkinter as t
import tkinter.font as tkFont


def add():
    sw = t.Tk()
    sw.title("Sum")
    sw.geometry("500x50")
    ftl = tkFont.Font(family='Times', size=18)
    try:
        a = text1.get()
        b = text2.get()
        s = float(a) + float(b)
        sum = t.Label(sw, font=ftl, fg="blue", text="Sum = " + str(s))
        sum.pack()
    except:
        sw.title("Error")
        error = t.Label(sw, font=ftl, fg="blue", text="Inputed data in not an Intiger.")
        error.pack()
    sw.mainloop()


def sub():
    dw = t.Tk()
    dw.title("Difference")
    dw.geometry("500x50")
    ftl = tkFont.Font(family='Times', size=18)
    try:
        a = text1.get()
        b = text2.get()
        d = float(a) - float(b)
        diff = t.Label(dw, font=ftl, fg="blue", text="Difference = " + str(d))
        diff.pack()
    except:
        dw.title("Error")
        error = t.Label(dw, font=ftl, fg="blue", text="Inputed data in not an Intiger.")
        error.pack()
    dw.mainloop()


def mul():
    pw = t.Tk()
    pw.title("Product")
    pw.geometry("500x50")
    ftl = tkFont.Font(family='Times', size=18)
    try:
        a = text1.get()
        b = text2.get()
        p = float(a) * float(b)
        pro = t.Label(pw, font=ftl, fg="blue", text="Product = " + str(p))
        pro.pack()
    except:
        pw.title("Error")
        error = t.Label(pw, font=ftl, fg="blue", text="Inputed data in not an Intiger.")
        error.pack()
    pw.mainloop()


def div():
    qw = t.Tk()
    qw.title("Sum")
    qw.geometry("500x50")
    ftl = tkFont.Font(family='Times', size=18)
    try:
        a = text1.get()
        b = text2.get()
        s = float(a) / float(b)
        quo = t.Label(qw, font=ftl, fg="blue", text="Quotient = " + str(s))
        quo.pack()
    except:
        qw.title("Error")
        error = t.Label(qw, font=ftl, fg="blue", text="Inputed data in not an Intiger.")
        error.pack()
        qw.mainloop()


def main():
    c = t.Tk()
    c.title("Calculator")
    c.geometry("252x277")
    c.minsize(252, 277)
    c.maxsize(252, 277)
    ft = tkFont.Font(family='Times', size=18)
    label1 = t.Label(c, font=ft, text="Enter 1st number:", fg="blue")
    label1.place(x=0, y=0, width=251, height=30)
    global text1
    text1 = t.Entry(c, font=ft, justify="center", bg="yellow", fg="red")
    text1.place(x=0, y=30, width=250, height=30)
    label2 = t.Label(c, font=ft, text="Enter 2nd number:", fg="blue")
    label2.place(x=0, y=60, width=251, height=30)
    global text2
    text2 = t.Entry(c, font=ft, justify="center", bg="yellow", fg="red")
    text2.place(x=0, y=90, width=250, height=30)
    btn1 = t.Button(c, text="+", font=ft, bg="black", fg="white", command=add)
    btn1.place(x=100, y=120, width=50, height=50)
    btn2 = t.Button(c, text="-", font=ft, bg="black", fg="white", command=sub)
    btn2.place(x=50, y=170, width=50, height=50)
    btn3 = t.Button(c, text="*", font=ft, bg="black", fg="white", command=mul)
    btn3.place(x=150, y=170, width=50, height=50)
    btn4 = t.Button(c, text="/", font=ft, bg="black", fg="white", command=div)
    btn4.place(x=100, y=220, width=50, height=50)
    c.mainloop()


if __name__ == '__main__':
    main()

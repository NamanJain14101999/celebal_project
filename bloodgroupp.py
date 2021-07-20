from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from  scrolling_area import *
import tkinter.messagebox
from tkcalendar import *
import time
root=Tk()
root.geometry("1200x890+0+0")
root.config(bg="SKYBLUE")
root.title("blood bank")
root.resizable(0,0)
l=Label(text="BLOOD DONOR BANK",fg="BLACK",bg="SKYBLUE",font=("Bradley Hand ITC", 24, "bold "))
l.pack()
local=time.asctime()
def blood():
    frame = Frame(root,width=1100,height=890,bg="yellow")
    frame.pack()
    img = ImageTk.PhotoImage(Image.open("hospital.jpg"))
    Label(frame,image=img,height=1200,width=1200).pack()
    b = Button(text="USER",width=20,bd=10,bg="TURQUOISE",fg="black",cursor="hand2",relief=RIDGE,command=lambda:add(frame,root))
    b.place(x=200,y=100)
    b1 = Button(text="ADMIN",width=20,bd=10,bg="TURQUOISE",fg="black",cursor="hand2",relief=RIDGE,command=lambda:details(frame,root))
    b1.place(x=750,y=100)
    frame.mainloop()

    #working of add button

def add(frame,root):
    frame.destroy()
    frame2= Frame(root,width=1100,height="890",bg="yellow")
    frame2.pack()
    img= ImageTk.PhotoImage(Image.open("hospital6.jpg"))
    Label(frame2,image=img,height=1000,width=1200).pack()
    #entry
    l1 = Label(text="NAME",fg="black",font=("Bell MT",14,"bold "))
    l1.place(x=20,y=100)
    e1 = Entry(textvariable=StringVar(),width=32, bd=7, font=("Bell MT",14,"bold"))
    e1.place(x=300,y=95)
    l2 = Label(text="BLOOD GROUP",fg="black",font=("Bell MT",14,"bold"))
    l2.place(x=20,y=210)
    variable=StringVar(frame2)
    variable.set(" ")
    e2 = OptionMenu(frame2,variable,'A+','A-','B+','B-','AB+','AB-','O+','O-')
    e2.config(width=47,bg="white",bd=7)
    e2.place(x=300, y=160)
    l3 = Label(text="DOB",fg="black",font=("Bell MT",14,"bold"))
    l3.place(x=20,y=310)
    var1=IntVar()
    e3 = DateEntry(textvariable=var1,width=32, bd=10, font=("Bell MT",14,"bold"))
    e3.place(x=300,y=300)
    l4 = Label(text="CONTACT",fg="black",font=("Bell MT",14,"bold"))
    l4.place(x=20,y=410)
    e4 = Entry(textvariable=IntVar(),width=32, bd=7, font=("Bell MT",14,"bold"))
    e4.place(x=300,y=400)
    l5 = Label(text="ADDRESS",fg="black",font=("Bell MT",14,"bold"))
    l5.place(x=20,y=520)
    e5 = Entry(textvariable=StringVar(),width=32,bd=7,font=("Bell MT",14,"bold"))
    e5.place(x=300,y=510)
    #buttons in add
    b2 = Button(text="SUBMIT",width=20,bd=10,bg="TURQUOISE",fg="black",relief=RIDGE,cursor="hand2",command=lambda:submit(frame2,root,e1,variable,e3,e4,e5))
    b2.place(x=20,y=600)
    b3 = Button(text="BACK",width=20,bd=10,bg="TURQUOISE",fg="black",relief=RIDGE,cursor="hand2",command=lambda:back(frame2,root))
    b3.place(x=400,y=600)
    b4 = Button(text="RESET",width=20,bd=10,bg="TURQUOISE",fg="black",relief=RIDGE,cursor="hand2",command=lambda:add(frame2,root))
    b4.place(x=780,y=600)

   # def reset():
    #    e1.delete(0, END)
    #    e3.delete(0, END)
    #    e4.delete(0, END)
    #    e5.delete(0, END)
   # b4 = Button(text="RESET", width=20, bd=10, bg="red", fg="black",command=reset)
    #b4.place(x=580, y=600)
    frame2.mainloop()
def back(frame2,root):
    frame2.destroy()
    blood()
def submit(frame2,root,e1,variable,e3,e4,e5):
    a=e1.get()
    b=variable.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()

    print(a,b,c,d,e)
    con=sqlite3.connect("BLOODDONATION")
    con.execute("create table if not exists TEST(NAME char[20],BLOODGROUP char[20],DOB int[10],CONTACT int[30],ADDRESS char[80])")
    query="insert into TEST(NAME,BLOODGROUP,DOB,CONTACT,ADDRESS)Values('{}','{}','{}',{},'{}')".format(a,b,c,d,e)
    i=con.execute(query)
    con.commit()
    m=con.execute("select * from TEST")
    print(list(m))
    print("DATA WILL BE SUCCESSFULLY INSERTED")
    con.close()
    if(len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0):
        tkinter.messagebox.showwarning("INCOMPLETE REGISTRATION", "FIRST FILL THE ENTRY BLOCKS")
    else:
        tkinter.messagebox.showinfo("SUCCESS", "REGISTRATION IS COMPLETED")

    #SHOW FUNCTION
def details(frame,root):
    frame.destroy()
    frame3= Frame(root,width=1100,height="890",bg="SKYBLUE")
    frame3.pack()
    img = ImageTk.PhotoImage(Image.open("hospital6.jpg"))
    Label(frame3,image=img,height=1500,width=5000).pack()
    a = IntVar()
    b = IntVar()
    c = IntVar()
    d = IntVar()
    e = IntVar()
    f = IntVar()
    g = IntVar()
    h = IntVar()
    s1 = Label(text="PLEASE SELECT A BLOOD GROUP",fg="black",bg="SKYBLUE",font=("Bell MT", 14, "bold "))
    s1.place(x=20,y=70)
    c1=Checkbutton(frame3,text='A+',height=2,width=2,bg="RED",relief=RIDGE,cursor="hand2",variable=a)
    c1.place(x=20,y=100)
    c2 = Checkbutton(frame3,text='A-',height=2,width=2,bg="RED",relief=RIDGE,cursor="hand2",variable=b)
    c2.place(x=20,y=160)
    c3 = Checkbutton(frame3,text='B+',height=2,width=2,bg="RED",relief=RIDGE,cursor="hand2",variable=c)
    c3.place(x=20,y=220)
    c4 = Checkbutton(frame3,text='B-',height=2,width=2,bg="RED",relief=RIDGE,cursor="hand2",variable=d)
    c4.place(x=20,y=280)
    c5 = Checkbutton(frame3,text='AB+',height=2,width=2,bg="RED",relief=RIDGE,cursor="hand2",variable=e)
    c5.place(x=20,y=340)
    c6 = Checkbutton(frame3,text='AB-',height=2,width=2,bg="RED",relief=RIDGE,cursor="hand2",variable=f)


    c6.place(x=20,y=400)
    c7 = Checkbutton(frame3,text='O+',height=2,width=2,bg="RED",relief=RIDGE,cursor="hand2",variable=g)
    c7.place(x=20, y=460)
    c8 = Checkbutton(frame3,text='O-',height=2,width=2,bg="RED",relief=RIDGE,cursor="hand2",variable=h)
    c8.place(x=20,y=520)
# buttons in details

    b5 = Button(text="OK",width=20,bd=10,bg="TURQUOISE",fg="black",relief=RIDGE,cursor="hand2",command=lambda:ok(frame3,root,a,b,c,d,e,f,g,h) )
    b5.place(x=200,y=600)
    b6 = Button(text="BACK",width=20,bd=10,bg="TURQUOISE",fg="black",relief=RIDGE,cursor="hand2",command=lambda:back1(frame3,root))
    b6.place(x=580,y=600)
    b7 = Button(text="RESET",width=20,bd=10,bg="TURQUOISE",fg="black",relief=RIDGE,cursor="hand2",command=lambda:details(frame3,root))
    b7.place(x=940,y=600)
    frame3.mainloop()
#back function in show
def back1(frame3,root):
    frame3.destroy()
    blood()
#OK FUNCTION IN DETAILS
def ok(frame3,root,a,b,c,d,e,f,g,h):
    frame3.destroy()
    frame4=Frame(root,width=1100,height="890",bg="SKYBLUE")
    frame4.pack()
   # textaera=Text(frame4,width=10,height=10,fg="black",bg="white")
   # textaera.place(x=20,y=35)b
    img=ImageTk.PhotoImage(Image.open('hospital7.jpg'))
    Label(frame4,image=img,height=5000,width=3000).pack()
    f1 =a.get()
    f2 =b.get()


    f3 =c.get()
    f4 =d.get()
    f5 =e.get()
    f6 =f.get()
    f7 =g.get()
    f8 =h.get()
    print(f1,f2,f3,f4,f5,f6,f7,f8)
    con=sqlite3.connect("BLOODDONATION")
    scrolling_area=Scrolling_Area(frame4,height=280)
    scrolling_area.place(x=39,y=150)
    table=Table(scrolling_area.innerframe,["NAME   ","BLOODGROUP    ","DOB  ","CONTACT  ","ADDRESS  "],column_minwidths=[222,222,222,222,222])
    table.pack(expand=True,fill=X)
    table.on_change_data(scrolling_area.update_viewport)
    #BACK BUTTON IN TABLE(0K)
    b8 = Button(text="BACK", width=20, bd=10, bg="yellow",relief=RIDGE,cursor="hand2", fg="black", command=lambda:details(frame4,root))
    b8.place(x=780,y=600)
    #def back2(frame4,root):
     #   frame4.destroy()
      #  details(frame3,root)

    if f1==1:
        o1=con.execute("select * from TEST where BLOODGROUP='A+'")
        con.commit()
        data=[]
        for row in o1:
            column=[]
            data.append(column)
            for r in row:
                print(r)
                column.append(r)
        table.set_data(data)

    if f2==1:
        o2 = con.execute("select * from TEST where BLOODGROUP='A-'")
        con.commit()
        data=[]
        for row in o2:
            column =[]
            data.append(column)
            for r in row:
                print(r)
                column.append(r)
        table.set_data(data)

    if f3==1:
        o3 = con.execute("select * from TEST where BLOODGROUP='B+'")
        con.commit()
        data=[]
        for row in o3:
            column = []
            data.append(column)
            for r in row:
                print(r)
                column.append(r)
        table.set_data(data)

    if f4==1:
        o4 = con.execute("select * from TEST where BLOODGROUP='B-'")
        con.commit()
        data =[]
        for row in o4:
            column = []
            data.append(column)
            for r in row:
                print(r)
                column.append(r)
        table.set_data(data)


    if f5 == 1:
        o5 = con.execute("select * from TEST where BLOODGROUP='AB+'")
        con.commit()
        data =[]
        for row in o5:
            column = []
            data.append(column)
            for r in row:
                print(r)
                column.append(r)
        table.set_data(data)

    if f6 == 1:
        o6 = con.execute("select * from TEST where BLOODGROUP='AB-'")
        con.commit()
        data = []
        for row in o6:
            column = []
            data.append(column)
            for r in row:
                print(r)
                column.append(r)
        table.set_data(data)


    if f7== 1:
        o7 = con.execute("select * from TEST where BLOODGROUP='O+'")
        con.commit()
        data = []
        for row in o7:
            column = []
            data.append(column)
            for r in row:
                print(r)
                column.append(r)
        table.set_data(data)

    if f8== 1:
        o8 = con.execute("select * from TEST where BLOODGROUP='O-'")
        con.commit()
        data=[]
        for row in o8:
            column = []
            data.append(column)
            for r in row:
                print(r)
                column.append(r)
        table.set_data(data)
    if(f1==0 and f2==0 and f3==0 and f4==0 and f5==0 and f6==0 and f7==0 and f8==0):
            tkinter.messagebox.showwarning("INCOMPLETE REGISTRATION", "FIRST FILL THE ENTRY BLOCKS")

    frame4.mainloop()
blood()
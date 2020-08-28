from tkinter import *
root=Tk()
root.title("Calculator")
root.configure(bg="Red")
Elements = ['789/','456*','123-','0.+']
def Display(f):
    global s1
    s1 = s1+f
    s.set(s1)
def Equal():
    global s1
    s1=''
    t=s.get()
    s1=str(eval(t))
    s.set(s1)
def clear():
    global s1
    s1=''
    s.set(s1)
def clear1():
    global s1
    s1=s1[:len(s1)-1]
    s.set(s1)
s1 = ''
s=StringVar()
e =Entry(text=s,bg="White",fg="Black",font=('arial',40,"bold"),justify='right',width=12)
e.grid(row=0,column=0,padx=3,pady=3,columnspan=4,sticky='nsew')
row1 = 1
col1 = 0
for i in Elements:
    col1=0
    for j in i:
        l = Button(root,text=j,bg="Black",fg="white",font=('arial',20,"bold"),width=2,height=2,command=lambda f=j:Display(f))
        l.grid(row=row1,column=col1,padx=3,pady=3,sticky='nsew')
        col1=col1+1
    row1=row1+1
l = Button(root,text="=",bg="Black",fg="white",font=('arial',20,"bold"),width=2,height=2,command=Equal)
l.grid(row=4,column=3,padx=3,pady=3,sticky='nsew')
l = Button(root,text="C",bg="Black",fg="white",font=('arial',20,"bold"),width=2,height=1,command=clear1)
l.grid(row=5,column=0,padx=3,pady=3,sticky='nsew',columnspan=2)
l = Button(root,text="CE",bg="Black",fg="white",font=('arial',20,"bold"),width=2,height=1,command=clear)
l.grid(row=5,column=2,padx=3,pady=3,sticky='nsew',columnspan=2)
for i in range(6):
    root.grid_rowconfigure(i,weight=1)
for i in range(4):
    root.grid_columnconfigure(i,weight=1)
root.mainloop()

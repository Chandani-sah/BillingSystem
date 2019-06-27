from tkinter import *
import random
import time;
root=Tk()

root.title("Restaurant Management System")
text_Input=StringVar();
operator=" "
Tops=Frame(root,width=1000,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=200,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#--------------------------------------------------Time--------------------------------------
localtime=time.asctime(time.localtime(time.time()))

#--------------------------------------------------------------------Information--------------------------------------------------------------------------------------------------
lbInfo=Label(Tops,font=('arial',35,'bold'),text="Restaurant Accounting",fg="Steel Blue",bd=10,anchor='w')
lbInfo.grid(row=0,column=0)

lbInf=Label(Tops,font=('arial',15,'bold'),text="NMIT, Bangalore 560064",fg="Steel Blue",bd=10,anchor='w')
lbInf.grid(row=3,column=0)
            
tim=Label(Tops,font=('arial',15,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
tim.grid(row=4,column=0)
#-----------------------------------------------------------------------calculator------------------------------------------------------------------------------------------------
def btnClick(numbers):
        global operator
        operator = operator + str(numbers)
        text_Input.set(operator)
def btnClear():
        global operator
        operator=" "
        text_Input.set(" ")

def btnequalInput():
        global operator,sum,sub_sum,tot_sum
        sum=str(eval(operator))
        sub_sum=str(eval(operator))
        text_Input.set(sum)
def ref():
        global sub_sum
        x=random.randint(10908,500876)
        randomref=str(x)
        rand.set(randomref)
        subtotal.set(sub_sum)
        t=int(serviceentry.get())+int(taxentry.get())+int(subentry.get())
        total.set(str(t))
        
def qexit():
        root.destroy()

def reset():
        rand.set(" ")
        water.set(" ")
        a.set(" ")
        b.set(" ")
        c.set(" ")
        d.set(" ")
        e.set(" ")
        subtotal.set(" ")
        total.set(" ")
        service_charge.set(" ")
        Tax.set(" ")
        cost.set(" ")
        
e1=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="white",justify="right")
e1.grid(columnspan=4)
#---------------------------------------------------------------------------Number Button------------------------------------------------------------------------------------------------------------
b7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="crimson",command=lambda:btnClick(7))
b7.grid(row=2,column=0)

b8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="crimson",command=lambda:btnClick(8))
b8.grid(row=2,column=1)

b9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="crimson",command=lambda:btnClick(9))
b9.grid(row=2,column=2)

b4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="crimson",command=lambda:btnClick(4))
b4.grid(row=3,column=0)

b5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="crimson",command=lambda:btnClick(5))
b5.grid(row=3,column=1)

b6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="crimson",command=lambda:btnClick(6))
b6.grid(row=3,column=2)

b3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="crimson",command=lambda:btnClick(1))
b3.grid(row=4,column=0)

b2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="crimson",command=lambda:btnClick(2))
b2.grid(row=4,column=1)

b1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="crimson",command=lambda:btnClick(3))
b1.grid(row=4,column=2)

b0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="crimson",command=lambda:btnClick(0))
b0.grid(row=5,column=1)

#----------------------------------------------------------------------operator  Button---------------------------------------------------------------------------------------------------------------------

bdiv=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="crimson",command=lambda:btnClick("/"))
bdiv.grid(row=2,column=3)

bmult=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="crimson",command=lambda:btnClick("*"))
bmult.grid(row=3,column=3)

bminus=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="crimson",command=lambda:btnClick("-"))
bminus.grid(row=4,column=3)

badd=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="crimson",command=lambda:btnClick("+"))
badd.grid(row=5,column=3)

bclear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="c",bg="crimson",command=btnClear)
bclear.grid(row=5,column=0)

bequal=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="crimson",command= btnequalInput)
bequal.grid(row=5,column=2)
#-------------------------------------------------------------Restaurant info-------------------------------------------------------------------------------------------------------------------------------------------------
rand = StringVar()
water=StringVar()
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
subtotal=StringVar()
total=StringVar()
service_charge=StringVar()
Tax=StringVar()
cost=StringVar()

billno=Label(f1,font=('arial',16,'bold'),text="Bill No:",bd=16,anchor='w')
billno.grid(row=0,column=0)
billentry=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="crimson",justify="right")
billentry.grid(row=0,column=1)

w=Label(f1,font=('arial',16,'bold'),text="PACKAGED WATER",bd=16,anchor='w')
w.grid(row=1,column=0)
wentry=Entry(f1,font=('arial',16,'bold'),textvariable=water,bd=10,insertwidth=4,bg="crimson",justify="right")
wentry.grid(row=1,column=1)

beer=Label(f1,font=('arial',16,'bold'),text="BEER",bd=16,anchor='w')
beer.grid(row=2,column=0)
beerentry=Entry(f1,font=('arial',16,'bold'),textvariable=a,bd=10,insertwidth=4,bg="crimson",justify="right")
beerentry.grid(row=2,column=1)


vodka=Label(f1,font=('arial',16,'bold'),text="VODKA",bd=16,anchor='w')
vodka.grid(row=3,column=0)
vodkaentry=Entry(f1,font=('arial',16,'bold'),textvariable=b,bd=10,insertwidth=4,bg="crimson",justify="right")
vodkaentry.grid(row=3,column=1)


cold=Label(f1,font=('arial',16,'bold'),text="COLD DRINKS",bd=16,anchor='w')
cold.grid(row=4,column=0)
coldentry=Entry(f1,font=('arial',16,'bold'),textvariable=c,bd=10,insertwidth=4,bg="crimson",justify="right")
coldentry.grid(row=4,column=1)


wishky=Label(f1,font=('arial',16,'bold'),text="WISHKY",bd=16,anchor='w')
wishky.grid(row=5,column=0)
wishkyentry=Entry(f1,font=('arial',16,'bold'),textvariable=d,bd=10,insertwidth=4,bg="crimson",justify="right")
wishkyentry.grid(row=5,column=1)
#-----------------------------------------------------------------Information 2------------------------------------------------------------------------------------------------
cocktail=Label(f1,font=('arial',16,'bold'),text="Cocktail",bd=16,anchor='w')
cocktail.grid(row=0,column=2)
cocktailentry=Entry(f1,font=('arial',16,'bold'),textvariable=e,bd=10,insertwidth=4,bg="crimson",justify="right")
cocktailentry.grid(row=0,column=3)

drinks=Label(f1,font=('arial',16,'bold'),text="cost of drinks",bd=16,anchor='w')
drinks.grid(row=1,column=2)
drinksentry=Entry(f1,font=('arial',16,'bold'),textvariable=cost,bd=10,insertwidth=4,bg="crimson",justify="right")
drinksentry.grid(row=1,column=3)


sub=Label(f1,font=('arial',16,'bold'),text="Sub-total",bd=16,anchor='w')
sub.grid(row=2,column=2)
subentry=Entry(f1,font=('arial',16,'bold'),textvariable=subtotal,bd=10,insertwidth=4,bg="crimson",justify="right")
subentry.grid(row=2,column=3)

service=Label(f1,font=('arial',16,'bold'),text="Service charge",bd=16,anchor='w')
service.grid(row=3,column=2)
serviceentry=Entry(f1,font=('arial',16,'bold'),textvariable=service_charge,bd=10,insertwidth=4,bg="crimson",justify="right")
serviceentry.grid(row=3,column=3)


tax=Label(f1,font=('arial',16,'bold'),text="Tax",bd=16,anchor='w')
tax.grid(row=4,column=2)
taxentry=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="crimson",justify="right")
taxentry.grid(row=4,column=3)


tot=Label(f1,font=('arial',16,'bold'),text="Total",bd=16,anchor='w')
tot.grid(row=5,column=2)
totentry=Entry(f1,font=('arial',16,'bold'),textvariable=total,bd=10,insertwidth=4,bg="crimson",justify="right")
totentry.grid(row=5,column=3)
#-----------------------------------------------------------------------Button------------------------------------------------------------------------------------------------------------------------------------
totalBut=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",command=ref).grid(row=7,column=1)

exitBut=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="EXIT",command=qexit).grid(row=7,column=2)

resetBut=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="RESET",command=reset).grid(row=7,column=3)

root.mainloop()

from tkinter import*
import time
import datetime
root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")
Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)
f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
localtime=time.asctime(time.localtime(time.time()))
lblInfo=Label(Tops,font=('arial',50,'bold'),text="VELAMMAL RESTAURANT",fg="Blue Violet",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Blue Violet",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
def Ref():
    if (Idly.get()==""):
        CoIdly=0
    else:
        CoIdly=float(Idly.get())
    if (Dosa.get()==""):
        CoDosa=0
    else:
        CoDosa=float(Dosa.get())
    if (Ven_Pongal.get()==""):
        CoVen_Pongal=0
    else:
        CoVen_Pongal=float(Ven_Pongal.get())
    if (Poori.get()==""):
        CoPoori=0
    else:
        CoPoori=float(Poori.get())  
    if (Methu_Vada.get()==""):
        CoMethu_Vada=0
    else:
        CoMethu_Vada=float(Methu_Vada.get())
    if (Pepsi.get()==""):
        CoPepsi=0
    else:
        CoPepsi=float(Pepsi.get())
    if (Cocacola.get()==""):
        CoCocacola=0
    else:
        CoCocacola=float(Cocacola.get())
    CostofIdly =CoIdly * 20
    CostofPepsi=CoPepsi * 25
    CostofCocacola=CoCocacola * 25
    CostofDosa = CoDosa* 40
    CostofVen_Pongal = CoVen_Pongal * 35
    CostPoori = CoPoori* 35
    CostMethu_Vada=CoMethu_Vada* 10
CostofMeal= "Rs", str('%.2f' %(CostofIdly+CostofPepsi+CostofCocacola+CostofDosa+CostofVen_Pongal+CostPoori+CostMethu_Vada))
PayTax=((CostofIdly+CostofPepsi+CostofCocacola+CostofDosa+CostofVen_Pongal+CostPoori+CostMethu_Vada) * 0.2)
TotalCost=(CostofIdly+CostofPepsi+CostofCocacola+CostofDosa+CostofVen_Pongal+CostPoori+CostMethu_Vada)
Ser_Charge= ((CostofIdly+CostofPepsi+CostofCocacola+CostofDosa+CostofVen_Pongal+CostPoori+CostMethu_Vada)/99)
Service = "Rs", str ('%.2f' % Ser_Charge)
OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))
PaidTax= "Rs", str ('%.2f' % PayTax)
Service_Charge.set(Service)
Cost.set(CostofMeal)
Tax.set(PaidTax)
SubTotal.set(CostofMeal)
Total.set(OverAllCost)
def qExit():
    root.destroy()
def Reset():
    rand.set("") 
    Idly.set("")
    Dosa.set("")
    Ven_Pongal.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Pepsi.set("")
    Cocacola.set("")
    Tax.set("")
    Cost.set("")
    Poori.set("")
    Methu_Vada.set("")
rand = StringVar()
Idly=StringVar()
Dosa=StringVar()
Ven_Pongal=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Pepsi=StringVar()
Cocacola=StringVar()
Tax=StringVar()
Cost=StringVar()
Poori=StringVar()
Methu_Vada=StringVar()
lblIdly= Label(f1, font=('arial', 16, 'bold'),text="Idly",bd=16,anchor="w")
lblIdly.grid(row=0, column=0)
txtIdly=Entry(f1, font=('arial',16,'bold'),textvariable=Idly,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtIdly.grid(row=0,column=1)
lblDosa= Label(f1, font=('arial', 16, 'bold'),text="Dosa",bd=16,anchor="w")
lblDosa.grid(row=1, column=0)
txtDosa=Entry(f1, font=('arial',16,'bold'),textvariable=Dosa,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDosa.grid(row=1,column=1)
lblVen_Pongal= Label(f1, font=('arial', 16, 'bold'),text="Ven_Pongal ",bd=16,anchor="w")
lblVen_Pongal.grid(row=2, column=0)
txtVen_Pongal=Entry(f1, font=('arial',16,'bold'),textvariable=Ven_Pongal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtVen_Pongal.grid(row=2,column=1)
lblPoori= Label(f1, font=('arial', 16, 'bold'),text="Poori",bd=16,anchor="w")
lblPoori.grid(row=3, column=0)
txtPoori=Entry(f1, font=('arial',16,'bold'),textvariable=Poori,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPoori.grid(row=3,column=1)

lblMethu_Vada= Label(f1, font=('arial', 16, 'bold'),text="Methu_Vada",bd=16,anchor="w")
lblMethu_Vada.grid(row=4, column=0)
txtMethu_Vada=Entry(f1, font=('arial',16,'bold'),textvariable=Methu_Vada,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtMethu_Vada.grid(row=4,column=1)

lblPepsi= Label(f1, font=('arial', 16, 'bold'),text="Pepsi",bd=16,anchor="w")
lblPepsi.grid(row=0, column=2)
txtPepsi=Entry(f1, font=('arial',16,'bold'),textvariable=Pepsi,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPepsi.grid(row=0,column=3)
lblCocacola= Label(f1, font=('arial', 16, 'bold'),text="Cocacola",bd=16,anchor="w")
lblCocacola.grid(row=1, column=2)
txtCocacola=Entry(f1, font=('arial',16,'bold'),textvariable=Cocacola,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCocacola.grid(row=1,column=3)
lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=2, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=2,column=3)
lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=3, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=3,column=3)
lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="GST",bd=16,anchor="w")
lblStateTax.grid(row=4, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)
root.mainloop()


from tkinter import *
import sqlite3
from functools import partial

##create the basic GUI window
root=Tk()
root.geometry("950x940")
root.title("INVENTORY MANAGEMENT SYSTEM")
Label(root,text="INVENTORY MANAGEMENT SYSTEM", font="Times 28", bg="Aqua").grid(row=0,column=16)

#global u
#global p

Username=StringVar()
Password=StringVar()    

# create the database
#def database():
#	u=Username.get()
#	p=Password.get()
#	conn=sqlite3.connect('myadmin.db')
#	with conn:
#		cursor=conn.cursor()
#		cursor.execute('CREATE TABLE IF NOT EXISTS ADMIN(Username Text,Password Text)')
#		cursor.execute('INSERT INTO ADMIN(Username,Password) VALUES(?,?)',(u,p))
#		conn.commit()
#validation of username and password
#def validatelogin():
	#print("Username entered:",Username.get())
	#print("Password entered:",Password.get())
	#if Username.get()==u and Password.get()==p:
	#rows=cursor.fetchall()
	#for rows in row:
		#if e1==u and e2==p:

# create database for the fabric inventory
#def fab_database():
	#SEASON=Sea.get()
	#SUPPLIER=Supp.get()
	#BUYER=Buy.get()
	#STYLENO=Sty.get()
	#
#		conn.commit()



def Exit():
	root.destroy()
def admin():
	admin=Toplevel()
	admin.geometry("950x940")
	admin.title("ADMIN USERS") 
	Label(admin,text="CHOOSE THE CATEGORY",font="Times 18").grid(row=0,column=17)
	fab_btn=Button(admin,text="FABRIC INVENTORY",command=fab,font="Times 16").grid(row=1,column=7)
	trim_btn=Button(admin,text="TRIMS INVENTORY",command=trim,font="Times 16").grid(row=1,column=14)
	pkg_btn=Button(admin,text="PACKAGING MATERIAL INVENTORY",command=pkgm,font="Times 16").grid(row=1,column=21)
	acc_btn=Button(admin,text="ACCESSORIES INVENTORY",command=accs,font="Times 16").grid(row=1,column=28)
	
## create window for fabric inventory
def fab():
	fab=Toplevel()
	fab.geometry("1050x1040")
	fab.title("FABRIC INENTORY")
	Label(fab,text="FABRIC INVENTORY",font="Times 18").grid(row=0,column=12)
	season=Label(fab,text="Season",font="Times 14").grid(row=2,column=0)
	e3=Entry(fab).grid(row=2,column=1)
	supplier=Label(fab,text="Supplier",font="Times 14").grid(row=2,column=7)
	e4=Entry(fab).grid(row=2,column=8)
	buyer=Label(fab,text="Buyer",font="Times 14").grid(row=2,column=14)
	e5=Entry(fab).grid(row=2,column=15)
	style_no=Label(fab,text="Style NO",font="Times 14").grid(row=2,column=21)
	e6=Entry(fab).grid(row=2,column=22)
	po_number=Label(fab,text="PO Number #",font="Times 14").grid(row=3,column=0)
	e7=Entry(fab).grid(row=3,column=1)
	fabric=Label(fab,text="Fabric",font="Times 14").grid(row=3,column=7)
	e8=Entry(fab).grid(row=3,column=8)
	color=Label(fab,text="Color",font="Times 14").grid(row=3,column=14)
	e9=Entry(fab).grid(row=3,column=15)
	color_code=Label(fab,text="Color Code",font="Times 14").grid(row=3,column=21)
	e10=Entry(fab).grid(row=3,column=22)
	cons=Label(fab,text="Fabric Construction",font="Times 14").grid(row=4,column=0)
	e11=Entry(fab).grid(row=4,column=1)
	width=Label(fab,text="Fabric Width",font="Times 14").grid(row=4,column=7)
	e12=Entry(fab).grid(row=4,column=8)
	order_qty=Label(fab,text="Order Quantity",font="Times 14").grid(row=4,column=14)
	e13=Entry(fab).grid(row=4,column=15)
	rec_date=Label(fab,text= "Receiving Date",font="Times 14").grid(row=4,column=21)
	e14=Entry(fab).grid(row=4,column=22)
	order_date=Label(fab,text="Order Date",font="Times 14").grid(row=5,column=0)                                                                    
	e15=Entry(fab).grid(row=5,column=1)
	invoice=Label(fab,text="Invoice NO. ##",font="Times 14").grid(row=5,column=7)
	e16=Entry(fab).grid(row=5,column=8)
	source=Label(fab,text="Shipment Source",font="Times 14").grid(row=5,column=14)
	e17=Entry(fab).grid(row=5,column=15)
	rack=Label(fab,text="Rack NO. #",font="Times 14").grid(row=5,column=21)
	e18=Entry(fab).grid(row=5,column=22)
	row=Label(fab,text="Row NO. #",font="Times 14").grid(row=6,column=14)
	e19=Entry(fab).grid(row=6,column=15)
	remark=Label(fab,text="Remark",font="Times 14").grid(row=6,column=21)
	e20=Entry(fab).grid(row=6,column=22)
	


##create function for trims
def trim():
	tr=Toplevel()
	tr.geometry("950x940")
	tr.title("TRIM INVENTORY")
	Label(tr,text="TRIM INVENTORY",font="Times 18").grid(row=0,column=12)
	po_trim=Label(tr,text="PO Number #:",font="Times 14").grid(row=2,column=0)
	e21=Entry(tr).grid(row=2,column=1)
	pr_trim=Label(tr,text="Product Name:",font="Times 14").grid(row=2,column=7)
	e22=Entry(tr).grid(row=2,column=8)
	ord_trim=Label(tr,text="Order Date:",font="Times 14").grid(row=2,column=14)
	e23=Entry(tr).grid(row=2,column=15)
	rcd_trim=Label(tr,text="Receive Date:",font="Times 14").grid(row=2,column=21)
	e24=Entry(tr).grid(row=2,column=22)
	orq_trim=Label(tr,text="Order Quantity:",font="Times 14").grid(row=3,column=0)
	e25=Entry(tr).grid(row=3,column=1)
	req_trim=Label(tr,text="Receive Quantity:",font="Times 14").grid(row=3,column=7)
	e26=Entry(tr).grid(row=3,column=8)
	styno_trim=Label(tr,text="Style NO:",font="Times 14").grid(row=3,column=14)
	e27=Entry(tr).grid(row=3,column=15)
	supp_trim=Label(tr,text="Supplier Name:",font="Times 14").grid(row=3,column=21)
	e28=Entry(tr).grid(row=3,column=22)
	buy_trim=Label(tr,text="Buyer Name:",font="Times 14").grid(row=4,column=0)
	e29=Entry(tr).grid(row=4,column=1)
	src_trim=Label(tr,text="Source Category:",font="Times 14").grid(row=4,column=7)
	e30=Entry(tr).grid(row=4,column=8)
	rmk_trim=Label(tr,text="Remark:",font="Times 14").grid(row=4,column=14)
	e31=Entry(tr).grid(row=4,column=15)
## create function for packaging material inventory
def pkgm():
	p=Toplevel()
	p.geometry("950x940")
	p.title("PACKAGING MATERIAL INVENTORY")
	Label(p,text="PACKAGING MATERIAL INVENTORY",font="Times 18").grid(row=0,column=12)
	po_pkg=Label(p,text="PO Number #:",font="Times 14").grid(row=2,column=0)
	e32=Entry(p).grid(row=2,column=1)
	pr_pkg=Label(p,text="Product Name:",font="Times 14").grid(row=2,column=7)
	e33=Entry(p).grid(row=2,column=8)
	ord_pkg=Label(p,text="Order Date:",font="Times 14").grid(row=2,column=14)
	e34=Entry(p).grid(row=2,column=15)
	rcd_pkg=Label(p,text="Receive Date:",font="Times 14").grid(row=2,column=21)
	e35=Entry(p).grid(row=2,column=22)
	orq_pkg=Label(p,text="Order Quantity:",font="Times 14").grid(row=3,column=0)
	e36=Entry(p).grid(row=3,column=1)
	req_pkg=Label(p,text="Receive Quantity:",font="Times 14").grid(row=3,column=7)
	e37=Entry(p).grid(row=3,column=8)
	styno_pkg=Label(p,text="Style NO:",font="Times 14").grid(row=3,column=14)
	e38=Entry(p).grid(row=3,column=15)
	supp_pkg=Label(p,text="Supplier Name:",font="Times 14").grid(row=3,column=21)
	e39=Entry(p).grid(row=3,column=22)
	buy_pkg=Label(p,text="Buyer Name:",font="Times 14").grid(row=4,column=0)
	e40=Entry(p).grid(row=4,column=1)
	src_pkg=Label(p,text="Source Category:",font="Times 14").grid(row=4,column=7)
	e41=Entry(p).grid(row=4,column=8)
	rmk_pkg=Label(p,text="Remark:",font="Times 14").grid(row=4,column=14)
	e42=Entry(p).grid(row=4,column=15)
# create function for accessories
def accs():
	a=Toplevel()
	a.geometry("950x940")
	a.title("ACCESSORIES INVENTORY")
	Label(a,text="ACCESSORIES INVENTORY",font="Times 18").grid(row=0,column=12)
	po_acc=Label(a,text="PO Number #:",font="Times 14").grid(row=2,column=0)
	e43=Entry(a).grid(row=2,column=1)
	pr_acc=Label(a,text="Product Name:",font="Times 14").grid(row=2,column=7)
	e44=Entry(a).grid(row=2,column=8)
	ord_acc=Label(a,text="Order Date:",font="Times 14").grid(row=2,column=14)
	e45=Entry(a).grid(row=2,column=15)
	rcd_acc=Label(a,text="Receive Date:",font="Times 14").grid(row=2,column=21)
	e46=Entry(a).grid(row=2,column=22)
	orq_acc=Label(a,text="Order Quantity:",font="Times 14").grid(row=3,column=0)
	e47=Entry(a).grid(row=3,column=1)
	req_acc=Label(a,text="Receive Quantity:",font="Times 14").grid(row=3,column=7)
	e48=Entry(a).grid(row=3,column=8)
	styno_acc=Label(a,text="Style NO:",font="Times 14").grid(row=3,column=14)
	e49=Entry(a).grid(row=3,column=15)
	supp_acc=Label(a,text="Supplier Name:",font="Times 14").grid(row=3,column=21)
	e50=Entry(a).grid(row=3,column=22)
	buy_acc=Label(a,text="Buyer Name:",font="Times 14").grid(row=4,column=0)
	e51=Entry(a).grid(row=4,column=1)
	src_acc=Label(a,text="Source Category:",font="Times 14").grid(row=4,column=7)
	e52=Entry(a).grid(row=4,column=8)
	rmk_acc=Label(a,text="Remark:",font="Times 14").grid(row=4,column=14)
	e53=Entry(a).grid(row=4,column=15)









username=Label(root,text="ADMIN USERNAME:",font="Times 16").grid(row=7,column=15)
e1=Entry(root, textvar=Username).grid(row=7,column=16)
password=Label(root,text="ADMIN PASSWORD:",font="Times 16").grid(row=8,column=15)
e2=Entry(root,textvar=Password).grid(row=8,column=16)

#validatelogin=partial(validatelogin,Username,Password)
login_btn=Button(root,text="LOGIN",command=admin,font="Times 16").grid(row=9,column=16)
exit_btn=Button(root,text="EXIT",command=Exit,font="Times 16").grid(row=10,column=16)

#SHOW TABLE myadmin;



root.mainloop()
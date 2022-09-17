import tkinter
from login import Login_Window
from tkinter import * 
from PIL import Image,ImageTk 
import tkinter as tk
import time
import sqlite3 
import os
from tkinter import messagebox
from employee import EmployeeClass 
from supplier import SupplierClass
from category import CategoryClass 
#from billing1 import BillClass
from product import Product
from sales import SalesClass
from purchase import PurchaseClass

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Pharmacy Management System")
        self.root.config(bg="white") 

        #=====title======#
        self.icon_title=PhotoImage(file="images/cart1.png") 
        title=Label(self.root,text="Pharmacy Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)   

        #=====logout-Button=====#
       
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1740,y=10,height=50,width=150)  

       
        #=====clock======#
        self.lbl_clock=Label(self.root,text="Welcome to Pharmacy Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)   

        #=======Menu======#
        self.MenuLogo=Image.open("images/menu.png")
        self.MenuLogo=self.MenuLogo.resize((280,200),Image.ANTIALIAS) 
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white") 
        LeftMenu.place(x=0,y=102,width=280,height=630)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)  

        self.icon_side=ImageTk.PhotoImage(file="images/arrow.png") 

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)

        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)  
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)  
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)  
        btn_purchase=Button(LeftMenu,text="Purchase",command=self.purchase,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)  
        btn_product=Button(LeftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)  
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)  
        btn_exit=Button(LeftMenu,text="Exit",command=self.exit,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)  

        #======Content=====#
        self.lbl_employee=Label(self.root,text="Total Employee\n [ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold")) 
        self.lbl_employee.place(x=300,y=120,height=150,width=300) 

        self.lbl_supplier=Label(self.root,text="Total Supplier\n [ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold")) 
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)  

        self.lbl_category=Label(self.root,text="Total Category\n [ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold")) 
        self.lbl_category.place(x=1000,y=120,height=150,width=300) 

        self.lbl_product=Label(self.root,text="Total Products\n [ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold")) 
        self.lbl_product.place(x=300,y=300,height=150,width=300) 

        self.lbl_sales=Label(self.root,text="Total Sales\n [ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold")) 
        self.lbl_sales.place(x=650,y=300,height=150,width=300)  
 
 
        #=====footer=====#
        lbl_footer=Label(self.root,text="PMS - Pharmacy Management System | @ TekSun Inc. | 2021", font=("times new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)  
        self.update_date_time()
        self.update_content()

#=============================================================================================================================================================================================#

    def employee(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=EmployeeClass(self.new_win) 



    def supplier(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=SupplierClass(self.new_win) 

    def purchase(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=PurchaseClass(self.new_win) 

    def category(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=CategoryClass(self.new_win) 

    def product(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=Product(self.new_win) 


    # def billing1(self):
    #     self.new_win=Toplevel(self.root) 
    #     self.new_obj=BillClass(self.new_win) 
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SalesClass(self.new_win)
    def exit(self):
        out=tkinter.messagebox.askyesno("login system","do you want to exit the system")
        if out>0:
            self.root.destroy() 
        return    

       
    

   # def login_window(self):
       # self.root.destroy()
       # import login

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Pharmacy Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)

    def update_content(self):
        con=sqlite3.connect(database=r'pharmacy.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n [ {str(len(employee))} ]")

            cur.execute("select * from product")
            product1=cur.fetchall()
            self.lbl_product.config(text=f"Total Products\n [ {str(len(product1))} ]")

            cur.execute("select * from supplier")
            supplier1=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Supplier\n [ {str(len(supplier1))} ]")


            cur.execute("select * from category")
            category1=cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n [ {str(len(category1))} ]") 

            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f"Total Sales\n [{str(bill)}]")


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")





    






if __name__=="__main__":
    root=Tk() 
    obj = IMS(root)
    root.mainloop()

from tkinter import* 
from tkinter import ttk
import sqlite3 
from tkinter import messagebox

class SupplierClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Supplier")
        self.root.geometry("1600x1090+290+140")
        self.root.config(bg="white")
        self.root.focus_force()


        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_email=StringVar()

          #======SearchFrame=======#
        # SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        # #SearchFrame.place(x=250,y=20,width=600,height=70) 

        #======Options======#
        # cmb_search=ttk.Combobox(self.root,textvariable=self.var_searchby,values=("Select","ID","Name","Email"),state='readonly',justify=CENTER,font=("goudy old style",15))  
        # cmb_search.place(x=10,y=10,width=180) 
        # cmb_search.current(0) 

        lbl_search=Label(self.root,text="Invoice No.",bg="white",font=("goudy old style",15))
        lbl_search.place(x=680,y=80)

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=780,y=80) 
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=1010,y=80,width=100,height=30)
        btn_showall=Button(self.root,text="Show All",command=self.fetch_data,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=1130,y=80,width=100,height=30)


        #======title========@
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        #=====Content======#

        #==========Row-1================#
        lbl_supplier_invioce=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=80)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=80,width=180)
        

        #================Row-2=====================#
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=120,width=180)


        #lbl_supplier_invioce=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=60)
        #txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=100,width=180)
    

        #================Row-3=====================#
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=160,width=180)

        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=180,y=200,width=180)
        

        #================Row-4=====================#
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=240)
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=240,width=470,height=90)
        
        
        #===============Buttons================#
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=350,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=350,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=350,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=350,width=110,height=35)

        #===============Employee Details-List================#
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=140,width=600,height=600) 

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL) 

        self.suppliertable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","email","desce"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set) 
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=X)
        scrollx.config(command=self.suppliertable.xview)
        scrolly.config(command=self.suppliertable.yview)
        self.suppliertable.heading("invoice",text="Invoice ID")
        self.suppliertable.heading("name",text="Name")
        self.suppliertable.heading("contact",text="Contact")
        self.suppliertable.heading("email",text="Email")
        self.suppliertable.heading("desce",text="Description")
        
        self.suppliertable["show"]="headings"

        self.suppliertable.column("invoice",width=90)
        self.suppliertable.column("name",width=100)
        self.suppliertable.column("contact",width=100)
        self.suppliertable.column("email",width=100)
        self.suppliertable.column("desce",width=100)
        self.suppliertable.bind("<ButtonRelease-1>",self.get_data)
        self.suppliertable.pack(fill=BOTH,expand=1) 

        self.fetch_data()

    # function
    def add(self):
        # if self.var_sup_invoice.get() == "":
        #     messagebox.showerror(
        #         "Error", "All Data fields are required!!!")
        #else:
        con=sqlite3.connect(database=r'pharmacy.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="" or self.var_name.get()=="":
                messagebox.showerror("Error","All Data fields are required!!!",parent=self.root)
            else:
                cur.execute("insert into supplier (invoice,name,contact,email,dese) values(?,?,?,?,?)",(self.var_sup_invoice.get(),
                                                                    self.var_name.get(),
                                                                    self.var_contact.get(),
                                                                    self.var_email.get(),
                                                                    self.txt_desc.get('1.0',END),
                                                                    ))
            con.commit()
            self.fetch_data()
            messagebox.showinfo("success", "Record has been inserted")
            self.clear()
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def fetch_data(self): 
        con=sqlite3.connect(database=r'pharmacy.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.suppliertable.delete(*self.suppliertable.get_children())   
            for row in rows:
                self.suppliertable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        #     con.commit()
        # con.close() 

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.fetch_data()

         

    def get_data(self,ev):
        cursors_row=self.suppliertable.focus()
        content=self.suppliertable.item(cursors_row)
        row=content['values']
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.var_email.set(row[3])

        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[4])

    def update(self):
        con=sqlite3.connect(database=r'pharmacy.db')
        cur=con.cursor()
        if self.var_sup_invoice.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:
            cur.execute("update supplier set name=?,contact=?,email=?, dese=? where invoice=?",(self.var_name.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.txt_desc.get('1.0',END), 
                                                                                        self.var_sup_invoice.get(),
                                                                                    ))
            
        con.commit()
        self.fetch_data()
        messagebox.showinfo("success","Record has been updated")

        self.clear()
        con.close()  
        # messagebox.showinfo("success","Record has been updated")


    def delete(self): 
        con=sqlite3.connect(database=r'pharmacy.db')
        cur=con.cursor()
        sql="delete from supplier where invoice=?"
        val=(self.var_sup_invoice.get(),)
        cur.execute(sql,val)
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()



    def search(self):
        con=sqlite3.connect(database=r'pharmacy.db')
        cur=con.cursor()
        #cur.execute("select * from supplier where invoice=%s", (self.var_searchtxt.get(),))
        #cur.execute("select * from medicine where "+str(self.search_by.get())+"LIKE"+str(self.search_txt.get())+"%")
        
        slq_query = "select * from supplier where invoice=?"
        val=(self.var_searchtxt.get(),)
        cur.execute(slq_query,val)
        row = cur.fetchone()

        if row!=0:
            self.suppliertable.delete(*self.suppliertable.get_children())   
            self.suppliertable.insert('',END,values=row)
            con.commit()

        else:
            messagebox.showerror("Error","No record found!!",parent=self.root)
            

        con.close() 

if __name__=="__main__":
    root=Tk()    
    ob=SupplierClass(root)    
    root.mainloop()
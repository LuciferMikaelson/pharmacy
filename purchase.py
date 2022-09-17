from tkinter import * 
from PIL import Image,ImageTk 
from tkinter import ttk
import sqlite3 
from supplier import SupplierClass 
from tkinter import messagebox 

class PurchaseClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x590+290+140") 
        self.root.title("Pharmacy Management System")
        self.root.config(bg="white") 
        self.root.focus_force() 

         #======All variables============#
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar() 

        # self.var_pid=StringVar()
        # self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.id_list=[] 
        self.typ_list=[]
        self.sup_list=[]
        self.sta_list=[]
        self.fetch_sup_typ_sta()
        self.var_id=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_date=StringVar()
        self.var_type=StringVar()
        self.var_status=StringVar()
        

        purchase_frame= Frame(self.root,bd=2,relief=RIDGE,bg="White")
        purchase_frame.place(x=10,y=10,width=450,height=550)

        #======title========@
        title=Label(purchase_frame,text="Manage Purchase Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        lbl_id=Label(purchase_frame,text="SupplierID",font=("goudy old style",18),bg="white").place(x=30,y=40)
        lbl_supplier=Label(purchase_frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=90)
        lbl_product_name=Label(purchase_frame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=140)
        lbl_quntity=Label(purchase_frame,text="Quantity",font=("goudy old style",18),bg="white").place(x=30,y=190)
        lbl_date=Label(purchase_frame,text="Date",font=("goudy old style",18),bg="white").place(x=30,y=240)
        lbl_type=Label(purchase_frame,text="Type",font=("goudy old style",18),bg="white").place(x=30,y=290)
        lbl_price=Label(purchase_frame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=340)
        lbl_status=Label(purchase_frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=390)
        # lbl_reorder=Label(purchase_frame,text="Reorder",font=("goudy old style",18),bg="white").place(x=30,y=360)



        #======Options======#
        cmb_id=ttk.Combobox(purchase_frame,textvariable=self.var_id,values=self.id_list,state='readonly',justify=CENTER,font=("goudy old style",15))  
        cmb_id.place(x=150,y=40,width=200) 
        cmb_id.current(0) 


        cmb_supp=ttk.Combobox(purchase_frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))  
        cmb_supp.place(x=150,y=90,width=200) 
        cmb_supp.current(0) 

        # cmb_sup=ttk.Combobox(purchase_frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))  
        # cmb_sup.place(x=150,y=110,width=200) 
        # cmb_sup.current(0) 

        txt_pname=Entry(purchase_frame,textvariable=self.var_pname,font=("goudy old style",15),bg='lightyellow').place(x=150,y=140,width=200)
        txt_qty=Entry(purchase_frame,textvariable=self.var_quantity,font=("goudy old style",15),bg='lightyellow').place(x=150,y=190,width=200)
        txt_date=Entry(purchase_frame,textvariable=self.var_date,font=("goudy old style",15),bg='lightyellow').place(x=150,y=240,width=200)  
        # txt_reorder=Entry(purchase_frame,textvariable=self.var_reorder,font=("goudy old style",15),bg='lightyellow').place(x=150,y=360,width=200)  
        
        cmb_type=ttk.Combobox(purchase_frame,textvariable=self.var_type,values=("Select","Sample","Purchase"),state='readonly',justify=CENTER,font=("goudy old style",15))  
        cmb_type.place(x=150,y=290,width=200) 
        cmb_type.current(0)
        
        txt_price=Entry(purchase_frame,textvariable=self.var_price,font=("goudy old style",15),bg='lightyellow').place(x=150,y=340,width=200)

        cmb_status=ttk.Combobox(purchase_frame,textvariable=self.var_status,values=("Select","Purchase","Return"),state='readonly',justify=CENTER,font=("goudy old style",15))  
        cmb_status.place(x=150,y=390,width=200) 
        cmb_status.current(0)
        

         #===============Buttons================# 
        btn_add=Button(purchase_frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=430,width=100,height=40)
        btn_update=Button(purchase_frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=430,width=100,height=40)
        btn_delete=Button(purchase_frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=430,width=100,height=40)
        btn_clear=Button(purchase_frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=430,width=100,height=40)
        btn_return=Button(purchase_frame,text="Return",command=self.returni,font=("goudy old style",15),bg="#0f4d7d",fg="white",cursor="hand2").place(x=175,y=490,width=100,height=40)


        #======SearchFrame=======#
        SearchFrame=LabelFrame(self.root,text="Search Purchase",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=700,height=80) 

        #======Options======#
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Supplier ID","ProductName","SupplierName"),state='readonly',justify=CENTER,font=("goudy old style",15))  
        cmb_search.place(x=10,y=10,width=180) 
        cmb_search.current(0) 

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10) 
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=430,y=9,width=100,height=30)
        btn_show=Button(SearchFrame,text="Show All",command=self.fetch_data,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=550,y=9,width=100,height=30)
        # btn_reorder=Button(SearchFrame,text="Reorder",command=self.fetch_data,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=670,y=9,width=100,height=30)

        #Details
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=700,height=390) 

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL) 

        self.PurchaseTable=ttk.Treeview(p_frame,columns=("invoice","Supplier","pname","quantity","date","type","price","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set) 
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=X)
        scrollx.config(command=self.PurchaseTable.xview)
        scrolly.config(command=self.PurchaseTable.yview)
        self.PurchaseTable.heading("invoice",text="Supplier ID")
        self.PurchaseTable.heading("Supplier",text="SupplierName")
        self.PurchaseTable.heading("pname",text="ProductName")
        self.PurchaseTable.heading("quantity",text="Quantity")
        self.PurchaseTable.heading("date",text="Date")
        self.PurchaseTable.heading("type",text="Type") 
        self.PurchaseTable.heading("price",text="Price")
        self.PurchaseTable.heading("status",text="Status")
         

        self.PurchaseTable["show"]="headings"

        self.PurchaseTable.column("invoice",width=90)
        self.PurchaseTable.column("Supplier",width=100) 
        self.PurchaseTable.column("pname",width=100)
        self.PurchaseTable.column("quantity",width=100)
        self.PurchaseTable.column("date",width=100)
        self.PurchaseTable.column("type",width=100) 
        self.PurchaseTable.column("price",width=100)
        self.PurchaseTable.column("status",width=100)
        
        self.PurchaseTable.bind("<ButtonRelease-1>",self.get_data)
        self.PurchaseTable.pack(fill=BOTH,expand=1) 
        
        self.fetch_data()
        # self.fetch_sup_typ_sta()
     # function
    
    def fetch_sup_typ_sta(self):
        self.id_list.append("Empty")
        self.sup_list.append("Empty")
        self.typ_list.append("Empty")
        self.sta_list.append("Empty")
        con=sqlite3.connect(database=r'pharmacy.db')
        cur = con.cursor()

        cur.execute("select invoice from supplier")
        sup=cur.fetchall()
        if len(sup)>0:
            del self.id_list[:]
            self.id_list.append("Select")
            for  i in sup:
                self.id_list.append(i[0])


        cur.execute("select name from supplier")
        cat=cur.fetchall()
        
        if len(cat)>0:
            del self.sup_list[:]
            self.sup_list.append("Select")
            for  i in cat:
                self.sup_list.append(i[0])
        #print(cat_list)
        
        
    def add(self):
        con=sqlite3.connect(database=r'pharmacy.db')
        cur = con.cursor()
        try:
            if self.var_id.get() ==""  :
                messagebox.showerror("Error", "All Data fields are required!!!",parent=self.root)
            else:
                cur.execute("insert into purchase (invoice,Supplier,pname,quantity,date,type,price,status) values(?,?,?,?,?,?,?,?)",(self.var_id.get(),
                                                                   
                                                                    self.var_sup.get(),
                                                                    self.var_pname.get(),
                                                                    
                                                                    self.var_quantity.get(),
                                                                    self.var_date.get(),
                                                                    self.var_type.get(),
                                                                    self.var_price.get(),
                                                                    self.var_status.get(),

                                                                    ))
            con.commit()
            self.fetch_data()
            messagebox.showinfo("success", "Record has been inserted",parent=self.root)

            self.clear()
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            # messagebox.showinfo("success", "Record has been inserted")

    def fetch_data(self): 
        con=sqlite3.connect(database=r'pharmacy.db')
        cur=con.cursor()
        try:
            cur.execute("select * from purchase")
            rows=cur.fetchall()
            #print(rows)
            self.PurchaseTable.delete(*self.PurchaseTable.get_children())   
            for row in rows:
                self.PurchaseTable.insert('',END,values=row)
        #     con.commit()
        # con.close() 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_id.set("Select") 
        self.var_sup.set("Select")
        self.var_pname.set("")
        self.var_quantity.set("")
        self.var_date.set("")
        self.var_type.set("Select")
        self.var_price.set("")
        self.var_status.set("Select") 
        self.var_searchtxt.set("")
        self.var_searchby.set("Select") 
        self.fetch_data()
        self.fetch_sup_typ_sta()

         

    def get_data(self,ev):
        cursors_row=self.PurchaseTable.focus()
        content=self.PurchaseTable.item(cursors_row)
        row=content['values']
        self.var_id.set(row[0])
        self.var_sup.set(row[1])
        self.var_pname.set(row[2])
        self.var_quantity.set(row[3])
        self.var_date.set(row[4])
        self.var_type.set(row[5])
        self.var_price.set(row[6])
        self.var_status.set(row[7])
        # self.var_reorder.set(row[7])
        

    def update(self):
        if self.var_id.get()== ""  :
            messagebox.showerror("Error","All fields are required!!!",parent=self.root)
        else:
            con=sqlite3.connect(database=r'pharmacy.db')
            cur=con.cursor()
            cur.execute("update purchase set Supplier=?, pname=?, quantity=?, date=?, type=?, price=?, status=? where invoice=?",(
                                                                                        self.var_sup.get(), 
                                                                                        self.var_pname.get(),
                                                                    
                                                                                        self.var_quantity.get(),
                                                                                        self.var_date.get(),
                                                                                        self.var_type.get(),
                                                                                        self.var_price.get(),
                                                                                        self.var_status.get(),
                                                                                        self.var_id.get(),

                                                                                    ))
        con.commit()
        self.fetch_data()
        messagebox.showinfo("success","Record has been updated",parent=self.root)

        self.clear()
        con.close()  
        # messagebox.showinfo("success","Record has been updated")


    def delete(self): 
        con=sqlite3.connect(database=r'pharmacy.db')
        cur=con.cursor()
        # sql="delete from prodcut where pid=%s"
        # val=(self.var_pid.get(),)
        # cur.execute(sql,val)
        cur.execute("delete from purchase where Supplier=?",(self.var_sup.get(),))
        con.commit()
        self.fetch_data()
        messagebox.showinfo("success","Record has been Deleted",parent=self.root)    

        self.clear()
        con.close()

    def returni(self):
        if self.var_id.get()== ""  :
            messagebox.showerror("Error","All fields are required!!!",parent=self.root)
        else:
            con=sqlite3.connect(database=r'pharmacy.db')
            cur=con.cursor()
            cur.execute("update purchase set Supplier=?, pname=?, quantity=?, date=?, type=?, price=?, status=? where invoice=?",(
                                                                                        self.var_sup.get(), 
                                                                                        self.var_pname.get(),
                                                                    
                                                                                        self.var_quantity.get(),
                                                                                        self.var_date.get(),
                                                                                        self.var_type.get(),
                                                                                        self.var_price.get(),
                                                                                        self.var_status.get(),
                                                                                        self.var_id.get(),

                                                                                    ))
        con.commit()
        self.fetch_data()
        messagebox.showinfo("success","Item has been Returned",parent=self.root)

        self.clear()
        con.close()  
        # messagebox.showinfo("success","Record has been updated")
        



    # def search(self):
    #     con=mysql.connector.connect(host="localhost",user="root",password="System#system75",database="med")
    #     cur=con.cursor()
    #     #cur.execute("select * from supplier where invoice=%s", (self.var_searchtxt.get(),))
    #     #cur.execute("select * from medicine where "+str(self.search_by.get())+"LIKE"+str(self.search_txt.get())+"%")
        
    #     slq_query = "select * from product where pid=%s"
    #     val=(self.var_searchtxt.get(),)
    #     cur.execute(slq_query,val)
    #     row = cur.fetchone()

    #     if row!=0:
    #         self.PurchaseTable.delete(*self.PurchaseTable.get_children())   
    #         self.PurchaseTable.insert('',END,values=row)
    #         con.commit()

    #     else:
    #         messagebox.showerror("Error","No record found!!",parent=self.root)
            

    #     con.close() 


    def search(self):
        con=sqlite3.connect(database=r'pharmacy.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by option",parent=self.root) 
            elif self.var_searchtxt.get()=="":  
                messagebox.showerror("Error","Search input should be Required",parent=self.root) 
            else:      
                cur.execute("select * from purchase where " +self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.PurchaseTable.delete(*self.PurchaseTable.get_children())   
                    for row in rows:
                        self.PurchaseTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
       

if __name__=="__main__":
    root=Tk() 
    obj = PurchaseClass(root) 
    root.mainloop()         

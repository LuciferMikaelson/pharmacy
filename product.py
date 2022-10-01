from tkinter import* 
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class Product:
    def __init__(self,root):
        self.root=root
        self.root.title("Product")
        self.root.geometry("1600x1090+290+140")
        self.root.config(bg="white")
        self.root.focus_force()

         #======All variables============#
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar() 

        self.var_pid=StringVar()
        # self.var_cat=StringVar()
        self.var_sup=StringVar()
        # self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_stock=StringVar()
        self.var_qty=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()
        

        product_Frame= Frame(self.root,bd=2,relief=RIDGE,bg="White")
        product_Frame.place(x=10,y=10,width=450,height=600)

        #======title========@
        title=Label(product_Frame,text="Manage Product Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        # lbl_category=Label(product_Frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_product_name=Label(product_Frame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_price=Label(product_Frame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_stock=Label(product_Frame,text="OP_Stock",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_qty=Label(product_Frame,text="C_Stock",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_date=Label(product_Frame,text="Date",font=("goudy old style",18),bg="white").place(x=30,y=310)

        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=360)
        # lbl_reorder=Label(product_Frame,text="Reorder",font=("goudy old style",18),bg="white").place(x=30,y=360)



        #======Options======#
        # cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))  
        # cmb_cat.place(x=150,y=60,width=200) 
        # cmb_cat.current(0) 

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))  
        cmb_sup.place(x=150,y=60,width=200) 
        cmb_sup.current(0) 

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg='lightyellow').place(x=150,y=110,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg='lightyellow').place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg='lightyellow').place(x=150,y=210,width=200)
        txt_stock=Entry(product_Frame,textvariable=self.var_stock,font=("goudy old style",15),bg='lightyellow').place(x=150,y=260,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg='lightyellow').place(x=150,y=310,width=200)  
        # txt_reorder=Entry(product_Frame,textvariable=self.var_reorder,font=("goudy old style",15),bg='lightyellow').place(x=150,y=360,width=200)  
        
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))  
        cmb_status.place(x=150,y=360,width=200) 
        cmb_status.current(0)
        

         #===============Buttons================#
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=500,width=100,height=40)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=500,width=100,height=40)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=500,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=500,width=100,height=40)

        #======SearchFrame=======#
        SearchFrame=LabelFrame(self.root,text="Search Product",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=700,height=80) 

        #======Options======#
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("pid","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))  
        cmb_search.place(x=10,y=10,width=180) 
        cmb_search.current(0) 

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10) 
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=430,y=9,width=100,height=30)
        btn_show=Button(SearchFrame,text="Show All",command=self.fetch_data,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=550,y=9,width=100,height=30)
        # btn_reorder=Button(SearchFrame,text="Reorder",command=self.fetch_data,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=670,y=9,width=100,height=30)

        #Details
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=700,height=500) 

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL) 

        self.ProductTable=ttk.Treeview(p_frame,columns=("pid","Supplier","name","price","stock","qty","date","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set) 
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=X)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("pid",text="P_ID")
        # self.ProductTable.heading("Category",text="Category")
        self.ProductTable.heading("Supplier",text="Supplier")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("stock",text="Tstock") 
        self.ProductTable.heading("qty",text="Qty")
        self.ProductTable.heading("date",text="Date")
        self.ProductTable.heading("status",text="Status")
         

        self.ProductTable["show"]="headings"

        self.ProductTable.column("pid",width=90)
        # self.ProductTable.column("Category",width=100)
        self.ProductTable.column("Supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("stock",width=100) 
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("date",width=100)
        self.ProductTable.column("status",width=100)
        
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.ProductTable.pack(fill=BOTH,expand=1) 
        
        #self.fetch_data()
        
     # function
    
    def sub(a,b):
        s = a-b
        retunr s
        
    def mul(a,b):
        s = a//b
        return s
    
    def add(a, b):
        sum = a+b
        return sum
    
    def fetch_cat_sup(self):
        #self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'pharmacy.db')
        cur = con.cursor()
        # cur.execute("select c_name from category")
        # cat=cur.fetchall()
        
        # if len(cat)>0:
        #     del self.cat_list[:]
        #     self.cat_list.append("Select")
        #     for  i in cat:
        #         self.cat_list.append(i[0])
        #print(cat_list)
        cur.execute("select name from supplier")
        sup=cur.fetchall()
        if len(sup)>0:
            del self.sup_list[:]
            self.sup_list.append("Select")
            for  i in sup:
                self.sup_list.append(i[0])

        
    def add(self):
        con=sqlite3.connect(database=r'pharmacy.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_name.get()=="":
                messagebox.showerror("Error", "All Data fields are required!!!")
            else:
                cur.execute("insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?,?)",(self.var_cat.get(),
                                                                    self.var_sup.get(),
                                                                    self.var_name.get(),
                                                                    self.var_price.get(),
                                                                    self.var_qty.get(),
                                                                    self.var_status.get(),

                                                                    ))
            con.commit()
            self.fetch_data()
            messagebox.showinfo("success", "Record has been inserted")

            self.clear()
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            # messagebox.showinfo("success", "Record has been inserted")

    def fetch_data(self): 
        con=sqlite3.connect(database=r'pharmacy.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            #print(rows)
            self.ProductTable.delete(*self.ProductTable.get_children())   
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        #     con.commit()
        # con.close() 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_pid.set("")
        self.var_cat.set("")
        self.var_sup.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("")
        self.var_searchtxt.set("")
        self.fetch_data()

         

    def get_data(self,ev):
        cursors_row=self.ProductTable.focus()
        content=self.ProductTable.item(cursors_row)
        row=content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
        self.var_reorder.set(row[7])
        

    def update(self):
        if self.var_pid.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:
            con=sqlite3.connect(database=r'pharmacy.db')
            cur=con.cursor()
            cur.execute("update product set Category=?,Supplier=?,name=?, price=?, qty=?,status=? where pid=?",(self.var_cat.get(),
                                                                                        self.var_sup.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_price.get(),
                                                                                        self.var_qty.get(),
                                                                                        self.var_status.get(),
                                                                                        
                                                                                        self.var_pid.get(),
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
        # sql="delete from prodcut where pid=%s"
        # val=(self.var_pid.get(),)
        # cur.execute(sql,val)
        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
        con.commit()
        self.fetch_data()
       # messagebox.showinfo("success","Record has been updated",parent=self.root)    

        self.clear()
        con.close()



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
    #         self.ProductTable.delete(*self.ProductTable.get_children())   
    #         self.ProductTable.insert('',END,values=row)
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
                cur.execute("select * from product where " +self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())   
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)      
                        
              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()    
    ob=Product(root)    
    root.mainloop()

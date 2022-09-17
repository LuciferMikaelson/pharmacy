from tkinter import *
import sqlite3 
from tkinter import messagebox, ttk
from PIL import Image, ImageTk


class CategoryClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Category")
        self.root.geometry("1600x1090+290+140")
        self.root.config(bg="white")
        self.root.focus_force()
        # variable
        self.var_cat_id = StringVar()
        self.var_name = StringVar()
        # title

        lbl_title = Label(self.root, text="Manage Product Category", font=("goudy old style", 30),
                          bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)

        lbl_name = Label(self.root, text="Enter Category Name", font=(
            "goudy old style", 30), bg="white").place(x=50, y=100)
        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "goudy old style", 18), bg="lightyellow").place(x=50, y=170, width=300)

        btn_add = Button(self.root, text="ADD", command=self.add, font=("goudy old style", 15),
                         bg="#4caf50", fg="white", cursor="hand2").place(x=360, y=170, width=150, height=30)
        btn_delete = Button(self.root, text="DELETE", command=self.delete, font=(
            "goudy old style", 15), bg="red", fg="white", cursor="hand2").place(x=520, y=170, width=150, height=30)

        # details

        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=700, y=100, width=380, height=250)

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.categorytable = ttk.Treeview(
            cat_frame, columns=("cid", "c_name"), yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.categorytable.xview)
        scrolly.config(command=self.categorytable.yview)

        self.categorytable.heading("cid", text="C ID")
        self.categorytable.heading("c_name", text="Name")
        self.categorytable["show"] = "headings"
        self.categorytable.column("cid", width=90)
        self.categorytable.column("c_name", width=100)
        self.categorytable.pack(fill=BOTH, expand=1)
        self.categorytable.bind("<ButtonRelease-1>",self.get_data)

        # image
        self.im1 = Image.open("images/im1.jpg")
        self.im1 = self.im1.resize((500, 250), Image.ANTIALIAS)
        self.im1 = ImageTk.PhotoImage(self.im1)

        self.lbl_im1 = Label(self.root, image=self.im1, bd=2, relief=RAISED)
        self.lbl_im1.place(x=50, y=220)

        self.fetch_data()

    # function
    def add(self):
        con=sqlite3.connect(database=r'pharmacy.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "All Data fields are required!!!")
            else:
                cur.execute("insert into category (c_name) values(?)",(self.var_name.get(),))
            
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
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.categorytable.delete(*self.categorytable.get_children())   
            for row in rows:
                self.categorytable.insert('',END,values=row)
        #     con.commit()
        # con.close() 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_cat_id.set("")
        self.var_name.set("")
         

    def get_data(self,ev):
        cursors_row=self.categorytable.focus()
        content=self.categorytable.item(cursors_row)
        row=content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self): 
        con=sqlite3.connect(database=r'pharmacy.db')
        cur=con.cursor()
        sql="delete from category where c_name=?"
        val=(self.var_name.get(),)
        cur.execute(sql,val)
        con.commit()
        self.fetch_data()
        messagebox.showinfo("success","Record has been deleted",parent=self.root)    

        self.clear()
        con.close()



if __name__=="__main__":

    root=Tk()    
    obj=CategoryClass(root)    
    root.mainloop()

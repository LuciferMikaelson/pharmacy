from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
import sqlite3 
from tkinter import messagebox
from employee import EmployeeClass
import os

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("GUI Analog Clock")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="#021e2f")
        
        self.var_uemail=StringVar()
        self.var_upass=StringVar()
    

        ######====background=====
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        ######frames=====
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=600,y=250,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)


        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,textvariable=self.var_uemail,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)


        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame,textvariable=self.var_upass,font=("times new roman",15),bg="lightgray")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)


        btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="Register new Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)

        btn_login=Button(login_frame,text="Login",command=self.logindata,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=250,y=380,width=180,height=40)
    




        ####====clock=====
        self.lbl=Label(self.root,text="\nAnalog Clock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=400,y=270,height=450,width=350)
        self.working()


    def register_window(self):
        self.root.destroy()
        import registration

    
    
                    

    # def login(self):
    #     if self.txt_email.get()=="" or self.txt_pass_.get()=="":
    #         messagebox.showerror("Error","All fields are required",parent=self.root)
    #     else:
    #         try:
    #             con=pymysql.connect(host="localhost",user="root",password="",database="employee6")
    #             cur=con.cursor()
    #             cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
    #             row=cur.fetchone()
    #             if row==None:
    #                 messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
    #             else:
    #                 messagebox.showinfo("Success","Welcome",parent=self.root)
    #                 self.root.destroy()
    #                 os.system("python dashboard.py")

    #                # import dashboard
    #             con.close()           
    #         except Exception as es:
    #              messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
                    


    def clock_image(self,hr,min_,sec_,):
        clock=Image.new("RGB",(400,400),(8,25,35)) 
        draw=ImageDraw.Draw(clock)
        #####for clock image
        bg=Image.open("images/cl2.jpg")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        ###=========for hour line image
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        ###=========for min line image
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
        ###=========for sec line image
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("images/clock_new.png")  

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

        #=============================Login File=============================================#
    def logindata(self):
        con=sqlite3.connect(database=r'pharmacy.db')
        cur=con.cursor()
        try:
            if self.var_uemail.get()=="" or self.var_upass.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root) 
            
            else:      
                cur.execute("select utype from employee where email=? AND pass=?", (self.var_uemail.get(),self.var_upass.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","InValid username or password",parent=self.root)
                    #import os
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")    
                    else:
                        self.root.destroy()
                        os.system("python billing1.py")     
                     

                     #write logout code
                        
              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)                



if __name__=="__main__":

    root=Tk()
    obj=Login_Window(root)
    root.mainloop()
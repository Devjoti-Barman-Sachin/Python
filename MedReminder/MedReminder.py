import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as st
from tkinter import ttk
from PIL import Image,ImageTk
import csv
import pandas as pd
from datetime import datetime
from win10toast import ToastNotifier




def login_page(root):
    #Functions

    def start_reminder():
        df=pd.read_csv("data.csv",sep=',')
        toaster = ToastNotifier()

        while True:
            now = datetime.now()
            current_hour = int(now.strftime("%I"))
            current_min = int(now.strftime("%M"))
            current_period = now.strftime("%p")
            d=str(datetime.now().day)
            m=str(datetime.now().month)
            y=str(datetime.now().year)


            n=len(df)

            for i in range(n):

                ed,em,ey=str(df['Exp Date'][i]).split("/")

                if (current_hour == df['Hours'][i]) and (current_min == df['Minitues'][i]) and (current_period == df['AM/PM'][i]):
                    msz="Please take "+"' "+df['Name'][i]+" '"+" now."
                    toaster.show_toast("MedReminder",msz,icon_path="Graphicloads-Medical-Health-Medicine-box-2.ico",duration=20)

                if (d==ed) and (m==em) and (y==ey):
                    msz = "' "+df['Name'][i]+" ' Medicine got expired."
                    toaster.show_toast("MedReminder",msz,icon_path="Graphicloads-Medical-Health-Medicine-box-2.ico",duration=20)

                if (int(df['Stock'][i]) < 2) :
                    msz = "' "+df['Name'][i]+" ' Medicine stock is low."
                    toaster.show_toast("MedReminder",msz,icon_path="Graphicloads-Medical-Health-Medicine-box-2.ico",duration=20)









    def update_user(name,pas):
        with open('user.csv', 'w', newline='') as file:
            fieldnames = ['Name','Password']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow( {'Name': name,
                            'Password': pas} )





    def add_data():
        with open('data.csv', 'a', newline='') as file:
            fieldnames = ['Name','Hours','Minitues','AM/PM','Exp Date','Stock']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writerow( {'Name': txt_medname.get(),
                            'Hours': txt_hour.get(),
                            'Minitues': txt_min.get(),
                            'AM/PM': txt_ampm.get(),
                            'Exp Date':txt_exp.get(),
                            'Stock': txt_total.get()} )

        show_data(update_txt)
        show_data(text_area)






    def show_data(box):
        dataset = pd.read_csv("data.csv")
        box.delete('1.0',tk.END)
        box.insert(tk.INSERT, dataset.head(100))



    def update_data():
        data = pd.read_csv("data.csv")

        n=int(index.get())
        f=field.get()
        data.loc[n, f] = value.get()

        data.to_csv("data.csv", index=False)

        show_data(update_txt)
        show_data(text_area)

        swap_function(Frame_reminder)




    def back_function(des,frame):
        des.destroy()
        frame.tkraise()




    #Frame swap Functions
    def swap_function(frame):
        frame.tkraise()





    #Login page button function under the login_page function
    def login_function():
        df=pd.read_csv("user.csv",sep=',')


        name=df['Name'][0]
        pas=str(df['Password'][0])

        if txt_pass.get()=="" or txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=page)

        elif txt_user.get()!=name or txt_pass.get()!=pas:
            messagebox.showerror("Error","Invalid Username/Password",parent=page)

        else:
            messagebox.showinfo("Welcome","Welcome to Med Reminder App",parent=page)
            swap_function(Frame_reminder)






    #Signup page button function under the login_page function
    def signup_function():
        if txt_username.get()=="" or txt_email.get()=="" or txt_spass.get()=="" or txt_conpass.get()==""  :
            messagebox.showerror("Error","Please fillup the fields first!",parent=page)
        else:
            messagebox.showinfo("Info","Registration Successfully Completed",parent=page)
            update_user(txt_username.get(),txt_spass.get())
            Frame_signup.destroy()
            swap_function(Frame_login)






    #Forgot password page button function under the login_page function
    def forgotpassdone_function():
        if txt_tpass.get()=="" or txt_tconpass.get()=="":
            messagebox.showerror("Error","Please fillup the fields first!",parent=page)
        else:
            messagebox.showinfo("Info","Password Changed Successfully!",parent=page)
            update_user(txt_tuser.get(),txt_tpass.get())
            Frame_fpass.destroy()
            swap_function(Frame_login)






    page=root
    #Overall structure



    #*****************************************************************update frame strats*********************************************************************
    update=tk.Frame(page,bg="light blue")
    update.place(x=0,y=0,height=700,width=500)

    title=tk.Label(update,text="Update Data",font=("Open Sans",22,"bold"),fg="black",bg="light blue").place(x=160,y=5)


    #Box
    update_txt = st.ScrolledText(update,bg="#03613D",fg="white",width = 59,height = 15)
    update_txt.place(x=3,y=50)
    show_data(update_txt)


    #Input
    index=tk.Label(update,text="Index number:",font=("Open Sans",13,"bold"),fg="black",bg="light blue").place(x=20,y=370)
    index=tk.Entry(update,font=("Open Sans",12))
    index.place(x=230,y=370,width=100,height=25)


    field=tk.Label(update,text="Choose a Filed to Modify:",font=("Open Sans",13,"bold"),fg="black",bg="light blue").place(x=20,y=420)
    field=ttk.Combobox(update)
    field['values']= ('Name','Hours','Minitues','AM/PM','Exp Date','Stock')
    field.place(x=230,y=420,width=100,height=25)


    value=tk.Label(update,text="Enter Data:",font=("Open Sans",13,"bold"),fg="black",bg="light blue").place(x=20,y=470)
    value=tk.Entry(update,font=("Open Sans",12))
    value.place(x=230,y=470,width=100,height=25)

    Update_btn=tk.Button(update,command=update_data,cursor="hand2",text="Update Schedule",fg="white",bg="#005f00",font=("Open sans",14)).place(x=155,y=570,width=180,height=40)
    back=tk.Button(update,command=lambda:swap_function(Frame_reminder),cursor="hand2",text="<<",fg="black",bg="white",font=("Open sans",18)).place(x=5,y=5,width=40,height=30)
    #********************************************************#update frame ends**************************************************************************







    #*****************************************************************Forgot password frame strats*********************************************************************
    Frame_fpass=tk.Frame(page,bg="light blue")
    Frame_fpass.place(x=0,y=0,height=700,width=500)

    #Input Box
    lbl_tuser=tk.Label(Frame_fpass,text="Username:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=51,y=170)
    txt_tuser=tk.Entry(Frame_fpass,font=("Open Sans",12),bg="lightgray")
    txt_tuser.place(x=54,y=200,width=350,height=35)

    lbl_tpass=tk.Label(Frame_fpass,text="Type Password:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=250)
    txt_tpass=tk.Entry(Frame_fpass,show='*',font=("Open Sans",12),bg="lightgray")
    txt_tpass.place(x=54,y=280,width=350,height=35)

    lbl_tconpass=tk.Label(Frame_fpass,text="Confirm Password:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=330)
    txt_tconpass=tk.Entry(Frame_fpass,show='*',font=("Open Sans",12),bg="lightgray")
    txt_tconpass.place(x=54,y=360,width=350,height=35)

    #Login and forgot password button
    Done_btn=tk.Button(Frame_fpass,command=forgotpassdone_function,cursor="hand2",text="Done",fg="white",bg="#e60000",font=("Open sans",18)).place(x=150,y=460,width=180,height=40)
    back=tk.Button(Frame_fpass,command=lambda:back_function(Frame_fpass,Frame_login),cursor="hand2",text="<<",fg="black",bg="white",font=("Open sans",18)).place(x=5,y=5,width=40,height=30)
    #********************************************************#Forgot password frame ends**************************************************************************








    #*****************************************************************reminder frame strats*********************************************************************
    Frame_reminder=tk.Frame(page,bg="light blue")
    Frame_reminder.place(x=0,y=0,height=700,width=500)

    title=tk.Label(Frame_reminder,text="Medicine Schedule",font=("Open Sans",22,"bold"),fg="black",bg="light blue").place(x=110,y=5)


    #Output Box
    text_area = st.ScrolledText(Frame_reminder,bg="#03613D",fg="white",width = 59,height = 15)
    text_area.place(x=3,y=50)

    show_data(text_area)



    #Input Box
    txt_medname=tk.Label(Frame_reminder,text="Medicine Name:",font=("Open Sans",13,"bold"),fg="black",bg="light blue").place(x=15,y=326)
    txt_medname=tk.Entry(Frame_reminder,font=("Open Sans",12))
    txt_medname.place(x=154,y=327,width=282,height=25)

    txt_time=tk.Label(Frame_reminder,text="Time:",font=("Open Sans",13,"bold"),fg="black",bg="light blue").place(x=15,y=400)

    txt_hour=tk.Label(Frame_reminder,text="(H)",font=("Open Sans",13,"bold"),fg="black",bg="light blue").place(x=159,y=370)
    txt_hour=ttk.Combobox(Frame_reminder)
    txt_hour['values']= ('00','01','02','03','04','05','06','07','08','09','10','11','12')
    txt_hour.place(x=154,y=400,width=40,height=25)

    txt_min=tk.Label(Frame_reminder,text="(M)",font=("Open Sans",13,"bold"),fg="black",bg="light blue").place(x=209,y=370)
    txt_min=ttk.Combobox(Frame_reminder)
    txt_min['values']= ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19',
                        '20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39',
                        '40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
    txt_min.place(x=204,y=400,width=40,height=25)

    txt_ampm=tk.Label(Frame_reminder,text="(AM / PM)",font=("Open Sans",13,"bold"),fg="black",bg="light blue").place(x=254,y=370)
    txt_ampm=ttk.Combobox(Frame_reminder)
    txt_ampm['values']=('AM','PM')
    txt_ampm.place(x=254,y=400,width=80,height=25)

    txt_exp=tk.Label(Frame_reminder,text="Exp Date(D/M/Y):",font=("Open Sans",13,"bold"),fg="black",bg="light blue").place(x=15,y=461)
    txt_exp=tk.Entry(Frame_reminder,font=("Open Sans",12))
    txt_exp.place(x=154,y=462,width=90,height=25)

    txt_total=tk.Label(Frame_reminder,text="Total Tablet:",font=("Open Sans",13,"bold"),fg="black",bg="light blue").place(x=254,y=461)
    txt_total=tk.Spinbox(Frame_reminder,from_=1,to=50)
    txt_total.place(x=364,y=462,width=70,height=25)




    #Add button
    Add_btn=tk.Button(Frame_reminder,command=add_data,cursor="hand2",text="Add Schedule",fg="white",bg="#e60000",font=("Open sans",14)).place(x=50,y=570,width=180,height=40)
    #Update button
    Update_btn=tk.Button(Frame_reminder,command=lambda:swap_function(update),cursor="hand2",text="Update Schedule",fg="white",bg="#005f00",font=("Open sans",14)).place(x=270,y=570,width=180,height=40)

    #start button
    Start_btn=tk.Button(Frame_reminder,command=start_reminder,cursor="hand2",text="Start Reminder",fg="white",bg="#0000aa",font=("Open sans",14)).place(x=152,y=630,width=180,height=40)
    back=tk.Button(Frame_reminder,command=lambda:back_function(Frame_reminder,Frame_login),cursor="hand2",text="<<",fg="black",bg="white",font=("Open sans",18)).place(x=5,y=5,width=40,height=30)
    #********************************************************#reminder frame ends**************************************************************************



    #*****************************************************************Signup frame strats*********************************************************************
    Frame_signup=tk.Frame(page,bg="light blue")
    Frame_signup.place(x=0,y=0,height=700,width=500)

    title=tk.Label(Frame_signup,text="Signup Page",font=("Open Sans",22,"bold"),fg="black",bg="light blue").place(x=150,y=5)

    #Input Box

    lbl_username=tk.Label(Frame_signup,text="*User Name:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=170)
    txt_username=tk.Entry(Frame_signup,font=("Open Sans",12),bg="lightgray")
    txt_username.place(x=54,y=200,width=350,height=35)

    lbl_age=tk.Label(Frame_signup,text="Age:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=250)
    txt_age=tk.Entry(Frame_signup,font=("Open Sans",12),bg="lightgray")
    txt_age.place(x=54,y=280,width=350,height=35)

    lbl_email=tk.Label(Frame_signup,text="*Email Address:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=330)
    txt_email=tk.Entry(Frame_signup,font=("Open Sans",12),bg="lightgray")
    txt_email.place(x=54,y=360,width=350,height=35)

    lbl_spass=tk.Label(Frame_signup,text="*Password:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=410)
    txt_spass=tk.Entry(Frame_signup,show='*',font=("Open Sans",12),bg="lightgray")
    txt_spass.place(x=54,y=440,width=350,height=35)

    lbl_conpass=tk.Label(Frame_signup,text="*Confirm Password:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=490)
    txt_conpass=tk.Entry(Frame_signup,show='*',font=("Open Sans",12),bg="lightgray")
    txt_conpass.place(x=54,y=520,width=350,height=35)

    #Signup and forgot password button
    Signup_btn=tk.Button(Frame_signup,command=signup_function,cursor="hand2",text="Signup",fg="white",bg="#e60000",font=("Open sans",18)).place(x=150,y=570,width=180,height=40)
    back=tk.Button(Frame_signup,command=lambda:back_function(Frame_signup,Frame_login),cursor="hand2",text="<<",fg="black",bg="white",font=("Open sans",18)).place(x=5,y=5,width=40,height=30)
    #********************************************************#Signup frame ends**************************************************************************



    #*****************************************************************Login frame strats*********************************************************************

    page.title("Med Reminder App")
    page.geometry("500x700")
    page.resizable(False,False)

    #Page background image
    page.cover=Image.open("img2.jpg").rotate(270)
    page.cover=ImageTk.PhotoImage(page.cover)
    page.bg=tk.Label(page,image=page.cover).place(x=0,y=0,relwidth=1,relheight=1)

    Frame_login=tk.Frame(page,bg="light blue")
    Frame_login.place(x=75,y=390,height=290,width=350)

    title=tk.Label(Frame_login,text="Login Here",font=("Open Sans",22,"bold"),fg="black",bg="light blue").place(x=92,y=5)

    #Input Box
    lbl_user=tk.Label(Frame_login,text="Username",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=20,y=60)
    txt_user=tk.Entry(Frame_login,font=("Open Sans",12),bg="lightgray")
    txt_user.place(x=24,y=90,width=300,height=35)

    lbl_pass=tk.Label(Frame_login,text="Password",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=20,y=140)
    txt_pass=tk.Entry(Frame_login,show='*',font=("Open Sans",14),bg="lightgray")
    txt_pass.place(x=24,y=170,width=300,height=35)

    #Login and forgot password button
    Login_btn=tk.Button(Frame_login,command=login_function,cursor="hand2",text="Login",fg="white",bg="blue",font=("Open sans",18)).place(x=84,y=215,width=180,height=40)
    Signup_btn=tk.Button(Frame_login,command=lambda:swap_function(Frame_signup),cursor="hand2",text="New member? Signup here",fg="black",bg="light blue",font=("Open sans",10),bd=0).place(x=15,y=265,width=180,height=20)
    Forgot_btn=tk.Button(Frame_login,command=lambda:swap_function(Frame_fpass),cursor="hand2",text="Forgot Password?",fg="black",bg="light blue",font=("Open sans",10),bd=0).place(x=215,y=265,width=120,height=20)
    #*****************************************************************#Login frame ends**************************************************************************






root=tk.Tk()
login_page(root)
root.mainloop()

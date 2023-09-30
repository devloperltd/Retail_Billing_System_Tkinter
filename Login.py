from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import webbrowser
import os
import sys

# Slider Lable Title Fictionality Part ===================

Count = 0
text = ''
def slider():
    global text, Count
    if Count == len(s):
        Count = 0
        text = ''
    text = text + s [Count]
    SliderLableTitle.config(text=text)
    Count+=1
    SliderLableTitle.after(300, slider)

# Run Social Media Command

Facebook='https://facebook.com/laroussiGsm'
Telegram='https://t.me/UncleAnonymous'
YouTube='https://www.youtube.com/'
WWebsite='https://laroussigsm.net/'
Author=''

def Link1():
    webbrowser.open_new(Facebook)
def Link2():
    webbrowser.open_new(Telegram)
def Link3():
    webbrowser.open_new(YouTube)
def Link4():
    webbrowser.open_new(WWebsite)
def About():
    messagebox.showinfo('By Laroussi Boulanouar' , 'Retail Billing System Project Free Open Source 2023')

# Run logIn UserName & Password Command

def logIn():
    if UserNameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('Error', 'Fields Cannot Be Empty !!')
    elif UserNameEntry.get()=='laroussi' and PasswordEntry.get()=='123456':
        messagebox.showinfo('Success', 'Welcome To Laroussi Retail Billing System V1.0')
        Laroussi_Login.destroy()
        import Market
    else:
        messagebox.showerror('Error', 'Please Enter Correct Username Or Password !!')                    

# Create GUI Part

Laroussi_Login = Tk()
Laroussi_Login.geometry('890x510+250+80')
Laroussi_Login.resizable(False , False)
Laroussi_Login.title('Retail Billing System V1.0 | Login System - https://laroussigsm.net/')
Laroussi_Login.iconbitmap('sale_shop_icon.ico')

# Create Slider Title style

s = 'LAROUSSI RETAIL BILLING SYSTEM FREE V0.1'
SliderLableTitle = Label(Laroussi_Login, text=s, font=('Arial Rounded MT Bold', 14, 'italic bold'), bg='#fbc531', fg='#192a56')
SliderLableTitle.pack(fill=X, ipady=0)
slider()

# Create Panal Frame style

Panal_frame = Frame(Laroussi_Login, width=250 ,height=550 ,bg='#2c2c54')
Panal_frame.place(x=0 , y=28)

UserNameImage1 = PhotoImage(file='cart.png')
UserNameImage2 = Label(Panal_frame, image=UserNameImage1, compound=CENTER, bg='#2c2c54')
UserNameImage2.place(x=183, y=20)


Heading1 = Label(Panal_frame, text='LAROUSSI', bg='#2c2c54', fg='#f1c40f', font=('Amerika Sans', 22, 'bold'), justify="center")
Heading1.place(x=40 , y=20)
Heading2 = Label(Panal_frame, text='RETAIL BILLING', bg='#2c2c54', fg='#f1f2f6', justify="center", font=('Calibri (Body)', 12))
Heading2.place(x=40 , y=55)
Heading3 = Label(Panal_frame, text='SYSTEM V0.1', bg='#2c2c54', fg='#f1f2f6', font=('Calibri (Body)', 12))
Heading3.place(x=40 , y=75)
Heading4Image = PhotoImage(file='whatsapp.png')
Heading4 = Label(Panal_frame, text=' +213 000000000', bg='#2c2c54', fg='#f1f2f6', font=('Calibri (Body)', 14, 'italic bold'), image=Heading4Image, compound=LEFT)
Heading4.place(x=20 , y=125)

# Create PSocial Media style

Facebook_BTN=Button(Panal_frame, text='Facebook Page', width=22, bg='#ffa502', fg='#1e272e', font=('Calibri (Body)', 12, 'bold'), cursor='hand2', bd=0, command=Link1)
Facebook_BTN.place(x=10, y=180)

Telegram_BTN=Button(Panal_frame, text='Telegram Channel', width=22, bg='#ffa502', fg='#1e272e', font=('Calibri (Body)', 12, 'bold'), cursor='hand2', bd=0, command=Link2)
Telegram_BTN.place(x=10, y=230)

YouTube_BTN=Button(Panal_frame, text='YouTube Channel', width=22, bg='#ffa502', fg='#1e272e', font=('Calibri (Body)', 12, 'bold'), cursor='hand2', bd=0, command=Link3)
YouTube_BTN.place(x=10, y=280)

Website_BTN=Button(Panal_frame, text='Website ', width=22, bg='#ffa502', fg='#1e272e', font=('Calibri (Body)', 12, 'bold'), cursor='hand2', bd=0, command=Link4)
Website_BTN.place(x=10, y=330)

About_BTN=Button(Panal_frame, text='About Developer', width=22, bg='#ffa502', fg='#1e272e', font=('Calibri (Body)', 12, 'bold'), cursor='hand2',bd=0, command=About)
About_BTN.place(x=10, y=380)

Close_BTN=Button(Panal_frame, text='Close', width=22, bg='#e74c3c', fg='#ecf0f1', font=('Calibri (Body)', 12, 'bold'), cursor='hand2',bd=0 , command=quit)
Close_BTN.place(x=10, y=435)

# Logo Main Preview 

Logo_main = PhotoImage(file='barbhuiya.png')
img1 = Label(Laroussi_Login , image=Logo_main)
img1.place(x=250 , y=28 , width=650 , height=340)

# Login Frame

Login_Frame = Frame(Laroussi_Login , width=650 , height=300 , bg='#2c2c54')
Login_Frame.place(x=250, y=330)

Logo_user = PhotoImage(file='qr-code.png')
img_user = Label(Laroussi_Login , image=Logo_user, bg='#2c2c54')
img_user.place(x=248, y=350)

UserNameImage = PhotoImage(file='userlabel.png')
User_Name = Label(Login_Frame, text='  User Name', fg='white', bg='#2c2c54', font=('Calibri (Body)', 14 ,'bold'), image=UserNameImage, compound=LEFT)
User_Name.place(x=180, y=28)
UserNameEntry = Entry(Login_Frame, font=('Calibri (Body)', 13,'bold'), justify='center', width=26)
UserNameEntry.place(x=350, y=34)

PasswordImage = PhotoImage(file='padlock.png')
Password_Title = Label(Login_Frame, text='  Password', fg='white', bg='#2c2c54', font=('Calibri (Body)', 14 ,'bold'), image=PasswordImage, compound=LEFT)
Password_Title.place(x=180, y=68)
PasswordEntry = Entry(Login_Frame, font=('Calibri (Body)', 13,'bold'), width=26, justify='center', show='*')
PasswordEntry.place(x=350, y=74)

BTN_Login=Button(Login_Frame ,text='Sign in' ,width=19 ,bg='#ffa502', fg='black', font=('Calibri (Body)', 14, 'bold'), cursor='hand2', bd=0 , command=logIn)
BTN_Login.place(x=350, y=115)


# Run the main loop
Laroussi_Login.mainloop()
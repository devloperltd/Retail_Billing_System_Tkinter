from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib

# Market GUI Part ===========

Laroussi = Tk()
Laroussi.title('Retail Billing System V1.0 - https://laroussigsm.net/')
Laroussi.geometry('1366x675+0+0')
Laroussi.resizable(False, False)
Laroussi.iconbitmap('sale_shop_icon.ico')
Title_Prpject = Label(Laroussi, text='LAROUSSI RETAIL BILLING SYSTEM', font=('Bahnschrift SemiLight SemiConde', 18, 'bold'), bg='#f53b57', fg='#ecf0f1', bd=2, relief=GROOVE)
Title_Prpject.pack(fill=X, pady=5)   
# Cosmetics Products Price Fonctionality ===========

def total():
    global GelDouche_Price, FacePowder_Price, NailPolish_Price, FalseEyelashes_Price, FacialMasks_Price, Shampoo_Price, Deodorants_Price, Lipstick_Price, FaceCream_Price, SunEucerin_Price
    global Rice_Price, Wheat_Price, Oats_Price, Chickpeas_Price, Cowpea_Price, Lentils_Price, Beans_Price, Barley_Price, Flour_Price, Maize_Price
    global Cheese_Price, Cream_Price, DryMilk_Price, Yawort_Price, MistakaCheese_Price, Mzzarella_Price, GoudaCheese_Price, CheddarCheese_Price, Butter_Price, Margarine_Price
    global AmountTotal

# Total Price Cosmetics Products & Fonctionality ===========

    GelDouche_Price = int(GelDoucheEntry.get())*20
    FacePowder_Price = int(FacePowderEntry.get())*50
    NailPolish_Price = int(NailPolishEntry.get())*30
    FalseEyelashes_Price = int(FalseEyelashesEntry.get())*65
    FacialMasks_Price = int(FacialMasksEntry.get())*80
    Shampoo_Price = int(ShampooEntry.get())*40
    Deodorants_Price = int(DeodorantsEntry.get())*10
    Lipstick_Price = int(LipstickEntry.get())*15
    FaceCream_Price = int(FaceCreamEntry.get())*55
    SunEucerin_Price = int(SunEucerinEntry.get())*45

    Total_Cosmetics_Price = GelDouche_Price + FacePowder_Price + NailPolish_Price + FalseEyelashes_Price + FacialMasks_Price + Shampoo_Price + Deodorants_Price + Lipstick_Price + FaceCream_Price + SunEucerin_Price
    Cosmetics_PriceEntry.delete(0, END)
    Cosmetics_PriceEntry.insert(0, f'{Total_Cosmetics_Price}  DA')

    Cosmetics_Tax = Total_Cosmetics_Price*0.10
    Cosmetics_TaxEntry.delete(0, END)
    Cosmetics_TaxEntry.insert(0, str(Cosmetics_Tax) + ' DA')

    # Total Price Grocery Products & Fonctionality ===========

    Rice_Price = int(RiceEntry.get())*200
    Wheat_Price = int(WheatEntry.get())*60
    Oats_Price = int(OatsEntry.get())*30
    Chickpeas_Price = int(ChickpeasEntry.get())*15
    Cowpea_Price = int(CowpeaEntry.get())*25
    Lentils_Price = int(LentilsEntry.get())*55
    Beans_Price = int(BeansEntry.get())*20
    Barley_Price = int(BarleyEntry.get())*40
    Flour_Price = int(FlourEntry.get())*10
    Maize_Price = int(MaizeEntry.get())*55

    Total_Grocery_Price = Rice_Price + Wheat_Price + Oats_Price + Chickpeas_Price + Cowpea_Price + Lentils_Price + Beans_Price + Barley_Price + Flour_Price + Maize_Price
    Grocery_PriceEntry.delete('0', END)
    Grocery_PriceEntry.insert('0', str(Total_Grocery_Price) + ' DA')

    Grocery_Tax = Total_Grocery_Price*0.05
    Grocery_TaxEntry.delete('0', END)
    Grocery_TaxEntry.insert('0', str(Grocery_Tax) + ' DA')

    # Total Price Milk Products & Fonctionality ===========

    Cheese_Price = int(CheeseEntry.get())*80
    Cream_Price = int(CreamEntry.get())*70
    DryMilk_Price = int(DryMilkEntry.get())*65
    Yawort_Price = int(YawortEntry.get())*30
    MistakaCheese_Price = int(MistakaCheeseEntry.get())*90
    Mzzarella_Price = int(MzzarellaEntry.get())*55
    GoudaCheese_Price = int(GoudaCheeseEntry.get())*80
    CheddarCheese_Price = int(CheddarCheeseEntry.get())*75
    Butter_Price = int(ButterEntry.get())*20
    Margarine_Price = int(MargarineEntry.get())*15

    Total_Milk_Price = Cheese_Price + Cream_Price + DryMilk_Price + Yawort_Price + MistakaCheese_Price + Mzzarella_Price + GoudaCheese_Price + CheddarCheese_Price + Butter_Price + Margarine_Price
    Milk_PriceEntry.delete('0', END)
    Milk_PriceEntry.insert('0', str(Total_Milk_Price) + ' DA')

    Milk_Tax = Total_Milk_Price*0.10
    Milk_TaxEntry.delete('0', END)
    Milk_TaxEntry.insert('0', str(Milk_Tax) + ' DA')

    # All Amount Total Fonctionality ===========

    AmountTotal = Total_Cosmetics_Price + Total_Grocery_Price + Total_Milk_Price + Cosmetics_Tax + Grocery_Tax + Milk_Tax

# Bill Area Fonctionality Conditions ===========

# Set Search Bill & Save Bill Area Fonctionality

def Search_Bill():
      for i in os.listdir('Bills/'):
            if i.split('.')[0] == BILL_NUMEntry.get():
                  f = open(f'Bills/{i}', 'r')
                  TextArea.delete('1.0', END)
                  for data in f:
                        TextArea.insert(END, data)
                  f.close()
                  break
      else:
            messagebox.showerror('Error', 'The Bill Number Is Not Found!')                  

if not os.path.exists('Bills'):
     os.mkdir('Bills')

billnumber=random.randint(100, 1000)
def Bill_Area():
      if Cust_DetailsEntry.get()== '' or PhoneLableEntry.get() == '':
            messagebox.showerror('Error' , 'Customer Details Are Required')
      elif Cosmetics_PriceEntry.get() == '' and  Grocery_PriceEntry.get() == '' and  Milk_PriceEntry.get() == '':
            messagebox.showerror('Error' , 'No Prodect Are Selected')
      elif Cosmetics_PriceEntry.get() == '0 DA' and  Grocery_PriceEntry.get() == '0 DA' and  Milk_PriceEntry.get() == '0 DA':
            messagebox.showerror('Error' , 'No Prodect Are Selected')    
      else:
            TextArea.delete('1.0', END)
            TextArea.insert(END, '\n\t\t**** WELCOME TO LAROUSSI SUPERMARKET **** \n')
            TextArea.insert(END, f'\n Bill Number : {billnumber}')
            TextArea.insert(END, f'\n Customer Name : {Cust_DetailsEntry.get()}')
            TextArea.insert(END, f'\n Customer Phone Number : {PhoneLableEntry.get()}')
            TextArea.insert(END, f'\n\n =============================================================')
            TextArea.insert(END, '\n Product\t\t\tQuantity\t\t\tPrice')
            TextArea.insert(END, f'\n =============================================================')

            # Variable Bill Area Cosmetics Products   
            
            if GelDoucheEntry.get()!='0':
                  TextArea.insert(END, f'\n Gel Douche\t\t\t{GelDoucheEntry.get()}\t\t\t{GelDouche_Price} DA')
            if FacePowderEntry.get()!='0':
                  TextArea.insert(END, f'\n Face Powder\t\t\t{FacePowderEntry.get()}\t\t\t{FacePowder_Price} DA')
            if NailPolishEntry.get()!='0':
                  TextArea.insert(END, f'\n Nail Polish\t\t\t{NailPolishEntry.get()}\t\t\t{NailPolish_Price} DA')
            if FalseEyelashesEntry.get()!='0':
                  TextArea.insert(END, f'\n False Eyelashes\t\t\t{FalseEyelashesEntry.get()}\t\t\t{FalseEyelashes_Price} DA')
            if FacialMasksEntry.get()!='0':
                  TextArea.insert(END, f'\n Facial Masks\t\t\t{FacialMasksEntry.get()}\t\t\t{FacialMasks_Price} DA')
            if ShampooEntry.get()!='0':
                  TextArea.insert(END, f'\n Facial Masks\t\t\t{ShampooEntry.get()}\t\t\t{Shampoo_Price} DA')
            if DeodorantsEntry.get()!='0':
                  TextArea.insert(END, f'\n Deodorants\t\t\t{DeodorantsEntry.get()}\t\t\t{Deodorants_Price} DA')
            if LipstickEntry.get()!='0':
                  TextArea.insert(END, f'\n Lipstick\t\t\t{LipstickEntry.get()}\t\t\t{Lipstick_Price} DA')
            if FaceCreamEntry.get()!='0':
                  TextArea.insert(END, f'\n Lipstick\t\t\t{FaceCreamEntry.get()}\t\t\t{FaceCream_Price} DA')
            if SunEucerinEntry.get()!='0':
                  TextArea.insert(END, f'\n Sun Eucerin\t\t\t{SunEucerinEntry.get()}\t\t\t{SunEucerin_Price} DA')

            # Variable Bill Area Grocery Products

            if RiceEntry.get()!='0':
                  TextArea.insert(END, f'\n Rice\t\t\t{RiceEntry.get()}\t\t\t{Rice_Price} DA')
            if WheatEntry.get()!='0':
                  TextArea.insert(END, f'\n Wheat\t\t\t{WheatEntry.get()}\t\t\t{Wheat_Price} DA')
            if OatsEntry.get()!='0':
                  TextArea.insert(END, f'\n Oats\t\t\t{OatsEntry.get()}\t\t\t{Oats_Price} DA')
            if ChickpeasEntry.get()!='0':
                  TextArea.insert(END, f'\n Chickpeas\t\t\t{ChickpeasEntry.get()}\t\t\t{Chickpeas_Price} DA')
            if CowpeaEntry.get()!='0':
                  TextArea.insert(END, f'\n Cowpea\t\t\t{CowpeaEntry.get()}\t\t\t{Cowpea_Price} DA')
            if LentilsEntry.get()!='0':
                  TextArea.insert(END, f'\n Lentils\t\t\t{LentilsEntry.get()}\t\t\t{Lentils_Price} DA')
            if BeansEntry.get()!='0':
                  TextArea.insert(END, f'\n Beans\t\t\t{BeansEntry.get()}\t\t\t{Beans_Price} DA')
            if BarleyEntry.get()!='0':
                  TextArea.insert(END, f'\n Barley\t\t\t{BarleyEntry.get()}\t\t\t{Barley_Price} DA')
            if FlourEntry.get()!='0':
                  TextArea.insert(END, f'\n Flour\t\t\t{FlourEntry.get()}\t\t\t{Flour_Price} DA')
            if MaizeEntry.get()!='0':
                  TextArea.insert(END, f'\n Maize\t\t\t{MaizeEntry.get()}\t\t\t{Maize_Price} DA')

            # Variable Bill Area Milk Products

            if CheeseEntry.get()!='0':
                  TextArea.insert(END, f'\n Cheese\t\t\t{CheeseEntry.get()}\t\t\t{Cheese_Price} DA')
            if CreamEntry.get()!='0':
                  TextArea.insert(END, f'\n Cream\t\t\t{CreamEntry.get()}\t\t\t{Cream_Price} DA')
            if DryMilkEntry.get()!='0':
                  TextArea.insert(END, f'\n Dry Milk\t\t\t{DryMilkEntry.get()}\t\t\t{DryMilk_Price} DA')
            if YawortEntry.get()!='0':
                  TextArea.insert(END, f'\n Yawort\t\t\t{YawortEntry.get()}\t\t\t{Yawort_Price} DA')
            if MistakaCheeseEntry.get()!='0':
                  TextArea.insert(END, f'\n Mistaka Cheese\t\t\t{MistakaCheeseEntry.get()}\t\t\t{MistakaCheese_Price} DA')
            if MzzarellaEntry.get()!='0':
                  TextArea.insert(END, f'\n Mzzarella\t\t\t{MzzarellaEntry.get()}\t\t\t{Mzzarella_Price} DA')
            if GoudaCheeseEntry.get()!='0':
                  TextArea.insert(END, f'\n Gouda Cheese\t\t\t{GoudaCheeseEntry.get()}\t\t\t{GoudaCheese_Price} DA')
            if CheddarCheeseEntry.get()!='0':
                  TextArea.insert(END, f'\n Cheddar Cheese\t\t\t{CheddarCheeseEntry.get()}\t\t\t{CheddarCheese_Price} DA')
            if ButterEntry.get()!='0':
                  TextArea.insert(END, f'\n Butter\t\t\t{ButterEntry.get()}\t\t\t{Butter_Price} DA')
            if MargarineEntry.get()!='0':
                  TextArea.insert(END, f'\n Margarine\t\t\t{MargarineEntry.get()}\t\t\t{Margarine_Price} DA')

            TextArea.insert(END,f'\n -------------------------------------------------------------') 

            if Cosmetics_TaxEntry.get()!='0.0 DA':
                  TextArea.insert(END,f'\n Cosmetics Tax :\t\t\t{Cosmetics_TaxEntry.get()}')
            if Grocery_TaxEntry.get()!='0.0 DA':
                  TextArea.insert(END,f'\n Grocery Tax :\t\t\t{Grocery_TaxEntry.get()}')
            if Milk_TaxEntry.get()!='0.0 DA':
                  TextArea.insert(END,f'\n Milk Tax :\t\t\t{Milk_TaxEntry.get()}') 

            TextArea.insert(END,f'\n\n Amount Total :\t\t\t{AmountTotal}')
            TextArea.insert(END,f'\n -------------------------------------------------------------')
            Save_Bill()

def Save_Bill():
      global billnumber
      result = messagebox.askyesno('Confirm' , 'Do You Want Save The Bill?')
      if result:
            Bill_Content=TextArea.get('1.0',END)
            file=open(f'Bills/{billnumber}.txt', 'w')
            file.write(Bill_Content)
            file.close()
            messagebox.showinfo('Success',f' Bill Number {billnumber} is Save Successfuly')
            billnumber = random.randint(500, 1000) 

# Set Sent Email Bill Fonctionality

def Clear():
      GelDoucheEntry.delete(0, END)
      FacePowderEntry.delete(0, END)
      NailPolishEntry.delete(0, END)
      FalseEyelashesEntry.delete(0, END)
      FacialMasksEntry.delete(0, END)
      ShampooEntry.delete(0, END)
      DeodorantsEntry.delete(0, END)
      LipstickEntry.delete(0, END)
      FaceCreamEntry.delete(0, END)
      SunEucerinEntry.delete(0, END)

      GelDoucheEntry.insert(0, 0)
      FacePowderEntry.insert(0, 0)
      NailPolishEntry.insert(0, 0)
      FalseEyelashesEntry.insert(0, 0)
      FacialMasksEntry.insert(0, 0)
      ShampooEntry.insert(0, 0)
      DeodorantsEntry.insert(0, 0)
      LipstickEntry.insert(0, 0)
      FaceCreamEntry.insert(0, 0)
      SunEucerinEntry.insert(0, 0)

      RiceEntry.delete(0, END)
      WheatEntry.delete(0, END)
      OatsEntry.delete(0, END)
      ChickpeasEntry.delete(0, END)
      CowpeaEntry.delete(0, END)
      LentilsEntry.delete(0, END)
      BeansEntry.delete(0, END)
      BarleyEntry.delete(0, END)
      FlourEntry.delete(0, END)
      MaizeEntry.delete(0, END)

      RiceEntry.insert(0, 0)
      WheatEntry.insert(0, 0)
      OatsEntry.insert(0, 0)
      ChickpeasEntry.insert(0, 0)
      CowpeaEntry.insert(0, 0)
      LentilsEntry.insert(0, 0)
      BeansEntry.insert(0, 0)
      BarleyEntry.insert(0, 0)
      FlourEntry.insert(0, 0)
      MaizeEntry.insert(0, 0)

      CheeseEntry.delete(0, END)
      CreamEntry.delete(0, END)
      DryMilkEntry.delete(0, END)
      YawortEntry.delete(0, END)
      MistakaCheeseEntry.delete(0, END)
      MzzarellaEntry.delete(0, END)
      GoudaCheeseEntry.delete(0, END)
      CheddarCheeseEntry.delete(0, END)
      ButterEntry.delete(0, END)
      MargarineEntry.delete(0, END)

      CheeseEntry.insert(0, 0)
      CreamEntry.insert(0, 0)
      DryMilkEntry.insert(0, 0)
      YawortEntry.insert(0, 0)
      MistakaCheeseEntry.insert(0, 0)
      MzzarellaEntry.insert(0, 0)
      GoudaCheeseEntry.insert(0, 0)
      CheddarCheeseEntry.insert(0, 0)
      ButterEntry.insert(0, 0)
      MargarineEntry.insert(0, 0)

      Cosmetics_TaxEntry.delete(0, END)
      Grocery_TaxEntry.delete(0, END)
      Milk_TaxEntry.delete(0, END)

      Cosmetics_PriceEntry.delete(0, END)
      Grocery_PriceEntry.delete(0, END)
      Milk_PriceEntry.delete(0, END)

      Cust_DetailsEntry.delete(0, END)
      PhoneLableEntry.delete(0, END)
      BILL_NUMEntry.delete(0, END)

      TextArea.delete('1.0', END)

def Sent_Email():
   def Send_Gmail():
       try:
            Ob=smtplib.SMTP('smtp.gmail.com', 587)
            Ob.starttls()
            Ob.login(SenderEntry.get(), PasswordEntry.get())
            Message = Email_TextArea.get('1.0' , END)
            Ob.sendmail(SenderEntry.get(), RecieverEntry.get(), Message)
            Ob.quit()
            messagebox.showinfo('Success', 'Bill Is Sent Successfuly', parent=Laroussi1)
       except:
            messagebox.showerror('Error', 'Somthing Went Wrong!!... Please Try Again', parent=Laroussi1)     

   if TextArea.get('1.0', END)=='\n':
       messagebox.showerror('Error', 'Bill Erea Is Empty')
   else:
      Laroussi1=Toplevel()
      Laroussi1.title('Send Bill To Email')
      Laroussi1.config(bg='#130f40')
      Laroussi1.resizable(0,0)
      Laroussi1.iconbitmap('email_send.ico')

      SenderFrame=LabelFrame(Laroussi1, text='SENDER', font=('Bahnschrift SemiLight SemiConde', 15,'bold'), bd=4, bg='#130f40', fg='#f5f6fa')
      SenderFrame.grid(row=0,column=0, padx=35, pady=20)

      SenderLabel=Label(SenderFrame,text="Sender's Email", font=('Cascadia Code', 12, 'bold'), bg='#130f40', fg='#f5f6fa')
      SenderLabel.grid(row=0,column=0, padx=10, pady=8)
      SenderEntry=Entry(SenderFrame, font=('arial', 14, 'bold'), bd=2, width=28, relief=RIDGE)
      SenderEntry.grid(row=0, column=1, padx=10, pady=8)

      PasswordLabel=Label(SenderFrame,text="Password", font=('Cascadia Code', 12, 'bold'), bg='#130f40', fg='#f5f6fa')
      PasswordLabel.grid(row=1,column=0, padx=10, pady=8, sticky='w')
      PasswordEntry=Entry(SenderFrame, font=('arial', 14, 'bold'), bd=2, width=28, relief=RIDGE, show='*')
      PasswordEntry.grid(row=1, column=1, padx=10, pady=8, sticky='w')

      RecipientFrame=LabelFrame(Laroussi1, text='CUSTOMER', font=('Bahnschrift SemiLight SemiConde', 15,'bold'), bd=4, bg='#130f40', fg='#f5f6fa')
      RecipientFrame.grid(row=1,column=0, padx=35, pady=20)

      RecieverLabel=Label(RecipientFrame,text="Email Address", font=('Cascadia Code', 12, 'bold'), bg='#130f40', fg='#f5f6fa')
      RecieverLabel.grid(row=0,column=0, padx=10, pady=8, sticky='w')
      RecieverEntry=Entry(RecipientFrame, font=('arial', 14, 'bold'), bd=2, width=28, relief=RIDGE)
      RecieverEntry.grid(row=0, column=1, padx=10, pady=8, sticky='w')

      MessageFrame=LabelFrame(Laroussi1, text='Message', font=('Cascadia Code', 16,'bold'), bd=4, bg='#130f40', fg='#f5f6fa')
      MessageFrame.grid(row=1,column=0, padx=10, pady=8)

      Email_TextArea=Text(RecipientFrame, font=('Cascadia Code', 10, 'bold'), bd=4, relief=SUNKEN, width=60, height=11)
      Email_TextArea.grid(row=2, column=0, columnspan=2)
      Email_TextArea.delete('1.0', END)
      Email_TextArea.insert(END, TextArea.get('1.0', END).replace('=', '').replace('-', ''))

      SendButton = Button(Laroussi1, text='SEND EMAIL', font=('Bahnschrift SemiLight SemiConde', 14, 'bold'), bg='#f1c40f', width=20, bd=0, command=Send_Gmail)
      SendButton.grid(row=2, column=0, pady=20)


      Laroussi1.mainloop      


# Set Praint Bill Fonctionality

def Praint_Bill():
      if TextArea.get('1.0', END)=='\n':
            messagebox.showerror('Error', 'Bill Erea Is Empty')
      else:
            file=tempfile.mktemp('.txt')
            open(file, 'w').write(TextArea.get('1.0', END))
            os.startfile(file, 'print')

# Customer Details Frame ===========

Customer_Details_Frame = LabelFrame(Laroussi, text='Customer Details', font=('Cascadia Code', 12, 'bold'), fg='#f1c40f', bd=3, relief=GROOVE, bg='#130f40')
Customer_Details_Frame.pack(fill=X)

NameLable = Label(Customer_Details_Frame, text='Customer Name', font=('Bahnschrift SemiLight SemiConde', 12, 'bold'), bg='#130f40', fg='#ecf0f1')
NameLable.grid(row=0 , column=0, padx=15,)
Cust_DetailsEntry = Entry(Customer_Details_Frame, font=('Arial', 14), width=20)
Cust_DetailsEntry.grid(row=0 , column=1, padx=8)

PhoneLable = Label(Customer_Details_Frame, text='Phone Number', font=('Bahnschrift SemiLight SemiConde', 12, 'bold'), bg='#130f40', fg='#ecf0f1')
PhoneLable.grid(row=0 , column=2, padx=15, pady=5)
PhoneLableEntry = Entry(Customer_Details_Frame, font=('Arial', 14), width=20)
PhoneLableEntry.grid(row=0 , column=3, padx=8)

BILL_NUM_Lable = Label(Customer_Details_Frame, text='Bill Number', font=('Bahnschrift SemiLight SemiConde', 12, 'bold'), bg='#130f40', fg='#ecf0f1')
BILL_NUM_Lable.grid(row=0 , column=4, padx=15, pady=5)
BILL_NUMEntry = Entry(Customer_Details_Frame, font=('Arial', 14), width=20)
BILL_NUMEntry.grid(row=0 , column=5, padx=8)

SearchBTN = Button(Customer_Details_Frame, text='SEARCH', font=('Arial', 11, 'bold'), width=15, bg='#f1c40f', bd=0, command=Search_Bill)
SearchBTN.grid(row=0 , column=6, padx=20, pady=10)

ProdectsFrame = Frame(Laroussi)
ProdectsFrame.pack(pady=5)

# Cosmetics Products Frame ===========

CosmeticsFrame = LabelFrame(ProdectsFrame, text='Cosmetics Products', font=('Cascadia Code', 12, 'bold'), fg='#f1c40f', bd=3, relief=GROOVE, bg='#130f40')
CosmeticsFrame.grid(row=0, column=0)

GelDouchelabel = Label(CosmeticsFrame, text='Gel Douche' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
GelDouchelabel.grid(row=0, column=0, pady=5, padx=10, sticky='w')
GelDoucheEntry = Entry(CosmeticsFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
GelDoucheEntry.grid(row=0, column=1, pady=5, padx=10, sticky='w')
GelDoucheEntry.insert(0, 0)

FacePowderlabel = Label(CosmeticsFrame, text='Face Powder' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
FacePowderlabel.grid(row=1, column=0, pady=5, padx=10, sticky='w')
FacePowderEntry = Entry(CosmeticsFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
FacePowderEntry.grid(row=1, column=1, pady=5, padx=10, sticky='w')
FacePowderEntry.insert(0, 0)

NailPolishlabel = Label(CosmeticsFrame, text='Nail Polish' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
NailPolishlabel.grid(row=2, column=0, pady=5, padx=10, sticky='w')
NailPolishEntry = Entry(CosmeticsFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
NailPolishEntry.grid(row=2, column=1, pady=5, padx=10, sticky='w')
NailPolishEntry.insert(0, 0)

FalseEyelasheslabel = Label(CosmeticsFrame, text='False Eyelashes' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
FalseEyelasheslabel.grid(row=3, column=0, pady=5, padx=10, sticky='w')
FalseEyelashesEntry = Entry(CosmeticsFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
FalseEyelashesEntry.grid(row=3, column=1, pady=5, padx=10, sticky='w')
FalseEyelashesEntry.insert(0, 0)

FacialMaskslabel = Label(CosmeticsFrame, text='Facial Masks' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
FacialMaskslabel.grid(row=4, column=0, pady=5, padx=10, sticky='w')
FacialMasksEntry = Entry(CosmeticsFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
FacialMasksEntry.grid(row=4, column=1, pady=5, padx=10, sticky='w')
FacialMasksEntry.insert(0, 0)

Shampoolabel = Label(CosmeticsFrame, text='Shampoo' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Shampoolabel.grid(row=5, column=0, pady=5, padx=10, sticky='w')
ShampooEntry = Entry(CosmeticsFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
ShampooEntry.grid(row=5, column=1, pady=5, padx=10, sticky='w')
ShampooEntry.insert(0, 0)

Deodorantslabel = Label(CosmeticsFrame, text='Deodorants' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Deodorantslabel.grid(row=6, column=0, pady=5, padx=10, sticky='w')
DeodorantsEntry = Entry(CosmeticsFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
DeodorantsEntry.grid(row=6, column=1, pady=5, padx=10, stick='w')
DeodorantsEntry.insert(0, 0)

Lipsticklabel = Label(CosmeticsFrame, text='Lipstick' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Lipsticklabel.grid(row=8, column=0, pady=5, padx=10, sticky='w')
LipstickEntry = Entry(CosmeticsFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
LipstickEntry.grid(row=8, column=1, pady=5, padx=10, stick='w')
LipstickEntry.insert(0, 0)

FaceCreamlabel = Label(CosmeticsFrame, text='Face Cream' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
FaceCreamlabel.grid(row=9, column=0, pady=5, padx=10, sticky='w')
FaceCreamEntry = Entry(CosmeticsFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
FaceCreamEntry.grid(row=9, column=1, pady=5, padx=10, stick='w')
FaceCreamEntry.insert(0, 0)

SunEucerinlabel = Label(CosmeticsFrame, text='Sun Eucerin' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
SunEucerinlabel.grid(row=10, column=0, pady=5, padx=10, sticky='w')
SunEucerinEntry = Entry(CosmeticsFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
SunEucerinEntry.grid(row=10, column=1, pady=5, padx=10, stick='w')
SunEucerinEntry.insert(0, 0)

# Grocery Products Frame ===========

GroceryFrame = LabelFrame(ProdectsFrame, text='Grocery Products', font=('Cascadia Code', 12, 'bold'), fg='#f1c40f', bd=3, relief=GROOVE, bg='#130f40')
GroceryFrame.grid(row=0, column=1)

Ricelabel = Label(GroceryFrame, text='Rice' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Ricelabel.grid(row=0, column=0, pady=5, padx=10, sticky='w')
RiceEntry = Entry(GroceryFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
RiceEntry.grid(row=0, column=1, pady=5, padx=10, stick='w')
RiceEntry.insert(0, 0)

Wheatlabel = Label(GroceryFrame, text='Wheat' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Wheatlabel.grid(row=1, column=0, pady=5, padx=10, sticky='w')
WheatEntry = Entry(GroceryFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
WheatEntry.grid(row=1, column=1, pady=5, padx=10, stick='w')
WheatEntry.insert(0, 0)

Oatslabel = Label(GroceryFrame, text='Oats' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Oatslabel.grid(row=2, column=0, pady=5, padx=10, sticky='w')
OatsEntry = Entry(GroceryFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
OatsEntry.grid(row=2, column=1, pady=5, padx=10, stick='w')
OatsEntry.insert(0, 0)

Chickpeaslabel = Label(GroceryFrame, text='Chickpeas' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Chickpeaslabel.grid(row=3, column=0, pady=5, padx=10, sticky='w')
ChickpeasEntry = Entry(GroceryFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
ChickpeasEntry.grid(row=3, column=1, pady=5, padx=10, stick='w')
ChickpeasEntry.insert(0, 0)

Cowpealabel = Label(GroceryFrame, text='Cowpea' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Cowpealabel.grid(row=4, column=0, pady=5, padx=10, sticky='w')
CowpeaEntry = Entry(GroceryFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
CowpeaEntry.grid(row=4, column=1, pady=5, padx=10, stick='w')
CowpeaEntry.insert(0, 0)

Lentilslabel = Label(GroceryFrame, text='Lentils' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Lentilslabel.grid(row=5, column=0, pady=5, padx=10, sticky='w')
LentilsEntry = Entry(GroceryFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
LentilsEntry.grid(row=5, column=1, pady=5, padx=10, stick='w')
LentilsEntry.insert(0, 0)

Beanslabel = Label(GroceryFrame, text='Beans' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Beanslabel.grid(row=6, column=0, pady=5, padx=10, sticky='w')
BeansEntry = Entry(GroceryFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
BeansEntry.grid(row=6, column=1, pady=5, padx=10, stick='w')
BeansEntry.insert(0, 0)

Barleylabel = Label(GroceryFrame, text='Barley' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Barleylabel.grid(row=7, column=0, pady=5, padx=10, sticky='w')
BarleyEntry = Entry(GroceryFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
BarleyEntry.grid(row=7, column=1, pady=5, padx=10, stick='w')
BarleyEntry.insert(0, 0)

Flourlabel = Label(GroceryFrame, text='Flour' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Flourlabel.grid(row=8, column=0, pady=5, padx=10, sticky='w')
FlourEntry = Entry(GroceryFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
FlourEntry.grid(row=8, column=1, pady=5, padx=10, stick='w')
FlourEntry.insert(0, 0)

Maizelabel = Label(GroceryFrame, text='Maize' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Maizelabel.grid(row=9, column=0, pady=5, padx=10, sticky='w')
MaizeEntry = Entry(GroceryFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
MaizeEntry.grid(row=9, column=1, pady=5, padx=10, stick='w')
MaizeEntry.insert(0, 0)

# Milk Products Frame ===========

MilkFrame = LabelFrame(ProdectsFrame, text='Milk Products', font=('Cascadia Code', 12, 'bold'), fg='#f1c40f', bd=3, relief=GROOVE, bg='#130f40')
MilkFrame.grid(row=0, column=2)

Cheeselabel = Label(MilkFrame, text='Cheese' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Cheeselabel.grid(row=0, column=0, pady=5, padx=10, sticky='w')
CheeseEntry = Entry(MilkFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
CheeseEntry.grid(row=0, column=1, pady=5, padx=10, stick='w')
CheeseEntry.insert(0, 0)

Creamlabel = Label(MilkFrame, text='Cream' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Creamlabel.grid(row=2, column=0, pady=5, padx=10, sticky='w')
CreamEntry = Entry(MilkFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
CreamEntry.grid(row=2, column=1, pady=5, padx=10, stick='w')
CreamEntry.insert(0, 0)

DryMilklabel = Label(MilkFrame, text='Dry Milk' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
DryMilklabel.grid(row=3, column=0, pady=5, padx=10, sticky='w')
DryMilkEntry = Entry(MilkFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
DryMilkEntry.grid(row=3, column=1, pady=5, padx=10, stick='w')
DryMilkEntry.insert(0, 0)

Yawortlabel = Label(MilkFrame, text='Yawort' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Yawortlabel.grid(row=4, column=0, pady=5, padx=10, sticky='w')
YawortEntry = Entry(MilkFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
YawortEntry.grid(row=4, column=1, pady=5, padx=10, stick='w')
YawortEntry.insert(0, 0)

MistakaCheeselabel = Label(MilkFrame, text='Mistaka Cheese' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
MistakaCheeselabel.grid(row=5, column=0, pady=5, padx=10, sticky='w')
MistakaCheeseEntry = Entry(MilkFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
MistakaCheeseEntry.grid(row=5, column=1, pady=5, padx=10, stick='w')
MistakaCheeseEntry.insert(0, 0)

Mzzarellalabel = Label(MilkFrame, text='Mzzarella' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Mzzarellalabel.grid(row=6, column=0, pady=5, padx=10, sticky='w')
MzzarellaEntry = Entry(MilkFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
MzzarellaEntry.grid(row=6, column=1, pady=5, padx=10, stick='w')
MzzarellaEntry.insert(0, 0)

GoudaCheeselabel = Label(MilkFrame, text='Gouda Cheese' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
GoudaCheeselabel.grid(row=7, column=0, pady=5, padx=10, sticky='w')
GoudaCheeseEntry = Entry(MilkFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
GoudaCheeseEntry.grid(row=7, column=1, pady=5, padx=10, stick='w')
GoudaCheeseEntry.insert(0, 0)

CheddarCheeselabel = Label(MilkFrame, text='Cheddar Cheese' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
CheddarCheeselabel.grid(row=8, column=0, pady=5, padx=10, sticky='w')
CheddarCheeseEntry = Entry(MilkFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
CheddarCheeseEntry.grid(row=8, column=1, pady=5, padx=10, stick='w')
CheddarCheeseEntry.insert(0, 0)

Butterlabel = Label(MilkFrame, text='Butter' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Butterlabel.grid(row=9, column=0, pady=5, padx=10, sticky='w')
ButterEntry = Entry(MilkFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
ButterEntry.grid(row=9, column=1, pady=5, padx=10, stick='w')
ButterEntry.insert(0, 0)

Margarinelabel = Label(MilkFrame, text='Margarine' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Margarinelabel.grid(row=10, column=0, pady=5, padx=10, sticky='w')
MargarineEntry = Entry(MilkFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
MargarineEntry.grid(row=10, column=1, pady=5, padx=10, stick='w')
MargarineEntry.insert(0, 0)

# Bill Frame ===========

BillFrame = Frame(ProdectsFrame, bd=7, relief=GROOVE)
BillFrame.grid(row=0, column=3, pady=5)

BillAreaLable = Label(BillFrame, text='Bills Customer', font=('Cascadia Code', 13, 'bold'), bd=2, relief=GROOVE, bg='#f7d794', pady=9)
BillAreaLable.pack(fill=X)

Scrol_Bar=Scrollbar(BillFrame, orient=VERTICAL)
Scrol_Bar.pack(side=RIGHT, fill=Y)

TextArea = Text(BillFrame, height=21, width=63, yscrollcommand=Scrol_Bar.set)
TextArea.pack()
Scrol_Bar.config(command=TextArea.yview)

# Bill Menu Frame ===========

Bill_MenuFrame = LabelFrame(Laroussi, text='Bill Menu', font=('Cascadia Code', 12, 'bold'), fg='#f1c40f', bd=2, relief=GROOVE, bg='#130f40')
Bill_MenuFrame.pack()

# Price Frame ===========

Cosmetics_Pricelabel = Label(Bill_MenuFrame, text='Cosmetics Price' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Cosmetics_Pricelabel.grid(row=0, column=0, pady=3, padx=10, sticky='w')
Cosmetics_PriceEntry = Entry(Bill_MenuFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
Cosmetics_PriceEntry.grid(row=0, column=1, pady=3, padx=10, stick='w')

Grocery_Pricelabel = Label(Bill_MenuFrame, text='Grocery Price' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Grocery_Pricelabel.grid(row=1, column=0, pady=3, padx=10, sticky='w')
Grocery_PriceEntry = Entry(Bill_MenuFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
Grocery_PriceEntry.grid(row=1, column=1, pady=3, padx=10, stick='w')

Milk_Pricelabel = Label(Bill_MenuFrame, text='Milk Price' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Milk_Pricelabel.grid(row=2, column=0, pady=3, padx=10, sticky='w')
Milk_PriceEntry = Entry(Bill_MenuFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
Milk_PriceEntry.grid(row=2, column=1, pady=3, padx=10, stick='w')

# Tax Frame ===========

Cosmetics_Taxlabel = Label(Bill_MenuFrame, text='Cosmetics Tax' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Cosmetics_Taxlabel.grid(row=0, column=2, pady=3, padx=10, sticky='w')
Cosmetics_TaxEntry = Entry(Bill_MenuFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
Cosmetics_TaxEntry.grid(row=0, column=3, pady=3, padx=10, stick='w')

Grocery_Taxlabel = Label(Bill_MenuFrame, text='Grocery Tax' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Grocery_Taxlabel.grid(row=1, column=2, pady=3, padx=10, sticky='w')
Grocery_TaxEntry = Entry(Bill_MenuFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
Grocery_TaxEntry.grid(row=1, column=3, pady=3, padx=10, stick='w')

Milk_Taxlabel = Label(Bill_MenuFrame, text='Milk Tax' ,font=('Cascadia Code', 12, 'bold'), fg='#ecf0f1', bg='#130f40')
Milk_Taxlabel.grid(row=2, column=2, pady=3, padx=10, sticky='w')
Milk_TaxEntry = Entry(Bill_MenuFrame, font=('Arial', 10, 'bold'), width=15, justify='center')
Milk_TaxEntry.grid(row=2, column=3, pady=3, padx=10, stick='w')

# Button Frame ===========

ButtonFrame = Frame(Bill_MenuFrame)
ButtonFrame.grid(row=0, column=4, rowspan=3)

TotalButton= Button(ButtonFrame, text='Total', font=('Arial', 11, 'bold'), width=15, bg='#2ecc71', bd=0, pady=15, command=total)
TotalButton.grid(row=0, column=0, pady=20, padx=9)

BillButton= Button(ButtonFrame, text='Bill', font=('Arial', 11, 'bold'), width=15, bg='#3498db', bd=0, pady=15, command=Bill_Area)
BillButton.grid(row=0, column=1, pady=20, padx=9)

EmailButton= Button(ButtonFrame, text='Email', font=('Arial', 11, 'bold'), width=15, bg='#f1c40f', bd=0, pady=15, command=Sent_Email)
EmailButton.grid(row=0, column=2, pady=20, padx=9)

PrintButton= Button(ButtonFrame, text='Print', font=('Arial', 11, 'bold'), width=15, bg='#786fa6', bd=0, pady=15, command=Praint_Bill)
PrintButton.grid(row=0, column=3, pady=20, padx=9)

ClearButton= Button(ButtonFrame, text='Clear', font=('Arial', 11, 'bold'), width=15, bg='#eb3b5a', bd=0, pady=15, command=Clear)
ClearButton.grid(row=0, column=4, pady=20, padx=9)



# Run the main loop
Laroussi.mainloop()
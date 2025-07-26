from tkinter import *
from tkinter import messagebox
from random import randint
from os import path,mkdir

if not path.exists('Generated bills'):
    mkdir('Generated bills')

bill_number = randint(500,1000)

def save_bill():
    global bill_number
    result = messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0,END)
        file = open(f'Generated bills/{bill_number}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'{bill_number} is saved successfully')
        bill_number = randint(500,1000)

# Functions part
def total():
    global soap_price,face_cream_price,face_wash_price,hair_spray_price,body_lotion_price
    global rice_price,oil_price,daal_price,wheat_price,sugar_price
    global maza_price,coke_price,pepsi_price,sprite_price,dew_price
    global total_bill
    # cosmetic price calculation
    soap_price = int(bathsoapEntry.get())*20
    face_cream_price = int(facecreamEntry.get())*50
    face_wash_price = int(facewashEntry.get())*100
    hair_spray_price = int(hairsprayEntry.get())*150
    body_lotion_price = int(bodylotionEntry.get())*200

    total_cosmetic_price = soap_price + face_cream_price + face_wash_price + hair_spray_price + body_lotion_price
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{total_cosmetic_price} Rs')
    cosmetic_tax=total_cosmetic_price*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmetic_tax) + ' Rs')
    # grocery price calculation
    rice_price = int(riceEntry.get())*30
    oil_price = int(foodoilEntry.get())*100
    daal_price = int(daalEntry.get())*120
    wheat_price = int(wheatEntry.get())*80
    sugar_price = int(sugarEntry.get())*90
    total_grocery_price = rice_price + oil_price + daal_price + wheat_price + sugar_price
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(total_grocery_price)+' Rs')
    grocery_tax=total_grocery_price*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocery_tax) + ' Rs')
    # drinks price calculation
    maza_price = int(mazaEntry.get())*30
    coke_price = int(cokeEntry.get())*60
    pepsi_price = int(pepsiEntry.get())*70
    sprite_price = int(spriteEntry.get())*90
    dew_price = int(dewEntry.get())*120
    total_drinks_price = maza_price + coke_price + pepsi_price + sprite_price + dew_price
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,str(total_drinks_price)+' Rs')
    drinks_tax=total_drinks_price*0.08
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,str(drinks_tax) + ' Rs')

    total_bill = total_cosmetic_price + total_grocery_price + total_drinks_price + cosmetic_tax + grocery_tax + drinks_tax

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
        messagebox.showerror('Error','No Products Are Selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs':
        messagebox.showerror('Error','No Products/ Are Selected or No Total of Products Found')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t\t**Welcome Customer**')
        textarea.insert(END,f'\nBill Number: {bill_number}')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END,f'\nPhone Number: {phoneEntry.get()}')
        textarea.insert(END,'\n******************************************************************')
        textarea.insert(END,'\nProduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n******************************************************************')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soap_price} Rs')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream Price\t{facecreamEntry.get()}\t\t\t{face_cream_price} Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{face_wash_price} Rs')
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hair_spray_price} Rs')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{body_lotion_price} Rs')
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t\t\t{riceEntry.get()}\t\t\t{rice_price} Rs')
        if foodoilEntry.get()!='0':
            textarea.insert(END,f'\nFood Oil\t\t\t{foodoilEntry.get()}\t\t\t{oil_price} Rs')
        if daalEntry.get()!='0':
            textarea.insert(END,f'\nDaal\t\t\t\t{daalEntry.get()}\t\t\t{daal_price} Rs')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t\t\t{wheatEntry.get()}\t\t\t{wheat_price} Rs')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t\t{sugarEntry.get()}\t\t\t{sugar_price} Rs')
        if mazaEntry.get()!='0':
            textarea.insert(END,f'\nMaza\t\t\t\t{mazaEntry.get()}\t\t\t{maza_price} Rs')
        if cokeEntry.get()!='0':
            textarea.insert(END,f'\nCoke\t\t\t\t{cokeEntry.get()}\t\t\t{coke_price} Rs')
        if pepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi\t\t\t\t{pepsiEntry.get()}\t\t\t{pepsi_price} Rs')
        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite\t\t\t\t{spriteEntry.get()}\t\t\t{sprite_price} Rs')
        if dewEntry.get()!='0':
            textarea.insert(END,f'\nDew\t\t\t\t\t{dewEntry.get()}\t\t\t{dew_price} Rs')
        textarea.insert(END,'\n******************************************************************')

        if cosmeticpriceEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t\t{cosmeticpriceEntry.get()}')
        if grocerytaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')
        if drinkstaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nDrinks Tax\t\t\t\t{drinkstaxEntry.get()}')
        textarea.insert(END,f'\nTotal Bill \t\t\t\t {total_bill}')
        textarea.insert(END,'\n******************************************************************')
        save_bill()

def clear():
    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    bodylotionEntry.insert(0,0)

    riceEntry.insert(0,0)
    foodoilEntry.insert(0,0)
    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    sugarEntry.insert(0,0)

    mazaEntry.insert(0,0)
    cokeEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    dewEntry.insert(0,0)

    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    drinkstaxEntry.delete(0,END)

    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    drinkspriceEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)

    textarea.delete(1.0,END)

# GUI part
root = Tk()
root.title("Billing Software - Tkinter")
root.geometry("1278x685") # widthxheight
root.iconbitmap('icon.ico') # for icon

# heading/title
headingLabel = Label(root,text='Billing Software',font=('times new roman',30,'bold'),bg='dodgerblue4',fg='white',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=10)

# first row customer details
customer_details_frame = LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='goldenrod3',bd=8,relief=GROOVE,bg='dodgerblue4')
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='dodgerblue4',fg='white')
nameLabel.grid(row=0,column=0,padx=20)
nameEntry = Entry(customer_details_frame,font=('arial',9),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel = Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='dodgerblue4',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry = Entry(customer_details_frame,font=('arial',9),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel = Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='dodgerblue4',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)
billnumberLabel = Entry(customer_details_frame,font=('arial',9),bd=7,width=18)
billnumberLabel.grid(row=0,column=5,padx=8)

searchButton = Button(customer_details_frame,text='SEARCH',font=('arial0',9,'bold'),bd=7)
searchButton.grid(row=0,column=6,padx=20,pady=8)

# second row, first column cosmetics
productsFrame = Frame(root,)
productsFrame.pack(pady=10)

cosmeticsFrame = LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='goldenrod3',bd=8,relief=GROOVE,bg='dodgerblue4')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel = Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathsoapEntry = Entry(cosmeticsFrame,font=('times new roman',13,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel = Label(cosmeticsFrame,text='Face Cream',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
facecreamEntry = Entry(cosmeticsFrame,font=('times new roman',13,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel = Label(cosmeticsFrame,text='Face Wash',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
facewashEntry = Entry(cosmeticsFrame,font=('times new roman',13,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel = Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairsprayEntry = Entry(cosmeticsFrame,font=('times new roman',13,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

bodylotionLabel = Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
bodylotionLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
bodylotionEntry = Entry(cosmeticsFrame,font=('times new roman',13,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=4,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

# second row, second column grocery
groceryFrame = LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),fg='goldenrod3',bd=8,relief=GROOVE,bg='dodgerblue4')
groceryFrame.grid(row=0,column=1)

riceLabel = Label(groceryFrame,text='Rice',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
riceEntry = Entry(groceryFrame,font=('times new roman',13,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

foodoilLabel = Label(groceryFrame,text='Food Oil',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
foodoilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
foodoilEntry = Entry(groceryFrame,font=('times new roman',13,'bold'),width=10,bd=5)
foodoilEntry.grid(row=1,column=1,pady=9,padx=10)
foodoilEntry.insert(0,0)

daalLabel = Label(groceryFrame,text='Daal',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
daalEntry = Entry(groceryFrame,font=('times new roman',13,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,0)

wheatLabel = Label(groceryFrame,text='Wheat',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
wheatEntry = Entry(groceryFrame,font=('times new roman',13,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

sugarLabel = Label(groceryFrame,text='Sugar',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
sugarEntry = Entry(groceryFrame,font=('times new roman',13,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)
sugarEntry.insert(0,0)

# second row, second column grocery
drinksFrame = LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),fg='goldenrod3',bd=8,relief=GROOVE,bg='dodgerblue4')
drinksFrame.grid(row=0,column=2)

mazaLabel = Label(drinksFrame,text='Maza',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
mazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
mazaEntry = Entry(drinksFrame,font=('times new roman',13,'bold'),width=10,bd=5)
mazaEntry.grid(row=0,column=1,pady=9,padx=10)
mazaEntry.insert(0,0)

cokeLabel = Label(drinksFrame,text='Coke',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
cokeLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
cokeEntry = Entry(drinksFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cokeEntry.grid(row=1,column=1,pady=9,padx=10)
cokeEntry.insert(0,0)

pepsiLabel = Label(drinksFrame,text='Pepsi',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
pepsiLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
pepsiEntry = Entry(drinksFrame,font=('times new roman',13,'bold'),width=10,bd=5)
pepsiEntry.grid(row=2,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLabel = Label(drinksFrame,text='Sprite',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
spriteLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
spriteEntry = Entry(drinksFrame,font=('times new roman',13,'bold'),width=10,bd=5)
spriteEntry.grid(row=3,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

dewLabel = Label(drinksFrame,text='Dew',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
dewLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
dewEntry = Entry(drinksFrame,font=('times new roman',13,'bold'),width=10,bd=5)
dewEntry.grid(row=4,column=1,pady=9,padx=10)
dewEntry.insert(0,0)

# second row, third column bill area
billframe = Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel = Label(billframe,text='Bill Area',font=('times new roman',13,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea = Text(billframe,height=14,width=66,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

# third row, first column bill menu
billmenuFrame = LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='goldenrod3',bd=8,relief=GROOVE,bg='dodgerblue4')
billmenuFrame.pack(fill=X)

cosmeticpriceLabel = Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
cosmeticpriceEntry = Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=9,padx=10)

grocerypriceLabel = Label(billmenuFrame,text='Grocery Price',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
grocerypriceEntry = Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=9,padx=10)

drinkspriceLabel = Label(billmenuFrame,text='Drinks Price',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
drinkspriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
drinkspriceEntry = Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=9,padx=10)

# third row, second column bill menu
cosmetictaxLabel = Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')
cosmetictaxEntry = Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=9,padx=10)

grocerytaxLabel = Label(billmenuFrame,text='Grocery Tax',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')
grocerytaxEntry = Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=9,padx=10)

drinkstaxLabel = Label(billmenuFrame,text='Drinks Tax',font=('times new roman',13,'bold'),bg='dodgerblue4',fg='white')
drinkstaxLabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')
drinkstaxEntry = Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=9,padx=10)

# third row, third column buttons
buttonFrame = Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=5,padx=90)

totalButton = Button(buttonFrame,text='Total',font=('arial',13,'bold'),bg='dodgerblue4',fg='white',bd=5,width=8,pady=2,command=total)
totalButton.grid(row=0,column=0,pady=36,padx=15)

billButton = Button(buttonFrame,text='Generate Bill',font=('arial',13,'bold'),bg='dodgerblue4',fg='white',bd=5,width=8,pady=2,padx=15,command=bill_area)
billButton.grid(row=0,column=1,pady=36,padx=15)

# emailButton = Button(buttonFrame,text='Email',font=('arial',13,'bold'),bg='dodgerblue4',fg='white',bd=5,width=8,pady=2)
# emailButton.grid(row=0,column=2,pady=36,padx=5)

# printButton = Button(buttonFrame,text='Print',font=('arial',13,'bold'),bg='dodgerblue4',fg='white',bd=5,width=8,pady=2)
# printButton.grid(row=0,column=3,pady=36,padx=5)

clearButton = Button(buttonFrame,text='Clear',font=('arial',13,'bold'),bg='dodgerblue4',fg='white',bd=5,width=8,pady=2,command=clear)
clearButton.grid(row=0,column=4,pady=36,padx=15)

root.mainloop()
from datetime import datetime
from tkinter import *
from tkinter import ttk
import pickle
from tkinter import messagebox
window = Tk()
window.geometry("550x500+500+100")
window.title("Starbucks Coffee Shop")
window.resizable(False, False)


alladmins={
    "Admin_1":"1admin",

    "Admin_2":"2admin"
        
}

try:
    open_alladmins_file = open('alladmins.txt', 'rb')
    alladmins = pickle.load(open_alladmins_file)
    open_alladmins_file.close()
except: 
    open_alladmins_file = open('alladmins.txt', 'wb')
    pickle.dump(alladmins, open_alladmins_file)
    open_alladmins_file.close()


allusers={
    "Aytac_Veyisli":{
        "name": "Aytac",
        "surname":"Veyisli",
        "email":"aytac@gmail.com",
        "passwrd":"aytac1234",
        "gender" : "female"
    },
    "Nermin_Eliyeva":{
        "name": "Nermin",
        "surname":"Eliyeva",
        "email":"nermin@gmail.com",
        "passwrd":"nermin1234",
        "gender": "female"
}
}


try:
    open_alluser_file = open('alluser.txt', 'rb')
    allusers = pickle.load(open_alluser_file)
    open_alluser_file.close()
except: 
    open_alluser_file = open('alluser.txt', 'wb')
    pickle.dump(allusers, open_alluser_file)
    open_alluser_file.close()
    


#===============================functions========================================
def open_register():
    frame_btns.forget()
    frame_register.pack()
    
def back_menu():
    frame_register.forget()
    frame_btns.pack()

def open_login():
    frame_btns.forget()
    frame_login.pack()
    
def back_menu_login():
    frame_login.forget()
    frame_btns.pack()
    
def back_menu_user():
    user_frame.forget()
    frame_login.pack()

reg_show_hide=True
def register_show_hide():
    global reg_show_hide
    if reg_show_hide:
         passwrd_entry.config(show="*")
         show_hide_btn.config(text="show")
         reg_show_hide=False
    else:
         passwrd_entry.config(show="")
         show_hide_btn.config(text="hide")
         reg_show_hide=True

log_show_hide=True
def login_show_hide():
    global log_show_hide
    if log_show_hide:
        passwrd_entry_login.config(show="*")
        show_hide_btn_login.config(text="show")
        log_show_hide=False
    else:
        passwrd_entry_login.config(show="")
        show_hide_btn_login.config(text="hide")
        log_show_hide=True
        
def yoxla():
    frame_login.forget()
    user_frame.pack()

def reg_func():
    username=username_entry.get()
    surname=surname_entry.get()
    name=name_entry.get()
    email = email_entry.get()
    gender = gender_combobox.get()
    passwrd = passwrd_entry.get()
    if not email in allusers.keys():
        if len(username)>=4:
            if username.isalpha()==True:
                if len(surname)>=4:
                    if surname.isalpha()==True: 
                        if len(name)>=4:
                            if name.isalpha()==True:                       
                                if email.count("@gmail.com")==1 or email.count("@hotmail.com")==1 or email.count("@mail.ru")==1:    
                                    if len(passwrd)>=6:
                                        if not passwrd.islower():
                                            if not passwrd.isupper():
                                                new_user={
                                                    username:{
                                                    "name" : username,
                                                    "surname" :surname,
                                                    "email" : email,
                                                    "passwrd" : passwrd,
                                                    "gender":gender
                                                }
                                                            
                                                }
                                                allusers.update(new_user)
                                                    
                                                open_alluser_file = open('alluser.txt', 'wb')
                                                pickle.dump(allusers, open_alluser_file)
                                                messagebox.showinfo("Qeydiyyat", "Qeydiyyat ugurla tamamlandi")
                                                open_alluser_file.close()
                                                #register_error_label.config("Qeydiyyat Bitdi")
                                                        
                                            else:
                                                register_error_label.config(text="Parolda minimum 1 kicik herf olmalidir")
                                        else:
                                            register_error_label.config(text="Parolda minimum 1 boyuk herf olmalidir")
                                    else:
                                        register_error_label.config(text="Parolda minimum 6 simvol olmalidir")
                                else:
                                    register_error_label.config(text="Email duzgun deyil.")
                            else:
                                register_error_label.config(text="Ad ancaq heriflerden ibaret olmalidir")
                        else:
                            register_error_label.config(text="Ad minimum 4 simvol olmalidir.")
                    else:
                        register_error_label.config(text="SoyAd ancaq heriflerden ibaret olmalidir.")    
                else:
                    register_error_label.config(text="SoyAd Minimum 4 Simbol Olmalidir.")
            else:
                register_error_label.config(text="Username ancaq heriflerden ibaret olmalidir")
        else:
            register_error_label.config(text="Username Minimum 4 Simbol Olmalidir.")
    else:
        register_error_label.config(text="Bu Email Artiq Movcuddur.")
        

def login_func():
    global allusers
    adminORuser = y.get()
    if adminORuser == "Admin":
        username_login_get = username_entry_login.get()
        password_login_get = passwrd_entry_login.get()
        if username_login_get in alladmins.keys():
            if password_login_get == alladmins[username_login_get]:
                m = messagebox.showinfo("Welcome to Starbucks", "Hello Admin!" )
                print(m)
                if m == "ok":
                    frame_login.forget()
                    admin_frame.pack()
                else:
                    frame_login.pack()
            else:
                messagebox.showerror("Error", "Parol yanlisdir")
        else:
            messagebox.showerror("Error", "Istifadeci adi yanlisdir")
    if adminORuser == "User":
        user_username_login_get = username_entry_login.get()
        user_password_login_get = passwrd_entry_login.get()
        if user_username_login_get in allusers:
            if user_password_login_get == allusers[user_username_login_get]["passwrd"]:
                m_user = messagebox.showinfo("Welcome to Starbucks", "Hello user!" )
                print(m_user)
                if m_user == "ok":
                    frame_login.forget()
                    user_frame.pack()
                else:
                    frame_login.pack()
            else:
                messagebox.showerror("Error", "Parol yanlisdir")
        else:
            messagebox.showerror("Error", "Istifadeci adi yanlisdir")
                

def odenis():
    messagebox.showinfo("Order", "Sifarisiniz tesdiq olundu")

def yadda_saxla():
    pass
    
umumi = 0
def sebet():
    global umumi
    top_sebet = Toplevel(user_frame)
    top_sebet.geometry("300x300")
    listbox_coffee = Listbox(top_sebet)
    listbox_coffee.pack(expand=True, fill=BOTH)
    americano_price = 7.5
    veranda_price = 6
    cappucino_price = 10
    espresso_price = 8.5
    flat_white_price = 12
    latte_price = 5
    macchiato_price = 11.5
    mocha_price = 5
    
    if americano_check_variable.get()=="1":
        listbox_coffee.insert(1, "Americano - 7.50 AZN")
        umumi+=americano_price
    if veranda_check_variable.get() == "1":
        listbox_coffee.insert(2, "Veranda - 6 AZN")
        umumi+=veranda_price
    if cappucino_check_variable.get() == "1":
        listbox_coffee.insert(3, "Cappucino - 10 AZN")
        umumi+=cappucino_price
    if espresso_check_variable.get() == "1":
        listbox_coffee.insert(4, "Espresso - 8.50 AZN")
        umumi+=espresso_price
    if flat_white_check_variable.get() == "1":
        listbox_coffee.insert(5, "Flat White - 12 AZN")
        umumi+=flat_white_price
    if latte_check_variable.get() == "1":
        listbox_coffee.insert(6, "Latte - 5 AZN")
        umumi+=latte_price
    if macchiato_check_variable.get() =="1":
        listbox_coffee.insert(7, "Macchiato - 11.50 AZN")
        umumi+=macchiato_price
    if mocha_check_variable.get() == "1":
        listbox_coffee.insert(8, "Mocha - 5 AZN")
        umumi+=mocha_price
    umumi_label = Label(top_sebet, text=f"Umumi mebleg {umumi} AZN", font=("times new roman", 16), bg="white")
    umumi_label.place(relx=0.02, rely=0.7)
    odenis_button = Button(top_sebet, text="Sifaris et", font=("times new roman", 14), command=odenis)
    odenis_button.place(relx=0.32, rely=0.8)
    

#==================================dizayn(register login btns)===============================
window.iconbitmap("icon.ico")
photo_1 = PhotoImage(file="sekil_1.gif")
frame_btns = Frame(window)
frame_btns.pack()
label_sekil_1 = Label(frame_btns, image=photo_1)
label_sekil_1.pack(expand=True, fill=BOTH)
reg_btn = Button(frame_btns, text = "Register", font=("Comic Sans MS", 10, "bold"), bg="white", fg="dark green", border=True, command=open_register)
reg_btn.place(relx = 0.06, rely= 0.1, relwidth=0.2, relheight=0.07)
log_in_btn = Button(frame_btns, text = "Log in", font=("Comic Sans MS", 10, "bold"), bg="white", fg="dark green", border=True, command=open_login)
log_in_btn.place(relx = 0.06, rely = 0.2, relwidth=0.2, relheight=0.07)


#==================================dizayn(register)============================================
photo_2 = PhotoImage(file="sekil_2.gif")
frame_register = Frame(window)
label_sekil_2 = Label(frame_register, image=photo_2)
label_sekil_2.pack(expand=True, fill=BOTH)


username_label = Label(frame_register, text = "Username", font=("Times New Roman", 14), bg="orange")
username_label.place(relx=0.05, rely=0.05)
username_entry = Entry(frame_register)
username_entry.place(relx=0.24, rely=0.06)

name_label = Label(frame_register, text="Name", font=("Times New Roman", 14), bg="orange")
name_label.place(relx=0.05, rely=0.15)
name_entry = Entry(frame_register)
name_entry.place(relx=0.24, rely=0.15)

surname_label = Label(frame_register, text="Surname", font=("Times New Roman", 14), bg="orange")
surname_label.place(relx=0.05, rely=0.25)
surname_entry = Entry(frame_register)
surname_entry.place(relx=0.24, rely=0.25)                 

passwrd_label = Label(frame_register, text="Password", font=("Times New Roman", 14), bg="orange")
passwrd_label.place(relx=0.55, rely=0.05)      
passwrd_entry = Entry(frame_register)
passwrd_entry.place(relx=0.73, rely=0.06, relwidth=0.15)
show_hide_btn = Button(frame_register, text="hide", command=register_show_hide)
show_hide_btn.place(relx=0.9, rely=0.06, relheight=0.04)

email_label = Label(frame_register, text="E-mail", font=("Times New Roman", 14), bg="orange")
email_label.place(relx=0.55, rely=0.15)
email_entry=Entry(frame_register)
email_entry.place(relx=0.73, rely=0.15)

gender_label = Label(frame_register, text="Gender", font=("Times New Roman", 14), bg="orange")
gender_label.place(relx=0.55, rely=0.25)
gender_inside_combo = ('Female', "Male")
x = StringVar()
x.set("empty")
gender_combobox = ttk.Combobox(frame_register, textvariable=x, values=gender_inside_combo )
gender_combobox.place(relx=0.73, rely=0.25, relwidth=0.23)
gender_combobox["state"]="readonly"


back_btns_menu = Button(frame_register, text="Menu", font=("Times New Roman", 14), fg="orange", command=back_menu )
back_btns_menu.place(relx=0.05, rely= 0.9)


resgister_button = Button(frame_register, text='Register', font=("Times New Roman", 18), fg="orange", command=reg_func)
resgister_button.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.1)

register_error_label=Label(frame_register, text="", font=("Times New Roman", 14), bg="orange"  )
register_error_label.place(relx=0.4 , rely=0.9)
#===========================dizayn(login)=======================================
frame_login = Frame(window)
photo_3 = PhotoImage(file='sekil_3.gif')
label_sekil_3 = Label(frame_login, image=photo_3)
label_sekil_3.pack(expand=True, fill=BOTH)


username_label_login = Label(frame_login, text="Username", font=("Times New Roman", 16))
username_label_login.place(relx=0.25, rely=0.3)
username_entry_login = Entry(frame_login)
username_entry_login.place(relx=0.44, rely=0.31)

passwrd_label_login = Label(frame_login, text="Password", font=("Times New Roman", 16))
passwrd_label_login.place(relx=0.25, rely=0.4)
passwrd_entry_login = Entry(frame_login)
passwrd_entry_login.place(relx=0.44, rely=0.41)
show_hide_btn_login = Button(frame_login, text="hide", command=login_show_hide)
show_hide_btn_login.place(relx=0.7, rely=0.41, relheight=0.04)
y = StringVar()
    
admin_rbtn = Radiobutton(frame_login, text="Admin", font=("times new roman", 10), value="Admin", variable=y, bg="orange", cursor="hand2")
admin_rbtn.place(relx = 0.3, rely=0.5)
user_rbtn = Radiobutton(frame_login, text="User", font=("times new roman", 10), value="User", variable=y, bg="orange", cursor="hand2")
user_rbtn.place(relx=0.55, rely=0.5)
login_button = Button(frame_login, text='Log in', font=("Times New Roman", 16), fg="orange", command=login_func)
login_button.place(relx=0.4, rely=0.7, relwidth=0.2)

back_btns_menu_login = Button(frame_login, text="Menu", font=("Times New Roman", 14), fg="orange", command=back_menu_login )
back_btns_menu_login.place(relx=0.05, rely= 0.9)

#=======================================Admin frame==============================================================
admin_frame=Frame(window)
photo_admin = PhotoImage(file='sekil_3.gif')
label_sekil_4 = Label(admin_frame, image=photo_3)
label_sekil_4.pack(expand=True, fill=BOTH)

ad_deyis_label = Label(admin_frame, text="Coffee adini deyis", font=("Times New Roman", 14), bg="orange")
ad_deyis_label.place(relx=0.02, rely=0.03)
ad_deyis_entry = Entry(admin_frame)
ad_deyis_entry.place(relx=0.6, rely=0.04)

coffee_names_change = ('Caffe Americano', 'Veranda Blend', 'Cappucino', 'Espresso', 'Flat White', 'Caffe Latte', 'Caramel Macchiato', 'Caffe Mocha')
c_n_ch =StringVar()
c_n_ch.set(coffee_names_change[0])
coffee_combo_change = ttk.Combobox(admin_frame, textvariable=c_n_ch, values=coffee_names_change)
coffee_combo_change.place(relx=0.3, rely=0.04)


coffee_qiymetini_deyis = Label(admin_frame, text="Qiymeti deyis", font=("Times New Roman", 14), bg="orange")
coffee_qiymetini_deyis.place(relx=0.02, rely=0.15)

coffee_qiymetini_deyis_entry = Entry(admin_frame)
coffee_qiymetini_deyis_entry.place(relx=0.6, rely=0.16)

coffee_names = ('Caffe Americano', 'Veranda Blend', 'Cappucino', 'Espresso', 'Flat White', 'Caffe Latte', 'Caramel Macchiato', 'Caffe Mocha')
c_n =StringVar()
c_n.set(coffee_names[0])
coffee_combo = ttk.Combobox(admin_frame, textvariable=c_n, values=coffee_names)
coffee_combo.place(relx=0.3, rely=0.16)


date_time = Label(admin_frame, text="Tarix ", font=("Times New Roman", 14 ), bg="orange")
date_time.place(relx=0.02, rely=0.6)




il_ay_gun = Label(admin_frame,text=datetime.today(), bg="grey", fg="white")
il_ay_gun.place(relx=0.2, rely=0.6)


yadda_saxla_button = Button(admin_frame, text='Yadda saxla', font=("Times New Roman", 18), fg="orange", command=yadda_saxla)
yadda_saxla_button.place(relx=0.4, rely=0.4, relwidth=0.3, relheight=0.1)



#=============================================user frame=================================================================

user_frame = Frame(window)
photo_user = PhotoImage(file='sekil_3.gif')
label_sekil_5 = Label(user_frame, image=photo_3)
label_sekil_5.pack(expand=True, fill=BOTH)
menu_user_coffe_label = Label(user_frame, text="~Coffee~", bg="orange", fg="black", font=('Comic Sans Ms', 22, "italic") )
menu_user_coffe_label.place(relx=0.3, rely=0.01, relwidth=0.4)
americano_label = Label(user_frame, text="Caffe Americano ...........................................................................................................", bg="white",  fg="grey", font=('Comic Sans Ms', 10, "italic"))
americano_label.place(relx=0.1, rely=0.2)
veranda_blend_label = Label(user_frame, text="Veranda Blend .................................................................................................................", bg="white",  fg="grey", font=('Comic Sans Ms', 10, "italic"))
veranda_blend_label.place(relx=0.1, rely=0.28)
cappucino_label = Label(user_frame, text="Cappucino ..........................................................................................................................", bg="white",  fg="grey", font=('Comic Sans Ms', 10, "italic"))
cappucino_label.place(relx=0.1, rely=0.36)
espresso_label = Label(user_frame, text="Espresso .............................................................................................................................", bg="white",  fg="grey", font=('Comic Sans Ms', 10, "italic"))
espresso_label.place(relx=0.1, rely=0.44)
flat_white_label = Label(user_frame, text="Flat White ........................................................................................................................", bg="white",  fg="grey", font=('Comic Sans Ms', 10, "italic"))
flat_white_label.place(relx=0.1, rely=0.52)
latte_label = Label(user_frame, text="Caffe Latte ......................................................................................................................", bg="white",  fg="grey", font=('Comic Sans Ms', 10, "italic"))
latte_label.place(relx=0.1, rely=0.6)
macchiato_label = Label(user_frame, text="Caramel Macchiato .......................................................................................................", bg="white",  fg="grey", font=('Comic Sans Ms', 10, "italic"))
macchiato_label.place(relx=0.1, rely=0.68)
mocha_label = Label(user_frame, text="Caffe Mocha ...................................................................................................................", bg="white",  fg="grey", font=('Comic Sans Ms', 10, "italic"))
mocha_label.place(relx=0.1, rely=0.76)


americano_check_variable = StringVar()
americano_check_variable.set('empty')
americano_check = Checkbutton(user_frame, text="Add", variable=americano_check_variable, bg="orange", cursor="hand2")
americano_check.place(relx=0.9, rely=0.2)

veranda_check_variable = StringVar()
veranda_check_variable.set("empty")
veranda_check = Checkbutton(user_frame, text="Add", variable=veranda_check_variable, bg="orange", cursor="hand2")
veranda_check.place(relx=0.9, rely=0.28)

cappucino_check_variable = StringVar()
cappucino_check_variable.set("empty")
cappucino_check = Checkbutton(user_frame, text="Add", variable=cappucino_check_variable, bg="orange", cursor="hand2")
cappucino_check.place(relx=0.9, rely=0.36)

espresso_check_variable = StringVar()
espresso_check_variable.set("empty")
espresso_check = Checkbutton(user_frame, text="Add", variable=espresso_check_variable, bg="orange", cursor="hand2")
espresso_check.place(relx=0.9, rely=0.44)

flat_white_check_variable = StringVar()
flat_white_check_variable.set("empty")
flat_white_check = Checkbutton(user_frame, text="Add", variable=flat_white_check_variable, bg="orange", cursor="hand2")
flat_white_check.place(relx=0.9, rely=0.52)

latte_check_variable = StringVar()
latte_check_variable.set("empty")
latte_check = Checkbutton(user_frame, text="Add", variable=latte_check_variable, bg="orange", cursor="hand2")
latte_check.place(relx=0.9, rely=0.6)

mocha_check_variable = StringVar()
mocha_check_variable.set("empty")
mocha_check = Checkbutton(user_frame, text="Add", variable=mocha_check_variable, bg="orange", cursor="hand2")
mocha_check.place(relx=0.9, rely=0.76)

macchiato_check_variable = StringVar()
macchiato_check_variable.set("empty")
macchiato_check = Checkbutton(user_frame, text="Add", variable=macchiato_check_variable, bg="orange", cursor="hand2")
macchiato_check.place(relx=0.9, rely=0.68)

back_btns_menu_user = Button(user_frame, text="Menu", font=("Times New Roman", 14), fg="orange", command=back_menu_user )
back_btns_menu_user.place(relx=0.05, rely= 0.9)

sebet_button = Button(user_frame, text='Sebete elave et', font=("Times New Roman", 18), fg="orange", command=sebet)
sebet_button.place(relx=0.35, rely=0.84, relwidth=0.4, relheight=0.1)


        

window.mainloop()
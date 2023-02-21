from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import sqlite3
import Guest
import Employee
import admin
import Dashboard
import admin_start


class AccountPage:
    def __init__(self, AccountSystem_window):
        self.AccountSystem_window = AccountSystem_window

        # Window Size and Placement
        AccountSystem_window.rowconfigure(0, weight=1)
        AccountSystem_window.columnconfigure(0, weight=1)
        height = 650
        width = 700
        x = (AccountSystem_window.winfo_screenwidth()//2)-(width//2)
        y = (AccountSystem_window.winfo_screenheight()//4)-(height//4)
        AccountSystem_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        AccountSystem_window.resizable(0, 0)

        # window Icon
        icon = PhotoImage(file='images//CoffeeShop-brand-logo.png')
        AccountSystem_window.iconphoto(True, icon)

        AccountSystem_window.title('COFFEE SHOP')

        # Navigating through windows
        sign_up = Frame(AccountSystem_window)
        sign_in = Frame(AccountSystem_window)
        landing_page = Frame(AccountSystem_window)

        for frame in (landing_page, sign_in, sign_up):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(landing_page)

        # ======================================================================================
        # =================== LANDING PAGE ========================================================
        # ======================================================================================
        landing_page.config(background='#ffffff')

        # ====== LOGO ==========
        logoIcon = Image.open('images//CoffeeShop-brand-logo.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(landing_page, image=photo, bg='#ffffff')
        logo.image = photo
        logo.place(x=20, y=45)

        brand_name = Label(landing_page, text='Batch 33 Cofee Shop', bg='#ffffff', fg='#ff6c38', font=("yu gothic ui", 15, "bold"))
        brand_name.place(x=83, y=53)

        text = Label(landing_page, text="FDA APPROVED", bg='#ffffff', font=("", 12, "bold"))
        text.place(x=20, y=140)
        txt = "• We produce hygienic and healthy coffee \nby all standards\t\t\t \n\n• Very Affordable and best Coffee in " \
              "town \nfor the past two and half years\t"
        text2 = Label(landing_page, text=txt,
                      fg="#6b6a69", bg='#ffffff', font=("", 11, "bold"))
        text2.place(x=15, y=180)

        # ====== LOGO ==========
        coffeeImage = Image.open('images//coffee3.gif')
        photo = ImageTk.PhotoImage(coffeeImage)
        coffee_image = Label(landing_page, image=photo, bg='#ffffff')
        coffee_image.image = photo
        coffee_image.place(x=30, y=370)


        pageDivide_line = Canvas(landing_page, width=1.5, height=900, bg="#e6e6e6", highlightthickness=0)
        pageDivide_line.place(x=350, y=0)

        # ========= RIGHT SIDE ===============
        # Label
        heading_label = Label(landing_page, text="To Continue,\n Please Login or Create New Account", font=("", 13, "bold"),
                              bg='#ffffff')
        heading_label.place(x=370, y=200)

        # Login Button
        login_button = Button(landing_page, text='Login', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='white',
                              cursor='hand2', activebackground='#fd6a36', activeforeground='white',
                              command=lambda: show_frame(sign_in))
        login_button.place(x=490, y=300)

        # Sign Up Button
        signUp_button = Button(landing_page, text='Create New Account', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='white',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='white',
                               command=lambda: show_frame(sign_up))
        signUp_button.place(x=440, y=350)

        def open_guest():
            win = Toplevel()
            Guest.GuestPage(win)
            AccountSystem_window.withdraw()
            win.deiconify()

        def open_employee():
            win = Toplevel()
            Dashboard.FirstPage(win)
            AccountSystem_window.withdraw()
            win.deiconify()

        def open_admin():
            win = Toplevel()
            admin_start.FirstPage(win)
            AccountSystem_window.withdraw()
            win.deiconify()

        # ==========================================================================================================
        # ================================ SIGN IN PAGE ============================================================
        # ==========================================================================================================
        sign_in.config(background='#ffffff')

        # ====== LOGO ==========
        logoIcon = Image.open('images//CoffeeShop-brand-logo.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(sign_in, image=photo, bg='#ffffff')
        logo.image = photo
        logo.place(x=20, y=45)

        brand_name = Label(sign_in, text='GIDEONS COFFEE SHOP', bg='#ffffff', fg='#ff6c38', font=("", 15, "bold"))
        brand_name.place(x=90, y=60)

        text = Label(sign_in, text="FDA APPROVED", bg='#ffffff', font=("", 12, "bold"))
        text.place(x=20, y=140)

        txt2 = "• We produce hygienic and healthy coffee \nby all standards\t\t\t \n\n• Very Affordable and best Coffee in " \
              "town \nfor the past two and half years\t"
        text2 = Label(sign_in, text=txt2,
                      fg="#6b6a69", bg='#ffffff', font=("", 11, "bold"))
        text2.place(x=20, y=180)

        # ====== LOGO ==========
        coffeeImage = Image.open('images//coffee3.gif')
        photo = ImageTk.PhotoImage(coffeeImage)
        coffee_image = Label(sign_in, image=photo, bg='#ffffff')
        coffee_image.image = photo
        coffee_image.place(x=30, y=370)


        pageDivide_line = Canvas(sign_in, width=1.5, height=900, bg="#e6e6e6", highlightthickness=0)
        pageDivide_line.place(x=350, y=0)

        heading = Label(sign_in, text="Sign In", font=("", 13, "bold"), bg='#ffffff')
        heading.place(x=490, y=50)

        Username = StringVar()
        Password = StringVar()

        def login_all():
            # Admin
            conn1 = sqlite3.connect("./Database/CoffeeShop.db")
            cursor1 = conn1.cursor()
            find_user1 = 'SELECT * FROM Admin_Account WHERE admin_username = ? and admin_password = ?'
            cursor1.execute(find_user1, [(username_entry.get()), (password_entry.get())])

            # Guest
            conn2 = sqlite3.connect("./Database/CoffeeShop.db")
            cursor2 = conn2.cursor()
            find_user2 = 'SELECT * FROM Guest_Account WHERE guest_username = ? and guest_password = ?'
            cursor2.execute(find_user2, [(username_entry.get()), (password_entry.get())])

            # Employee
            conn3 = sqlite3.connect("./Database/CoffeeShop.db")
            cursor3 = conn3.cursor()
            find_user3 = 'SELECT * FROM Employee_Account WHERE employee_username = ? and employee_password = ?'
            cursor3.execute(find_user3, [(username_entry.get()), (password_entry.get())])

            result3 = cursor3.fetchall()
            result2 = cursor2.fetchall()
            result1 = cursor1.fetchall()

            if result2:
                messagebox.showinfo("Success", 'Logged in Successfully,\n\nClick "OK" to continue.')
                open_guest()
            elif result1:
                messagebox.showinfo("Success", 'Logged in Successfully,\n\nClick "OK" to continue.')
                open_admin()
            elif result3:
                messagebox.showinfo("Success", 'Logged in Successfully,\n\nClick "OK" to continue.')
                open_employee()
            else:
                messagebox.showerror("Failed", "Wrong Login details, please try again.")

        # ========================================================================
        # ============================Username====================================
        # ========================================================================
        username_label = Label(sign_in, text='Username', fg="#27221c", bg='#ffffff', font=("", 12, "bold"))
        username_label.place(x=380, y=150)
        username_entry = Entry(sign_in, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69",
                               font=("", 12, 'bold'), textvariable=Username)
        username_entry.place(x=380, y=182, width=290, height=34)
        username_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

        # ========================================================================
        # ============================Password====================================
        # ========================================================================
        password_label = Label(sign_in, text='Password', fg="#27221c", bg='#ffffff', font=("", 12, "bold"))
        password_label.place(x=380, y=250)
        password_entry = Entry(sign_in, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69", font=("", 12), show="•",
                               textvariable=Password)
        password_entry.place(x=380, y=282, width=290, height=34)
        password_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

        loginButton = Button(sign_in, fg='#f8f8f8', text='Login', bg='#ff6c38', font=("", 12, "bold"),
                             cursor='hand2', activebackground='#ff6c38', command=login_all)
        loginButton.place(x=380, y=370, width=290, height=40)

        line = Canvas(sign_in, width=286, height=1.5, bg="#e6e6e6", highlightthickness=0)
        line.place(x=380, y=440)
        label = Label(sign_in, text='No Account Yet', bg='#ffffff')
        label.place(x=480, y=430)

        createButton = Button(sign_in, fg='#f8f8f8', text='Create New Account', bg='#4286f5', font=("", 12, "bold"),
                              cursor='hand2', activebackground='#4286f5', command=lambda: show_frame(sign_up))
        createButton.place(x=380, y=470, width=290, height=40)

        # function for show and hide password
        def password_command():
            if password_entry.cget('show') == "•":
                password_entry.config(show="")
            else:
                password_entry.config(show="•")

        # Check Button
        show_password = Checkbutton(sign_in, text="Show password", bg='#ffffff', fg='#27221c', command=password_command)
        show_password.place(x=380, y=332)


        def forgot_password():
            win = Toplevel()
            window_width = 350
            window_height = 350
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            position_top = int(screen_height / 4 - window_height / 4)
            position_right = int(screen_width / 2 - window_width / 2)
            win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
            win.title('Forgot Password')
            # win.iconbitmap('images//aa.ico')
            win.configure(background='#f8f8f8')
            win.resizable(0, 0)

            # Variables
            username = StringVar()
            password = StringVar()
            confirmPassword = StringVar()

            # ====== Email ====================
            username_entry3 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                                    textvariable=username)
            username_entry3.place(x=40, y=30, width=256, height=34)
            username_entry3.config(highlightbackground="black", highlightcolor="black")
            username_label3 = Label(win, text='• Username', fg="#89898b", bg='#f8f8f8',
                                    font=("yu gothic ui", 11, 'bold'))
            username_label2.place(x=40, y=0)

            # ====  New Password ==================
            new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                                       textvariable=password)
            new_password_entry.place(x=40, y=110, width=256, height=34)
            new_password_entry.config(highlightbackground="black", highlightcolor="black")
            new_password_label = Label(win, text='• New Password', fg="#89898b", bg='#f8f8f8',
                                       font=("yu gothic ui", 11, 'bold'))
            new_password_label.place(x=40, y=80)

            # ====  Confirm Password ==================
            confirm_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2
                                           , textvariable=confirmPassword)
            confirm_password_entry.place(x=40, y=190, width=256, height=34)
            confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
            confirm_password_label = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                           font=("yu gothic ui", 11, 'bold'))
            confirm_password_label.place(x=40, y=160)

            # ======= Update password Button ============
            update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#ff6c38', font=("", 12, "bold"),
                                 cursor='hand2', activebackground='#ff6c38', command=lambda: change_password())
            update_pass.place(x=40, y=240, width=256, height=50)



            # ========= DATABASE CONNECTION FOR FORGOT PASSWORD=====================
            def change_password():
                db = sqlite3.connect("./Database/CoffeeShop.db")
                cur = db.cursor()

                #insert = '''update Guest_Account set guest_password=? where guest_username=? '''
                #cur.execute(insert, [new_password_entry.get(), username_entry3.get(), ])
                #db.commit()
                #db.close()
                #messagebox.showinfo('Congrats', 'Password changed successfully')





        forgotPassword = Button(sign_in, text='Forgot password', font=("", 10, "bold"), bg='#ffffff', fg='#4286f5',
                                borderwidth=0, activebackground='#f8f8f8', command=lambda: forgot_password(), cursor="hand2")
        forgotPassword.place(x=540, y=332)

        # =============================================================================================================
        # ================================ SIGN UP PAGE ===============================================================
        # =============================================================================================================
        sign_up.config(background='#ffffff')

        # ====== LOGO ==========
        logoIcon = Image.open('images//CoffeeShop-brand-logo.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(sign_up, image=photo, bg='#ffffff')
        logo.image = photo
        logo.place(x=20, y=45)

        brand_name = Label(sign_up, text='Batch 33 ', bg='#ffffff', fg='#ff6c38', font=("", 15, "bold"))
        brand_name.place(x=90, y=60)

        text = Label(sign_up, text="FDA APPROVED", bg='#ffffff', font=("", 12, "bold"))
        text.place(x=20, y=140)
        txt3 = "• We produce hygienic and healthy coffee \nby all standards\t\t\t \n\n• Very Affordable and best Coffee in " \
              "town \nfor the past two and half years\t"
        text2 = Label(sign_up, text=txt3,
                      fg="#6b6a69", bg='#ffffff', font=("", 11, "bold"))
        text2.place(x=20, y=180)

        # ====== LOGO ==========
        coffeeImage = Image.open('images//coffee3.gif')
        photo = ImageTk.PhotoImage(coffeeImage)
        coffee_image = Label(sign_up, image=photo, bg='#ffffff')
        coffee_image.image = photo
        coffee_image.place(x=30, y=370)


        pageDivide_line = Canvas(sign_up, width=1.5, height=900, bg="#e6e6e6", highlightthickness=0)
        pageDivide_line.place(x=350, y=0)

        heading = Label(sign_up, text="Create New Account", font=("", 13, "bold"), bg='#ffffff')
        heading.place(x=440, y=30)

        FullName = StringVar()
        Username2 = StringVar()
        Password2 = StringVar()
        def signup_all():
            check_counter = 0
            warn = ""
            if fullname_entry.get() == "":
                warn = "Please enter your full name"
            else:
                check_counter += 1

            if username_entry2.get() == "":
                warn = "Please enter your username"
            else:
                check_counter += 1

            if password_entry2.get() == "":
                warn = "Please make sure your PASSWORD, USERNAME AND FULLNAME Fields are not empty"
            else:
                check_counter += 1

            if check_counter == 3:
                try:
                    connection = sqlite3.connect("./Database/CoffeeShop.db")
                    cur = connection.cursor()
                    cur.execute("INSERT INTO Guest_Account(guest_fullname, guest_username, guest_password) VALUES(?,?,?)",
                                (FullName.get(), Username2.get(), Password2.get()))

                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Success", 'New account created successfully\n\nClick "OK" to continue')
                    open_guest()

                except Exception as ep:
                    messagebox.showerror('', ep)
            else:
                messagebox.showerror('Error', warn)


        # ========================================================================
        # ============================Full name====================================
        # ========================================================================
        fullname_label = Label(sign_up, text='Fullname', fg="#27221c", bg='#ffffff', font=("", 12, "bold"))
        fullname_label.place(x=380, y=80)
        fullname_entry = Entry(sign_up, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69",
                               font=("", 12, 'bold'), textvariable=FullName)
        fullname_entry.place(x=380, y=112, width=290, height=34)
        fullname_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

        # ========================================================================
        # ============================Username====================================
        # ========================================================================
        username_label2 = Label(sign_up, text='Username', fg="#27221c", bg='#ffffff', font=("", 12, "bold"))
        username_label2.place(x=380, y=165)
        username_entry2 = Entry(sign_up, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69",
                                font=("", 12, 'bold'), textvariable=Username2)
        username_entry2.place(x=380, y=197, width=290, height=34)
        username_entry2.config(highlightbackground="#6b6a69", highlightcolor="black")

        # ========================================================================
        # ============================Password====================================
        # ========================================================================
        password_label2 = Label(sign_up, text='Password', fg="#27221c", bg='#ffffff', font=("", 12, "bold"))
        password_label2.place(x=380, y=250)
        password_entry2 = Entry(sign_up, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69", font=("", 12), show='•',
                                textvariable=Password2)
        password_entry2.place(x=380, y=282, width=290, height=34)
        password_entry2.config(highlightbackground="#6b6a69", highlightcolor="black")

        signupButton = Button(sign_up, fg='#f8f8f8', text='Create Account', bg='#ff6c38', font=("", 12, "bold"),
                              cursor='hand2', activebackground='#ff6c38', command=signup_all)
        signupButton.place(x=380, y=370, width=290, height=40)

        line = Canvas(sign_up, width=286, height=1.5, bg="#e6e6e6", highlightthickness=0)
        line.place(x=380, y=440)
        label = Label(sign_up, text='Already have account', bg='#ffffff')
        label.place(x=460, y=430)

        sign_inButton = Button(sign_up, fg='#f8f8f8', text='Login', bg='#4286f5', font=("", 12, "bold"),
                               cursor='hand2', activebackground='#4286f5', command=lambda: show_frame(sign_in))
        sign_inButton.place(x=380, y=470, width=290, height=40)

        # function for show and hide password

        def password_command2():
            if password_entry2.cget('show') == '•':
                password_entry2.config(show='')
            else:
                password_entry2.config(show='•')

        # Check Button
        show_password2 = Checkbutton(sign_up, text="Show password", bg='#ffffff', fg='#27221c',
                                     command=password_command2)
        show_password2.place(x=380, y=332)


        #AccountSystem_window.mainloop()

def page():
    window = Tk()
    AccountPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()

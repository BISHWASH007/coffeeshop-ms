from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
import admin_start
import AccountSystem
import admin
import Inventory


class InventoryPage:
    def __init__(self, account_window):
        self.account_window = account_window

        # Window Size and Placement
        account_window.rowconfigure(0, weight=1)
        account_window.columnconfigure(0, weight=1)
        screen_width = account_window.winfo_screenwidth()
        screen_height = account_window.winfo_height()
        app_width = 1366
        app_height = 700
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 160) - (app_height / 160)
        account_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        account_window.title("Coffee Management System")

        # window Icon
        icon = PhotoImage(file='images//CoffeeShop-brand-logo.png')
        account_window.iconphoto(True, icon)

        account_window.config(background='#f6f6f9')

        # ====== MENU BAR ==========
        logoIcon = Image.open('images//CoffeeShop-brand-logo.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(account_window, image=photo, bg='#f6f6f9')
        logo.image = photo
        logo.place(x=0, y=0)

        menuBar_line = Canvas(account_window, width=1500, height=1.5, bg="#e6e6e6", highlightthickness=0)
        menuBar_line.place(x=0, y=60)

        admIcon = Image.open('images//feeling.png')
        photo = ImageTk.PhotoImage(admIcon)
        adm = Label(account_window, image=photo, bg='#f6f6f9')
        adm.image = photo
        adm.place(x=1290, y=5)

        admLabel = Label(account_window, text='ADMIN', font=('yu gothic ui', 18, 'bold'), fg='#ffc329', bg='#f6f6f9')
        admLabel.place(x=1195, y=11)

        # ========== HOME BUTTON =======
        home_button = Button(account_window, text='Home', bg='#f6f6f9', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                             command=lambda: home())
        home_button.place(x=70, y=15)

        def home():
            win = Toplevel()
            admin_start.FirstPage(win)
            account_window.withdraw()
            win.deiconify()

        # ========== MANAGE BUTTON =======
        manage_button = Button(account_window, text='Manage', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='#ffffff',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a')
        manage_button.place(x=150, y=15)

        # ========== PRODUCTS BUTTON =======
        product_button = Button(account_window, text='Products', bg='#f6f6f9', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                                cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                command=lambda: product())
        product_button.place(x=250, y=15)


    
        def logout():
            win = Toplevel()
            AccountSystem.AccountPage(win)
            account_window.withdraw()
            win.deiconify()

        # ========== LOG OUT =======
        logout_button = Button(account_window, text='Logout', bg='#f6f6f9', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                               command=logout)
        logout_button.place(x=420, y=15)

        def product():
            account_window.withdraw()
            os.system("python admin.py")
            account_window.destroy()

        def bill():
            win = Toplevel()
            Inventory.InventoryPage(win)
            account_window.withdraw()
            win.deiconify()

        # PRODUCTS BUTTON
        productsFrame = LabelFrame(account_window, bg='#ffffff', bd='2.4')
        productsFrame.place(x=550, y=70, width=100, height=80)

        productsLabel = Label(productsFrame, text="Products", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
        productsLabel.place(x=10, y=0)

        productsIcon = Image.open('images//shopping-bag.png')
        photo = ImageTk.PhotoImage(productsIcon)
        products = Button(productsFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                          activebackground="#ffffff", command=product)
        products.image = photo
        products.place(x=0, y=22)

        # BILL BUTTON
        billFrame = LabelFrame(account_window, bg='#ffffff', bd='2.4')
        billFrame.place(x=660, y=70, width=100, height=80)

        billLabel = Label(billFrame, text="   Bill", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
        billLabel.place(x=10, y=0)

        billIcon = Image.open('images//bill.png')
        photo = ImageTk.PhotoImage(billIcon)
        bill = Button(billFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                      activebackground="#ffffff", command=bill)
        bill.image = photo
        bill.place(x=0, y=22)


        def exit2():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=account_window)
            if sure == True:
                account_window.destroy()

        button6 = Button(account_window)
        button6.place(relx=0.762, rely=0.022, width=86, height=25)
        button6.configure(relief="flat")
        button6.configure(overrelief="flat")
        button6.configure(activebackground="#fd6a36")
        button6.configure(cursor="hand2")
        button6.configure(foreground="#ffffff")
        button6.configure(background="#fd6a36")
        button6.configure(font="-family {Poppins SemiBold} -size 10")
        button6.configure(borderwidth="0")
        button6.configure(text="""Exit""")
        button6.configure(command=exit2)

        # ============= GUEST =============================
        guest_id = StringVar()
        guest_fullname = StringVar()
        guest_username = StringVar()
        guest_password = StringVar()

        guest_id_entry = Entry(account_window, textvariable=guest_id)
        guest_id_entry.place(relx=0.050, rely=0.169)
        guest_id_entry = Entry(account_window, textvariable=guest_fullname)
        guest_id_entry.place(relx=0.050, rely=0.169)
        guest_id_entry = Entry(account_window, textvariable=guest_username)
        guest_id_entry.place(relx=0.050, rely=0.169)
        guest_id_entry = Entry(account_window, textvariable=guest_password)
        guest_id_entry.place(relx=0.050, rely=0.169)

        def show_all_guest():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute("select * from Guest_Account")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.tree.delete(*self.tree.get_children())
                for row in rows:
                    self.tree.insert('', END, values=row)
                conn.commit()
            conn.close()

        def upgrade():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO Employee_Account values(?,?,?,?)",
                        (employee_id.get(), employee_fullname.get(), employee_username.get(), employee_password.get()))
            conn.commit()
            conn.close()
            show_all_employee()
            clear_employee()
            delete_guest()
            show_all_guest()
            messagebox.showinfo("Success", "User Upgrade to EMPLOYEE was Successful")

        def upgrade_admin():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO Admin_Account values(?,?,?,?)",
                        (admin_id.get(), admin_fullname.get(), admin_username.get(), admin_password.get()))
            conn.commit()
            conn.close()
            clear_employee()
            delete_guest()
            show_all_guest()
            show_all_admin()
            clear_admin()
            messagebox.showinfo("Success", "User Upgrade to ADMIN was Successful")

        def delete_guest():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM Guest_Account where guest_id=?", guest_id.get())
            conn.commit()
            show_all_employee()
            show_all_guest()
            clear_employee()
            conn.close()


        def guest_info(ev):
            viewInfo = self.tree.focus()
            coffee_data = self.tree.item(viewInfo)
            row = coffee_data['values']
            employee_id.set(row[0])
            employee_fullname.set(row[1])
            employee_username.set(row[2])
            employee_password.set(row[3])
            guest_id.set(row[0])
            guest_fullname.set(row[1])
            guest_username.set(row[2])
            guest_password.set(row[3])
            admin_id.set(row[0])
            admin_fullname.set(row[1])
            admin_username.set(row[2])
            admin_password.set(row[3])

        style = ttk.Style()
        style.theme_use("clam")
        self.scrollbarx = Scrollbar(account_window, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(account_window, orient=VERTICAL)
        self.tree = ttk.Treeview(account_window)
        self.tree.place(relx=0.020, rely=0.109, width=480, height=200)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        #self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        #self.tree.bind("<Double-1>", self.double_tap)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.372, rely=0.103, width=22, height=84)
        self.scrollbarx.place(relx=0.020, rely=0.40, width=84, height=22)

        self.tree.configure(
            columns=(
                "GuestID",
                "FullName",
                "UserName",
                "Password",
            )
        )

        self.tree.heading("GuestID", text="#", anchor=W)
        self.tree.heading("FullName", text="New Account Full Name", anchor=W)
        self.tree.heading("UserName", text="Username", anchor=W)
        self.tree.heading("Password", text="Password", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=40)
        self.tree.column("#2", stretch=NO, minwidth=0, width=210)
        self.tree.column("#3", stretch=NO, minwidth=0, width=140)
        self.tree.column("#4", stretch=NO, minwidth=0, width=200)
        show_all_guest()
        self.tree.bind("<ButtonRelease-1>", guest_info)

        # ============= EMPLOYEE =============================

        def show_all_employee():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute("select * from Employee_Account")
            rows = cur.fetchall()
            if len(rows) != 0:
                employee_tree.delete(*employee_tree.get_children())
                for row in rows:
                    employee_tree.insert('', END, values=row)
                conn.commit()
            conn.close()

        def employee_info(ev):
            viewInfo = employee_tree.focus()
            coffee_data = employee_tree.item(viewInfo)
            row = coffee_data['values']
            employee_id.set(row[0])
            employee_fullname.set(row[1])
            employee_username.set(row[2])
            employee_password.set(row[3])
            admin_id.set(row[0])
            admin_fullname.set(row[1])
            admin_username.set(row[2])
            admin_password.set(row[3])

        def add_employee():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO Employee_Account values(?,?,?,?)",
                        (employee_id.get(), employee_fullname.get(), employee_username.get(), employee_password.get()))
            conn.commit()
            conn.close()
            show_all_employee()
            clear_employee()
            messagebox.showinfo("Success", "Employee Records Added Successfully")

        def delete_employee():
            try:
                tree_view_content = employee_tree.focus()
                tree_view_items = employee_tree.item(tree_view_content)
                tree_view_values = tree_view_items['values'][1]
                ask = messagebox.askyesno("Warning",
                                          f"Are you sure you want to delete records of\n\n\t {tree_view_values}")
                if ask is True:
                    conn = sqlite3.connect("./Database/CoffeeShop.db")
                    cur = conn.cursor()
                    cur.execute("DELETE FROM Employee_Account where employee_id=?", employee_id.get())
                    conn.commit()
                    show_all_employee()
                    show_all_guest()
                    clear_employee()
                    conn.close()
                    messagebox.showinfo("Success",
                                        f" {tree_view_values} records has been deleted Successfully")
                else:
                    pass

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error",
                                     "There is some error deleting the data\n Make sure you have Selected the data")

        def update_employee():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute(
                "UPDATE Employee_Account set employee_fullname=?,employee_username=?,employee_password=? where "
                "employee_id=?",
                (employee_fullname.get(), employee_username.get(), employee_password.get(), employee_id.get()))
            conn.commit()
            conn.close()
            show_all_employee()
            clear_employee()
            messagebox.showinfo("Success", "Employee Records updated Successfully")

        def del_emp():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM Employee_Account where employee_id=?", employee_id.get())
            conn.commit()
            show_all_employee()
            clear_employee()
            conn.close()

        def upgrade_employee():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO Admin_Account values(?,?,?,?)",
                        (admin_id.get(), admin_fullname.get(), admin_username.get(), admin_password.get()))
            conn.commit()
            conn.close()
            del_emp()
            clear_employee()
            clear_admin()
            show_all_admin()
            messagebox.showinfo("Success", "User Upgrade to Employee Records was Successful")

        scrollbarx = Scrollbar(account_window, orient=HORIZONTAL)
        scrollbary = Scrollbar(account_window, orient=VERTICAL)
        employee_tree = ttk.Treeview(account_window)
        employee_tree.place(relx=0.220, rely=0.425, width=485, height=350)
        employee_tree.configure(
            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set
        )
        employee_tree.configure(selectmode="extended")

        # self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        # self.tree.bind("<Double-1>", self.double_tap)

        scrollbary.configure(command=employee_tree.yview)
        scrollbarx.configure(command=employee_tree.xview)

        scrollbary.place(relx=0.579, rely=0.503, width=22, height=84)
        scrollbarx.place(relx=0.390, rely=0.938, width=84, height=22)

        employee_tree.configure(
            columns=(
                "EmployeeID",
                "EmployeeName",
                "UserName",
                "Password",
            )
        )

        employee_tree.heading("EmployeeID", text="#", anchor=W)
        employee_tree.heading("EmployeeName", text="Employee Full Name", anchor=W)
        employee_tree.heading("UserName", text="Username", anchor=W)
        employee_tree.heading("Password", text="Password", anchor=W)

        employee_tree.column("#0", stretch=NO, minwidth=0, width=0)
        employee_tree.column("#1", stretch=NO, minwidth=0, width=40)
        employee_tree.column("#2", stretch=NO, minwidth=0, width=210)
        employee_tree.column("#3", stretch=NO, minwidth=0, width=140)
        employee_tree.column("#4", stretch=NO, minwidth=0, width=200)
        show_all_employee()
        employee_tree.bind("<ButtonRelease-1>", employee_info)

        employee_id = StringVar()
        employee_fullname = StringVar()
        employee_username = StringVar()
        employee_password = StringVar()

        # ID NAME AND ENTRY
        idLabel = Label(account_window, text="EMPLOYEE NUMBER", bg='#f6f6f9', font=("yu gothic ui", 12, "bold"))
        idLabel.place(relx=0.019, rely=0.466)

        idName_entry = Entry(account_window, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                             font=("", 12, 'bold'), textvariable=employee_id)
        idName_entry.place(relx=0.134, rely=0.466, width=65, height=30)
        idName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # COFFEE NAME AND ENTRY
        coffeeLabel = Label(account_window, text="EMPLOYEE  FULL  NAME", bg='#f6f6f9', font=("yu gothic ui", 12, "bold"))
        coffeeLabel.place(relx=0.034, rely=0.53)

        coffeeName_entry = Entry(account_window, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                 font=("", 12, 'bold'), textvariable=employee_fullname)
        coffeeName_entry.place(relx=0.019, rely=0.57, width=225, height=34)
        coffeeName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # COFFEE TYPE AND ENTRY
        typeLabel = Label(account_window, text="EMPLOYEE  USERNAME", bg='#f6f6f9', font=("yu gothic ui", 12, "bold"))
        typeLabel.place(relx=0.034, rely=0.620)

        typeName_entry = Entry(account_window, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                               font=("", 12, 'bold'), textvariable=employee_username)
        typeName_entry.place(relx=0.019, rely=0.661, width=225, height=34)
        typeName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # COFFEE DISCOUNT AND ENTRY
        discountLabel = Label(account_window, text="EMPLOYEE PASSWORD", bg='#f6f6f9', font=("yu gothic ui", 12, "bold"))
        discountLabel.place(relx=0.032, rely=0.71)

        discountName_entry = Entry(account_window, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                   font=("", 12, 'bold'), textvariable=employee_password)
        discountName_entry.place(relx=0.019, rely=0.75, width=225, height=34)
        discountName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        def clear_employee():
            employee_id.set("")
            employee_fullname.set("")
            employee_username.set("")
            employee_password.set("")

        self.button3 = Button(account_window)
        self.button3.place(relx=0.11, rely=0.830, width=86, height=25)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#fd6a36")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#fd6a36")
        self.button3.configure(font="-family {Poppins SemiBold} -size 10")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Clear""")
        self.button3.configure(command=clear_employee)

        self.button4 = Button(account_window)
        self.button4.place(relx=0.025, rely=0.830, width=84, height=25)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#fd6a36")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#fd6a36")
        self.button4.configure(font="-family {Poppins SemiBold} -size 10")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Add""")
        self.button4.configure(command=add_employee)

        self.button5 = Button(account_window)
        self.button5.place(relx=0.025, rely=0.890, width=86, height=25)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#fd6a36")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#fd6a36")
        self.button5.configure(font="-family {Poppins SemiBold} -size 10")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""Update""")
        self.button5.configure(command=update_employee)

        self.button6 = Button(account_window)
        self.button6.place(relx=0.11, rely=0.890, width=86, height=25)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#fd6a36")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#fd6a36")
        self.button6.configure(font="-family {Poppins SemiBold} -size 10")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Delete""")
        self.button6.configure(command=delete_employee)

        self.button7 = Button(account_window)
        self.button7.place(relx=0.025, rely=0.940, width=202, height=25)
        self.button7.configure(relief="flat")
        self.button7.configure(overrelief="flat")
        self.button7.configure(activebackground="#fd6a36")
        self.button7.configure(cursor="hand2")
        self.button7.configure(foreground="#ffffff")
        self.button7.configure(background="#fd6a36")
        self.button7.configure(font="-family {Poppins SemiBold} -size 10")
        self.button7.configure(borderwidth="0")
        self.button7.configure(text="""Upgrade Account to Employee""")
        self.button7.configure(command=upgrade)

        # ================ ADMIN ===============================
        admin_id = StringVar()
        admin_fullname = StringVar()
        admin_username = StringVar()
        admin_password = StringVar()


        def clear_admin():
            admin_id.set("")
            admin_fullname.set("")
            admin_username.set("")
            admin_password.set("")

        def admin_info(ev):
            viewInfo = admin_tree.focus()
            coffee_data = admin_tree.item(viewInfo)
            row = coffee_data['values']
            admin_id.set(row[0])
            admin_fullname.set(row[1])
            admin_username.set(row[2])
            admin_password.set(row[3])

        def add_admin():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO Admin_Account values(?,?,?,?)",
                        (admin_id.get(), admin_fullname.get(), admin_username.get(), admin_password.get()))
            conn.commit()
            conn.close()
            show_all_admin()
            clear_admin()
            messagebox.showinfo("Success", "Admin Records Added Successfully")

        def delete_admin():
            try:
                tree_view_content = admin_tree.focus()
                tree_view_items = admin_tree.item(tree_view_content)
                tree_view_values = tree_view_items['values'][1]
                ask = messagebox.askyesno("Warning",
                                          f"Are you sure you want to delete records of\n\n\t {tree_view_values}")
                if ask is True:
                    conn = sqlite3.connect("./Database/CoffeeShop.db")
                    cur = conn.cursor()
                    cur.execute("DELETE FROM Admin_Account where admin_id=?", admin_id.get())
                    conn.commit()
                    show_all_admin()
                    show_all_guest()
                    clear_admin()
                    conn.close()
                    messagebox.showinfo("Success",
                                        f" {tree_view_values} records has been deleted Successfully")
                else:
                    pass

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error",
                                     "There is some error deleting the data\n Make sure you have Selected the data")

        def update_admin():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute(
                "UPDATE Admin_Account set admin_fullname=?,admin_username=?,admin_password=? where "
                "admin_id=?",
                (admin_fullname.get(), admin_username.get(), admin_password.get(), admin_id.get()))
            conn.commit()
            conn.close()
            show_all_admin()
            clear_admin()
            messagebox.showinfo("Success", "Admin Records updated Successfully")

        def show_all_admin():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute("select * from Admin_Account")
            rows = cur.fetchall()
            if len(rows) != 0:
                admin_tree.delete(*admin_tree.get_children())
                for row in rows:
                    admin_tree.insert('', END, values=row)
                conn.commit()
            conn.close()

        scrollbarx = Scrollbar(account_window, orient=HORIZONTAL)
        scrollbary = Scrollbar(account_window, orient=VERTICAL)
        admin_tree = ttk.Treeview(account_window)
        admin_tree.place(relx=0.620, rely=0.425, width=480, height=350)
        admin_tree.configure(
            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set
        )
        admin_tree.configure(selectmode="extended")

        # self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        # self.tree.bind("<Double-1>", self.double_tap)

        scrollbary.configure(command=admin_tree.yview)
        scrollbarx.configure(command=admin_tree.xview)

        scrollbary.place(relx=0.972, rely=0.503, width=22, height=84)
        scrollbarx.place(relx=0.690, rely=0.938, width=84, height=22)

        admin_tree.configure(
            columns=(
                "AdminID",
                "AdminFullName",
                "AdminUserName",
                "AdminPassword",
            )
        )

        admin_tree.heading("AdminID", text="#", anchor=W)
        admin_tree.heading("AdminFullName", text="Admin Full Name", anchor=W)
        admin_tree.heading("AdminUserName", text="Username", anchor=W)
        admin_tree.heading("AdminPassword", text="Password", anchor=W)

        admin_tree.column("#0", stretch=NO, minwidth=0, width=0)
        admin_tree.column("#1", stretch=NO, minwidth=0, width=40)
        admin_tree.column("#2", stretch=NO, minwidth=0, width=210)
        admin_tree.column("#3", stretch=NO, minwidth=0, width=140)
        admin_tree.column("#4", stretch=NO, minwidth=0, width=200)
        show_all_admin()
        admin_tree.bind("<ButtonRelease-1>", admin_info)

        # ID NAME AND ENTRY
        idLabel = Label(account_window, text="ADMIN NUMBER", bg='#f6f6f9', font=("yu gothic ui", 12, "bold"))
        idLabel.place(relx=0.619, rely=0.099)

        idName_entry = Entry(account_window, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                             font=("", 11, 'bold'), textvariable=admin_id)
        idName_entry.place(relx=0.720, rely=0.099, width=65, height=30)
        idName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # COFFEE NAME AND ENTRY
        coffeeLabel = Label(account_window, text="ADMIN  FULL  NAME", bg='#f6f6f9',
                            font=("yu gothic ui", 12, "bold"))
        coffeeLabel.place(relx=0.639, rely=0.148)

        coffeeName_entry = Entry(account_window, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                 font=("", 12, 'bold'), textvariable=admin_fullname)
        coffeeName_entry.place(relx=0.619, rely=0.188, width=225, height=34)
        coffeeName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # COFFEE TYPE AND ENTRY
        typeLabel = Label(account_window, text="ADMIN  USERNAME", bg='#f6f6f9', font=("yu gothic ui", 12, "bold"))
        typeLabel.place(relx=0.639, rely=0.238)

        typeName_entry = Entry(account_window, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                               font=("", 12, 'bold'), textvariable=admin_username)
        typeName_entry.place(relx=0.619, rely=0.278, width=225, height=34)
        typeName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # COFFEE DISCOUNT AND ENTRY
        discountLabel = Label(account_window, text="ADMIN PASSWORD", bg='#f6f6f9', font=("yu gothic ui", 12, "bold"))
        discountLabel.place(relx=0.639, rely=0.328)

        discountName_entry = Entry(account_window, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                   font=("", 12, 'bold'), textvariable=admin_password)
        discountName_entry.place(relx=0.619, rely=0.368, width=225, height=34)
        discountName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        self.button3 = Button(account_window)
        self.button3.place(relx=0.846, rely=0.255, width=86, height=25)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#fd6a36")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#fd6a36")
        self.button3.configure(font="-family {Poppins SemiBold} -size 10")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Clear""")
        self.button3.configure(command=clear_admin)

        self.button4 = Button(account_window)
        self.button4.place(relx=0.846, rely=0.107, width=84, height=25)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#fd6a36")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#fd6a36")
        self.button4.configure(font="-family {Poppins SemiBold} -size 10")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Add""")
        self.button4.configure(command=add_admin)

        self.button5 = Button(account_window)
        self.button5.place(relx=0.846, rely=0.155, width=86, height=25)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#fd6a36")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#fd6a36")
        self.button5.configure(font="-family {Poppins SemiBold} -size 10")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""Update""")
        self.button5.configure(command=update_admin)

        self.button6 = Button(account_window)
        self.button6.place(relx=0.846, rely=0.205, width=86, height=25)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#fd6a36")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#fd6a36")
        self.button6.configure(font="-family {Poppins SemiBold} -size 10")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Delete""")
        self.button6.configure(command=delete_admin)

        self.button8 = Button(account_window)
        self.button8.place(relx=0.809, rely=0.309, width=202, height=25)
        self.button8.configure(relief="flat")
        self.button8.configure(overrelief="flat")
        self.button8.configure(activebackground="#fd6a36")
        self.button8.configure(cursor="hand2")
        self.button8.configure(foreground="#ffffff")
        self.button8.configure(background="#fd6a36")
        self.button8.configure(font="-family {Poppins SemiBold} -size 10")
        self.button8.configure(borderwidth="0")
        self.button8.configure(text="""Upgrade New Account to Admin""")
        self.button8.configure(command=upgrade_admin)

        self.button9 = Button(account_window)
        self.button9.place(relx=0.809, rely=0.365, width=202, height=25)
        self.button9.configure(relief="flat")
        self.button9.configure(overrelief="flat")
        self.button9.configure(activebackground="#fd6a36")
        self.button9.configure(cursor="hand2")
        self.button9.configure(foreground="#ffffff")
        self.button9.configure(background="#fd6a36")
        self.button9.configure(font="-family {Poppins SemiBold} -size 10")
        self.button9.configure(borderwidth="0")
        self.button9.configure(text="""Upgrade Employee to Admin""")
        self.button9.configure(command=upgrade_employee)






def page():
    window = Tk()
    InventoryPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()

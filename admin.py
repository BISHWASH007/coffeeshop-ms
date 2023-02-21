import sqlite3
import re
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
from PIL import ImageTk, Image
import os
import tempfile
import AccountSystem
import Accounts
import admin_start
import Inventory
# ============================================


class SecondPage:
    def __init__(self, manage_page):
        self.manage_page = manage_page

        # Window Size and Placement
        manage_page.rowconfigure(0, weight=1)
        manage_page.columnconfigure(0, weight=1)
        screen_width = manage_page.winfo_screenwidth()
        screen_height = manage_page.winfo_height()
        app_width = 1366
        app_height = 750
        x = (screen_width/2)-(app_width/2)
        y = (screen_height/160)-(app_height/160)
        manage_page.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        manage_page.title("Coffee Management System")

        user = StringVar()
        passwd = StringVar()
        fname = StringVar()
        lname = StringVar()
        new_user = StringVar()
        new_passwd = StringVar()

        cust_name = StringVar()
        cust_num = StringVar()
        cust_new_bill = StringVar()
        cust_search_bill = StringVar()
        bill_date = StringVar()

        with sqlite3.connect("./Database/CoffeeShop.db") as db:
            cur = db.cursor()

        def random_bill_number(stringLength):
            lettersAndDigits = string.ascii_letters.upper() + string.digits
            strr=''.join(random.choice(lettersAndDigits) for i in range(stringLength-2))
            return ('BB'+strr)

        def valid_phone(phn):
            if re.match(r"[789]\d{9}$", phn):
                return True
            return True

        def purchase_window(Event=None):
            manage_page.withdraw()
            global biller
            global page2
            biller = Toplevel()
            page2 = BillWindow(biller)
            page2.time()
            biller.protocol("WM_DELETE_WINDOW", exitt)
            biller.mainloop()

        def exitt():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=biller)
            if sure == True:
                biller.destroy()
                manage_page.destroy()

        def exitt2():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=manage_page)
            if sure == True:
                manage_page.destroy()

        manage_page.protocol("WM_DELETE_WINDOW", exitt2)

        def product_window(self):
            sure = messagebox.askyesno("Warning", "Data Which is not saved will be lost, \n Are you "
                                                  "sure you want to go back?", parent=biller)
            if sure == True:
                self.entry2.delete(0, END)
                self.entry3.delete(0, END)
                self.entry1.delete(0, END)
                biller.destroy()
                manage_page.deiconify()

        def back():
            sure = messagebox.askyesno("Warning", "Data Which is not saved will be lost, \n Are you "
                                                  "sure you want to go back?", parent=biller)
            if sure == True:
                biller.destroy()
                manage_page.deiconify()

        class Manage:
            def __init__(self, Manage_window):
                self.Manage_window = Manage_window

                # Window Size and Placement
                Manage_window.rowconfigure(0, weight=1)
                Manage_window.columnconfigure(0, weight=1)
                screen_width = Manage_window.winfo_screenwidth()
                screen_height = Manage_window.winfo_height()
                app_width = 1300
                app_height = 690
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 160) - (app_height / 160)
                Manage_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

                Manage_window.title("Coffee Management System")

                # window Icon
                icon = PhotoImage(file='images//CoffeeShop-brand-logo.png')
                Manage_window.iconphoto(True, icon)

                # Navigating through windows
                product_page = Frame(Manage_window)
                purchase_page = Frame(Manage_window)

                for frame in (product_page, purchase_page):
                    frame.grid(row=0, column=0, sticky='nsew')

                def show_frame(frame):
                    frame.tkraise()

                show_frame(product_page)

                # ======================================================================================
                # =================== HOME PAGE ========================================================
                # ======================================================================================
                product_page.config(background='#f6f6f9')

                coverFrame = Frame(product_page, bg='#ffffff')
                coverFrame.place(x=315, y=80, width=1055, height=630)

                topFrame = LabelFrame(coverFrame, bg='#f1f1f1', bd='2.4')
                topFrame.place(x=53, y=106, width=897, height=40)

                # coverFrame_line = Canvas(coverFrame, width=1055, height=1.5, bg="#108cff", highlightthickness=0)
                # coverFrame_line.place(x=0, y=130)

                coverFrame2 = Frame(product_page, bg='#ffffff')
                coverFrame2.place(x=0, y=80, width=290, height=630)

                # ====== MENU BAR ==========
                logoIcon = Image.open('images//CoffeeShop-brand-logo.png')
                photo = ImageTk.PhotoImage(logoIcon)
                logo = Label(product_page, image=photo, bg='#f6f6f9')
                logo.image = photo
                logo.place(x=0, y=0)

                menuBar_line = Canvas(product_page, width=1500, height=1.5, bg="#e6e6e6", highlightthickness=0)
                menuBar_line.place(x=0, y=60)

                admIcon = Image.open('images//feeling.png')
                photo = ImageTk.PhotoImage(admIcon)
                adm = Label(product_page, image=photo, bg='#f6f6f9')
                adm.image = photo
                adm.place(x=1250, y=5)

                admLabel = Label(product_page, text='ADMIN', font=('yu gothic ui', 18, 'bold'), fg='#ffc329', bg='#f6f6f9')
                admLabel.place(x=1160, y=11)

                # ========== HOME BUTTON =======
                home_button = Button(product_page, text='Home', bg='#f6f6f9', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                                     cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                     command=lambda: home())
                home_button.place(x=70, y=15)

                def home():
                    win = Toplevel()
                    admin_start.FirstPage(win)
                    Manage_window.withdraw()
                    win.deiconify()

                # ========== MANAGE BUTTON =======
                manage_button = Button(product_page, text='Manage', bg='#fd6a36', font=("", 13, "bold"), bd=0,
                                       fg='#ffffff',
                                       cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a')
                manage_button.place(x=150, y=15)

                # ========== PRODUCTS BUTTON =======
                product_button = Button(product_page, text='Products', bg='#f6f6f9', font=("", 13, "bold"), bd=0,
                                        fg='#7a7a7a',
                                        cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                        command=lambda: product())
                product_button.place(x=250, y=15)


                def logout():
                    win = Toplevel()
                    AccountSystem.AccountPage(win)
                    Manage_window.withdraw()
                    win.deiconify()

                # ========== LOG OUT =======
                logout_button = Button(product_page, text='Logout', bg='#f6f6f9', font=("", 13, "bold"), bd=0,
                                       fg='#7a7a7a',
                                       cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                       command=logout)
                logout_button.place(x=420, y=15)

                def product():
                    Manage_window.withdraw()
                    os.system("python admin.py")
                    Manage_window.destroy()

                def exit():
                    exit_command = messagebox.askyesno("Edit Teacher Records", "Are you sure you want to exit")
                    if exit_command > 0:
                        manage_page.destroy()

                self.button6 = Button(product_page)
                self.button6.place(relx=0.762, rely=0.022, width=86, height=25)
                self.button6.configure(relief="flat")
                self.button6.configure(overrelief="flat")
                self.button6.configure(activebackground="#fd6a36")
                self.button6.configure(cursor="hand2")
                self.button6.configure(foreground="#ffffff")
                self.button6.configure(background="#fd6a36")
                self.button6.configure(font="-family {Poppins SemiBold} -size 10")
                self.button6.configure(borderwidth="0")
                self.button6.configure(text="""Exit""")
                self.button6.configure(command=exit)

                # Manage Coffee Label
                manageCoffee = Label(coverFrame2, text='MANAGE COFFEE', font=("yu gothic ui", 13, "bold"), bg='#ffffff',
                                     fg='#ff6c38')
                manageCoffee.place(x=80, y=0)

                coverFrame3 = LabelFrame(coverFrame2, bg='#ffffff', bd='2.4')
                coverFrame3.place(x=20, y=80, width=250, height=475)

                # Coffee Image
                coffeeImage = Image.open('images//menu-6.png')
                photo = ImageTk.PhotoImage(coffeeImage)
                coffeeImg = Label(coverFrame2, image=photo, bg='#ffffff')
                coffeeImg.image = photo
                coffeeImg.place(x=100, y=35)

                coffee = StringVar()
                type = StringVar()
                discount = StringVar()
                in_stock = StringVar()
                price = StringVar()
                coffee_id = StringVar()

                # ID NAME AND ENTRY
                idLabel = Label(coverFrame3, text="#", bg='#ffffff', font=("yu gothic ui", 13, "bold"))
                idLabel.place(x=5, y=41)

                idName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                         font=("", 11, 'bold'), textvariable=coffee_id)
                idName_entry.place(x=22, y=44, width=40, height=24)
                idName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

                # COFFEE NAME AND ENTRY
                coffeeLabel = Label(coverFrame3, text="COFFEE", bg='#ffffff', font=("yu gothic ui", 12, "bold"))
                coffeeLabel.place(x=90, y=40)

                coffeeName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                         font=("", 12, 'bold'), textvariable=coffee)
                coffeeName_entry.place(x=10, y=70, width=225, height=34)
                coffeeName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

                # COFFEE TYPE AND ENTRY
                typeLabel = Label(coverFrame3, text="TYPE", bg='#ffffff', font=("yu gothic ui", 12, "bold"))
                typeLabel.place(x=90, y=105)

                typeName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                       font=("", 12, 'bold'), textvariable=type)
                typeName_entry.place(x=10, y=135, width=225, height=34)
                typeName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

                # COFFEE DISCOUNT AND ENTRY
                discountLabel = Label(coverFrame3, text="DISCOUNT", bg='#ffffff', font=("yu gothic ui", 12, "bold"))
                discountLabel.place(x=90, y=170)

                discountName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                         font=("", 12, 'bold'), textvariable=discount)
                discountName_entry.place(x=10, y=200, width=225, height=34)
                discountName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

                # IN STOCK AND ENTRY
                inStockLabel = Label(coverFrame3, text="IN STOCK", bg='#ffffff', font=("yu gothic ui", 12, "bold"))
                inStockLabel.place(x=90, y=240)

                inStock_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                      font=("", 12, 'bold'), textvariable=in_stock)
                inStock_entry.place(x=10, y=270, width=225, height=34)
                inStock_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

                # PRICE AND ENTRY
                priceLabel = Label(coverFrame3, text="PRICE", bg='#ffffff', font=("yu gothic ui", 12, "bold"))
                priceLabel.place(x=90, y=310)

                price_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                    font=("", 12, 'bold'), textvariable=price)
                price_entry.place(x=80, y=340, width=100, height=34)
                price_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

                currencyLabel = Label(coverFrame3, text="$", bg='#ffffff', font=("yu gothic ui", 34, "bold"))
                currencyLabel.place(x=45, y=320)

                # =====================================================================================================================
                #                TKINTER     TREE VIEW
                # =====================================================================================================================
                def show_all():
                    conn = sqlite3.connect("./Database/CoffeeShop.db")
                    cur = conn.cursor()
                    cur.execute("select * from Coffee_Category")
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        coffee_tree.delete(*coffee_tree.get_children())
                        for row in rows:
                            coffee_tree.insert('', END, values=row)
                        conn.commit()
                    conn.close()

                    # ======== Fetch =========

                def coffee_info(ev):
                    viewInfo = coffee_tree.focus()
                    coffee_data = coffee_tree.item(viewInfo)
                    row = coffee_data['values']
                    coffee_id.set(row[0])
                    coffee.set(row[1])
                    type.set(row[2])
                    discount.set(row[3])
                    in_stock.set(row[4])
                    price.set(row[5])

                def add_coffee():
                    if coffee_id.get() == "":
                        messagebox.showerror("Failed", "Coffee Number( # ) can't be empty")
                    else:
                        conn = sqlite3.connect("./Database/CoffeeShop.db")
                        cur = conn.cursor()
                        cur.execute("INSERT INTO Coffee_Category values(?,?,?,?,?,?)",
                                    (coffee_id.get(), coffee.get(), type.get(), discount.get(), in_stock.get(), price.get()))
                        conn.commit()
                        conn.close()
                        show_all()
                        messagebox.showinfo("Success", "Coffee Records Added Successfully")

                def delete_records():
                    try:
                        tree_view_content = coffee_tree.focus()
                        tree_view_items = coffee_tree.item(tree_view_content)
                        tree_view_values = tree_view_items['values'][1]
                        ask = messagebox.askyesno("Warning",
                                                  f"Are you sure you want to delete records of {tree_view_values}")
                        if ask is True:
                            conn = sqlite3.connect("./Database/CoffeeShop.db")
                            cur = conn.cursor()
                            cur.execute("DELETE FROM Coffee_Category where coffee_id=?", [coffee_id.get()])
                            conn.commit()
                            show_all()
                            clear_all()
                            conn.close()
                            messagebox.showinfo("Success",
                                                f" {tree_view_values} records has been deleted Successfully")
                        else:
                            pass

                    except BaseException as msg:
                        print(msg)
                        messagebox.showerror("Error",
                                             "There is some error deleting the data\n Make sure you have Selected the data")

                def update():
                    conn = sqlite3.connect("./Database/CoffeeShop.db")
                    cur = conn.cursor()
                    cur.execute(
                        "UPDATE Coffee_Category set coffee_name=?,type=?,discount=?,in_stock=?,coffee_price=? where "
                        "coffee_id=?",
                        (coffee.get(), type.get(), discount.get(), in_stock.get(), price.get(), coffee_id.get()))
                    conn.commit()
                    conn.close()
                    show_all()
                    # self.Reset()
                    messagebox.showinfo("Success", "Coffee Record updated Successfully")

                self.button3 = Button(coverFrame3)
                self.button3.place(relx=0.539, rely=0.849, width=86, height=25)
                self.button3.configure(relief="flat")
                self.button3.configure(overrelief="flat")
                self.button3.configure(activebackground="#fd6a36")
                self.button3.configure(cursor="hand2")
                self.button3.configure(foreground="#ffffff")
                self.button3.configure(background="#fd6a36")
                self.button3.configure(font="-family {Poppins SemiBold} -size 10")
                self.button3.configure(borderwidth="0")
                self.button3.configure(text="""Delete""")
                self.button3.configure(command=delete_records)

                self.button4 = Button(coverFrame3)
                self.button4.place(relx=0.059, rely=0.849, width=84, height=25)
                self.button4.configure(relief="flat")
                self.button4.configure(overrelief="flat")
                self.button4.configure(activebackground="#fd6a36")
                self.button4.configure(cursor="hand2")
                self.button4.configure(foreground="#ffffff")
                self.button4.configure(background="#fd6a36")
                self.button4.configure(font="-family {Poppins SemiBold} -size 10")
                self.button4.configure(borderwidth="0")
                self.button4.configure(text="""Add""")
                self.button4.configure(command=add_coffee)

                self.button5 = Button(coverFrame3)
                self.button5.place(relx=0.059, rely=0.929, width=86, height=25)
                self.button5.configure(relief="flat")
                self.button5.configure(overrelief="flat")
                self.button5.configure(activebackground="#fd6a36")
                self.button5.configure(cursor="hand2")
                self.button5.configure(foreground="#ffffff")
                self.button5.configure(background="#fd6a36")
                self.button5.configure(font="-family {Poppins SemiBold} -size 10")
                self.button5.configure(borderwidth="0")
                self.button5.configure(text="""Update""")
                self.button5.configure(command=update)

                def clear_all():
                    coffee_id.set("")
                    coffee.set("")
                    type.set("")
                    discount.set("")
                    in_stock.set("")
                    price.set("")

                self.button6 = Button(coverFrame3)
                self.button6.place(relx=0.539, rely=0.929, width=86, height=25)
                self.button6.configure(relief="flat")
                self.button6.configure(overrelief="flat")
                self.button6.configure(activebackground="#fd6a36")
                self.button6.configure(cursor="hand2")
                self.button6.configure(foreground="#ffffff")
                self.button6.configure(background="#fd6a36")
                self.button6.configure(font="-family {Poppins SemiBold} -size 10")
                self.button6.configure(borderwidth="0")
                self.button6.configure(text="""Clear""")
                self.button6.configure(command=clear_all)

                # PURCHASE BUTTON
                purchaseFrame = LabelFrame(coverFrame, bg='#ffffff', bd='2.4')
                purchaseFrame.place(x=200, y=10, width=100, height=80)

                purchaseLabel = Label(purchaseFrame, text="Purchase", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
                purchaseLabel.place(x=10, y=0)

                purchaseIcon = Image.open('images//marketplace.png')
                photo = ImageTk.PhotoImage(purchaseIcon)
                purchase = Button(purchaseFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                                  activebackground="#ffffff", command=lambda: purchase_window())
                purchase.image = photo
                purchase.place(x=0, y=22)

                # PRODUCTS BUTTON
                productsFrame = LabelFrame(coverFrame, bg='#ffffff', bd='2.4')
                productsFrame.place(x=50, y=10, width=100, height=80)

                productsLabel = Label(productsFrame, text="Products", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
                productsLabel.place(x=10, y=0)

                productsIcon = Image.open('images//shopping-bag.png')
                photo = ImageTk.PhotoImage(productsIcon)
                products = Button(productsFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                                  activebackground="#ffffff")
                products.image = photo
                products.place(x=0, y=22)

                # BILL BUTTON

                def bill():
                    win = Toplevel()
                    Inventory.InventoryPage(win)
                    Manage_window.withdraw()
                    win.deiconify()

                billFrame = LabelFrame(coverFrame, bg='#ffffff', bd='2.4')
                billFrame.place(x=350, y=10, width=100, height=80)

                billLabel = Label(billFrame, text="   Bill", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
                billLabel.place(x=10, y=0)

                billIcon = Image.open('images//bill.png')
                photo = ImageTk.PhotoImage(billIcon)
                bill = Button(billFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                              activebackground="#ffffff", command=bill)
                bill.image = photo
                bill.place(x=0, y=22)

                # ACCOUNTS BUTTON

                def accounts():
                    win = Toplevel()
                    Accounts.InventoryPage(win)
                    Manage_window.withdraw()
                    win.deiconify()

                accountsFrame = LabelFrame(coverFrame, bg='#ffffff', bd='2.4')
                accountsFrame.place(x=500, y=10, width=100, height=80)

                accountsLabel = Label(accountsFrame, text="Accounts", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
                accountsLabel.place(x=10, y=0)

                accountsIcon = Image.open('images//accounts_icon.png')
                photo = ImageTk.PhotoImage(accountsIcon)
                accounts = Button(accountsFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                                  activebackground="#ffffff", command=accounts)
                accounts.image = photo
                accounts.place(x=0, y=22)

                style = ttk.Style()
                style.theme_use("clam")
                scrollbarx = Scrollbar(product_page, orient=HORIZONTAL)
                scrollbary = Scrollbar(product_page, orient=VERTICAL)
                coffee_tree = ttk.Treeview(coverFrame)
                coffee_tree.place(relx=0.0500, rely=0.228, width=896, height=410)
                coffee_tree.configure(
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set
                )
                coffee_tree.configure(selectmode="extended")

                scrollbary.configure(command=coffee_tree.yview)
                scrollbarx.configure(command=coffee_tree.xview)

                scrollbary.place(relx=0.976, rely=0.323, width=25, height=412)
                scrollbarx.place(relx=0.242, rely=0.979, width=1015, height=15)

                coffee_tree.configure(
                    columns=(
                        "CoffeeID",
                        "CoffeeName",
                        "Type",
                        "Discount",
                        "InStock",
                        "Price"
                    )
                )

                coffee_tree.heading("CoffeeID", text="#", anchor=N)
                coffee_tree.heading("CoffeeName", text="COFFEE", anchor=N)
                coffee_tree.heading("Type", text="TYPE", anchor=N)
                coffee_tree.heading("Discount", text="DISCOUNT", anchor=N)
                coffee_tree.heading("InStock", text="IN STOCK", anchor=N)
                coffee_tree.heading("Price", text="PRICE", anchor=N)

                coffee_tree.column("#0", stretch=NO, minwidth=0, width=0)
                coffee_tree.column("#1", stretch=NO, minwidth=0, width=50, anchor=N)
                coffee_tree.column("#2", stretch=NO, minwidth=0, width=288, anchor=N)
                coffee_tree.column("#3", stretch=NO, minwidth=0, width=176, anchor=N)
                coffee_tree.column("#4", stretch=NO, minwidth=0, width=110, anchor=N)
                coffee_tree.column("#5", stretch=NO, minwidth=0, width=110, anchor=N)
                coffee_tree.column("#6", stretch=NO, minwidth=0, width=160, anchor=N)
                coffee_tree.bind("<ButtonRelease-1>", coffee_info)
                show_all()




                # ============ LINES ================================
                design_line = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line.place(x=53, y=168)

                design_line2 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line2.place(x=53, y=188)

                design_line3 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line3.place(x=53, y=208)

                design_line4 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line4.place(x=53, y=228)

                design_line5 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line5.place(x=53, y=248)

                design_line6 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line6.place(x=53, y=268)

                design_line7 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line7.place(x=53, y=288)

                design_line8 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line8.place(x=53, y=308)

                design_line9 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line9.place(x=53, y=328)

                design_line10 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line10.place(x=53, y=348)

                design_line11 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line11.place(x=53, y=368)

                design_line12 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line12.place(x=53, y=388)

                design_line13 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line13.place(x=53, y=408)

                design_line14 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line14.place(x=53, y=428)

                design_line15 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line15.place(x=53, y=448)

                design_line16 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line16.place(x=53, y=468)

                design_line17 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line17.place(x=53, y=488)

                design_line18 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line18.place(x=53, y=508)

                design_line19 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line19.place(x=53, y=528)

                # ===================================================================================================
                # ================================ PURCHASE PAGE ====================================================
                # ===================================================================================================


        class CoffeeItem:
            def __init__(self, coffee, price, qty):
                self.product_name = coffee
                self.price = price
                self.qty = qty

        class Cart:
            def __init__(self):
                self.items = []
                self.dictionary = {}

            def add_item(self, item):
                self.items.append(item)

            def remove_item(self):
                self.items.pop()

            def remove_items(self):
                self.items.clear()

            def total(self):
                total = 0.0
                for i in self.items:
                    total += i.price * i.qty
                return total

            def isEmpty(self):
                if len(self.items) == 0:
                    return True

            def allCart(self):
                for i in self.items:
                    if (i.product_name in self.dictionary):
                        self.dictionary[i.product_name] += i.qty
                    else:
                        self.dictionary.update({i.product_name:i.qty})

        class BillWindow:
            def __init__(self, top=None):
                top.geometry("1350x768")
                top.resizable(0, 0)
                top.title("Billing Management")
                top.config(background='#f6f6f9')

                logoIcon = Image.open('images//CoffeeShop-brand-logo.png')
                photo = ImageTk.PhotoImage(logoIcon)
                logo = Label(biller, image=photo, bg='#f6f6f9')
                logo.image = photo
                logo.place(x=5, y=0)

                menuBar_line = Canvas(biller, width=1500, height=1.5, bg="#e6e6e6", highlightthickness=0)
                menuBar_line.place(x=0, y=60)

                admIcon = Image.open('images//feeling.png')
                photo = ImageTk.PhotoImage(admIcon)
                adm = Label(biller, image=photo, bg='#f6f6f9')
                adm.image = photo
                adm.place(x=1300, y=5)

                admLabel = Label(biller, text='ADMIN', font=('yu gothic ui', 18, 'bold'), fg='#ffc329', bg='#f6f6f9')
                admLabel.place(x=1210, y=11)

                # ========== HOME BUTTON =======
                home_button = Button(biller, text='Home', bg='#f6f6f9', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                                     cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                     command=lambda: home())
                home_button.place(x=70, y=15)

                def home():
                    biller.withdraw()
                    os.system("python admin_start.py")
                    biller.destroy()

                # ========== MANAGE BUTTON =======
                manage_button = Button(biller, text='Manage', bg='#fd6a36', font=("", 13, "bold"), bd=0,
                                       fg='#ffffff',
                                       cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a')
                manage_button.place(x=150, y=15)

                # ========== PRODUCTS BUTTON =======
                product_button = Button(biller, text='Products', bg='#f6f6f9', font=("", 13, "bold"), bd=0,
                                        fg='#7a7a7a',
                                        cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                        command=lambda: product())
                product_button.place(x=250, y=15)

                # ========== HELP BUTTON =======


                def logout():
                    biller.withdraw()
                    os.system("python AccountSystem.py")
                    biller.destroy()

                # ========== LOG OUT =======
                logout_button = Button(biller, text='Logout', bg='#f6f6f9', font=("", 13, "bold"), bd=0,
                                       fg='#7a7a7a',
                                       cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                       command=logout)
                logout_button.place(x=420, y=15)

                def product():
                    biller.withdraw()
                    os.system("python admin.py")
                    biller.destroy()

                # PURCHASE BUTTON
                purchaseFrame = LabelFrame(biller, bg='#ffffff', bd='2.4')
                purchaseFrame.place(x=670, y=80, width=100, height=80)

                purchaseLabel = Label(purchaseFrame, text="Purchase", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
                purchaseLabel.place(x=10, y=0)

                purchaseIcon = Image.open('images//marketplace.png')
                photo = ImageTk.PhotoImage(purchaseIcon)
                purchase = Button(purchaseFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                                  activebackground="#ffffff", command=product)
                purchase.image = photo
                purchase.place(x=0, y=22)

                # PRODUCTS BUTTON
                productsFrame = LabelFrame(biller, bg='#ffffff', bd='2.4')
                productsFrame.place(x=820, y=80, width=100, height=80)

                productsLabel = Label(productsFrame, text="Products", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
                productsLabel.place(x=10, y=0)

                productsIcon = Image.open('images//shopping-bag.png')
                photo = ImageTk.PhotoImage(productsIcon)
                products = Button(productsFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                                  activebackground="#ffffff", command=product)
                products.image = photo
                products.place(x=0, y=22)

                def bill():
                    win = Toplevel()
                    Inventory.InventoryPage(win)
                    biller.withdraw()
                    win.deiconify()

                def account():
                    win = Toplevel()
                    Accounts.InventoryPage(win)
                    biller.withdraw()
                    win.deiconify()

                # BILL BUTTON
                billFrame = LabelFrame(biller, bg='#ffffff', bd='2.4')
                billFrame.place(x=970, y=80, width=100, height=80)

                billLabel = Label(billFrame, text="   Bill", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
                billLabel.place(x=10, y=0)

                billIcon = Image.open('images//bill.png')
                photo = ImageTk.PhotoImage(billIcon)
                bill = Button(billFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                              activebackground="#ffffff", command=bill)
                bill.image = photo
                bill.place(x=0, y=22)

                # ACCOUNTS BUTTON
                accountsFrame = LabelFrame(biller, bg='#ffffff', bd='2.4')
                accountsFrame.place(x=1120, y=80, width=100, height=80)

                accountsLabel = Label(accountsFrame, text="Accounts", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
                accountsLabel.place(x=10, y=0)

                accountsIcon = Image.open('images//accounts_icon.png')
                photo = ImageTk.PhotoImage(accountsIcon)
                accounts = Button(accountsFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                                  activebackground="#ffffff", command=account)
                accounts.image = photo
                accounts.place(x=0, y=22)

                self.coverFrame2 = Frame(biller, bg='#ffffff')
                self.coverFrame2.place(x=0, y=80, width=575, height=645)

                self.coverFrame3 = LabelFrame(self.coverFrame2, bg='#ffffff', bd='2.4')
                self.coverFrame3.place(x=20, y=90, width=535, height=475)

                self.coffeeImage = Image.open('images//menu-6.png')
                photo = ImageTk.PhotoImage(self.coffeeImage)
                self.coffeeImg = Label(self.coverFrame2, image=photo, bg='#ffffff')
                self.coffeeImg.image = photo
                self.coffeeImg.place(x=220, y=30)

                self.coverFrame4 = LabelFrame(self.coverFrame2, bg='#ffffff', bd='2.4')
                self.coverFrame4.place(x=20, y=570, width=535, height=75)

                #
                self.coverFrame5 = Frame(biller, bg='#ffffff')
                self.coverFrame5.place(x=1070, y=235, width=275, height=490)

                self.coverFrame6 = LabelFrame(self.coverFrame5, bg='#ffffff', bd='2.4')
                self.coverFrame6.place(x=10, y=10, width=255, height=475)

                self.genBill_no = Label(self.coverFrame6, text='Bill Number', font=("yu gothic ui", 10, "bold"),
                                        bg='#ffffff', fg='#000000')
                self.genBill_no.place(relx=0.180, rely=0.056)

                self.genCashier_name = Label(self.coverFrame6, text='Cashier Name', font=("yu gothic ui", 10, "bold"),
                                             bg='#ffffff', fg='#000000')
                self.genCashier_name.place(relx=0.200, rely=0.680)

                self.genBill_date = Label(self.coverFrame6, text='Bill Date', font=("yu gothic ui", 10, "bold"),
                                          bg='#ffffff', fg='#000000')
                self.genBill_date.place(relx=0.180, rely=0.256)

                self.genCom_number = Label(self.coverFrame6, text='Company Number', font=("yu gothic ui", 10, "bold"),
                                          bg='#ffffff', fg='#000000')
                self.genCom_number.place(relx=0.180, rely=0.456)

                self.clock = Label(biller)
                self.clock.place(relx=0, rely=0.105, width=102, height=36)
                self.clock.configure(font="-family {Poppins Light} -size 12")
                self.clock.configure(foreground="#000000")
                self.clock.configure(background="#ffffff")

                self.quantity = Label(biller)
                self.quantity.place(x=45, y=484)
                self.quantity.configure(font="-family {Poppins Light} -size 11")
                self.quantity.configure(foreground="#000000")
                self.quantity.configure(text="Quantity")
                self.quantity.configure(background="#ffffff")

                self.coffee_name = Label(biller)
                self.coffee_name.place(x=45, y=430)
                self.coffee_name.configure(font="-family {Poppins Light} -size 11")
                self.coffee_name.configure(foreground="#000000")
                self.coffee_name.configure(text="Coffee Name")
                self.coffee_name.configure(background="#ffffff")

                self.discount = Label(biller)
                self.discount.place(x=45, y=374)
                self.discount.configure(font="-family {Poppins Light} -size 11")
                self.discount.configure(foreground="#000000")
                self.discount.configure(text="Discount ( % )")
                self.discount.configure(background="#ffffff")

                self.payment_method = Label(biller)
                self.payment_method.place(x=45, y=313)
                self.payment_method.configure(font="-family {Poppins Light} -size 11")
                self.payment_method.configure(foreground="#000000")
                self.payment_method.configure(text="Bill Type")
                self.payment_method.configure(background="#ffffff")

                self.company_number = Label(biller)
                self.company_number.place(x=45, y=258)
                self.company_number.configure(font="-family {Poppins Light} -size 11")
                self.company_number.configure(foreground="#000000")
                self.company_number.configure(text="Company Number")
                self.company_number.configure(background="#ffffff")

                self.cashier_name = Label(biller)
                self.cashier_name.place(x=45, y=205)
                self.cashier_name.configure(font="-family {Poppins Light} -size 11")
                self.cashier_name.configure(foreground="#000000")
                self.cashier_name.configure(text="Cashier Fullname")
                self.cashier_name.configure(background="#ffffff")

                self.entry1 = ttk.Entry(biller)
                self.entry1.place(relx=0.035, rely=0.300, width=477, height=24)
                self.entry1.configure(font="-family {Poppins} -size 12")
                self.entry1.configure(textvariable=cust_name)

                self.entry2 = ttk.Entry(biller)
                self.entry2.place(relx=0.035, rely=0.368, width=477, height=24)
                self.entry2.configure(font="-family {Poppins} -size 10")
                self.entry2.configure(textvariable=cust_num)
                self.companyNumber_txt = str(8798236784)
                self.entry2.insert(0, self.companyNumber_txt)

                self.entry3 = Entry(biller, highlightthickness=2)
                self.entry3.place(relx=0.402, rely=0.019, width=350, height=29)
                self.entry3.configure(font="-family {Poppins} -size 11")
                self.entry3.configure(relief="flat")
                self.entry3.configure(highlightbackground="#6b6a69", highlightcolor="#fd6a36")
                self.entry3.configure(textvariable=cust_search_bill)
                self.search_txt = "Enter Bill Number to Search............"
                self.entry3.insert(0, self.search_txt)
                self.entry3.bind("<1>", self.clear_search)

                searchIcon = Image.open('images//search.png')
                photo = ImageTk.PhotoImage(searchIcon)
                search = Label(biller, image=photo, bg='#f6f6f9')
                search.image = photo
                search.place(relx=0.378, rely=0.019)

                self.button2 = Button(biller)
                self.button2.place(relx=0.660, rely=0.019, width=76, height=29)
                self.button2.configure(relief="flat")
                self.button2.configure(overrelief="flat")
                self.button2.configure(activebackground="#fd6a36")
                self.button2.configure(cursor="hand2")
                self.button2.configure(foreground="#ffffff")
                self.button2.configure(background="#fd6a36")
                self.button2.configure(font="-family {Poppins SemiBold} -size 12")
                self.button2.configure(borderwidth="0")
                self.button2.configure(text="""Search""")
                self.button2.configure(command=self.search_bill)

                self.button3 = Button(biller)
                self.button3.place(relx=0.048, rely=0.869, width=86, height=25)
                self.button3.configure(relief="flat")
                self.button3.configure(overrelief="flat")
                self.button3.configure(activebackground="#fd6a36")
                self.button3.configure(cursor="hand2")
                self.button3.configure(foreground="#ffffff")
                self.button3.configure(background="#fd6a36")
                self.button3.configure(font="-family {Poppins SemiBold} -size 10")
                self.button3.configure(borderwidth="0")
                self.button3.configure(text="""Total""")
                self.button3.configure(command=self.total_bill)

                self.button4 = Button(biller)
                self.button4.place(relx=0.141, rely=0.869, width=84, height=25)
                self.button4.configure(relief="flat")
                self.button4.configure(overrelief="flat")
                self.button4.configure(activebackground="#fd6a36")
                self.button4.configure(cursor="hand2")
                self.button4.configure(foreground="#ffffff")
                self.button4.configure(background="#fd6a36")
                self.button4.configure(font="-family {Poppins SemiBold} -size 10")
                self.button4.configure(borderwidth="0")
                self.button4.configure(text="""Generate""")
                self.button4.configure(command=self.gen_bill)

                self.button5 = Button(biller)
                self.button5.place(relx=0.230, rely=0.869, width=86, height=25)
                self.button5.configure(relief="flat")
                self.button5.configure(overrelief="flat")
                self.button5.configure(activebackground="#fd6a36")
                self.button5.configure(cursor="hand2")
                self.button5.configure(foreground="#ffffff")
                self.button5.configure(background="#fd6a36")
                self.button5.configure(font="-family {Poppins SemiBold} -size 10")
                self.button5.configure(borderwidth="0")
                self.button5.configure(text="""Clear""")
                self.button5.configure(command=self.clear_bill)

                def exit_command():
                    exit_command = messagebox.askyesno("Exit", "Are you sure you want to exit")
                    if exit_command > 0:
                        biller.destroy()
                        manage_page.destroy()

                self.button6 = Button(biller)
                self.button6.place(relx=0.762, rely=0.022, width=86, height=25)
                self.button6.configure(relief="flat")
                self.button6.configure(overrelief="flat")
                self.button6.configure(activebackground="#fd6a36")
                self.button6.configure(cursor="hand2")
                self.button6.configure(foreground="#ffffff")
                self.button6.configure(background="#fd6a36")
                self.button6.configure(font="-family {Poppins SemiBold} -size 10")
                self.button6.configure(borderwidth="0")
                self.button6.configure(text="""Exit""")
                self.button6.configure(command=exit_command)

                self.button7 = Button(biller)
                self.button7.place(relx=0.098, rely=0.784, width=86, height=26)
                self.button7.configure(relief="flat")
                self.button7.configure(overrelief="flat")
                self.button7.configure(activebackground="#fd6a36")
                self.button7.configure(cursor="hand2")
                self.button7.configure(foreground="#ffffff")
                self.button7.configure(background="#fd6a36")
                self.button7.configure(font="-family {Poppins SemiBold} -size 10")
                self.button7.configure(borderwidth="0")
                self.button7.configure(text="""Add To Cart""")
                self.button7.configure(command=self.add_to_cart)

                self.button8 = Button(biller)
                self.button8.place(relx=0.274, rely=0.784, width=84, height=26)
                self.button8.configure(relief="flat")
                self.button8.configure(overrelief="flat")
                self.button8.configure(activebackground="#fd6a36")
                self.button8.configure(cursor="hand2")
                self.button8.configure(foreground="#ffffff")
                self.button8.configure(background="#fd6a36")
                self.button8.configure(font="-family {Poppins SemiBold} -size 10")
                self.button8.configure(borderwidth="0")
                self.button8.configure(text="""Clear""")
                self.button8.configure(command=self.clear_selection)

                self.button9 = Button(biller)
                self.button9.place(relx=0.194, rely=0.784, width=68, height=26)
                self.button9.configure(relief="flat")
                self.button9.configure(overrelief="flat")
                self.button9.configure(activebackground="#fd6a36")
                self.button9.configure(cursor="hand2")
                self.button9.configure(foreground="#ffffff")
                self.button9.configure(background="#fd6a36")
                self.button9.configure(font="-family {Poppins SemiBold} -size 10")
                self.button9.configure(borderwidth="0")
                self.button9.configure(text="""Remove""")
                self.button9.configure(command=self.remove_product)

                text_font = ("Poppins", "9")
                style = ttk.Style()
                style.theme_use("clam")
                self.combo1 = ttk.Combobox(biller)
                self.combo1.place(relx=0.035, rely=0.440, width=477, height=26)

                find_category = "SELECT type FROM Coffee_Category"
                cur.execute(find_category)
                result1 = cur.fetchall()
                cat = []
                for i in range(len(result1)):
                    if (result1[i][0] not in cat):
                        cat.append(result1[i][0])

                self.combo1.configure(values=cat)
                self.combo1.configure(state="readonly")
                self.combo1.configure(font="-family {Poppins SemiBold} -size 9")
                self.combo1.option_add("*TCombobox*Listbox.font", text_font)
                self.combo1.option_add("*TCombobox*Listbox.selectBackground", "#fd6a36")
                #self.combo1.bind('<1>', self.entry1)

                self.combo2 = ttk.Combobox(biller)
                self.combo2.place(relx=0.035, rely=0.520, width=477, height=26)
                self.combo2.configure(font="-family {Poppins SemiBold} -size 9")
                self.combo2.option_add("*TCombobox*Listbox.font", text_font)
                self.combo2.configure(state="disabled")

                self.combo3 = ttk.Combobox(biller)
                self.combo3.place(relx=0.035, rely=0.590, width=477, height=26)
                self.combo3.configure(state="disabled")
                self.combo3.configure(font="-family {Poppins SemiBold} -size 9")
                self.combo3.option_add("*TCombobox*Listbox.font", text_font)

                self.entry4 = ttk.Entry(biller)
                self.entry4.place(relx=0.035, rely=0.660, width=477, height=26)
                self.entry4.configure(font="-family {Poppins SemiBold} -size 9")
                self.entry4.configure(foreground="#108cff")
                self.entry4.configure(state="disabled")

                self.Scrolledtext1 = tkst.ScrolledText(top)
                self.Scrolledtext1.place(relx=0.439, rely=0.306, width=450, height=490)
                self.Scrolledtext1.configure(borderwidth=0)
                self.Scrolledtext1.configure(font="-family {Podkova} -size 9")
                self.Scrolledtext1.configure(state="normal")
                head = "\n\n\t\t GIDEONS COFFEE SHOP\n" \
                       "\t\t C12 TEMA GHANA\n\n\t\t THANK YOU FOR CHOOSING OUR COFFEE\n" \
                       "\t\t WE HOPE TO SEE YOU NEXT TIME\n\n\n" + "\tCOFFEE\t  -----  \tQUANTITY\t  -----  \tPRICE ( $ )\n"
                self.Scrolledtext1.insert('insert', head)

                self.combo1.bind("<<ComboboxSelected>>", self.get_category)

                btn_print = Button(top, text="""Print""", command=lambda: print_area(self.Scrolledtext1.get('1.0', END)),
                                   overrelief="flat", bd=0, foreground="#ffffff", relief="flat", cursor="hand2",
                                   font="-family {Poppins SemiBold} -size 10", bg='#ff6c38', activebackground="#ff6c38")
                btn_print.place(relx=0.322, rely=0.868, width=86, height=25)

                def print_area(txt):
                    temp_file = tempfile.mktemp('.txt')
                    open(temp_file, 'w').write(txt)
                    os.startfile(temp_file, 'print')

            def get_category(self, Event):
                self.combo2.configure(state="readonly")
                self.combo2.set('')
                self.combo3.set('')
                find_subcat = "SELECT discount FROM Coffee_Category WHERE type = ?"
                cur.execute(find_subcat, [self.combo1.get()])
                result2 = cur.fetchall()
                subcat = []
                for j in range(len(result2)):
                    if (result2[j][0] not in subcat):
                        subcat.append(result2[j][0])

                self.combo2.configure(values=subcat)
                self.combo2.bind("<<ComboboxSelected>>", self.get_subcat)
                self.combo3.configure(state="disabled")

            def get_subcat(self, Event):
                self.combo3.configure(state="readonly")
                self.combo3.set('')
                find_product = "SELECT coffee_name FROM Coffee_Category WHERE type = ? and discount = ?"
                cur.execute(find_product, [self.combo1.get(), self.combo2.get()])
                result3 = cur.fetchall()
                pro = []
                for k in range(len(result3)):
                    pro.append(result3[k][0])

                self.combo3.configure(values=pro)
                self.combo3.bind("<<ComboboxSelected>>", self.show_qty)
                self.entry4.configure(state="disabled")

            def show_qty(self, Event):
                self.entry4.configure(state="normal")
                self.qty_label = Label(biller)
                self.qty_label.place(relx=0.033, rely=0.694, width=82, height=26)
                self.qty_label.configure(font="-family {Poppins SemiBold} -size 9")
                self.qty_label.configure(anchor="w")

                product_name = self.combo3.get()
                find_qty = "SELECT in_stock FROM Coffee_Category WHERE coffee_name = ?"
                cur.execute(find_qty, [product_name])
                results = cur.fetchone()
                self.qty_label.configure(text="In Stock: {}".format(results[0]))
                self.qty_label.configure(background="#ffffff")
                self.qty_label.configure(foreground="#333333")

            cart = Cart()

            def add_to_cart(self):
                self.Scrolledtext1.configure(state="normal")
                strr = self.Scrolledtext1.get('1.0', END)
                if strr.find('Total') == -1:
                    product_name = self.combo3.get()
                    if (product_name != ""):
                        product_qty = self.entry4.get()
                        find_mrp = "SELECT coffee_price, in_stock FROM Coffee_Category WHERE coffee_name = ?"
                        cur.execute(find_mrp, [product_name])
                        results = cur.fetchall()
                        stock = results[0][1]
                        mrp = results[0][0]
                        if product_qty.isdigit() == True:
                            if (stock - int(product_qty)) >= 0:
                                sp = mrp * int(product_qty)
                                item = CoffeeItem(product_name, mrp, int(product_qty))
                                self.cart.add_item(item)
                                self.Scrolledtext1.configure(state="normal")
                                divide = "\t" + ("-" * 70) + "\n"
                                self.Scrolledtext1.insert('insert', divide)
                                bill_text = "\t{}\t  -----  \t{}\t  -----  \t{}\n".format(product_name, product_qty, sp)
                                self.Scrolledtext1.insert('insert', bill_text)
                                self.Scrolledtext1.configure(state="disabled")
                            else:
                                messagebox.showerror("Oops!", "Out of stock. Check quantity.", parent=biller)
                        else:
                            messagebox.showerror("Oops!", "Invalid quantity.", parent=biller)
                    else:
                        messagebox.showerror("Oops!", "Choose a product.", parent=biller)
                else:
                    self.Scrolledtext1.delete('1.0', END)
                    new_li = []
                    li = strr.split("\n")
                    for i in range(len(li)):
                        if len(li[i]) != 0:
                            if li[i].find('Total') == -1:
                                new_li.append(li[i])
                            else:
                                break
                    for j in range(len(new_li) - 1):
                        self.Scrolledtext1.insert('insert', new_li[j])
                        self.Scrolledtext1.insert('insert', '\n')
                    product_name = self.combo3.get()
                    if (product_name != ""):
                        product_qty = self.entry4.get()
                        find_mrp = "SELECT coffee_price, in_stock, coffee_id FROM Coffee_Category WHERE coffee_name = ?"
                        cur.execute(find_mrp, [product_name])
                        results = cur.fetchall()
                        stock = results[0][1]
                        mrp = results[0][0]
                        if product_qty.isdigit() == True:
                            if (stock - int(product_qty)) >= 0:
                                sp = results[0][0] * int(product_qty)
                                item = CoffeeItem(product_name, mrp, int(product_qty))
                                self.cart.add_item(item)
                                self.Scrolledtext1.configure(state="normal")
                                bill_text = "{}\t\t\t\t\t\t{}\t\t\t\t\t   {}\n".format(product_name, product_qty, sp)
                                self.Scrolledtext1.insert('insert', bill_text)
                                self.Scrolledtext1.configure(state="disabled")
                            else:
                                messagebox.showerror("Oops!", "Out of stock. Check quantity.", parent=biller)
                        else:
                            messagebox.showerror("Oops!", "Invalid quantity.", parent=biller)
                    else:
                        messagebox.showerror("Oops!", "Choose a product.", parent=biller)

            def remove_product(self):
                if(self.cart.isEmpty()!=True):
                    self.Scrolledtext1.configure(state="normal")
                    strr = self.Scrolledtext1.get('1.0', END)
                    if strr.find('Total')==-1:
                        try:
                            self.cart.remove_item()
                        except IndexError:
                            messagebox.showerror("Oops!", "Cart is empty", parent=biller)
                        else:
                            self.Scrolledtext1.configure(state="normal")
                            get_all_bill = (self.Scrolledtext1.get('1.0', END).split("\n"))
                            new_string = get_all_bill[:len(get_all_bill)-3]
                            self.Scrolledtext1.delete('1.0', END)
                            for i in range(len(new_string)):
                                self.Scrolledtext1.insert('insert', new_string[i])
                                self.Scrolledtext1.insert('insert','\n')

                            self.Scrolledtext1.configure(state="disabled")
                    else:
                        try:
                            self.cart.remove_item()
                        except IndexError:
                            messagebox.showerror("Oops!", "Cart is empty", parent=biller)
                        else:
                            self.Scrolledtext1.delete('1.0', END)
                            new_li = []
                            li = strr.split("\n")
                            for i in range(len(li)):
                                if len(li[i])!=0:
                                    if li[i].find('Total')==-1:
                                        new_li.append(li[i])
                                    else:
                                        break
                            new_li.pop()
                            for j in range(len(new_li)-1):
                                self.Scrolledtext1.insert('insert', new_li[j])
                                self.Scrolledtext1.insert('insert','\n')
                            self.Scrolledtext1.configure(state="disabled")

                else:
                    messagebox.showerror("Oops!", "Add a product.", parent=biller)

            def wel_bill(self):
                self.name_message = Text(biller)
                self.name_message.place(relx=0.820, rely=0.782, width=176, height=30)
                self.name_message.configure(font="-family {Podkova} -size 10")
                self.name_message.configure(borderwidth=0)
                self.name_message.configure(background="#ffffff")

                self.num_message = Text(biller)
                self.num_message.place(relx=0.820, rely=0.652, width=90, height=30)
                self.num_message.configure(font="-family {Podkova} -size 10")
                self.num_message.configure(borderwidth=0)
                self.num_message.configure(background="#ffffff")

                self.bill_message = Text(biller)
                self.bill_message.place(relx=0.820, rely=0.392, width=176, height=26)
                self.bill_message.configure(font="-family {Podkova} -size 10")
                self.bill_message.configure(borderwidth=0)
                self.bill_message.configure(background="#ffffff")

                self.bill_date_message = Text(biller)
                self.bill_date_message.place(relx=0.820, rely=0.520, width=90, height=26)
                self.bill_date_message.configure(font="-family {Podkova} -size 10")
                self.bill_date_message.configure(borderwidth=0)
                self.bill_date_message.configure(background="#ffffff")

            def total_bill(self):
                if self.cart.isEmpty():
                    messagebox.showerror("Oops!", "Add a product.", parent=biller)
                else:
                    self.Scrolledtext1.configure(state="normal")
                    strr = self.Scrolledtext1.get('1.0', END)
                    if strr.find('Total')==-1:
                        self.Scrolledtext1.configure(state="normal")
                        divider = "\n\n" + "\t" + ("-" * 70) + "\n"
                        self.Scrolledtext1.insert('insert', divider)
                        total = "\tTotal\t\t\t$. {}\n".format(self.cart.total())
                        self.Scrolledtext1.insert('insert', total)
                        divider2 = "\t" + ("-" * 70) + "\n\n\tCashier : "
                        self.Scrolledtext1.insert('insert', divider2)
                        self.Scrolledtext1.configure(state="normal")
                    else:
                        return

            state = 1
            def gen_bill(self):

                if self.state == 1:
                    strr = self.Scrolledtext1.get('1.0', END)
                    self.wel_bill()
                    if(cust_name.get()==""):
                        messagebox.showerror("Oops!", "Please enter a name.", parent=biller)
                    elif(cust_num.get()==""):
                        messagebox.showerror("Oops!", "Please enter a number.", parent=biller)
                    elif valid_phone(cust_num.get())==False:
                        messagebox.showerror("Oops!", "Please enter a valid number.", parent=biller)
                    elif(self.cart.isEmpty()):
                        messagebox.showerror("Oops!", "Cart is empty.", parent=biller)
                    else:
                        if strr.find('Total')==-1:
                            self.total_bill()
                            self.gen_bill()
                        else:
                            self.name_message.insert(END, cust_name.get())
                            self.name_message.configure(state="disabled")

                            self.num_message.insert(END, cust_num.get())
                            self.num_message.configure(state="disabled")

                            cust_new_bill.set(random_bill_number(8))

                            self.bill_message.insert(END, cust_new_bill.get())
                            self.bill_message.configure(state="disabled")

                            bill_date.set(str(date.today()))

                            self.bill_date_message.insert(END, bill_date.get())
                            self.bill_date_message.configure(state="disabled")

                            self.Scrolledtext1.insert(END, cust_name.get())
                            s1 = "\t     - RECEIPT # : "
                            self.Scrolledtext1.insert('insert', s1)
                            self.Scrolledtext1.insert(END, cust_new_bill.get())
                            s2 = "\n\n\tDATE : "
                            self.Scrolledtext1.insert('insert', s2)
                            self.Scrolledtext1.insert(END, bill_date.get())
                            s3 = "\n\t" + ("-"*70) + "\n\t     FOR COMPLAINTS CALL : "
                            self.Scrolledtext1.insert('insert', s3)
                            self.Scrolledtext1.insert(END, cust_num.get())




                            with sqlite3.connect("./Database/CoffeeShop.db") as db:
                                cur = db.cursor()
                            insert = (
                                "INSERT INTO Inventory(bill_number, date, cashier_name, contact, bill_details) VALUES(?,?,?,?,?)"
                            )
                            cur.execute(insert, [cust_new_bill.get(), bill_date.get(), cust_name.get(), cust_num.get(), self.Scrolledtext1.get('1.0', END)])
                            db.commit()
                            #print(self.cart.items)
                            print(self.cart.allCart())
                            for name, qty in self.cart.dictionary.items():
                                update_qty = "UPDATE Coffee_Category SET in_stock = in_stock - ? WHERE coffee_name = ?"
                                cur.execute(update_qty, [qty, name])
                                db.commit()
                            messagebox.showinfo("Success!!", "Bill Generated", parent=biller)
                            self.entry1.configure(state="disabled", background="#ffffff", foreground="#000000")
                            self.entry2.configure(state="disabled", background="#ffffff", foreground="#000000")
                            self.state = 0
                else:
                    return

            def clear_bill(self):
                self.wel_bill()
                self.entry1.configure(state="normal")
                self.entry2.configure(state="normal")
                self.entry1.delete(0, END)
                # self.entry2.delete(0, END)
                # self.entry3.delete(0, END)
                self.name_message.configure(state="normal")
                self.num_message.configure(state="normal")
                self.bill_message.configure(state="normal")
                self.bill_date_message.configure(state="normal")
                self.Scrolledtext1.configure(state="normal")
                self.name_message.delete(1.0, END)
                self.num_message.delete(1.0, END)
                self.bill_message.delete(1.0, END)
                self.bill_date_message.delete(1.0, END)
                self.Scrolledtext1.delete(1.0, END)
                self.name_message.configure(state="disabled")
                self.num_message.configure(state="disabled")
                self.bill_message.configure(state="disabled")
                self.bill_date_message.configure(state="disabled")
                # self.Scrolledtext1.configure(state="disabled")
                self.cart.remove_items()
                self.state = 1
                head = "\n\n\t\t GIDEONS COFFEE SHOP\n" \
                       "\t\t C12 TEMA GHANA\n\n\t\t THANK YOU FOR CHOOSING OUR COFFEE\n" \
                       "\t\t WE HOPE TO SEE YOU NEXT TIME\n\n\n" + "\tCOFFEE\t  -----  \tQUANTITY\t  -----  \tPRICE ( $ )\n"
                self.Scrolledtext1.insert('insert', head)

            def clear_selection(self):
                self.entry4.delete(0, END)
                self.combo1.configure(state="normal")
                self.combo2.configure(state="normal")
                self.combo3.configure(state="normal")
                self.combo1.delete(0, END)
                self.combo2.delete(0, END)
                self.combo3.delete(0, END)
                self.combo2.configure(state="disabled")
                self.combo3.configure(state="disabled")
                self.entry4.configure(state="disabled")
                try:
                    self.qty_label.configure(foreground="#ffffff")
                except AttributeError:
                    pass

            def clear_search(self, events):
                self.entry3.delete(0, "end")

            def search_bill(self):
                find_bill = "SELECT * FROM Inventory WHERE bill_number = ?"
                cur.execute(find_bill, [cust_search_bill.get().rstrip()])
                results = cur.fetchall()
                if results:
                    # self.clear_bill()
                    self.wel_bill()
                    self.name_message.insert(END, results[0][2])
                    self.name_message.configure(state="disabled")

                    self.num_message.insert(END, results[0][3])
                    self.num_message.configure(state="disabled")

                    self.bill_message.insert(END, results[0][0])
                    self.bill_message.configure(state="disabled")

                    self.Scrolledtext1.delete(1.0, END)
                    self.bill_date_message.insert(END, results[0][1])
                    self.bill_date_message.configure(state="disabled")

                    self.Scrolledtext1.configure(state="normal")
                    self.Scrolledtext1.insert(END, results[0][4])
                    self.Scrolledtext1.configure(state="disabled")

                    #self.entry1.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                    #self.entry2.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")

                    self.state = 0

                else:
                    messagebox.showerror("Error!!", "Bill not found.", parent=biller)
                    self.entry3.delete(0, END)

            def time(self):
                string = strftime("%H:%M:%S %p")
                self.clock.config(text=string)
                self.clock.after(1000, self.time)

        page1 = Manage(manage_page)
        manage_page.bind("<Return>", purchase_window)
        manage_page.mainloop()


def page():
    window = Tk()
    SecondPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()

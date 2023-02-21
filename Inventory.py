from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
import admin_start
import AccountSystem
import Accounts


class InventoryPage:
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
        coverFrame2.place(x=0, y=80, width=320, height=630)

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
                               fg='#ffffff', command=lambda: product(),
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

        def exit_command():
            exit_command = messagebox.askyesno("Exit", "Are you sure you want to exit")
            if exit_command > 0:
                Manage_window.destroy()

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
        self.button6.configure(command=exit_command)

        coverFrame3 = LabelFrame(coverFrame2, bg='#ffffff', bd='2.4')
        coverFrame3.place(x=20, y=10, width=300, height=355)

        bill_number = StringVar()
        date = StringVar()
        cashier_name = StringVar()
        contact = StringVar()
        bill_details = StringVar()

        # COFFEE NAME AND ENTRY
        coffeeLabel = Label(coverFrame3, text="BILL NUMBER", bg='#ffffff', font=("yu gothic ui", 12, "bold"))
        coffeeLabel.place(x=90, y=10)

        coffeName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                 font=("", 12, 'bold'), textvariable=bill_number)
        coffeName_entry.place(x=10, y=40, width=275, height=34)
        coffeName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # COFFEE TYPE AND ENTRY
        typeLabel = Label(coverFrame3, text="DATE", bg='#ffffff', font=("yu gothic ui", 12, "bold"))
        typeLabel.place(x=120, y=75)

        typeName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                               font=("", 12, 'bold'), textvariable=date)
        typeName_entry.place(x=10, y=105, width=275, height=34)
        typeName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # COFFEE DISCOUNT AND ENTRY
        discountLabel = Label(coverFrame3, text="CASHIER NAME", bg='#ffffff', font=("yu gothic ui", 12, "bold"))
        discountLabel.place(x=90, y=140)

        discountName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                   font=("", 12, 'bold'), textvariable=cashier_name)
        discountName_entry.place(x=10, y=170, width=275, height=34)
        discountName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # IN STOCK AND ENTRY
        inStockLabel = Label(coverFrame3, text="CONTACT", bg='#ffffff', font=("yu gothic ui", 12, "bold"))
        inStockLabel.place(x=110, y=210)

        inStock_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                              font=("", 12, 'bold'), textvariable=contact)
        inStock_entry.place(x=10, y=240, width=275, height=34)
        inStock_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # PRICE AND ENTRY
        priceLabel = Label(coverFrame2, text="BILL DETAILS", bg='#ffffff', font=("yu gothic ui", 12, "bold"))
        priceLabel.place(x=115, y=369)

        price_entry = Label(product_page, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                            font=("", 12, 'bold'), textvariable=bill_details)
        price_entry.place(x=5, y=480, width=355, height=195)
        price_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # =====================================================================================================================
        #                TKINTER     TREE VIEW
        # =====================================================================================================================
        def show_all():
            conn = sqlite3.connect("./Database/CoffeeShop.db")
            cur = conn.cursor()
            cur.execute("select * from Inventory")
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
            bill_number.set(row[0])
            date.set(row[1])
            cashier_name.set(row[2])
            contact.set(row[3])
            bill_details.set(row[4])

        def clear_all():
            bill_number.set("")
            date.set("")
            cashier_name.set("")
            contact.set("")
            bill_details.set("")

        def delete_invoice():

            try:
                tree_view_content = coffee_tree.focus()
                tree_view_items = coffee_tree.item(tree_view_content)
                tree_view_values = tree_view_items['values'][0]
                ask = messagebox.askyesno("Warning",
                                          f"Are you sure you want to delete records of {tree_view_values}")
                if ask is True:

                    conn = sqlite3.connect("./Database/CoffeeShop.db")
                    cur = conn.cursor()
                    delete = "DELETE FROM INVENTORY WHERE bill_number = ?"
                    cur.execute(delete, [coffeName_entry.get()])
                    conn.commit()
                    show_all()
                    clear_all()
                    conn.close()
                    messagebox.showinfo("Success", f" {tree_view_values} records has been deleted Successfully")
                else:
                    pass

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error",
                                     "There is some error deleting the data\n Make sure you have Selected the data")


        self.button3 = Button(coverFrame3)
        self.button3.place(relx=0.599, rely=0.849, width=86, height=25)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#fd6a36")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#fd6a36")
        self.button3.configure(font="-family {Poppins SemiBold} -size 10")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Delete""")
        self.button3.configure(command=delete_invoice)

        self.button6 = Button(coverFrame3)
        self.button6.place(relx=0.209, rely=0.849, width=86, height=25)
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

        def accounts():
            win = Toplevel()
            Accounts.InventoryPage(win)
            Manage_window.withdraw()
            win.deiconify()

        # PURCHASE BUTTON
        purchaseFrame = LabelFrame(coverFrame, bg='#ffffff', bd='2.4')
        purchaseFrame.place(x=200, y=10, width=100, height=80)

        purchaseLabel = Label(purchaseFrame, text="Purchase", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
        purchaseLabel.place(x=10, y=0)

        purchaseIcon = Image.open('images//marketplace.png')
        photo = ImageTk.PhotoImage(purchaseIcon)
        purchase = Button(purchaseFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                          activebackground="#ffffff", command=lambda: product())
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
                          activebackground="#ffffff", command=lambda: product())
        products.image = photo
        products.place(x=0, y=22)

        # BILL BUTTON
        billFrame = LabelFrame(coverFrame, bg='#ffffff', bd='2.4')
        billFrame.place(x=350, y=10, width=100, height=80)

        billLabel = Label(billFrame, text="   Bill", font=("yu gothic ui", 12, 'bold'), bg='#ffffff')
        billLabel.place(x=10, y=0)

        billIcon = Image.open('images//bill.png')
        photo = ImageTk.PhotoImage(billIcon)
        bill = Button(billFrame, image=photo, bg='#ffffff', width=93, height=52, bd=0, cursor='hand2',
                      activebackground="#ffffff")
        bill.image = photo
        bill.place(x=0, y=22)

        # ACCOUNTS BUTTON
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

        self.coverFrame2 = Frame(productsFrame, bg='#ffffff')
        self.coverFrame2.place(x=0, y=80, width=575, height=645)

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
        scrollbarx.place(relx=0.282, rely=0.939, width=950, height=25)

        coffee_tree.configure(
            columns=(
                "BillNumber",
                "Date",
                "CashierName",
                "contact"
            )
        )

        coffee_tree.heading("BillNumber", text="BILL NUMBER", anchor=N)
        coffee_tree.heading("Date", text="DATE", anchor=N)
        coffee_tree.heading("CashierName", text="CASHIER NAME", anchor=N)
        coffee_tree.heading("contact", text="CONTACT", anchor=N)
        #coffee_tree.heading("BillDetails", text="#", anchor=N)

        coffee_tree.column("#0", stretch=NO, minwidth=0, width=0)
        coffee_tree.column("#1", stretch=NO, minwidth=0, width=230, anchor=N)
        coffee_tree.column("#2", stretch=NO, minwidth=0, width=150, anchor=N)
        coffee_tree.column("#3", stretch=NO, minwidth=0, width=352, anchor=N)
        coffee_tree.column("#4", stretch=NO, minwidth=0, width=110, anchor=N)
        #coffee_tree.column("#5", stretch=NO, minwidth=0, width=50, anchor=N)
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

        def exitt2():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=Manage_window)
            if sure == True:
                Manage_window.destroy()

        Manage_window.protocol("WM_DELETE_WINDOW", exitt2)


def page():
    window = Tk()
    InventoryPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()

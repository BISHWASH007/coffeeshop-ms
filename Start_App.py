from tkinter import *
from tkinter.ttk import Progressbar
import sys
import AccountSystem
import os

root = Tk()
# root.resizable(0, 0)
image = PhotoImage(file='images//coffeeShop-ico.png')

height = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)
#root.wm_attributes('-alpha', 0.9)
root.wm_attributes('-topmost', True)
root.config(background='#fd6a36')

welcome_label = Label(text='WELCOME TO Batch33 Cofee Shop', bg='#fd6a36', font=("yu gothic ui", 15, "bold"), fg='black')
welcome_label.place(x=80, y=25)

bg_label = Label(root, image=image, bg='#fd6a36')
bg_label.place(x=130, y=65)

progress_label = Label(root, text="Please Wait...", font=('yu gothic ui', 13, 'bold'), fg='black', bg='#fd6a36')
progress_label.place(x=190, y=350)
progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=15, y=390)

exit_btn = Button(text='x', bg='#fd6a36', command=lambda: exit_window(), bd=0, font=("yu gothic ui", 16, "bold"),
                  activebackground='#fd6a36', fg='white')
exit_btn.place(x=490, y=0)


def exit_window():
    sys.exit(root.destroy())


def top():
    root.withdraw()
    os.system("python AccountSystem.py")
    root.destroy()


i = 0


def load():
    global i
    if i <= 10:
        txt = 'Please Wait...  ' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000, load)
        progress['value'] = 10*i
        i += 1
    else:
        top()


load()


load()
root.mainloop()

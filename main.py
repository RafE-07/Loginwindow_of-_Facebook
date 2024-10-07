from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handel_login():
    email = email_input.get()
    password= password_input.get()
    
    if email =='abc@gmail.com' and password =='1234':
        messagebox.showinfo('Facebook','Login successful')

    else :
        messagebox.showerror('Error','Login Failed')    


root = Tk()

root.title("login forn")
root.iconbitmap('facebook.ico.ico')

root.geometry('270x300')
root.configure(background ='#F0EDE6')
img = Image.open('Black Icon- Facebook.jpg')
resized_img = img.resize((55,55))
img  = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)
img_label.pack(pady=(10,3))

text_label = Label(root,text='Facebook')
text_label.pack()
text_label.config(font=('verdana',10))

email_label = Label(root,text='Enter Email')
email_label.pack(pady=(15,3))
email_label.config(font=('verdana',8))

email_input = Entry(root,width=40)
email_input.pack(ipady=2.5,pady=(1,10))


password_label = Label(root,text='Enter Password')
password_label.pack(pady=(15,3))
password_label.config(font=('verdana',8))

password_input = Entry(root,width=40)
password_input.pack(ipady=2.5,pady=(1,5))

login_btn = Button(root,text='Login here',bg='black',fg = 'white' ,command = handel_login)
login_btn.pack(pady=(10,5))
login_btn.config(font=('verdana',10))
root.mainloop()

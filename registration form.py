from tkinter import*
import os

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()    


def login_success():
    global screen3
    screen3=Toplevel(window)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login success").pack()
    Button(screen3,text="OK", command=delete2).pack()
    

def password_not_recognizeed():
    global screen4
    screen4=Toplevel(window)
    screen4.title("Error")
    screen4.geometry("150x100")
    Label(screen4, text="Password error").pack()
    Button(screen4,text="OK", command=delete3).pack()

def user_not_found():
    global screen5
    screen5=Toplevel(window)
    screen5.title("Error")
    screen5.geometry("150x100")
    Label(screen5, text="Username error").pack()
    Button(screen5,text="OK", command=delete4).pack()
    

def register_user():

    username_info=username.get()
    password_info=password.get()

    file =open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration success", fg="green", font=('Calibri', 15)).pack()
    
def register():
    global screen1
    screen1=Toplevel(window)
    screen1.title("Register form")
    screen1.geometry("300x250")
   
    global username
    global password
    global username_entry
    global password_entry
    
    username=StringVar()
    password=StringVar()

    Label(screen1, text="Please, enter details below").pack()
    Label(screen1, text=" ").pack()
    Label(screen1, text="Username * ").pack()
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="Password * ").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1, text=" ").pack()
    button_register_user=Button(screen1, text="Register", width=10, height=1, command=register_user)
    button_register_user.pack()
    
def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files=os.listdir()
    print(list_of_files)
    print(username1)
    if username1 in list_of_files:
        file1=open(username1, "r")
        verify=file1.read().splitlines()
        if password1 in verify:
            login_success()
            print("Login successful")
        else:
            print("Password is wrong")
            password_not_recognizeed()
            
    else:
        print("Wrong username")
        user_not_found()
        

    

    
def login():
    global screen2
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    screen2=Toplevel(window)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please, enter details below to login ").pack()
    Label(screen2, text=" ").pack()

    username_verify=StringVar()
    password_verify=StringVar()

     
    Label(screen2, text="Username * ").pack()
    username_entry1=Entry(screen2,textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text=" ").pack()
    Label(screen2,text="Password * ").pack()
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_entry1.pack()

    Label(screen2, text=" ").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()

    
    

def main_screen():
    global window
    global username
    global password
    window=Tk()
    window.title("Register and Login System")
    window.geometry("300x250")
    
    #components
    heading=Label(window, text="Hello!", bg="grey", width="300")
    heading.pack()
    username_text=Label(window, text="Username")
    username_text.pack()
    password_text=Label(window, text="Password")
    password_text.pack()
    label=Label(window, text="")
    label.pack()
    
    button_login=Button(window, text="Login", width=20, command=login)
    button_login.pack()

    button_register=Button(window, text="Register",  width=20, command=register)
    button_register.pack()
    
    

    window.mainloop()

main_screen()
    

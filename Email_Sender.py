from tkinter import *
import smtplib
import re

# Manage access credentials
def login():
    if validate_login():
        global username
        global password
        username = str(entry1.get())
        password = str(entry2.get())
        global server
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        f2.pack()
        btn2.grid()
        label4['text'] = "Logged In!"
        root.after(10, root.grid)
        f1.pack_forget()
        root.after(10, root.grid)
        f2.pack()
        label9.grid_remove()
        root.after(10, root.grid)


# Hide login menu once logged in
def hide_login_label():
    f2.pack_forget()
    f3.pack_forget()
    root.after(10, root.grid)


# Function to handle sending emails
def send_mail():
    if validate_message():
        label9.grid_remove()
        root.after(10, root.grid)
        receiver = str(entry3.get())
        subject = str(entry4.get())
        msgbody = str(entry5.get())
        msg = "From: " + username + "\n" + "To: " + receiver + "\n" + "Subject: " + subject + "\n" + msgbody
        try:
            server.sendmail(username, receiver, msg)
            label9.grid()
            label9['text'] = "Mail Sent!"
            root.after(10, label9.grid)
        except Exception as e:
            label9.grid()
            label9['text'] = "Error in sending your email"
            root.after(10, label9.grid)


# Function to handle logout/exit session
def logout():
    try:
        server.quit()
        f3.pack_forget()
        f2.pack()
        label4.grid()
        label4['text'] = "Logged Out successfully"
        btn2.grid_remove()
        f1.pack()
        #Delete password from memery:
        entry2.delete(0, END)
        root.after(10, root.grid)
    except Exception as e:
        label4['text'] = "Error in Logout"


# Validate login credentials
def validate_login():
    email_text = str(entry1.get())
    pass_text = str(entry2.get())
    if(email_text == "") or (pass_text == ""):
        f2.pack()
        label4.grid()
        label4['text'] = "Please ensure both email and password fields are completed with the correct credentials."
        btn2.grid_remove()
        root.after(10, root.grid)
        return False
    else:
        EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not EMAIL_REGEX.match(email_text):
            f2.pack()
            label4.grid()
            label4['text'] = "Please enter a valid Email Address"
            btn2.grid_remove()
            root.after(10, root.grid)
            return False
        else:
            return True


# Validate message format and length
def validate_message():
    email_text = str(entry3.get())
    subject_text = str(entry4.get())
    msg_text = str(entry5.get())

    if (email_text == "") or (subject_text == "") or (msg_text == ""):
        label9.grid()
        label9['text'] = "Please complete all fields"
        root.after(10, root.grid)
        return False
    else:
        EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not EMAIL_REGEX.match(email_text):
            label9.grid()
            label9['text'] = "Please enter a valid email address"
            root.after(10, root.grid)
            return False
        elif(len(subject_text) < 3) or (len(msg_text) < 3):
            label9.grid()
            label9['text'] = "Please ensure you enter at least 3 characters"
            root.after(10, root.grid)
            return False
        else:
            return True


root = Tk()
root.title('Email Application')

f1 = Frame(root, width=1000, height=800)
f1.pack(side=TOP)

label1 = Label(f1, width=25, text="Enter credentials:", font=("Calibri 18 bold"))
label1.grid(row=0, columnspan=3, pady=10, padx=10)

label2 = Label(f1, text='Email Address').grid(row=1, sticky=E, pady=5, padx=10)
label3 = Label(f1, text='Password').grid(row=2, sticky=E, pady=5, padx=10)

entry1 = Entry(f1)
entry2 = Entry(f1, show="*")

entry1.grid(row=1, column=1, pady=5)
entry2.grid(row=2, column=1)

btn1 = Button(f1, text="Login", width=10, bg="black", fg="white", command= lambda: login())
btn1.grid(row=3, columnspan=3, pady=10)

f2 = Frame(root)
f2.pack(side=TOP, expand=NO, fill=NONE)

label4 = Label(f2, width=20, bg="green", fg="black", text="You are currently logged in!", font=("Calibri 12 bold"))
label4.grid(row=0, column=0, columnspan=3, pady=5)

btn2 = Button(f2, text="Logout", bg="black", fg="white", command= lambda: logout())
btn2.grid(row=0, column=4, sticky=E, pady=10, padx=(5,0))

f3 = Frame(master=root)
f3.pack(side=TOP, expand=NO, fill=NONE)

label5 = Label(f3, width=20, text="Compose Email", font=("Calibri 18 bold"))
label5.grid(row=0, columnspan=3, pady=10)

label6 = Label(f3, text="To").grid(row=1, sticky=E, pady=5)
label7 = Label(f3, text="Subject").grid(row=1, sticky=E, pady=5)
label8 = Label(f3, text="Body").grid(row=1, sticky=E)

entry3 = Entry(f3)
entry4 = Entry(f3)
entry5 = Entry(f3)

entry3.grid(row=1, column=1, pady=5)
entry4.grid(row=2, column=1, pady=5)
entry5.grid(row=3, column=1, pady=5, rowspan=3, ipady=10)

btn3 = Button(f3, text="Send Email", width=10, bg="black", fg="white", command= lambda: send_mail())

btn3.grid(row=6, columnspan=3, pady=10)

label9 = Label(f3, width=20, fg="white", bg="black", font=("Calibri 18 bold"))
label9.grid(row=7, columnspan=3, pady=5)

hide_login_label()

root.mainloop()




from tkinter import *

from tkinter import messagebox
#import db
import dashboard
import smtplib
from email.mime.text import MIMEText
from tkinter import messagebox

#from Pro import send_mail



def send_mail(ge):
    try:
        body = '''Welcome to VES learning ,you have successfully  registered '''
        msg = MIMEText(body)

        fromaddr = "pythonproject325"
        toaddr = ge       # do get wala thing here

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Verfication from VESIT course"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "pp@123456")
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPRecipientsRefused:
        messagebox.showinfo("Please enter correct email id")


class RegisterWindow:

    def __init__(self):
        self.win = Tk()
        # reset the window and background color
        self.canvas = Canvas(self.win, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 1200 / 2)
        y = int(height / 2 - 600 / 2)
        str1 = "1200x600+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("VESLine Registraton")
        #print(ge)

    def add_frame(self):
        self.frame = Frame(self.win, height=500, width=1050)
        self.frame.place(x=80, y=50)

        x, y = 70, 20

        # now create a login form

        self.label = Label(self.frame, text="User Registration")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=400, y=y + 0)

        self.label1 = Label(self.frame, text="Enter Full Name:")
        self.label1.config(font=("Courier", 12, 'bold'))
        self.label1.place(x=350, y=y + 60)

        self.name = Entry(self.frame, font='Courier 12')
        self.name.place(x=550, y=y + 60)

        self.label2 = Label(self.frame, text="Enter Phone Number:")
        self.label2.config(font=("Courier", 12, 'bold'))
        self.label2.place(x=350, y=y + 100)

        self.phoneno = Entry(self.frame, font='Courier 12')
        self.phoneno.place(x=550, y=y + 100)

        self.label3 = Label(self.frame, text="Enter VesID")
        self.label3.config(font=("Courier", 12, 'bold'))
        self.label3.place(x=350, y=y + 140)

        self.email = Entry(self.frame, font='Courier 12')
        self.email.place(x=550, y=y + 140)

        self.label3 = Label(self.frame, text="Select Class:")
        self.label3.config(font=("Courier", 12, 'bold'))
        self.label3.place(x=350, y=y + 180)

        self.s1 = Spinbox(self.frame, values=('D5', 'D10', 'D15', 'D20'), width=15, fg='white', bg='black',
                          font=('Arial', 12, 'bold italic'))
        self.var = IntVar()
        self.s1.place(x=550, y=200)

        self.label3 = Label(self.frame, text="Select Year:")
        self.label3.config(font=("Courier", 12, 'bold'))
        self.label3.place(x=350, y=y + 220)

        self.r1 = Radiobutton(self.frame, text='F.E.', value=1, font=("Courier", 12, 'bold'))  # Add radiobutton
        self.r2 = Radiobutton(self.frame, text='S.E.', value=2, font=("Courier", 12, 'bold'))  # Add radiobutton
        self.r1.place(x=550, y=240)
        self.r2.place(x=630, y=240)
        self.r3 = Radiobutton(self.frame, text='T.E.', value=3, font=("Courier", 12, 'bold'))  # Add radiobutton
        self.r4 = Radiobutton(self.frame, text='B.E.', value='4', font=("Courier", 12, 'bold'))  # Add radiobutton
        self.r3.place(x=550, y=260)
        self.r4.place(x=630, y=260)
        self.var = IntVar()

        self.label3 = Label(self.frame, text="Enter your Rollno")
        self.label3.config(font=("Courier", 12, 'bold'))
        self.label3.place(x=350, y=y + 300)

        self.rollno = Entry(self.frame, font='Courier 12')
        self.rollno.place(x=550, y=y + 300)

        self.label9 = Label(self.frame, text="Enter Password:")
        self.label9.config(font=("Courier", 12, 'bold'))
        self.label9.place(x=350, y=y + 340)

        self.password = Entry(self.frame, show='*', font='Courier 12')
        self.password.place(x=550, y=y + 340)

        self.label8 = Label(self.frame, text="Enter Password Again:")
        self.label8.config(font=("Courier", 12, 'bold'))
        self.label8.place(x=320, y=y + 380)

        self.password2 = Entry(self.frame, show='*', font='Courier 12')
        self.password2.place(x=550, y=y + 380)

        self.button = Button(self.frame, text="REGISTER", font='Courier 15 bold', bg='#b02a30', fg='white',
                             command=self.register)
        self.button.place(x=470, y=y + 420)

        self.labelmsg = Label(self.frame, text='')
        self.labelmsg.config(font=('Courier', 12, 'bold'))
        self.labelmsg.place(x=470, y=y + 210)

        self.win.mainloop()



    def register(self):
        # get the data and store it into tuple (data)
        data = (
            self.name.get(),
            self.phoneno.get(),
            self.email.get(),
            self.s1.get(),
            self.rollno.get(),
            self.password.get(),
            self.password2.get(),
        )
        ge=self.email.get()




        # validations
        if (self.password.get() == self.password2.get()):
            if (
                    self.name.get() == "" or self.phoneno.get() == "" or self.email.get() == "" or self.s1.get() == "" or self.rollno.get() == "" or self.password.get() == "" or self.password2.get() == ""):
                messagebox.showinfo("ALERT", "ALL FIELDS ARE REQUIRED!")
            else:
                res = db.user_register(data)
                if res:
                    send_mail(ge)
                    messagebox.showinfo("DONE", "Registration Successful!")
                    self.win.destroy()
                    x = dashboard.DashboardWindow(ge)
                    x.add_frame(ge)

                else:
                    messagebox.showinfo("ALERT", "Please try again!")


        else:
            messagebox.showinfo("RE-ENTER Password", "THE PASSWORDS DO NOT MATCH")

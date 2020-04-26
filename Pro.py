from tkinter import *
import PIL
from PIL import Image, ImageTk
import smtplib
from email.mime.text import MIMEText
from tkinter import messagebox
import mysql.connector
from MyCourses import runCourse

user_data = {'name': 'some name', 'email': 'some_email'}

class CourseFrame(Frame):
    def __init__(self, master, image, course, prof, institute, duration, data,gemail, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self['background'] = 'white'
        self['borderwidth'] = 2
        self['highlightthickness'] = 2
        self['highlightcolor'] = 'white'
        self['highlightbackground'] = 'white'
        self['relief'] = FLAT

        self.image = self.create_image(image)

        self.imageLabel = Label(self,
                                image=self.image,
                                borderwidth=0, relief="flat")
        self.courseName = Label(self, text=course, fg="Black", font=("Helvetica", 12), bg="white")
        self.profName = Label(self, text=prof, fg="Blue", font=("Helvetica", 11), bg="white")
        self.instituteName = Label(self, text=institute, fg="grey",
                                   font=("Helvetica", 11),
                                   bg="white")
        self.durationLabel = Label(self, text=duration, fg="grey",
                                   font=("Helvetica", 12),
                                   bg="white")
        self.enroll = Button(self, text="ENROLL", fg="white", bg="red", font=("Lucida", 9),
                             command=lambda d=data: self.enrolled(d,gemail))


        self.imageLabel.grid(row=0, column=0)
        self.courseName.grid(row=1, column=0, sticky='w')
        self.profName.grid(row=2, column=0, sticky='w')
        self.instituteName.grid(row=3, column=0, sticky='w')
        self.durationLabel.grid(row=4, column=0, sticky='w')
        self.enroll.grid(row=5, column=0)

        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        self.configure(highlightcolor='blue', highlightbackground='blue')

    def on_leave(self, event):
        self.configure(highlightcolor='white', highlightbackground='white')

    def create_image(self, filename):
        img = Image.open(filename)
        img.thumbnail((500, 500))
        img = img.resize((300, 200), Image.ANTIALIAS)
        p_img = PIL.ImageTk.PhotoImage(img)
        return p_img

    def enrolled(self, data, gemail):

        #email = user_data['email']

        details=(
               0,
               0,
               0,
               0,
               0,
               gemail


        )

        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database='student')
        c = con.cursor()

        fetch = (
            gemail

                )
        print(gemail)
        query = c.execute("SELECT pyenrolled,cnenrolled,coaenrolled,osenrolled,javaenrolled FROM studentsenrolled  WHERE email = %s", (gemail, ))
        result=c.fetchone()
        print(result)

        con.commit()
        if (result==None):
            print("1")
            c.execute( "INSERT INTO studentsenrolled (pyenrolled,coaenrolled,cnenrolled,osenrolled,javaenrolled,email) VALUES (%s,%s,%s,%s,%s,%s)",details)
            con.commit()


        if data=='python':
            send_python(gemail)
            print("data=python")
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database='student')
            c = con.cursor()
            get=(
                1,
                gemail
            )

            c.execute("UPDATE studentsenrolled SET pyenrolled = %s WHERE email = %s",get)

            con.commit()

        if data == 'coa':
                 send_coa(gemail)
                 #print("data=coa")
                 con = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     passwd="",
                     database='student')
                 c = con.cursor()
                 get = (
                     1,
                    gemail
                )

                 c.execute("UPDATE studentsenrolled SET coaenrolled = %s WHERE email = %s", get)

                 con.commit()

        if data == 'os':
                send_os(gemail)
                print("data=os")
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database='student')
                c = con.cursor()
                get = (
                    1,
                    gemail
                 )

                c.execute("UPDATE studentsenrolled SET osenrolled = %s WHERE email = %s", get)

                con.commit()

        if data == 'cn':
                send_cn(gemail)
                print("data=cn")
                get = (
                     1,
                    gemail
                )

                con = mysql.connector.connect(
                    host="localhost",
                     user="root",
                     passwd="",
                     database='student')
                c = con.cursor()
                c.execute("UPDATE studentsenrolled SET cnenrolled = %s WHERE email = %s", get)

                con.commit()

        if data == 'java':
                send_java(gemail)
                #print("data=java")
                get = (
                    1,
                    gemail
                )

                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database='student')
                c = con.cursor()
                c.execute("UPDATE studentsenrolled SET javaenrolled = %s WHERE email = %s", get)
                con.commit()




def send_python(gemail):
    try:
        body = '''Congratualations you have successfully enrolled for Python Course'''
        msg = MIMEText(body)

        fromaddr = "pythonproject325"
        toaddr=gemail

        msg['From']=fromaddr
        msg['To']=toaddr
        msg['Subject']="Verfication from VESIT course"
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fromaddr,"pp@123456")
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPRecipientsRefused:
        print("error")
        messagebox.showinfo("This Email id does not exist,Please enter correct email id")

def send_coa(gemail):
    try:
        body = '''Congratualations you have successfully enrolled for COA Course'''
        msg = MIMEText(body)

        fromaddr = "pythonproject325"
        toaddr=gemail

        msg['From']=fromaddr
        msg['To']=toaddr
        msg['Subject']="Verfication from VESIT course"
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fromaddr,"pp@123456")
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPRecipientsRefused:
        print("error")
        messagebox.showinfo("This Email id does not exist,Please enter correct email id")

def send_os(gemail):
    try:
        body = '''Congratualations you have successfully enrolled for OS Course'''
        msg = MIMEText(body)

        fromaddr = "pythonproject325"
        toaddr=gemail
        msg['From']=fromaddr
        msg['To']=toaddr
        msg['Subject']="Verfication from VESIT course"
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fromaddr,"pp@123456")
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPRecipientsRefused:
        print("error")
        messagebox.showinfo("This Email id does not exist,Please enter correct email id")

def send_cn(gemail):
    try:
        body = '''Congratualations you have successfully enrolled for CN Course'''
        msg = MIMEText(body)

        fromaddr = "pythonproject325"
        toaddr=gemail

        msg['From']=fromaddr
        msg['To']=toaddr
        msg['Subject']="Verfication from VESIT course"
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fromaddr,"pp@123456")
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPRecipientsRefused:
        print("error")
        messagebox.showinfo("This Email id does not exist,Please enter correct email id")

def send_java(gemail):
    try:
        body = '''Congratualations you have successfully enrolled for JAVA Course'''
        msg = MIMEText(body)

        fromaddr = "pythonproject325"
        toaddr=gemail

        msg['From']=fromaddr
        msg['To']=toaddr
        msg['Subject']="Verfication from VESIT course"
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fromaddr,"pp@123456")
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPRecipientsRefused:
        print("error")
        messagebox.showinfo("This Email id does not exist,Please enter correct email id")


class Pro(Tk):
    def __init__(self, ge,*args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #print(ge)
        self.title('project')
        self.state('zoomed')
        self.geometry('3000x3000')

        self.mainFrame = Frame(self)

        self.canvas = Canvas(self.mainFrame, bg='blue')
        scrollbar = Scrollbar(self.mainFrame,
                              orient='vertical',
                              command=self.canvas.yview
                              )

        scrollable_frame = Frame(self.canvas, bg='pink')

        scrollable_frame.bind(
            '<Configure>',
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox('all')
            )
        )

        def size(event):
            self.canvas.create_window((0, 0),
                                 window=scrollable_frame,
                                 anchor='nw',
                                 width=event.width
                                 )

        self.canvas.bind('<Configure>', size)

        main = Frame(scrollable_frame, bg='#EEEEEE')
        main.grid(row=0, column=0, sticky='nsew')
        scrollable_frame.grid_rowconfigure(0, weight=1)
        scrollable_frame.grid_columnconfigure(0, weight=1)

        course = CourseFrame(main,
                             padx=10,
                             pady=10,
                             image='111.png',
                             course='PYTHON PROGRAMMING\n ',
                             prof='prof.Vidya Pujari',
                             institute='Indian Instititute of technology bombay  ',
                             duration='Duration:8weeks(Starts 4-may-2020) ',
                             data='python',
                             gemail=ge)

        course.grid(row=0, column=0, pady=20)
        course2 = CourseFrame(main,
                              padx=10,
                              pady=10,
                              image='222.png',
                              course='OPERATING SYSTEMS\n ',
                              prof='prof.Sandeep Uthala',
                              institute='Indian Instititute of technology bombay  ',
                              duration='Duration:5weeks(Starts 1-may-2020) ',
                              data='os',
                              gemail=ge)

        course2.grid(row=1, column=0)

        course3 = CourseFrame(main,
                              padx=10,
                              pady=10,
                              image='333.png',
                              course='COMPUTER ORGANIZATION\n ',
                              prof='prof.Asma Parveen',
                              institute='Indian Instititute of technology bombay  ',
                              duration='Duration:10weeks(Starts 8-may-2020) ',
                              data='coa',
                              gemail=ge)

        course3.grid(row=0, column=1)
        course4 = CourseFrame(main,
                              padx=10,
                              pady=10,
                              image='444.png',
                              course='COMPUTER NETWORKS\n ',
                              prof='prof.Pooja Shetty',
                              institute='Indian Instititute of technology bombay  ',
                              duration='Duration:14weeks(Starts 12-may-2020) ',
                              data='cn',
                              gemail=ge)

        course4.grid(row=0, column=2)

        course5 = CourseFrame(main,
                              padx=10,
                              pady=10,
                              image='555.png',
                              course='JAVA PROGRAMMING\n ',
                              prof='prof.POOJA SHETTY',
                              institute='Indian Instititute of technology bombay  ',
                              duration='Duration:11weeks(Starts 6-may-2020) ',
                              data='java',
                              gemail=ge)
        
        course5.grid(row=1, column=1)
        butm= Button(self, text="GO TO MY COURSES", fg="white", bg="red", font=("Lucida", 9), command=lambda ge=ge: self.mycourse(ge))
        butm.pack(pady=10)
        
        main.grid_rowconfigure((0, 1), weight=1)
        main.grid_columnconfigure((0, 1, 2), weight=1)

        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        self.canvas.pack(fill='both', expand=True)
        self.mainFrame.pack(fill='both', expand=True)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    def mycourse(self, ge):
            print("my courses")
            print(ge)
            self.destroy()
            runCourse(ge)


def runPro(ge):
    import os
    # os.chdir(os.getcwd()[:-5])

    root = Pro(ge)
    

    root.mainloop()


def ge(args):
    pass


if __name__ == '__main__':
    runPro(ge)

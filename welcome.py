from tkinter import *
import login
import register
#import aboutus


class WelcomeWindow:

    # create a constructor

    def __init__(self):
        self.win = Tk()

        # reset the window and background color
        self.canvas = Canvas(self.win, width=1200, height=700, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 1200 / 2)
        y = int(height / 2 - 700 / 2)
        str1 = "1200x700+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("VESLine")

        self.Label_text = [
            "This project is done to make a learning  platform for all ves students, students can learn through video lectures, self-assessment through quizzes and assignments.",
            "All the courses are interactive and are available free of cost to any learner.",
            "Courses included are:",
            "1.Python",
            "2.Operation System (OS)",
            "3.Computer Networks(CN)",
            "4.Computer architecture and organization(COA)",
            "5.Java",
        ]

    def add_frame(self):
        # place the photo in the frame
        # you can find the images from flaticon.com site
        self.img = PhotoImage(file=r'college2.png')
        self.label = Label(self.win, image=self.img)
        self.label.place(x=0, y=0)

        self.message = Message(text="WELCOME TO VES LEARNING", width=600, font=('arial', 25, 'underline italic'),
                               bg='black', fg='white')

        self.message.place(x=600, y=400, anchor='center')

        def All_Courses():
            self.win.destroy()
            # self.new_win1 = Toplevel(self.win)
            # self.label = Label(self.new_win1, text="Courses: ")
            #
            # self.listbox = Listbox(self.new_win1)
            #
            # self.listbox.insert(1, "Python")
            #
            # self.listbox.insert(2, "CN")

            # self.listbox.insert(3, "COA")
            #
            # self.listbox.insert(4, "OS")
            #
            # self.listbox.insert(5, "Java")p
            #
            # self.label.pack()
            # self.listbox.pack()

        def Progress():
            self.new_win2 = Toplevel(self.win)
            self.label = Label(self.new_win2)
            self.label.pack()

        self.button1 = Button(text="All Courses", font=('helvetica', 16, 'underline italic'),
                              activebackground="#e7b909", bg='#b02a30', fg='white', command=All_Courses)
        self.button1.place(x=850, y=40)

        self.button3 = Button(text="About Us", font=('lucida', 16, 'underline italic')
                              , activebackground="#e7b909", bg='#b02a30', fg='white', command=self.aboutus)
        self.button3.place(x=1000, y=40)

        self.button99 = Button(text="LOGIN", font=('lucida', 20, 'underline italic')
                               , bg='#b02a30', fg='white', activebackground="#e7b909", command=self.login)
        self.button99.place(x=480, y=450)

        self.button98 = Button(text="Register", font=('lucida', 20, 'underline italic')
                               , bg='#b02a30', fg='white', activebackground="#e7b909", command=self.register)
        self.button98.place(x=580, y=450)

        self.win.mainloop()

    # open a new window on button press
    def login(self):
        # destroy current window
        self.win.destroy()

        # open the new window
        log = login.LoginWindow()
        log.add_frame()

    # open a new window on button press
    def register(self):
        # destroy current window
        self.win.destroy()

        # open the new window
        reg = register.RegisterWindow()
        reg.add_frame()

    # open a new window on button press
    def aboutus(self):
        # destroy current window2
        self.win.destroy()

        # open the new window
        abu = aboutus.AboutUsWindow()
        abu.add_frame()


if __name__ == "__main__":
    x = WelcomeWindow()
    import os
    os.chdir(os.getcwd())
    x.add_frame()

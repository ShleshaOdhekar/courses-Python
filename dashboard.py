from tkinter import *
#import aboutus2
from Pro import runPro



class DashboardWindow(Tk):
    def __init__(self, ge, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # reset the window and background color
        self.canvas = Canvas(self, width=1200, height=700, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        x = int(width / 2 - 1200 / 2)
        y = int(height / 2 - 700 / 2)
        str1 = "1200x700+" + str(x) + "+" + str(y)
        self.geometry(str1)

        # disable resize of the window
        self.resizable(width=False, height=False)

        # change the title of the window
        self.title("VESLine")

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
        print(ge)
        self.add_frame(ge)

    def second(self, ge):
        print("but")
        self.button4 = Button(text="About Us", font=('lucida', 16)
                              , activebackground="white", bg='Maroon', fg='white', command=lambda ge=ge: self.pro(ge))
        self.button4.place(x=1150, y=40)

    def first(self, ge):
        self.img2 = PhotoImage(file='college2.PNG')
        print(self.img2)
        self.label = Label(self,
                            image=self.img2
                           )
        self.label.place(x=0, y=0)

        self.message = Message(text="WELCOME TO VES LEARNING", width=600, font=('lucida', 25),
                               fg='black')

        self.message.place(x=600, y=400, anchor='center')

        self.button1 = Button(text="All Courses", font=('lucida', 16), activebackground="white",
                              bg='Maroon', fg='white', command=self.All_Courses)
        self.button1.place(x=700, y=40)

        # self.button2 = Button(text="Progress", font=('lucida', 16, 'underline normal'), activebackground="white",
        #                       bg='Maroon', fg='white', command=Progress)
        # self.button2.place(x=850, y=40)

        self.button3 = Button(text="About Us", font=('lucida', 16)
                              , activebackground="white", bg='Maroon', fg='white', command=self.aboutus)
        self.button3.place(x=1000, y=40)
        self.second(ge)

    def add_frame(self, ge):
        print("addframeof dashboard")
        print(ge)
        self.first(ge)

    def All_Courses(self):
        pass

    #         self.new_win1 = Toplevel(self.win)
    #         self.label = Label(self.new_win1, text="Courses: ")
    #
    #         self.listbox = Listbox(self.new_win1)
    #
    #         self.listbox.insert(1, "Python")
    #
    #         self.listbox.insert(2, "CN")
    #
    #         self.listbox.insert(3, "COA")
    #
    #         self.listbox.insert(4, "OS")
    #
    #         self.listbox.insert(5, "Java")
    #
    #         self.label.pack()
    #         self.listbox.pack()
    #
    #     def Progress():
    #         self.new_win2 = Toplevel(self.win)
    #         self.label = Label(self.new_win2)
    #         self.label.pack()

    # open a new window on button press
    def aboutus(self):
        pass

    #     # destroy current window

    #     self.win.destroy()
    #
    #     # open the new window
    #     abo = aboutus2.AboutUsWindow()
    #     abo.add_frame()
    #

    def pro(self, ge):
        # pass
        print("pro of dash ")
        print(ge)
        self.destroy()
        runPro(ge)

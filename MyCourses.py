from tkinter import *
import PIL
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import sys
import mysql.connector

class CourseFrame(Frame):
    def __init__(self, master, image, course, prof, institute,  duration, data, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self['background'] = 'white'
        self['borderwidth'] = 2
        self['highlightthickness'] = 2
        self['highlightcolor'] = 'white'
        self['highlightbackground'] = 'white'
        self['relief'] = FLAT

        self.image = self.create_image(image)

        self.imageLabel = Label(self, image=self.image, borderwidth=0, relief="flat")
        self.courseName = Label(self, text=course, fg="Black", font=("Helvetica", 12), bg="white")
        self.profName = Label(self, text=prof, fg="Blue", font=("Helvetica", 11), bg="white")
        self.instituteName = Label(self, text=institute, fg="grey",
                                   font=("Helvetica", 11),
                                   bg="white")
        self.durationLabel = Label(self, text=duration, fg="grey",
                                   font=("Helvetica", 12),
                                   bg="white")
        self.enroll = Button(self, text="GO", fg="white", bg="red", font=("comic sans", 9), command=lambda d=data: self.open(d))

        self.imageLabel.grid(row=0, column=0)
        self.courseName.grid(row=1, column=0, sticky='w')
        self.profName.grid(row=2, column=0, sticky='w')
        self.instituteName.grid(row=3, column=0, sticky='w')
        self.durationLabel.grid(row=4, column=0, sticky='w')
        self.enroll.grid(row=5, column=0)

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

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
    
    pyexec = sys.executable

    def open(self, data):
        #PathPy = filedialog.askopenfilename(title="Open a file",filetypes=[('PYTHON file','.py')])
        
        os.system( data )

    
class MyCourses(Tk):
    def __init__(self, ge, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        print(ge)
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

        # course = [['python', 'coa', 'cn'], ['os', 'java']]
        #
        # for i, j in enumerate(course):
        #     for a, b in enumerate(j):
        #         course = CourseFrame(main)
        #         course.grid(row=i, column=a, sticky='nsew', padx=10, pady=10)
        
        con = mysql.connector.connect(host="localhost",user="root",passwd="",database='studentsenrolled')
        if con.is_connected():
            print("Connection established")
        c = con.cursor()
        m= "2018.megha.shahri@ves.ac.in"
        #m=ge
        str="Select pyenrolled, coaenrolled, cnenrolled, osenrolled, javaenrolled from studentsenrolled where email= '%s'"
        args= m
        c.execute(str%args)
        result= c.fetchone()
        print(result)
        if result[0]==1:
            print('Python')
            data= 'course1fin.py'
            course = CourseFrame(main,
                                 padx=10,
                                 pady=10,
                                 image='111.png',
                                 course='PYTHON PROGRAMMING\n ',
                                 prof='prof.Vidya Pujari',
                                 institute='Indian Instititute of technology bombay  ',
                                 duration='Duration:8weeks(Starts 4-may-2020) ',
                                 data='course1fin.py')
            course.grid(row=0, column=0, pady=20)
        if result[1]==1:
            print('Coa')
            course2 = CourseFrame(main,
                                  padx=10,
                                  pady=10,
                                  image='222.png',
                                  course='OPERATING SYSTEMS\n ',
                                  prof='prof.Sandeep Uthala',
                                  institute='Indian Instititute of technology bombay  ',
                                  duration='Duration:5weeks(Starts 1-may-2020) ',
                                  data='course2.py')
            course2.grid(row=1, column=0)
        if result[2]==1:
            course3 = CourseFrame(main,
                                  padx=10,
                                  pady=10,
                                  image='333.png',
                                  course='COMPUTER ORGANIZATION\n ',
                                  prof='prof.Asma Parveen',
                                  institute='Indian Instititute of technology bombay  ',
                                  duration='Duration:10weeks(Starts 8-may-2020) ',
                                  data='course3.py')

            course3.grid(row=0, column=1)
        if result[3]==1:
            course4 = CourseFrame(main,
                                  padx=10,
                                  pady=10,
                                  image='444.png',
                                  course='COMPUTER NETWORKS\n ',
                                  prof='prof.Pooja Shetty',
                                  institute='Indian Instititute of technology bombay  ',
                                  duration='Duration:14weeks(Starts 12-may-2020) ',
                                  data='course4.py')

            course4.grid(row=0, column=2)
        if result[4]==1:
            course5 = CourseFrame(main,
                                  padx=10,
                                  pady=10,
                                  image='555.png',
                                  course='JAVA PROGRAMMING\n ',
                                  prof='prof.POOJA SHETTY',
                                  institute='Indian Instititute of technology bombay  ',
                                  duration='Duration:11weeks(Starts 6-may-2020) ',
                                  data='course5.py')

            course5.grid(row=1, column=1)
        

        main.grid_rowconfigure((0, 1), weight=1)
        main.grid_columnconfigure((0, 1, 2), weight=1)

        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        self.canvas.pack(fill='both', expand=True)
        self.mainFrame.pack(fill='both', expand=True)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    
def runCourse(ge):
    import os
    # os.chdir(os.getcwd()[:-5])

    root = MyCourses(ge)
    root.mainloop()
def ge(args):
    pass

if __name__ == '__main__':
    runCourse(ge)


    


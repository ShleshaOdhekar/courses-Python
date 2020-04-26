from tkinter import *
import PIL
from PIL import Image, ImageTk


user_data = {'name': 'some name', 'email': 'some_email'}


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
        self.enroll = Button(self, text="GO", fg="white", bg="red", font=("comic sans", 9), command=lambda d=data: self.enrolled(d))

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
    def enrolled(self, data):
        email = user_data['email']
        print(data)
        print(email)
        # con = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     passwd="",
        #     database='student')
        #
        # c = con.cursor()
        # c.execute("select * from 'studentsenrolled' where 'student_email'=%s")
        # record = c.fetchone()
        # print(record)
        # con.commit()
        # con.close()


if __name__ == '__main__':
    root = Tk()
    root.title('project')
    root.state('zoomed')
    root.geometry('3000x3000')

    mainFrame = Frame(root)

    canvas = Canvas(mainFrame, bg='blue')
    scrollbar = Scrollbar(mainFrame,
                          orient='vertical',
                          command=canvas.yview
                          )

    scrollable_frame = Frame(canvas, bg='pink')

    scrollable_frame.bind(
        '<Configure>',
        lambda e: canvas.configure(
            scrollregion=canvas.bbox('all')
        )
    )

    def size(event):
        canvas.create_window((0, 0),
                             window=scrollable_frame,
                             anchor='nw',
                             width=event.width
                             )

    canvas.bind('<Configure>', size)

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
    

    course = CourseFrame(main,
                         padx=10,
                         pady=10,
                         image='111.png',
                         course='PYTHON PROGRAMMING\n ',
                         prof='prof.Vidya Pujari',
                         institute='Indian Instititute of technology bombay  ',
                         duration='Duration:8weeks(Starts 4-may-2020) ',
                         data='python')
    

    course.grid(row=0, column=0, pady=20)
    course2 = CourseFrame(main,
                          padx=10,
                          pady=10,
                          image='222.png',
                          course='OPERATING SYSTEMS\n ',
                          prof='prof.Sandeep Uthala',
                          institute='Indian Instititute of technology bombay  ',
                          duration='Duration:5weeks(Starts 1-may-2020) ',
                          data='os')

    course2.grid(row=1, column=0)

    course3 = CourseFrame(main,
                          padx=10,
                          pady=10,
                          image='333.png',
                          course='COMPUTER ORGANIZATION\n ',
                          prof='prof.Asma Parveen',
                          institute='Indian Instititute of technology bombay  ',
                          duration='Duration:10weeks(Starts 8-may-2020) ',
                          data='coa')

    course3.grid(row=0, column=1)
    course4 = CourseFrame(main,
                          padx=10,
                          pady=10,
                          image='444.png',
                          course='COMPUTER NETWORKS\n ',
                          prof='prof.Pooja Shetty',
                          institute='Indian Instititute of technology bombay  ',
                          duration='Duration:14weeks(Starts 12-may-2020) ',
                          data='cn')

    course4.grid(row=0, column=2)

    course5 = CourseFrame(main,
                          padx=10,
                          pady=10,
                          image='555.png',
                          course='JAVA PROGRAMMING\n ',
                          prof='prof.POOJA SHETTY',
                          institute='Indian Instititute of technology bombay  ',
                          duration='Duration:11weeks(Starts 6-may-2020) ',
                          data='java')

    course5.grid(row=1, column=1)
    

    main.grid_rowconfigure((0, 1), weight=1)
    main.grid_columnconfigure((0, 1, 2), weight=1)

    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill='y')
    canvas.pack(fill='both', expand=True)
    mainFrame.pack(fill='both', expand=True)

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    root.mainloop()

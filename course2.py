import cv2
from tkinter import *
from tkinter import ttk
    
app = Tk()
app.geometry("3000x3000")
#canvas=tk.Canvas(app)
mainFrame = Frame(app, height=3000)

canvas = Canvas(mainFrame)
scrollbar = Scrollbar(mainFrame,
                      orient='vertical',
                      command=canvas.yview
                      )

scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    '<Configure>',
    lambda e: canvas.configure(
        scrollregion=canvas.bbox('all')
    )
)

canvas.create_window((0, 0),
                     window=scrollable_frame,
                     anchor='nw'
                     )

#code
photo1 = PhotoImage(file = r"cntopic.png")
Label(scrollable_frame, image=photo1, bg="black").pack(pady=20, fill='x')
label1=Label(scrollable_frame, text= 'Click here for video lecture', font=("Times", 10), fg="black", bg="#4C65DC")
label1.pack()

#canvas.pack(fill='both', expand='True')  
#canvas.config(width=480,height=360)  
#line=canvas.create_line(25,25,200,25,fill='blue',width=5)
photo = PhotoImage(file = r"cnlec.png") 
  
# here, image option is used to 
# set image on button
def rescale_frame(frame, percent=250):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
def play_vid():
    cap = cv2.VideoCapture('vid1.mp4')


    # Check if camera opened successfully
    if (cap.isOpened()== False):
      print("Error opening video stream or file")

    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        #farme.read()
        if ret == True:

            # Display the resulting frame
            frame75= rescale_frame(frame, percent=250)
            cv2.imshow('Frame', frame75)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) == ord('q'):
                break

        # Break the loop
        else:
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()
Button(scrollable_frame, text = 'Click Me !', image = photo, command=play_vid).pack(side = 'top', pady=20)

#tab view
style = ttk.Style()
style.theme_create( "MyStyle",  settings={
        "TNotebook": {"configure": {"tabmargins": [1, 2, 1, 0] , "background": "#F4F4A3"} },
        "TNotebook.Tab": {"configure": {"padding": [30, 30] , "background": "brown", "foreground": "white"}, "map":{"background": [("selected", "#1976BC")], "expand": [("selected", [1, 1, 1, 0])]}}})

style.theme_use("MyStyle")
tab_control = ttk.Notebook(scrollable_frame)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Week 1')
tab_control.add(tab2, text='Week 2')
tab_control.add(tab3, text='Week 3')
tab_control.add(tab4, text='Week 4')
tab_control.pack(expand=True, fill='x', padx=40)
title1= Label(tab1, text="Week 1", font=("Times", 20), fg="#349310", bg="#F4F4A3")
title1.pack(pady=30, fill='x')

label2= Label(tab1, font=("Times", 15), text="Python has been an object-oriented language since it existed. Because of this, creating and using classes and objects are downright easy.\n This chapter helps you become an expert in using Python's object-oriented programming support.\nIf you do not have any previous experience with object-oriented (OO) programming, you may want to consult\n an introductory course on it or at least a tutorial of some sort so that you have a grasp of the basic concepts\n.However, here is small introduction of Object-Oriented Programming (OOP) to bring you at speed −\n\nOverview of OOP Terminology\n\nClass − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class.\nThe attributes are data members (class variables and instance variables) and methods, accessed via dot notation.\nClass variable − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class methods.\n Class variables are not used as frequently as instance variables are.Data member − A class variable or instance variable that holds data associated with a class and its objects.\nFunction overloading − The assignment of more than one behavior to a particular function. The operation \nperformed varies by the types of objects or arguments involved.\nInstance variable − A variable that is defined inside a method and belongs only to the current instance of a class.\nInheritance − The transfer of the characteristics of a class to other classes that are derived from it.\nInstance − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.\nInstantiation − The creation of an instance of a class.\nMethod − A special kind of function that is defined in a class definition.\nObject − A unique instance of a data structure that defined by its class. An object comprises both data members \n(class variables and instance variables) and methods.\nOperator overloading − The assignment of more than one function to a particular operator.")
label2.pack(pady=20, padx=20, side='left', fill='x')
title2= Label(tab2, text="Week 2", font=("Times", 20), fg="#349310", bg="#F4F4A3")
title2.pack(pady=30, fill='x')

label3= Label(tab2, font=("Times", 15), text="Python has been an object-oriented language since it existed. Because of this, creating and using classes and objects are downright easy.\n This chapter helps you become an expert in using Python's object-oriented programming support.\nIf you do not have any previous experience with object-oriented (OO) programming, you may want to consult\n an introductory course on it or at least a tutorial of some sort so that you have a grasp of the basic concepts\n.However, here is small introduction of Object-Oriented Programming (OOP) to bring you at speed −\n\nOverview of OOP Terminology\n\nClass − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class.\nThe attributes are data members (class variables and instance variables) and methods, accessed via dot notation.\nClass variable − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class methods.\n Class variables are not used as frequently as instance variables are.Data member − A class variable or instance variable that holds data associated with a class and its objects.\nFunction overloading − The assignment of more than one behavior to a particular function. The operation \nperformed varies by the types of objects or arguments involved.\nInstance variable − A variable that is defined inside a method and belongs only to the current instance of a class.\nInheritance − The transfer of the characteristics of a class to other classes that are derived from it.\nInstance − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.\nInstantiation − The creation of an instance of a class.\nMethod − A special kind of function that is defined in a class definition.\nObject − A unique instance of a data structure that defined by its class. An object comprises both data members \n(class variables and instance variables) and methods.\nOperator overloading − The assignment of more than one function to a particular operator.")
label3.pack(pady=20, padx=20, side='left', fill='x')
title3= Label(tab3, text="Week 3", font=("Times", 20), fg="#349310", bg="#F4F4A3")
title3.pack(pady=30, fill='x')

label4= Label(tab3, font=("Times", 15), text="Python has been an object-oriented language since it existed. Because of this, creating and using classes and objects are downright easy.\n This chapter helps you become an expert in using Python's object-oriented programming support.\nIf you do not have any previous experience with object-oriented (OO) programming, you may want to consult\n an introductory course on it or at least a tutorial of some sort so that you have a grasp of the basic concepts\n.However, here is small introduction of Object-Oriented Programming (OOP) to bring you at speed −\n\nOverview of OOP Terminology\n\nClass − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class.\nThe attributes are data members (class variables and instance variables) and methods, accessed via dot notation.\nClass variable − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class methods.\n Class variables are not used as frequently as instance variables are.Data member − A class variable or instance variable that holds data associated with a class and its objects.\nFunction overloading − The assignment of more than one behavior to a particular function. The operation \nperformed varies by the types of objects or arguments involved.\nInstance variable − A variable that is defined inside a method and belongs only to the current instance of a class.\nInheritance − The transfer of the characteristics of a class to other classes that are derived from it.\nInstance − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.\nInstantiation − The creation of an instance of a class.\nMethod − A special kind of function that is defined in a class definition.\nObject − A unique instance of a data structure that defined by its class. An object comprises both data members \n(class variables and instance variables) and methods.\nOperator overloading − The assignment of more than one function to a particular operator.")
label4.pack(pady=20, padx=20, side='left', fill='x')
title4= Label(tab4, text="Week 4", font=("Times", 20), fg="#349310", bg="#F4F4A3")
title4.pack(pady=30, fill='x')
label5= Label(tab4, font=("Times", 15), text="Python has been an object-oriented language since it existed. Because of this, creating and using classes and objects are downright easy.\n This chapter helps you become an expert in using Python's object-oriented programming support.\nIf you do not have any previous experience with object-oriented (OO) programming, you may want to consult\n an introductory course on it or at least a tutorial of some sort so that you have a grasp of the basic concepts\n.However, here is small introduction of Object-Oriented Programming (OOP) to bring you at speed −\n\nOverview of OOP Terminology\n\nClass − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class.\nThe attributes are data members (class variables and instance variables) and methods, accessed via dot notation.\nClass variable − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class methods.\n Class variables are not used as frequently as instance variables are.Data member − A class variable or instance variable that holds data associated with a class and its objects.\nFunction overloading − The assignment of more than one behavior to a particular function. The operation \nperformed varies by the types of objects or arguments involved.\nInstance variable − A variable that is defined inside a method and belongs only to the current instance of a class.\nInheritance − The transfer of the characteristics of a class to other classes that are derived from it.\nInstance − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.\nInstantiation − The creation of an instance of a class.\nMethod − A special kind of function that is defined in a class definition.\nObject − A unique instance of a data structure that defined by its class. An object comprises both data members \n(class variables and instance variables) and methods.\nOperator overloading − The assignment of more than one function to a particular operator.")
label5.pack(pady=20, padx=20, side='left', fill='x')


def button_countdown(root,i, label):                                 #for timer
    if i > 0:
        i -= 1
        label.set(i)
        root.after(1000, lambda: button_countdown(root,i, label))
    else:
        if (pressed==True):                 #so tht if submit button is clicked again screen should not appear if counter=0
            pass
        else:
            close(root)

def close(root):
    root.destroy()
    cal_score()


def cal_score():
    score=0

    g1 = v1.get()
    g2 = v2.get()
    g3 = v3.get()
    g4 = v4.get()
    g5 = v5.get()

    if g1== 4:
        score = score + 1

    if g2== 7:
        score = score + 1


    if g3 == 9:
        score = score + 1


    if g4 == 15:
        score = score + 1


    if g5== 17:
        score = score + 1


    root1 = Tk()                            #new window
    root1.geometry('3000x3000')


    mainFrame = Frame(root1, height=3000)
    canvas = Canvas(mainFrame)
    scrollbar = Scrollbar(mainFrame,
                          orient='vertical',
                          command=canvas.yview
                          )

    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        '<Configure>',
        lambda e: canvas.configure(
            scrollregion=canvas.bbox('all')
        )
    )

    canvas.create_window((0, 0),
                         window=scrollable_frame,
                         anchor='nw'
                         )

    root1.title("CN QUIZ")
    question_answer = [
        {
            'question': '1.Application layer protocol defines:',
            'answer': ['types of messages exchanged', 'message format, syntax and semantics', 'rules for when and how processes send and respond to messages', 'all of the above']
        },

        {
            'question': '2.The network layer concerns with:',
            'answer': ['bits', 'frames', 'packets', 'none of the above']
        },

        {
            'question': '3.Simple mail transfer protocol (SMTP) utilizes ____ as the transport layer protocol for electronic mail transfer.',
            'answer': ['TCP', 'UDP', 'SCTP','DCCP']
        },

        {
            'question': '4.The HTTP request message is sent in ____ part of three-way handshake.',
            'answer': ['First', 'Second','Third','None of the above']
        },
        {
            'question': '5.The physical layer concerns with:',
            'answer': ['bit by bit delivery', 'process to process delivery', 'application to application delivery', 'none of the above']
        }
    ]


    f0 = Frame(scrollable_frame, width=800, height=40)
    Label(f0, text="ASSIGNMENT RESULTS", font="lucida 23 bold", height=0, fg="white", bg="black").pack(anchor="center",
                                                                                                       side="top",
                                                                                                       padx=580)
    f0.pack(side="top")
    Label(scrollable_frame, text="Thank you for answering the questions. " + str(score) + " of " + str(
        len(question_answer)) + " questions answered right", font="Verdana 15 bold", relief='solid', bg='green',
          fg='white').pack(anchor="center", pady=25, ipadx=10)

    label1 = Label(scrollable_frame, text=question_answer[0]['question'], font="lucida 12 normal")
    label1.pack(anchor='w')

    if g1==4:
        labela = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
        labela.pack(anchor='e')
    elif g1!=4:
        labela = Label(scrollable_frame, text='0 point', font="lucida 10 bold")
        labela.pack(anchor='e')

    l101 =Label(scrollable_frame, text="a)"+" "+question_answer[0]['answer'][0],font="lucida 12 normal")
    l101.pack(anchor='w')

    l111= Label(scrollable_frame, text="b)"+" "+question_answer[0]['answer'][1],font="lucida 12 normal")
    l111.pack(anchor='w')

    l121 = Label(scrollable_frame, text="c)"+" "+question_answer[0]['answer'][2], font="lucida 12 normal")
    l121.pack(anchor='w')

    l131 = Label(scrollable_frame, text="d)"+" "+question_answer[0]['answer'][3],fg="green",font="lucida 12 normal")
    l131.pack(anchor='w')

    labela1 = Label(scrollable_frame, text='Your Answer:', font="lucida 12 bold")
    labela1.pack(anchor='w')

    if g1==4:
        labela1 = Label(scrollable_frame, text='Right',fg="green", font="lucida 12 bold")
        labela1.pack(anchor='w')
    elif g1 != 4:
        labela1 = Label(scrollable_frame, text='Wrong',fg="red", font="lucida 12 bold")
        labela1.pack(anchor='w')

    label = Label(scrollable_frame, text=' ', font="lucida 12 bold")
    label.pack()

    label21 = Label(scrollable_frame, text=question_answer[1]['question'], font="lucida 12 normal")
    label21.pack(anchor='w')


    if g2==7:
        labelb = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
        labelb.pack(anchor='e')
    elif g2!=7:
        labelb = Label(scrollable_frame, text='0 point', font="lucida 10 bold")
        labelb.pack(anchor='e')

    l201= Label(scrollable_frame, text="a)"+" "+question_answer[1]['answer'][0],font="lucida 12 normal")
    l201.pack(anchor='w')

    l211 = Label(scrollable_frame, text="b)"+" "+question_answer[1]['answer'][1],font="lucida 12 normal")
    l211.pack(anchor='w')

    l221 =Label(scrollable_frame, text="c)"+" "+question_answer[1]['answer'][2], fg="green",font="lucida 12 normal")
    l221.pack(anchor='w')

    l231 = Label(scrollable_frame, text="d)"+" "+question_answer[1]['answer'][3],font="lucida 12 normal")
    l231.pack(anchor='w')

    labelb1 = Label(scrollable_frame, text='Your Answer:', font="lucida 12 bold")
    labelb1.pack(anchor='w')

    if g2== 7:
        labelb1 = Label(scrollable_frame, text='Right', fg="green", font="lucida 12 bold")
        labelb1.pack(anchor='w')
    elif g2 != 7:
        labelb1 = Label(scrollable_frame, text='Wrong', fg="red", font="lucida 12 bold")
        labelb1.pack(anchor='w')

    label = Label(scrollable_frame, text=' ', font="lucida 12 bold")
    label.pack()

    label31 = Label(scrollable_frame, text=question_answer[2]['question'], font="lucida 12 normal")
    label31.pack(anchor='w')

    if g3==9:
        labelc = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
        labelc.pack(anchor='e')
    elif g3!=9:
        labelc = Label(scrollable_frame, text='0 point', font="lucida 10 bold")
        labelc.pack(anchor='e')

    l301 =Label(scrollable_frame, text="a)"+" "+question_answer[2]['answer'][0],fg="green", font="lucida 12 normal")
    l301.pack(anchor='w')

    l311 = Label(scrollable_frame, text="b)"+" "+question_answer[2]['answer'][1],font="lucida 12 normal")
    l311.pack(anchor='w')

    l321 = Label(scrollable_frame, text="c)"+" "+question_answer[2]['answer'][2],font="lucida 12 normal")
    l321.pack(anchor='w')

    l331 = Label(scrollable_frame, text="d)"+" "+question_answer[2]['answer'][3],font="lucida 12 normal")
    l331.pack(anchor='w')

    labelc1 = Label(scrollable_frame, text='Your Answer:', font="lucida 12 bold")
    labelc1.pack(anchor='w')

    if g3 == 9:
        labelc1 = Label(scrollable_frame, text='Right', fg="green", font="lucida 12 bold")
        labelc1.pack(anchor='w')
    elif g3 != 9:
        labelc1 = Label(scrollable_frame, text='Wrong', fg="red", font="lucida 12 bold")
        labelc1.pack(anchor='w')

    label = Label(scrollable_frame, text=' ', font="lucida 12 bold")
    label.pack()

    label4 = Label(scrollable_frame, text=question_answer[3]['question'], font="lucida 12 normal")
    label4.pack(anchor='w')

    if g4==15:
        labeld = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
        labeld.pack(anchor='e')
    elif g4!=15:
        labeld = Label(scrollable_frame, text='0 point', font="lucida 10 bold")
        labeld.pack(anchor='e')

    l401 = Label(scrollable_frame, text="a)"+" "+question_answer[3]['answer'][0],font="lucida 12 normal")
    l401.pack(anchor='w')

    l411 = Label(scrollable_frame, text="b)"+" "+question_answer[3]['answer'][1],font="lucida 12 normal")
    l411.pack(anchor='w')

    l421 = Label(scrollable_frame, text="c)"+" "+question_answer[3]['answer'][2],fg="green",font="lucida 12 normal")
    l421.pack(anchor='w')

    l431 =Label(scrollable_frame, text="d)"+" "+question_answer[3]['answer'][3], font="lucida 12 normal")
    l431.pack(anchor='w')

    labeld1 = Label(scrollable_frame, text='Your Answer:', font="lucida 12 bold")
    labeld1.pack(anchor='w')

    if g4 == 15:
        labeld1 = Label(scrollable_frame, text='Right', fg="green", font="lucida 12 bold")
        labeld1.pack(anchor='w')
    elif g4 != 15:
        labeld1 = Label(scrollable_frame, text='Wrong', fg="red", font="lucida 12 bold")
        labeld1.pack(anchor='w')

    label = Label(scrollable_frame, text=' ', font="lucida 12 bold")
    label.pack()

    label5 = Label(scrollable_frame, text=question_answer[4]['question'], font="lucida 12 normal")
    label5.pack(anchor='w')

    if g5==17:
        labele = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
        labele.pack(anchor='e')
    elif g5!=17:
        labele = Label(scrollable_frame, text='0 point', font="lucida 10 bold")
        labele.pack(anchor='e')

    l501 = Label(scrollable_frame, text="a)"+" "+question_answer[4]['answer'][0],fg="green",font="lucida 12 normal")
    l501.pack(anchor='w')

    l511 = Label(scrollable_frame, text="b)"+" "+question_answer[4]['answer'][1],font="lucida 12 normal")
    l511.pack(anchor='w')

    l521 =Label(scrollable_frame, text="c)"+" "+question_answer[4]['answer'][2],font="lucida 12 normal")
    l521.pack(anchor='w')

    l531 = Label(scrollable_frame, text="d)"+" "+question_answer[4]['answer'][3],font="lucida 12 normal")
    l531.pack(anchor='w')

    labele1 = Label(scrollable_frame, text='Your Answer:', font="lucida 12 bold")
    labele1.pack(anchor='w')

    if g5 == 17:
        labele1 = Label(scrollable_frame, text='Right', fg="green", font="lucida 12 bold")
        labele1.pack(anchor='w')
    elif g5 != 17:
        labele1 = Label(scrollable_frame, text='Wrong', fg="red", font="lucida 12 bold")
        labele1.pack(anchor='w')

    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side='right', fill='y')

    canvas.pack(fill='both', expand=True)
    mainFrame.pack(fill='both', expand=True)
    root1.mainloop()

pressed=False
def count_check():

    global pressed
    pressed=TRUE
    cal_score()


def cnquiz():
    app.destroy()
    root = Tk()
    root.geometry('3000x3000')
    root.title("VESIT")

    mainFrame = Frame(root, height=3000)

    canvas = Canvas(mainFrame)
    scrollbar = Scrollbar(mainFrame,
                          orient='vertical',
                          command=canvas.yview
                          )

    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        '<Configure>',
        lambda e: canvas.configure(
            scrollregion=canvas.bbox('all')
        )
    )

    canvas.create_window((0, 0),
                         window=scrollable_frame,
                         anchor='nw'
                         )

    logo1 = PhotoImage(file="newwww.png")
    w1 = Label(root,
               image=logo1
               )

    w1.pack(anchor="center", side="top", pady=50)

    root.title("CN QUIZ")
    question_answer = [
        {
            'question': '1.Application layer protocol defines:',
            'answer': ['types of messages exchanged', 'message format, syntax and semantics',
                       'rules for when and how processes send and respond to messages', 'all of the above']
        },

        {
            'question': '2.The network layer concerns with:',
            'answer': ['bits', 'frames', 'packets', 'none of the above']
        },

        {
            'question': '3.Simple mail transfer protocol (SMTP) utilizes ____ as the transport layer protocol for electronic mail transfer.',
            'answer': ['TCP', 'UDP', 'SCTP', 'DCCP']
        },

        {
            'question': '4.The HTTP request message is sent in ____ part of three-way handshake.',
            'answer': ['First', 'Second', 'Third', 'None of the above']
        },
        {
            'question': '5.The physical layer concerns with:',
            'answer': ['bit by bit delivery', 'process to process delivery', 'application to application delivery',
                       'none of the above']
        }
    ]

    f0 = Frame(scrollable_frame, width=800, height=40)
    Label(f0, text="CN ASSIGNMENT", font="lucida 23 bold", height=0, fg="white", bg="black").pack(anchor="center",
                                                                                                  side="top", padx=620)
    f0.pack(side='top')

    counter = 10
    button_label = StringVar()
    button_label.set(counter)
    pressed = False
    button_countdown(root, counter, button_label)
    f0.pack(side='top')
    label = Label(scrollable_frame, text='Time left to complete assignment:', font="lucida 12 bold")
    label.pack(anchor='nw')

    Button(scrollable_frame, fg="white", padx=120, pady=5, bg='black', textvariable=button_label, command=close).pack(
        anchor="nw")

    global v1
    global v2
    global v3
    global v4
    global v5
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    v5 = IntVar()
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    v5 = IntVar()
    label = Label(scrollable_frame, text=' ', font="lucida 12 normal")
    label.pack(anchor='w')

    label = Label(scrollable_frame, text=question_answer[0]['question'], font="lucida 12 normal")
    label.pack(anchor='w')

    labela = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
    labela.pack(anchor='e')

    Rb10 = Radiobutton(scrollable_frame, text=question_answer[0]['answer'][0], variable=v1, value=1,
                       font="lucida 12 normal")
    Rb10.pack(anchor='w')

    Rb11 = Radiobutton(scrollable_frame, text=question_answer[0]['answer'][1], variable=v1, value=2,
                       font="lucida 12 normal")
    Rb11.pack(anchor='w')

    Rb12 = Radiobutton(scrollable_frame, text=question_answer[0]['answer'][2], variable=v1, value=3,
                       font="lucida 12 normal")
    Rb12.pack(anchor='w')

    Rb13 = Radiobutton(scrollable_frame, text=question_answer[0]['answer'][3], variable=v1, value=4,
                       font="lucida 12 normal")
    Rb13.pack(anchor='w')

    label = Label(scrollable_frame, text=' ', font="lucida 10 bold")
    label.pack()

    label2 = Label(scrollable_frame, text=question_answer[1]['question'], font="lucida 12 normal")
    label2.pack(anchor='w')

    labelb = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
    labelb.pack(anchor='e')

    Rb20 = Radiobutton(scrollable_frame, text=question_answer[1]['answer'][0], variable=v2, value=5,
                       font="lucida 12 normal")
    Rb20.pack(anchor='w')

    Rb21 = Radiobutton(scrollable_frame, text=question_answer[1]['answer'][1], variable=v2, value=6,
                       font="lucida 12 normal")
    Rb21.pack(anchor='w')

    Rb22 = Radiobutton(scrollable_frame, text=question_answer[1]['answer'][2], variable=v2, value=7,
                       font="lucida 12 normal")
    Rb22.pack(anchor='w')

    Rb23 = Radiobutton(scrollable_frame, text=question_answer[1]['answer'][3], variable=v2, value=8,
                       font="lucida 12 normal")
    Rb23.pack(anchor='w')

    label = Label(scrollable_frame, text=' ', font="lucida 12 bold")
    label.pack()

    label3 = Label(scrollable_frame, text=question_answer[2]['question'], font="lucida 12 normal")
    label3.pack(anchor='w')

    labelc = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
    labelc.pack(anchor='e')

    Rb30 = Radiobutton(scrollable_frame, text=question_answer[2]['answer'][0], variable=v3, value=9,
                       font="lucida 12 normal")
    Rb30.pack(anchor='w')

    Rb31 = Radiobutton(scrollable_frame, text=question_answer[2]['answer'][1], variable=v3, value=10,
                       font="lucida 12 normal")
    Rb31.pack(anchor='w')

    Rb32 = Radiobutton(scrollable_frame, text=question_answer[2]['answer'][2], variable=v3, value=11,
                       font="lucida 12 normal")
    Rb32.pack(anchor='w')

    Rb33 = Radiobutton(scrollable_frame, text=question_answer[2]['answer'][3], variable=v3, value=12,
                       font="lucida 12 normal")
    Rb33.pack(anchor='w')

    label = Label(scrollable_frame, text=' ', font="lucida 10 bold")
    label.pack()

    label4 = Label(scrollable_frame, text=question_answer[3]['question'], font="lucida 12 normal")
    label4.pack(anchor='w')

    labeld = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
    labeld.pack(anchor='e')

    Rb40 = Radiobutton(scrollable_frame, text=question_answer[3]['answer'][0], variable=v4, value=13,
                       font="lucida 12 normal")
    Rb40.pack(anchor='w')

    Rb41 = Radiobutton(scrollable_frame, text=question_answer[3]['answer'][1], variable=v4, value=14,
                       font="lucida 12 normal")
    Rb41.pack(anchor='w')

    Rb42 = Radiobutton(scrollable_frame, text=question_answer[3]['answer'][2], variable=v4, value=15,
                       font="lucida 12 normal")
    Rb42.pack(anchor='w')

    Rb43 = Radiobutton(scrollable_frame, text=question_answer[3]['answer'][3], variable=v4, value=16,
                       font="lucida 12 normal")
    Rb43.pack(anchor='w')

    label = Label(scrollable_frame, text=' ', font="lucida 10 bold")
    label.pack()

    label5 = Label(scrollable_frame, text=question_answer[4]['question'], font="lucida 12 normal")
    label5.pack(anchor='w')

    labele = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
    labele.pack(anchor='e')

    Rb50 = Radiobutton(scrollable_frame, text=question_answer[4]['answer'][0], variable=v5, value=17,
                       font="lucida 12 normal")
    Rb50.pack(anchor='w')

    Rb51 = Radiobutton(scrollable_frame, text=question_answer[4]['answer'][1], variable=v5, value=18,
                       font="lucida 12 normal")
    Rb51.pack(anchor='w')

    Rb52 = Radiobutton(scrollable_frame, text=question_answer[4]['answer'][2], variable=v5, value=19,
                       font="lucida 12 normal")
    Rb52.pack(anchor='w')

    Rb53 = Radiobutton(scrollable_frame, text=question_answer[4]['answer'][3], variable=v5, value=20,
                       font="lucida 12 normal")
    Rb53.pack(anchor='w')
    submit = Button(scrollable_frame, text="SUBMIT", fg="white", command=count_check, padx=15, pady=5, bg='Maroon')
    submit.pack(anchor='c', ipadx=50)

    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side='right', fill='y')

    canvas.pack(fill='both', expand=True)
    mainFrame.pack(fill='both', expand=True)

    root.mainloop()





submit = Button(scrollable_frame, text="Go for Quiz", fg="white", bg='Maroon',command=cnquiz)
submit.pack(anchor='center', ipadx=50,side="bottom")

#to the bottom
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
canvas.pack(fill='both', expand=True)
mainFrame.pack(fill='both', expand=True)



app.mainloop()

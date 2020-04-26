import cv2
from tkinter import *
from tkinter import ttk
  
app = Tk()
#app.geometry("1000x1000")
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
photo1 = PhotoImage(file = r"Pythontopic.png")
Label(scrollable_frame, image=photo1, bg="black").pack(pady=20, fill='x')
label1=Label(scrollable_frame, text= 'Click here for video lecture', font=("Times", 10), fg="black", bg="#4C65DC")
label1.pack()

#canvas.pack(fill='both', expand='True')  
#canvas.config(width=480,height=360)  
#line=canvas.create_line(25,25,200,25,fill='blue',width=5)
photo = PhotoImage(file = r"pythonpic.png") 
  
# here, image option is used to 
# set image on button
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
            cv2.imshow('Frame', frame)

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


#to the bottom
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
canvas.pack(fill='both', expand=True)
mainFrame.pack(fill='both', expand=True)



app.mainloop()

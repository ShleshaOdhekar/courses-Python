import cv2
from tkinter import *
from tkinter import ttk
from ffpyplayer.player import MediaPlayer

    
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
photo1 = PhotoImage(file = r"ostopic.png")
Label(scrollable_frame, image=photo1, bg="brown").pack(pady=20, fill='x')
label1=Label(scrollable_frame, text= 'Click here for video lecture', font=("Times", 10), fg="black", bg="#4C65DC")
label1.pack()

#canvas.pack(fill='both', expand='True')  
#canvas.config(width=480,height=360)  
#line=canvas.create_line(25,25,200,25,fill='blue',width=5)
photo = PhotoImage(file = r"oslec.png") 
  
# here, image option is used to 
# set image on button
def rescale_frame(frame, percent=250):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
def play_vid():
    cap = cv2.VideoCapture('vid3.mp4')
    player = MediaPlayer('vid3.mp4')
    # Check if camera opened successfully
    if (cap.isOpened()== False):
      print("Error opening video stream or file")

    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame

        ret, frame = cap.read()
        audio_frame, val = player.get_frame()
        #farme.read()
        if ret == True:

            # Display the resulting frame
            frame75= rescale_frame(frame, percent=200)
            cv2.imshow('Frame', frame75)
            if val != 'eof' and audio_frame is not None:
            #audio
                img, t = audio_frame
            key = cv2.waitKey(28)
            if key == ord('q'):
                break
            if key == ord('p'):
                player.toggle_pause()
                cv2.waitKey(-1) #wait until any key is pressed
                player.toggle_pause()
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

label2= Label(tab1, font=("Times", 15), text="Following are some of important functions of an operating System.\n\nMemory Management\n\nProcessor Management\n\nDevice Management\n\nFile Management\n\nSecurity\n\nControl over system performance\n\nJob accounting\n\nError detecting aids\n\nCoordination between other software and users\n\n")
label2.pack(pady=20, padx=20, fill='x')
title2= Label(tab2, text="Week 2", font=("Times", 20), fg="#349310", bg="#F4F4A3")
title2.pack(pady=30, fill='x')

label3= Label(tab2, font=("Times", 15), text="Memory Management\n\nMemory management refers to management of Primary Memory or Main Memory. Main memory is a large array of words or bytes where each word or byte has its own address.\nMain memory provides a fast storage that can be accessed directly by the CPU. For a program to be executed, it must in the main memory.\nAn Operating System does the following activities for memory management −\nKeeps tracks of primary memory, i.e., what part of it are in use by whom, what part are not in use.\nIn multiprogramming, the OS decides which process will get memory when and how much.\nAllocates the memory when a process requests it to do so.\nDe-allocates the memory when a process no longer needs it or has been terminated.\n\nProcessor Management\n\nIn multiprogramming environment, the OS decides which process gets the processor when and for how much time. This function is called process scheduling.\nAn Operating System does the following activities for processor management −\nKeeps tracks of processor and status of process. The program responsible for this task is known as traffic controller.\nAllocates the processor (CPU) to a process.\nDe-allocates processor when a process is no longer required.\n\nDevice Management\n\nAn Operating System manages device communication via their respective drivers. It does the following activities for device management −\nKeeps tracks of all devices. Program responsible for this task is known as the I/O controller.\nDecides which process gets the device when and for how much time.\nAllocates the device in the efficient way.\nDe-allocates devices.\n")
label3.pack(pady=20, padx=20, fill='x')
title3= Label(tab3, text="Week 3", font=("Times", 20), fg="#349310", bg="#F4F4A3")
title3.pack(pady=30, fill='x')

label4= Label(tab3, font=("Times", 15), text="The process scheduling is the activity of the process manager that handles the removal of the running process from the CPU and the selection of another process\non the basis of a particular strategy.\nProcess scheduling is an essential part of a Multiprogramming operating systems. Such operating systems allow more than one process to be loaded into the\nexecutable memory at a time and the loaded process shares the CPU using time multiplexing.\n\nProcess Scheduling Queues\n\nThe OS maintains all PCBs in Process Scheduling Queues. The OS maintains a separate queue for each of the process states and PCBs of all processes\nin the same execution state are placed in the same queue. When the state of a process is changed, its PCB is unlinked from its current queue and \nmoved to its new state queue.\n\nThe Operating System maintains the following important process scheduling queues −\n\nJob queue − This queue keeps all the processes in the system.\nReady queue − This queue keeps a set of all processes residing in main memory, ready and waiting to execute. A new process is always put in this queue.\nDevice queues − The processes which are blocked due to unavailability of an I/O device constitute this queue.\n\nSchedulers\n\nSchedulers are special system software which handle process scheduling in various ways.\n\n Their main task is to select the jobs to be submitted into the system and to decide which process to run.\n \nSchedulers are of three types −\n\nLong-Term Scheduler\n\nShort-Term Scheduler\n\nMedium-Term Scheduler\n")
label4.pack(pady=20, padx=20, fill='x')
title4= Label(tab4, text="Week 4", font=("Times", 20), fg="#349310", bg="#F4F4A3")
title4.pack(pady=30, fill='x')
label5= Label(tab4, font=("Times", 15), text="Algorithms\n\nA Process Scheduler schedules different processes to be assigned to the CPU based on particular scheduling algorithms.\n\nThere are six popular process scheduling algorithms which we are going to discuss in this chapter −\n\nFirst-Come, First-Served (FCFS) Scheduling\n\nShortest-Job-Next (SJN) Scheduling\n\nPriority Scheduling\n\nShortest Remaining Time\n\nRound Robin(RR) Scheduling\n\nMultiple-Level Queues Scheduling\n\nThese algorithms are either non-preemptive or preemptive. Non-preemptive algorithms are designed so that once a process enters the running state,\nit cannot be preempted until it completes its allotted time, whereas the preemptive scheduling is based on priority where a scheduler may preempt\na low priority running process anytime when a high priority process enters into a ready state.\n\nFirst Come First Serve (FCFS)\n\nJobs are executed on first come, first serve basis.\nIt is a non-preemptive, pre-emptive scheduling algorithm.\nEasy to understand and implement.\nIts implementation is based on FIFO queue.\nPoor in performance as average wait time is high.\n")
label5.pack(pady=20, padx=20, fill='x')


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

    if g1 == 1:
        score = score + 1

    if g2 == 6:
        score = score + 1

    if g3 == 9:
        score = score + 1

    if g4 == 13:
        score = score + 0.5
    elif g4 == 14:
        score = score + 0.5
    elif g4 == 15:
        score = score + 1

    if g5 == 19:
        score = score + 1

    root1 = Tk()  # new window
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

    root1.title("OS QUIZ")
    question_answer = [
        {
            'question': '1.To access the services of operating system, the interface is provided by the:',
            'answer': ['system calls', 'API', 'library', 'assembly instructions']
        },

        {
            'question': '2.Which one of the following is the deadlock avoidance algorithm?',
            'answer': ['elevator algorithm', 'bankers algorithm', 'round-robin algorithm', 'karns algorithm']
        },
        {
            'question': '3.Which module gives control of the CPU to the process selected by the short-term scheduler?',
            'answer': ['dispatcher', 'scheduler', 'interrupt', 'one of the above']
        },
        {
            'question': '4.A system is in the safe state if:',
            'answer': ['the system can allocate resources to each process in some order and still avoid a deadlock',
                       'there exist a safe sequence', 'both (a) and (b)', 'none of the above']
        },
        {
            'question': '5.Semaphore is a/an _______ to solve the critical section problem.',
            'answer': ['hardware for a system', 'special program for a system', 'integer variable', 'none of the above']
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

    if g1 == 1:
        labela = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
        labela.pack(anchor='e')
    elif g1 != 1:
        labela = Label(scrollable_frame, text='0 point', font="lucida 10 bold")
        labela.pack(anchor='e')

    l101 = Label(scrollable_frame, text="a)" + " " + question_answer[0]['answer'][0], fg="green",
                 font="lucida 12 normal")
    l101.pack(anchor='w')

    l111 = Label(scrollable_frame, text="b)" + " " + question_answer[0]['answer'][1], font="lucida 12 normal")
    l111.pack(anchor='w')

    l121 = Label(scrollable_frame, text="c)" + " " + question_answer[0]['answer'][2], font="lucida 12 normal")
    l121.pack(anchor='w')

    l131 = Label(scrollable_frame, text="d)" + " " + question_answer[0]['answer'][3], font="lucida 12 normal")
    l131.pack(anchor='w')

    labela1 = Label(scrollable_frame, text='Your Answer:', font="lucida 12 bold")
    labela1.pack(anchor='w')

    if g1 == 1:
        labela1 = Label(scrollable_frame, text='Right', fg="green", font="lucida 12 bold")
        labela1.pack(anchor='w')
    elif g1 != 1:
        labela1 = Label(scrollable_frame, text='Wrong', fg="red", font="lucida 12 bold")
        labela1.pack(anchor='w')

    label = Label(scrollable_frame, text=' ', font="lucida 12 bold")
    label.pack()

    label21 = Label(scrollable_frame, text=question_answer[1]['question'], font="lucida 12 normal")
    label21.pack(anchor='w')

    if g2 == 6:
        labelb = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
        labelb.pack(anchor='e')
    elif g2 != 6:
        labelb = Label(scrollable_frame, text='0 point', font="lucida 10 bold")
        labelb.pack(anchor='e')

    l201 = Label(scrollable_frame, text="a)" + " " + question_answer[1]['answer'][0], font="lucida 12 normal")
    l201.pack(anchor='w')

    l211 = Label(scrollable_frame, text="b)" + " " + question_answer[1]['answer'][1], fg="green",
                 font="lucida 12 normal")
    l211.pack(anchor='w')

    l221 = Label(scrollable_frame, text="c)" + " " + question_answer[1]['answer'][2], font="lucida 12 normal")
    l221.pack(anchor='w')

    l231 = Label(scrollable_frame, text="d)" + " " + question_answer[1]['answer'][3], font="lucida 12 normal")
    l231.pack(anchor='w')

    labelb1 = Label(scrollable_frame, text='Your Answer:', font="lucida 12 bold")
    labelb1.pack(anchor='w')

    if g2 == 6:
        labelb1 = Label(scrollable_frame, text='Right', fg="green", font="lucida 12 bold")
        labelb1.pack(anchor='w')
    elif g2 != 6:
        labelb1 = Label(scrollable_frame, text='Wrong', fg="red", font="lucida 12 bold")
        labelb1.pack(anchor='w')

    label = Label(scrollable_frame, text=' ', font="lucida 12 bold")
    label.pack()

    label31 = Label(scrollable_frame, text=question_answer[2]['question'], font="lucida 12 normal")
    label31.pack(anchor='w')

    if g3 == 9:
        labelc = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
        labelc.pack(anchor='e')
    elif g3 != 9:
        labelc = Label(scrollable_frame, text='0 point', font="lucida 10 bold")
        labelc.pack(anchor='e')

    l301 = Label(scrollable_frame, text="a)" + " " + question_answer[2]['answer'][0], fg="green",
                 font="lucida 12 normal")
    l301.pack(anchor='w')

    l311 = Label(scrollable_frame, text="b)" + " " + question_answer[2]['answer'][1], font="lucida 12 normal")
    l311.pack(anchor='w')

    l321 = Label(scrollable_frame, text="c)" + " " + question_answer[2]['answer'][2], font="lucida 12 normal")
    l321.pack(anchor='w')

    l331 = Label(scrollable_frame, text="d)" + " " + question_answer[2]['answer'][3], font="lucida 12 normal")
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

    if g4 == 15:
        labeld = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
        labeld.pack(anchor='e')
    elif g4 == 14:
        labeld = Label(scrollable_frame, text='0.5 point', font="lucida 10 bold")
        labeld.pack(anchor='e')
    elif g4 == 13:
        labeld = Label(scrollable_frame, text='0.5 point', font="lucida 10 bold")
        labeld.pack(anchor='e')
    elif g4 == 16:
        labeld = Label(scrollable_frame, text='0 point', font="lucida 10 bold")
        labeld.pack(anchor='e')

    l401 = Label(scrollable_frame, text="a)" + " " + question_answer[3]['answer'][0], font="lucida 12 normal")
    l401.pack(anchor='w')

    l411 = Label(scrollable_frame, text="b)" + " " + question_answer[3]['answer'][1], font="lucida 12 normal")
    l411.pack(anchor='w')

    l421 = Label(scrollable_frame, text="c)" + " " + question_answer[3]['answer'][2], fg="green",
                 font="lucida 12 normal")
    l421.pack(anchor='w')

    l431 = Label(scrollable_frame, text="d)" + " " + question_answer[3]['answer'][3], font="lucida 12 normal")
    l431.pack(anchor='w')

    labeld1 = Label(scrollable_frame, text='Your Answer:', font="lucida 12 bold")
    labeld1.pack(anchor='w')
    if g4 == 15:
        labeld1 = Label(scrollable_frame, text='Right', fg="green", font="lucida 12 bold")
        labeld1.pack(anchor='w')
        score = score + 1
    elif g4 == 14:
        labeld1 = Label(scrollable_frame, text='Partially Right', fg="green", font="lucida 12 bold")
        labeld1.pack(anchor='w')
        score = score + 0.5
    elif g4 == 13:
        labeld1 = Label(scrollable_frame, text='Partially Right', fg="green", font="lucida 12 bold")
        labeld1.pack(anchor='w')
        score = score + 0.5
    elif g4 != 13 or g4 != 14 or g4 != 15:
        labeld1 = Label(scrollable_frame, text='Wrong', fg="red", font="lucida 12 bold")
        labeld1.pack(anchor='w')

    label = Label(scrollable_frame, text=' ', font="lucida 12 bold")
    label.pack()

    label5 = Label(scrollable_frame, text=question_answer[4]['question'], font="lucida 12 normal")
    label5.pack(anchor='w')

    if g5 == 19:
        labele = Label(scrollable_frame, text='1 point', font="lucida 10 bold")
        labele.pack(anchor='e')
    elif g5 != 19:
        labele = Label(scrollable_frame, text='0 point', font="lucida 10 bold")
        labele.pack(anchor='e')

    l501 = Label(scrollable_frame, text="a)" + " " + question_answer[4]['answer'][0], font="lucida 12 normal")
    l501.pack(anchor='w')

    l511 = Label(scrollable_frame, text="b)" + " " + question_answer[4]['answer'][1], font="lucida 12 normal")
    l511.pack(anchor='w')

    l521 = Label(scrollable_frame, text="c)" + " " + question_answer[4]['answer'][2], fg="green",
                 font="lucida 12 normal")
    l521.pack(anchor='w')

    l531 = Label(scrollable_frame, text="d)" + " " + question_answer[4]['answer'][3], font="lucida 12 normal")
    l531.pack(anchor='w')

    labele1 = Label(scrollable_frame, text='Your Answer:', font="lucida 12 bold")
    labele1.pack(anchor='w')

    if g5 == 19:
        labele1 = Label(scrollable_frame, text='Right', fg="green", font="lucida 12 bold")
        labele1.pack(anchor='w')
    elif g5 != 19:
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

def osquiz():
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

    root.title("OS QUIZ")
    question_answer = [
        {
            'question': '1.To access the services of operating system, the interface is provided by the:',
            'answer': ['system calls', 'API', 'library', 'assembly instructions']
        },

        {
            'question': '2.Which one of the following is the deadlock avoidance algorithm?',
            'answer': ['elevator algorithm', 'bankers algorithm', 'round-robin algorithm', 'karns algorithm']
        },
        {
            'question': '3.Which module gives control of the CPU to the process selected by the short-term scheduler?',
            'answer': ['dispatcher', 'scheduler', 'interrupt', 'one of the above']
        },
        {
            'question': '4.A system is in the safe state if:',
            'answer': ['the system can allocate resources to each process in some order and still avoid a deadlock',
                       'there exist a safe sequence', 'both (a) and (b)', 'none of the above']
        },
        {
            'question': '5.Semaphore is a/an _______ to solve the critical section problem.',
            'answer': ['hardware for a system', 'special program for a system', 'integer variable', 'none of the above']
        }
    ]

    f0 = Frame(scrollable_frame, width=800, height=40)
    Label(f0, text="OS ASSIGNMENT", font="lucida 23 bold", height=0, fg="white", bg="black").pack(anchor="center",
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


submit = Button(scrollable_frame, text="Go for Quiz", fg="white", bg='Maroon',command=osquiz)
submit.pack(anchor='center', ipadx=50,side="bottom")

#to the bottom
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
canvas.pack(fill='both', expand=True)
mainFrame.pack(fill='both', expand=True)



app.mainloop()

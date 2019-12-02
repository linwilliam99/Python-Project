from tkinter import*
import project
def report(count,filename):
    win=Tk()
    win.title("*** words b-gone")
    win.geometry("630x400")

    topframe = Frame(win,bg='#6a736c',height='20')
    topframe.pack(fill=X)
    can1 = Canvas(topframe,height='20',bg="#6a736c",highlightthickness=0)
    can1.pack(side=LEFT, padx=5, pady=5)

    invisoframe = Frame(win,width=200,height=250) # invisible container frame
    invisoframe.pack()
    titleheight = 100 # set variable to height of title frame
    titleframe = Frame(invisoframe,width=500,height=titleheight,bg="#1c1f1d") # top title frame
    titleframe.pack(fill=X) # fill entire container frame
    titleframe.pack_propagate(0) # enforce frame size, do not change to content size
    title = Label(titleframe,text="Welcome to Bad Words B-Gone",fg="white",bg="#1c1f1d")
    title.config(font=("Arial", 22))
    title.pack(ipady=titleheight/2) # set internal padding to place title in centre

    #Book Name Label
    bookname = Label(win, text = filename, borderwidth = 2, relief="raised", font = ('Sans','25','bold'))
    bookname.pack(anchor = 'nw', pady = 15, padx = 10)

    #Words Detected Label
    ewords = Label(win, text = """# of
    Explicit Words Detected
    = """ + str(count), borderwidth = 2, relief="raised")
    ewords.pack(side= LEFT, padx = 10)
    
    #Which Words Label
    detected = Label(win, text = """Words Detected
    Blah Blah Blah
    Yada Yada Yada""", borderwidth = 2, relief="raised")
    detected.pack(side= LEFT,)
    #PDF Download Button
    pdf = Button(win, text="""PDF Download""", state=DISABLED, font = ('Sans','25','bold'))
    pdf.pack(side = LEFT, padx = 10)



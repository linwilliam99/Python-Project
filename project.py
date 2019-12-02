from tkinter import filedialog
from tkinter import*
import project2
from better_profanity import profanity
win= Tk()

somewhat= IntVar()
clean = IntVar()
scean = IntVar()

def create_window():
    window=Toplevel(win)
win.title("*** words b-gone")
win.geometry("630x400")

def getFilename():
    content = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    print(content)
    if content is not None:
        count = removeBadWords(content)
        win.destroy()
        project2.report(count,content)
        

def removeBadWords(filename):
    fi = open(filename,"r")
    allwords = fi.readlines()
    fi.close()

    profanity.load_censor_words()
    badwords = profanity.CENSOR_WORDSET
    #print(badwords)
    count = 0
    censorwords(filename)

    for line in allwords:
        #print(line,"lines")
        for word in line.split():
            #print(word)
            if (word in badwords):
                count += 1
            
    return count
def censorwords(filename):
    fi = open(filename,"r")
    text = fi.read()
    censored_text = profanity.censor(text)
    print(filename[0:-4]+"censored.txt")
    write_to = open(filename[0:-4]+"censored.txt", "a+")
    write_to.write(censored_text)
    write_to.close()
    fi.close()






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


download = Label(win, text ="""Please Download a Novel From
https://openlibrary.org/""", borderwidth=2, relief="raised")
download.pack(anchor='nw', pady = 10)




select = Button(win, text="Please Select Your Book File ", command=getFilename, font = ('Sans','14','bold'))
select.pack(anchor = CENTER, pady = 20)


'''
somewhat = Checkbutton(win, text = "Somewhat Clean", variable = somewhat, \
                       onvalue = 1, offvalue = 0, height=5, \
                       width = 20)
somewhat.pack(side = LEFT)


clean = Checkbutton(win, text = "Clean", variable = clean, \
                       onvalue = 1, offvalue = 0, height=5, \
                       width = 20)
clean.pack(side = LEFT)

sclean =Checkbutton(win, text = "Squeaky Clean", variable = sclean, \
                       onvalue = 1, offvalue = 0, height=5, \
                       width = 20)
sclean.pack(side = LEFT)
'''

submit = Button(win, text="submit ", command=create_window, font = ('Sans','20','bold'))
submit.pack(side = RIGHT, pady = 20, padx=100)





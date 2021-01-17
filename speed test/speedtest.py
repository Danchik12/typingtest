from tkinter import *
import datetime
import random
from fuzzywuzzy import fuzz
start_tim=datetime.datetime.now().replace(microsecond=0)

words=["You have come very fast","Then reread the letter again","I am going to travel round the world","Linda likes collecting postcards",
       "John and his wife are from Sydney","Richard Nixon was the president of the USA","In the future robots will work at the factories",
       "My sister is having her hair cut at the moment","They said we should not wait for them","My favorite beach is called Emerson Beach",
       "Every morning we look for shells in the sand","I eat a sandwich and an apple"]

    
def worden(words):
    random.shuffle(words)
    random.choice(words)
    word=words[0]
    return word
def start(event):
    global start_tim
    start_tim=datetime.datetime.now().replace(microsecond=0)
    return start_tim


   
word=worden(words)

def accuracy(event):
    global start_tim
    text=entry.get()
    c=fuzz.ratio(word,text)
    ass['text']="точность "+str(c)+"%"
    now=datetime.datetime.now().replace(microsecond=0)
    timen=now-start_tim
    time['text']="Время "+str(timen)+"s"
    entry.config(state="readonly",fg="black")
    




    
root=Tk()
root.title("Speed test")
root.geometry("400x400")
root.configure(background='black')

label=Label(root,width=40,fg="yellow",bg="black",font=("Comic Sans MS",14, "bold"),height=5)
label['text']="Typing Speed Test"
label.pack(side=TOP)

lab=Label(root,width=40,fg="yellow",bg="black", font=("Comic Sans MS",10, "bold"),height=5)
lab['text']=word
lab.pack(side=TOP)

entry=Entry(root,width=40,fg="yellow",bg="black",font=("Comic Sans MS",10, "bold"),justify=CENTER,bd=5)
entry.bind('<Return>',accuracy)
entry.bind('<Button-1>',start)
entry.pack(side=TOP)

f1=Frame(root,bg="black")
f1.pack(side=TOP)

time=Label(f1,bg="black",fg="red",font=("Comic Sans MS",10, "bold"),width=18)
time.pack(side=LEFT)

ass=Label(f1,bg="black",fg="red",width=18,font=("Comic Sans MS",10, "bold"))
ass.pack(side=LEFT)




root.mainloop()



import tkinter
from tkinter import *

root=Tk()
root.title("TO DO LIST")
root.geometry("400x650+400+100")
root.resizable(False,False)


task_list= []

def addTask():
    task = t_entry.get()
    t_entry.delete(0,END)

    if task :
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def deletetask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)
def openTaskFile():

    try:
        global task_list
        with open("taskfile.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)

    except:
        file=open("tasklist.txt","w")
        file.close()
#icon

img_icn= PhotoImage(file="task.png")
root.iconphoto(False,img_icn)

#top bar
topimg = PhotoImage(file="topbar.png")
Label(root,image=topimg).pack()

dimg = PhotoImage(file="dock.png")
Label(root,image=dimg,bg="#32405b").place(x=30,y=25)

nimg = PhotoImage(file="task.png")
Label(root,image=nimg,bg="#32405b").place(x=340,y=18)

head=Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b")
head.place(x=130,y=20)

#main
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
t_entry=Entry(frame,width=18,font="arial 20",bd=0)
t_entry.place(x=10,y=7)
t_entry.focus()

button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
frame1= Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1,font="arial 12", width=40 ,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
del_icn=PhotoImage(file="delete.png")
Button(root,image=del_icn,bd=0,command=deletetask).pack(side=BOTTOM,pady=13)

root.mainloop()
import tkinter
def clicked():
    l1.configure(text="Button was clicked!")
root=tkinter.Tk()
root.geometry('350x200')
l1=tkinter.Label(root,text="Skill Lab Experiments",font=("Comic Sans MS",20))
l1.pack()
bt=tkinter.Button(root,text="Enter",command=clicked)
bt.pack()
root.mainloop()
                                                         

import tkinter as tk
root=tk.Tk()
root.geometry("300x200")
frame=tk.Frame(root,bd=5,relief="sunken")
frame.pack(pady=20,padx=20)
label=tk.Label(frame,text="Inside the frame")
label.pack(pady=10)
button=tk.Button(frame,text="Click Me")
button.pack()
root.mainloop()


from tkinter import *
from tkinter import messagebox

from sympy import expand

root = Tk()
root.geometry('500x450+500+200')
root.title('TODO')
root.config(bg='#223441')
root.resizable(width=False, height=False)

class App:
    def __init__(self, root):
        

        frame = Frame(root)
        frame.pack(pady=10)

        self.listbox = Listbox(
            frame,
            width=25,
            height=8,
            font=('Times', 18),
            bd=0,
            fg='#464646',
            highlightthickness=0,
            selectbackground='#a6a6a6',
            activestyle='none'
        )
        self.listbox.pack(side=LEFT, fill=BOTH)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=BOTH)

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.entry = Entry(root, font=('times', 24))
        self.entry.pack(pady=20)

        button_frame = Frame(root)
        button_frame.pack(pady=20)

        addTask_button = Button(
            button_frame,
            text='Add task',
            font=('times', 14),
            bg='#c5f776',
            padx=20,
            pady=10,
            command=self.newTask
        )
        addTask_button.pack(fill=BOTH, expand=True, side=LEFT)

        delTask_button = Button(
            button_frame,
            text='Delete task',
            font=('times', 14),
            bg='#ff8b61',
            padx=20,
            pady=10,
            command=self.deleteTask
        )
        delTask_button.pack(side=RIGHT, expand=True, fill=BOTH)

        root.bind('<Return>', self.newTask)
    
    def newTask(self, event=0):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(END, task)
            self.entry.delete(0, "end")
        else:
            messagebox.showwarning("warning", "Please enter some task.")

    def deleteTask(self):
        self.listbox.delete(ANCHOR)


App(root)
root.mainloop()
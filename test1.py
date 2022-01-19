#Taharih Rogers
#tkinter Lab
#ver 1.0
#This is an exercise to create a state feedback form
#file name: tkinterLab.py

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:
    def __init__(self, master):

        master.title('Maine Feedback')
        master.resizable(False, False)
        master.configure(background = '#ff69b4')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#ff69b4')
        self.style.configure('TButton', background = '#ff69b4')
        self.style.configure('TLabel', background = '#ff69b4', font = ('Papyrus', 12))
        self.style.configure('Header.TLabel', font = ('Comic Sans', 18, 'bold'))
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        

        self.logo = PhotoImage(file = 'flag_of_maine_resized.png')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan =2)
        ttk.Label(self.frame_header, text = 'Thank you for choosing the gorgeous state of Maine!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300, text = ("We hope you enjoyed your time exploring the beautiful scenery. "
                                             "Please tell us what you thought about your time with us.")).grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Name: ').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email: ').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments: ').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Papyrus', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Papyrus', 10))
        self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Papyrus', 10))

        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0, padx = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 1, padx = 5, sticky = 'w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messabebox.showinfo(title = "Maine Feedback", message = "Comments Submitted!")

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')


def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__": main()

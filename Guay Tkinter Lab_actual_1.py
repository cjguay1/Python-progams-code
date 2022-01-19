#Christopher Guay
#tkinter Lab
#ver 1.0
#This is an exercise to create a state feedback form
#file name: tkinterLab.py

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class Feedback:
    def __init__(self, master):

        master.title('Explore Massachusetts Feedback')
        master.resizable(False, False)
        master.configure(background = '#add8e6')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#add8e6')
        self.style.configure('TButton', background = '#add8e6')
        self.style.configure('TLabel', background = '#add8e6', font = ('Times New Roman', 12))
        self.style.configure('Header.TLabel', font = ('Comic Sans', 18, 'bold'))
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        

        self.logo = PhotoImage(file = 'jonny_hoo_1.png')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan =2)
        ttk.Label(self.frame_header, text = 'Thanks for visiting!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300, text = "Hope to see you again soon! ").grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Name: ').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email: ').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments: ').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Times New Roman', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Times New Roman', 10))
        self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Times New Roman', 10))

        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0, padx = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 1, padx = 5, sticky = 'w')
        ttk.Button(self.frame_content, text = 'Return Comments', command = self.return_comments).grid(row = 5, column = 0, padx = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Return Records', command = self.return_records).grid(row = 5, column = 1, padx = 5, sticky = 'w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))

        output = open('comments.txt', 'a')
        output.write('Name: {}\n'.format(self.entry_name.get()))
        output.write('Email: {}\n'.format(self.entry_email.get()))
        output.write('Comments: {}\n'.format(self.text_comments.get(1.0, 'end')))
        output.close()

        db = sqlite3.connect('Comments.db')
        cur = db.cursor()
        cur.execute("drop table if exists Comments")
        cur.execute("""
            create table entries(
            name TEXT,
            email TEXT
            comments TEXT
            )""")
        cur.execute('insert into entries(name, email, comments) values ("Name: {}","Email: {}","Comments: {}")')
        
        self.clear()
        messagebox.showinfo(title = "Explore Massachusetts Feedback", message = "Comments Submitted!")

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')

    def return_comments(self):
        f = open('comments.txt', 'r')
        for line in f:
            print(line.rstrip())

    def return_records(self):
        cur.execute("SELECT * FROM test")
        print(cur.fetchall())   

import sqlite3
          

def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__": main()

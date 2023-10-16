from tkinter import *
 
root = Tk()
 
c = Canvas(width=300, height=300, bg='white')
c.pack()

c.create_oval(100, 30, 200, 290,
              fill='pink',
              outline='black')

c.create_oval(180, 150, 280, 295,
              fill='pink',
              outline='black')



root.mainloop()

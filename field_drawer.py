# отрисовка поля для морского боя

import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg = 'white', height = 600, width = 600)
k = 1
for i in range(8):
    canvas.create_line((0, 75 * k),(600, 75 * k), fill ='black')
    canvas.create_line((75 * k, 0),(75 * k, 600), fill ='black')
    k += 1
canvas.pack()
master.mainloop()

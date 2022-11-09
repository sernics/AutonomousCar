import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

def getWidth():
    width = entry1.get()
    print(width)

button1 = tk.Button(text='Get the width of the matrix window', command=getWidth)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
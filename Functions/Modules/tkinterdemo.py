import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Program")
mainWindow.geometry('1024x800')

label = tkinter.Label(mainWindow, text='Hello world')
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='left')
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.pack(side='top', anchor='n')
button2.pack(side='top', anchor='s')
button3.pack(side='top', anchor='e')

mainWindow.mainloop()
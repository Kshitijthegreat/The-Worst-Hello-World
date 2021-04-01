import subprocess as sp
import tkinter as tk
import os
def bruh():
    os.environ['FLASK_APP'] = 'web.py'
    sp.run('start http://localhost:5000' ,shell=True)
    sp.run('flask run', shell=True)
root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=500, bg='#0000ff')
canvas.pack()
frame = tk.Frame(root, bg='white')
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
runapp = tk.Button(frame, text='Run app', padx=10, pady=10, fg='white', bg='#00ff00', command=bruh)
runapp.pack()
tk.mainloop()
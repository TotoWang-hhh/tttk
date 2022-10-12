import tkinter as tk
import tkinter.ttk as ttk
import tttk

win=tk.Tk()

def osnk():
    osnk=tttk.Osnk(root=win,entry=enter)

numenter=tttk.NumEnterOld(win)
numenter.frame.pack()

enter=ttk.Entry(win)
enter.pack()
enter.insert(tk.END,'OSNK Test')

ttk.Button(win,text='屏幕数字键盘\nOnscreen Number Keyboard',command=osnk).pack()

numenteronly=tttk.NumEnter(win,width=10)
numenteronly.frame.pack()

win.mainloop()

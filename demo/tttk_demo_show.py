import tkinter.messagebox as msgbox
import tkinter as tk
import tkinter.ttk as ttk
from tttk import tttk

import webbrowser

win=tk.Tk()

def osnk():
    osnk=tttk.Osnk(root=win,entry=osnktst.enter)

def func(arg=''):
    print('您一定触发了什么吧！')

toptip=tk.Frame(win,bg='#FFFFFF') #顶部提示
tk.Label(toptip,text='这个Demo简单粗暴地包含了tttk的所有控件\n且尽可能地指定更少的参数并使用默认值',font=('微软雅黑',15),bg='#FFFFFF').pack(padx=25,fill=tk.X)
#tk.Label(toptip,text='',bg='#FFFFFF').pack(fill=tk.X) #底部间隔
toptip.pack(fill=tk.X)

##################################################

tk.Label(win,text='').pack() #空白分隔

numenterpt=ttk.LabelFrame(win,text='NumEnter和NumEnterOld')

tttk.NumEnterOld(numenterpt).pack()
tttk.NumEnter(numenterpt).pack()

numentererrpt=ttk.LabelFrame(numenterpt,text='存在潜在问题时')
tttk.NumEnterOld(numentererrpt,minnum=0,maxnum=0).pack()
tttk.NumEnter(numentererrpt,minnum=0,maxnum=0).pack()
numentererrpt.pack(fill=tk.X,padx=5,pady=5)

numenterpt.pack(fill=tk.X,padx=15,pady=10)

##################################################

osnkpt=ttk.LabelFrame(win,text='Osnk')

osnktst=tttk.TipEnter(osnkpt,text='测试用输入框',command=osnk,btntxt='打开屏幕数字键盘')
osnktst.pack(fill=tk.X,padx=15,pady=5)
ttk.Button(osnkpt,text='打开屏幕数字键盘（备用按钮）',command=osnk).pack(fill=tk.X,padx=15,pady=5)

osnkpt.pack(fill=tk.X,padx=15,pady=10)

##################################################

tipenterpt=ttk.LabelFrame(win,text='TipEnter')

tttk.TipEnter(tipenterpt,command=func).pack(fill=tk.X,padx=15,pady=5)
tttk.TipEnter(tipenterpt).pack(fill=tk.X,padx=15,pady=5)

tipenterpt.pack(fill=tk.X,padx=15,pady=10)

##################################################

btnrowpt=ttk.LabelFrame(win,text='BtnRow')

tk.Label(btnrowpt,text='您可以查看代码来学习如何指定其内容',fg='#A3A3A3').pack() #灰色提示文本
tttk.BtnRow(btnrowpt,content={'百度':lambda:webbrowser.open("https://www.baidu.com"),'示例':func,'打开屏幕键盘':osnk}).pack(padx=15,pady=5)

btnrowpt.pack(fill=tk.X,padx=15,pady=10)

##################################################

tk.Label(win,text='').pack()

win.mainloop()

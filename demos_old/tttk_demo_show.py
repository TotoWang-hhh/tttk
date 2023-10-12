import tkinter.messagebox as msgbox
import tkinter as tk
import tkinter.ttk as ttk
import tttk

import webbrowser
import os

root=tk.Tk()
root.title('tttk Demo')
root.protocol("WM_DELETE_WINDOW", exit)
root.resizable(0,0)

win=tk.Toplevel()
win.transient(root)
win.title('Page 1 | tttk Demo')
win.protocol("WM_DELETE_WINDOW", win.withdraw)
win.resizable(0,0)
win.update()
win.withdraw()

winb=tk.Toplevel()
winb.transient(root)
winb.title('Page 2 | tttk Demo')
winb.protocol("WM_DELETE_WINDOW", winb.withdraw)
winb.resizable(0,0)
winb.update()
winb.withdraw()

def osnk():
    osnk=tttk.Osnk(root=win,entry=osnktst.enter)

def func(arg=''):
    print('您一定触发了什么吧！')

toptip=tk.Frame(root,bg='#FFFFFF') #顶部提示
tk.Label(toptip,text='这个Demo简单粗暴地包含了tttk的所有控件\n且尽可能地指定更少的参数并使用默认值',bg='#FFFFFF').pack(padx=25,fill=tk.X)
#tk.Label(toptip,text='',bg='#FFFFFF').pack(fill=tk.X) #底部间隔
toptip.pack(fill=tk.X)

##################################################
#页面选择
ttk.Button(root,text='Page 1',command=win.deiconify).pack(fill=tk.X)
ttk.Button(root,text='Page 2',command=winb.deiconify).pack(fill=tk.X)
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

tk.Label(win,text='').pack() #空白分隔
##################################################
tk.Label(winb,text='').pack() #空白分隔


menupt=ttk.Labelframe(winb,text='Menu')

menu=tttk.Menu(winb,content={'百度':lambda:webbrowser.open("https://www.baidu.com"),'示例':func,'打开系统屏幕键盘':lambda:os.system('start osk')})
ttk.Button(menupt,text='单击显示菜单',command=menu.show).pack(padx=15,pady=10)

menupt.pack(fill=tk.X,padx=15,pady=10)

##################################################

flyoutpt=ttk.Labelframe(winb,text='Flyout')


flyoutbtn=ttk.Button(flyoutpt,text='单击显示悬浮展示框')
flyoutbtn.pack(padx=15,pady=10)

flyout=tttk.Flyout(flyoutbtn)
tk.Label(flyout,text='此为悬浮展示框内容',fg='#0000ff',bg='#eeeeee',justify='left').pack(padx=15,pady=10,anchor='w')
tk.Label(flyout,text='Flyout继承自Toplevel，\n所以您可以在此放置任何内容',fg='#ff0000',bg='#eeeeee',justify='left').pack(padx=15,pady=10,anchor='w')
ttk.Button(flyout,text='关闭',command=flyout.hidetip).pack(padx=25,pady=10,anchor='w')

flyoutbtn['command']=flyout.showtip

flyoutpt.pack(fill=tk.X,padx=15,pady=10)

##################################################

tooltippt=ttk.Labelframe(winb,text='ToolTip')

tiplabel=tk.Label(tooltippt,text='将鼠标悬浮于此显示悬浮提示',bg='#cccccc')
tiplabel.pack(fill=tk.X,padx=15,pady=10)

tttk.ToolTip(tiplabel,'此为悬浮提示的提示内容')

tooltippt.pack(fill=tk.X,padx=15,pady=10)

tk.Label(winb,text='').pack() #空白分隔
##################################################

tk.mainloop()

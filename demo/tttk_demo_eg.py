import tkinter.messagebox as msgbox
import tkinter as tk
import tkinter.ttk as ttk
from tttk import tttk

win=tk.Tk()

def osnk():
    osnk=tttk.Osnk(root=win,entry=nenter.enter)

def yzm():
    nenter.btn['text']='已发送'
    nenter.btn['state']='disabled'
    win.after(3000,lambda:msgbox.showinfo('哈哈','希望您不要惦记着那个验证码:)'))

toptip=tk.Frame(win,bg='#FFFFFF') #顶部提示
tk.Label(toptip,text='这个注册表单包含了tttk的所有控件，\n它们的用法或许也能给您些许提示。',font=('微软雅黑',15),bg='#FFFFFF').pack(padx=15,fill=tk.X)
tk.Label(toptip,text='本表单旨在展示控件，并不会真正提交',font=('微软雅黑',15,'bold'),bg='#FFFFFF').pack(padx=15,fill=tk.X)
tk.Label(toptip,text='',bg='#FFFFFF').pack(fill=tk.X) #底部间隔
toptip.pack(fill=tk.X)


tk.Label(win,text='').pack() #空白分隔

tk.Label(win,text='请选择您的年龄').pack()

tk.Label(win,text='您可以比较两种数字输入框的样式和功能',fg='#A3A3A3').pack() #灰色提示文本

tttk.NumEnterOld(win,minnum=0).pack()
tttk.NumEnter(win,width=10,minnum=0).pack()

tk.Label(win,text='请正确设置最大值、最小值参数，否则以下就是结果',fg='#A3A3A3').pack() #灰色提示文本
tttk.NumEnterOld(win,minnum=0,maxnum=0).pack()
tttk.NumEnter(win,minnum=0,maxnum=0).pack()


tk.Label(win,text='').pack() #空白分隔

tk.Label(win,text='请输入您的联系方式').pack()

tk.Label(win,text='以下为带按钮的输入框（传入了command参数）及其各种用法',fg='#A3A3A3').pack() #灰色提示文本

nenter=tttk.TipEnter(win,text='电话号码 (+86)',command=yzm,btntxt='获取验证码')
nenter.pack(fill=tk.X,padx=15)
nenter.set('数字键盘与此输入框绑定')

menter=tttk.TipEnter(win,'您的邮箱',btntxt='X 清空')
menter.command=menter.clear #如果需要清空自己，则需要单独指定（未来计划改进）
menter.refresh() #如果实例化后再指定command，可能还是不会显示按钮，此时需调用refresh函数
menter.pack(fill=tk.X,padx=15)

tttk.TipEnter(win,text='报告缺失的联系方式',command=lambda:msgbox.showinfo('哈哈','才不会提交呢\n信不信随你')).pack(fill=tk.X,padx=15)

ttk.Button(win,text='屏幕数字键盘',command=osnk).pack()


tk.Label(win,text='').pack() #空白分隔

tk.Label(win,text='以下为不带按钮的输入框（未传入command参数）',fg='#A3A3A3').pack() #灰色提示文本

tttk.TipEnter(win,text='您的姓名').pack(fill=tk.X,padx=15)


tk.Label(win,text='').pack() #空白分隔

tk.Label(win,text='按钮行（BtnRow）控件，您可以查看代码来学习如何指定其内容',fg='#A3A3A3').pack() #灰色提示文本

tttk.BtnRow(win,content={'注册':lambda:msgbox.showinfo('哈哈','告诉过你了这是假的！'),'登录':lambda:msgbox.showinfo('哈哈','告诉过你了这是假的！'),'帮助':lambda:msgbox.showinfo('这里没有帮助','你不会看看窗口顶部吗？'),
                         '关于Demo':lambda:msgbox.showinfo('关于','这是tttk的Demo\ntttk和其Demo都是 真_人工智障 的作品')}).pack()

tk.Label(win,text='').pack()

win.mainloop()

#tttk
#2022 By 真_人工智障
#一个tkinter的增强库，提供一系列基于tkinter的有用的控件。
#本项目目前不依赖任何第三方库。
#注：本项目不能起到美化的作用
#本项目遵循MPL2.0开源许可

import tkinter as tk
import tkinter.ttk as ttk
#没错接下来就是这个更好使的tttk:)

import time

#数字输入框
#在输入框的两边分别是“减一”和“加一”的按钮。点击输入框会触发编辑模式，左边按钮会变成空白并被禁用，右边会变成提交按钮，点击提交后，如果输入的内容为数字，则会设定输入框内的值并恢复原状。
#参数：窗口，默认值（0），最小值（无），最大值（无）
#最初用于/来源：Goclass计分板插件
class NumEnterOld(tk.Frame):
    def __init__(self,parent,value=0,minnum=None,maxnum=None):
        self.parent=parent
        self.value=value
        self.minnum=minnum
        self.maxnum=maxnum
        tk.Frame.__init__(self,self.parent,width=125)
        self.btnsub=ttk.Button(self,text='-',command=self.sub)
        self.btnsub.pack(side=tk.LEFT)
        self.btnadd=ttk.Button(self,text='+',command=self.add)
        self.btnadd.pack(side=tk.RIGHT)
        self.numenter=ttk.Entry(self)
        self.numenter.pack(fill=tk.BOTH,expand=True)
        self.numenter.bind('<FocusIn>',self.changeui)
        if minnum!=None and maxnum!=None: #若同时指定了最小值和最大值，则检测是否存在问题
            if maxnum<=minnum:
                self.numenter.delete(0,tk.END)
                self.numenter.insert(tk.END,'[已禁用] 存在潜在错误')
                self.numenter['state']='readonly'
                self.numenter.unbind('<FocusIn>')
                self.btnsub['state']='disabled'
                self.btnadd['state']='disabled'
                return
        self.refresh()
    def refresh(self):
        #self.numenter['state']='enabled'
        self.numenter.delete('0',tk.END)
        self.numenter.insert(tk.END,str(self.value))
        #self.numenter['state']='readonly'
        if self.minnum!=None:
            if self.minnum>=self.value:
                self.btnsub['state']='disabled'
            else:
                self.btnsub['state']='enabled'
        elif self.maxnum!=None:
            if self.maxnum<=self.value:
                self.btnadd['state']='disabled'
            else:
                self.btnadd['state']='enabled'
        else:
            self.btnadd['state']='enabled'
            self.btnsub['state']='enabled'
    def changeui(self,xx_event=''):
        self.btnsub['state']='disabled'
        self.btnsub['text']=''
        self.btnadd['text']='√'
        self.btnadd['command']=self.refresh_with_numenter
    def refresh_with_numenter(self,xx_event=''):
        if self.numenter.get().isdigit():
            self.value=int(self.numenter.get())
        self.btnsub['state']='enabled'
        self.btnsub['text']='-'
        self.btnadd['text']='+'
        self.btnadd['command']=self.add
        self.refresh()
    def sub(self,num=1):
        self.value-=num
        self.refresh()
    def add(self,num=1):
        self.value+=num
        self.refresh()
    def get(self):
        return self.value

#屏幕数字键盘
#实例化后会立即以“root”参数内的内容作为父窗口创建弹窗，包含0~9的数字键、负号键和退格按钮。点击按钮将会在“entry”参数的输入框内进行对应操作
#参数：父级窗口，绑定的输入框，窗口标题（'数字软键盘'）
#最初用于/来源：Goclass计分板插件
#可能不符合系统控件样式
class Osnk():
    def __init__(self,root,entry,title='数字软键盘'):
        #窗口
        self.win=tk.Toplevel()
        self.root=root
        self.entry=entry
        self.win.title(title)
        self.win.transient(self.root)
        #所有按键
        tk.Button(self.win,text='1',command=lambda:self.entry.insert(tk.INSERT,'1'),width=5,bg='#FFFFFF',bd=0,font=('微软雅黑',17)).grid(row=1,column=1)
        tk.Button(self.win,text='2',command=lambda:self.entry.insert(tk.INSERT,'2'),width=5,bg='#FFFFFF',bd=0,font=('微软雅黑',17)).grid(row=1,column=2)
        tk.Button(self.win,text='3',command=lambda:self.entry.insert(tk.INSERT,'3'),width=5,bg='#FFFFFF',bd=0,font=('微软雅黑',17)).grid(row=1,column=3)
        tk.Button(self.win,text='4',command=lambda:self.entry.insert(tk.INSERT,'4'),width=5,bg='#FFFFFF',bd=0,font=('微软雅黑',17)).grid(row=2,column=1)
        tk.Button(self.win,text='5',command=lambda:self.entry.insert(tk.INSERT,'5'),width=5,bg='#FFFFFF',bd=0,font=('微软雅黑',17)).grid(row=2,column=2)
        tk.Button(self.win,text='6',command=lambda:self.entry.insert(tk.INSERT,'6'),width=5,bg='#FFFFFF',bd=0,font=('微软雅黑',17)).grid(row=2,column=3)
        tk.Button(self.win,text='7',command=lambda:self.entry.insert(tk.INSERT,'7'),width=5,bg='#FFFFFF',bd=0,font=('微软雅黑',17)).grid(row=3,column=1)
        tk.Button(self.win,text='8',command=lambda:self.entry.insert(tk.INSERT,'8'),width=5,bg='#FFFFFF',bd=0,font=('微软雅黑',17)).grid(row=3,column=2)
        tk.Button(self.win,text='9',command=lambda:self.entry.insert(tk.INSERT,'9'),width=5,bg='#FFFFFF',bd=0,font=('微软雅黑',17)).grid(row=3,column=3)
        tk.Button(self.win,text='-',command=lambda:self.entry.insert(tk.INSERT,'-'),width=5,bd=0,font=('微软雅黑',17)).grid(row=4,column=1)
        tk.Button(self.win,text='0',command=lambda:self.entry.insert(tk.INSERT,'0'),width=5,bg='#FFFFFF',bd=0,font=('微软雅黑',17)).grid(row=4,column=2)
        tk.Button(self.win,text='<',command=lambda:self.entry.delete(self.entry.index(tk.INSERT)-1,tk.INSERT),width=5,bg='#802020',fg='#FFFFFF',bd=0,font=('微软雅黑',17)).grid(row=4,column=3)
        #禁止更改窗口宽高
        self.win.resizable(0,0)

#另一个数字输入框
#与NumEnterOld几乎相同，但输入框实际为Label，只能输入数字（其他输入将不会被响应）和符号（效果为改变数字正负），搭配数字软键盘使用。
#参数：窗口，默认值，输入框宽度（7），最小值（无），最大值（无），背景色（无），前景色（无），文本背景（无）
#最初用于/来源：Goclass计分板插件
#可能不符合系统控件样式。这玩意我花了一个中午才写出来。
class NumEnter(tk.Frame):
    def __init__(self,win,value=0,width=7,fontsize=20,minnum=None,maxnum=None,bg=None,fg=None,txtbg='#FFFFFF'):
        #整个Frame
        tk.Frame.__init__(self,win,bg=bg)
        self.bg=bg
        self.fg=fg
        #一些值
        self.win=win
        self.value=value
        self.minnum=minnum
        self.maxnum=maxnum
        self.show_key_code_when_insert=False
        #“-”按钮
        self.btnsub=tk.Button(self,text='-',command=self.sub,bg=bg,fg=fg,font=('微软雅黑'),width=5,bd=0)
        self.btnsub.pack(side=tk.LEFT,fill=tk.X)
        #“+”按钮
        self.btnadd=tk.Button(self,text='+',command=self.add,bg=bg,fg=fg,font=('微软雅黑'),width=5,bd=0)
        self.btnadd.pack(side=tk.RIGHT,fill=tk.X)
        #分数显示（曾经的输入框）
        self.numenter=tk.Label(self,bg=txtbg,fg=fg,bd=0,width=width,font=('consolas',fontsize))
        self.numenter.pack(fill=tk.BOTH,expand=True)
        self.numenter.bind('<Double-Button-1>',self.changeui)
        if minnum!=None and maxnum!=None: #若同时指定了最小值和最大值，则检测是否存在问题
            if maxnum<=minnum:
                self.numenter['font']=('微软雅黑',int(fontsize/2.5))
                self.numenter['width']=int(int(self.numenter['width'])*2.5)
                self.numenter['text']='[已禁用] 存在潜在错误'
                self.numenter.unbind('<Double-Button-1>')
                self.btnsub['state']='disabled'
                self.btnadd['state']='disabled'
                return
        self.refresh()
    def refresh(self):#刷新函数
        #self.numenter['state']='enabled'
        self.numenter['text']=str(self.value)
        #self.numenter['state']='readonly'
        if self.minnum!=None:
            if self.minnum>=self.value:
                self.btnsub['state']='disabled'
            else:
                self.btnsub['state']='normal'
        elif self.maxnum!=None:
            if self.minnum>=self.value:
                self.btnsub['state']='disabled'
            else:
                self.btnsub['state']='normal'
        else:
            self.btnadd['state']='normal'
            self.btnsub['state']='normal'
    def changeui(self,xx_event=''):#点击输入框切换到编辑界面
        #self.btnsub['state']='disabled'
        #self.numenter.delete('0',tk.END)#先清空，以免没看界面然后输错
        self.numenter['text']=''
        self.btnsub['text']='软键盘'
        self.btnsub['command']=self.osnk
        self.btnadd['text']='√'
        self.btnadd['command']=self.refresh_with_numenter
        self.numenter.unbind('<Double-Button-1>')
        self.numenter.bind('<Return>',self.refresh_with_numenter)
        self.numenter.bind('<KeyPress-0>',lambda event:self.insert(num='0'))
        self.numenter.bind('<KeyPress-1>',lambda event:self.insert(num='1'))
        self.numenter.bind('<KeyPress-2>',lambda event:self.insert(num='2'))
        self.numenter.bind('<KeyPress-3>',lambda event:self.insert(num='3'))
        self.numenter.bind('<KeyPress-4>',lambda event:self.insert(num='4'))
        self.numenter.bind('<KeyPress-5>',lambda event:self.insert(num='5'))
        self.numenter.bind('<KeyPress-6>',lambda event:self.insert(num='6'))
        self.numenter.bind('<KeyPress-7>',lambda event:self.insert(num='7'))
        self.numenter.bind('<KeyPress-8>',lambda event:self.insert(num='8'))
        self.numenter.bind('<KeyPress-9>',lambda event:self.insert(num='9'))
        self.numenter.bind('<KeyPress-->',lambda event:self.insert(event=event,num='o'))
        self.numenter.bind('<KeyPress-BackSpace>',lambda event:self.insert(num='b'))
        ###
        self.numenter.focus()
    def insert(self,event='',num='0'):
        #print(str(type(event)))
        if self.show_key_code_when_insert:
            if type(event)!=str:
                try:
                    print(event.keycode)
                except Exception as e:
                    print('发生了原本潜在的错误，请在https://github.com/totowang-hhh/tttk/issues反馈')
                    print('event类型：'+type(event).__str__)
                    print(type(event))
                    print('报错信息：')
                    print(e)
            else:
                print('没有传入正确的event')
        #print(type(event.keycode))
        #print('触发insert并给予参数'+self.numenter['text']+str(num))
        #判断输入的是否是可接受的字符
        accept=['0','1','2','3','4','5','6','7','8','9','b']
        if num in accept:
            if num=='b':
                self.numenter['text']=self.numenter['text'][0:len(self.numenter['text'])-1]
            else:
                self.numenter['text']=self.numenter['text']+str(num)
        elif num=='-':#在屏幕数字键盘上输入负号时切换正负
            if self.numenter['text'].isdigit and self.numenter['text']!=0 and self.numenter['text']!='':
                self.numenter['text']=str(-1*int(self.numenter['text']))
        elif num=='o' and (int(event.keycode)==189 or int(event.keycode)==109):#在实体键盘上输入负号时切换正负（键码189为键盘0和=中间的减号，键码109为作者电脑数字小键盘的减号，不知道其他电脑的109是什么……）
            if self.numenter['text'].isdigit and self.numenter['text']!=0 and self.numenter['text']!='':
                self.numenter['text']=str(-1*int(self.numenter['text']))
    def index(xx_arg1=0,xx_arg2=0):
        return 0
    def delete(self,xx_start='',xx_end=''):
        self.numenter['text']=self.numenter['text'][0:len(self.numenter['text'])-1]
    def refresh_with_numenter(self,xx_event=''):#杂乱到无法写注释，总之就是点击“√”完成编辑所执行的
        if self.numenter['text'].replace('-','').isdigit():
            self.value=int(self.numenter['text'])
        self.numenter.unbind('<Return>')
        self.numenter.unbind('<KeyPress-0>')
        self.numenter.unbind('<KeyPress-1>')
        self.numenter.unbind('<KeyPress-2>')
        self.numenter.unbind('<KeyPress-3>')
        self.numenter.unbind('<KeyPress-4>')
        self.numenter.unbind('<KeyPress-5>')
        self.numenter.unbind('<KeyPress-6>')
        self.numenter.unbind('<KeyPress-7>')
        self.numenter.unbind('<KeyPress-8>')
        self.numenter.unbind('<KeyPress-9>')
        self.numenter.unbind('<KeyPress-->')
        self.numenter.unbind('<KeyPress-BackSpace>')
        self.numenter.bind('<Double-Button-1>',self.changeui)
        self.btnsub['state']='normal'
        self.btnsub['font']=('微软雅黑')
        self.btnadd['font']=('微软雅黑')
        self.btnsub['text']='-'
        self.btnadd['text']='+'
        self.btnsub['command']=self.sub
        self.btnadd['command']=self.add
        self.refresh()
    def sub(self,num=1):#减法
        self.value-=num
        self.refresh()
    def add(self,num=1):#加法
        self.value+=num
        self.refresh()
    def get(self):#返回目前的值
        return self.value
    def osnk(self):
        kb=Osnk(self.win,self)

#带提示和按钮（可选）的输入框
#会在输入框左边显示一段提示文字，可以提示用户需要输入什么。如果传入了command参数，则会在输入框右边显示一个按钮，可以作为提交按钮。
#参数：父级，提示文字（'请填写'），指令（无），按钮文本（'提交'），前景色（无），背景色（无），字体（无），字体大小（无）
#最初用于/来源：tkwebview2 Demo Launcher
class TipEnter(tk.Frame):
    def __init__(self,parent,text='请填写',command=None,btntxt='提交',bg=None,fg=None,font=None,fontsize=None):
        self.parent=parent
        self.text=text
        self.bg=bg
        self.fg=fg
        self.command=command
        self.btntxt=btntxt
        if fontsize!=None:
            self.font=('微软雅黑',fontsize)
        else:
            self.font=font
        tk.Frame.__init__(self,self.parent,bg=self.bg)
        self.tip=tk.Label(self,text=self.text+' ',bg=self.bg,fg=self.fg,font=self.font)
        self.tip.pack(fill=tk.Y,side=tk.LEFT)
        self.enter=ttk.Entry(self,font=self.font)
        if self.command!=None:
            self.btn=ttk.Button(self,text=self.btntxt,bg=self.bg,fg=self.fg,command=self.command)
            self.btn.pack(side=tk.RIGHT,fill=tk.Y)
            self.enter.bind("<Return>",lambda event:self.command())
        self.enter.pack(fill=tk.BOTH,expand=True)
    def set(self,txt):
        self.clear()
        self.enter.insert(0,txt)
    def clear(self):
        self.enter.delete(0,tk.END)
    def get(self,**kw):
        return self.enter.get(**kw)
    def refresh(self):
        self.__init__(self.parent,self.text,self.command,self.btntxt,self.fg,self.bg,self.font)

#按钮行
#包含一排按钮，您只需要简单地指定控件的父容器和按钮内容即可，详见说明文档。注：“bg”参数指定的是Frame的背景。
#参数：父级，按钮内容，按钮间隔（5），背景（无）
#最初用于/来源：tkwebview2 Demo Launcher
class BtnRow(tk.Frame):
    def __init__(self,parent,content,seperate=5,bg=None):
        self.parent=parent
        self.bg=bg
        self.content=content
        self.seperate=seperate
        self.btns=[]
        tk.Frame.__init__(self,self.parent,bg=self.bg)
        self.btns=[]
        for txt in list(self.content.keys()):
            self.btns.append(ttk.Button(self,text=txt,command=self.content[txt]))
            self.btns[list(self.content.keys()).index(txt)].pack(side=tk.LEFT,padx=seperate/2)

#菜单
#创建一个包含多个文本选项的菜单，多用于右键菜单或下拉菜单。
#参数：父级，菜单内容，菜单位置，宽度，背景色（'#ffffff'），前景色（'#000000'），选中项背景色（'#cccccc'），
#     选中项前景色（'#000000'），是否显示取消按钮（True），取消按钮文本（'取消'），取消按钮前景色（'#cc0000'）
#最初用于/来源：PyVP Client > PyVP Modules > ui
class Menu(tk.Toplevel):
    '''
    原注释：
    是个tttk的好苗子，等到这玩意加进tttk后就有可供参考的内容了
    唯一需要注意的是，content即菜单内容中不能有文字重复项，否则可能会有bug
    content的格式与tttk.BtnRow大同小异，可以到tttk文档或readme中查看
    pos，为相对于屏幕左上角的坐标元组或'cur'表示鼠标位置
    '''
    def __init__(self,parent,content,pos='cur',width=100,bg='#ffffff',fg='#000000',selbg='#cccccc',selfg='#000000',
                 showcancelbtn=True,canceltxt='取消',cancelfg='#cc0000',cancelselfg='#cc0000'):
        tk.Toplevel.__init__(self)
        self.parent=parent
        self.title('Menu')
        self.overrideredirect(True)
        #self.transient(self.parent)
        self.wm_attributes('-topmost',True)
        self.content=content
        self.pos=pos
        self.width=width
        self.btns=[]
        for i in list(content.keys()):
            self.btns.append(tk.Button(self,text=i,command=lambda lambda_i=i:self.do(self.content[lambda_i]),bg=bg,fg=fg,bd=0,anchor='w'))
        for btn in self.btns:
            btn.pack(fill=tk.X)
            btn.bind('<Enter>',lambda event,lambda_btn=btn:self.setcolor(lambda_btn,selbg,selfg))
            btn.bind('<Leave>',lambda event,lambda_btn=btn:self.setcolor(lambda_btn,bg,fg))
        if showcancelbtn:
            cancelbtn=tk.Button(self,text=canceltxt,command=self.hide,bg=bg,fg=cancelfg,bd=0,anchor='w')
            cancelbtn.pack(fill=tk.X)
            cancelbtn.bind('<Enter>',lambda event,lambda_btn=cancelbtn:self.setcolor(lambda_btn,selbg,cancelselfg))
            cancelbtn.bind('<Leave>',lambda event,lambda_btn=cancelbtn:self.setcolor(lambda_btn,bg,cancelfg))
        self.update()
        self.geometry(str(self.width)+'x'+str(self.winfo_height()))
        self.withdraw()
    def setcolor(self,btn,newbg,newfg):
        btn['bg']=newbg
        btn['fg']=newfg
    def getpos(self):
        if self.pos=='cur':
            posx=self.parent.winfo_x()+self.parent.winfo_pointerx()
            posy=self.parent.winfo_y()+self.parent.winfo_pointery()
            return (self.parent.winfo_pointerx(),self.parent.winfo_pointery())
        else:
            return self.pos
    def show(self):
        self.deiconify()
        newx,newy=self.getpos()
        self.geometry(str(self.width)+'x'+str(self.winfo_height())+'+'+str(newx+10)+'+'+str(newy+10))
    def _hide(self):
        self.withdraw()
    def hide(self):
        for i in range(0,5):
            self.wm_attributes('-alpha',1-0.2*i)
            self.update()
            time.sleep(0.02)
        self._hide()
        self.wm_attributes('-alpha',1)
    def do(self,func):
        self.hide()
        func()

#悬浮提示
#创建一个包含一行文本的悬浮提示，一般用于功能提示、全文显示等。
#参数：父级，提示内容
#最初用于/来源：PyVP Server > ui
class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.text=text
        widget.bind('<Enter>', self.enter)
        widget.bind('<Leave>', self.leave)
    def enter(self,event):
        self.showtip(self.text)
    def leave(self,event):
        self.hidetip()
    #当光标移动指定控件是显示消息
    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx()+30
        y = y + cy + self.widget.winfo_rooty()+30
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text,justify=tk.LEFT,
                      background="white", relief=tk.SOLID, borderwidth=1,
                      font=("微软雅黑", "10"))
        label.pack(side=tk.BOTTOM)
    #当光标移开时提示消息隐藏
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

#悬浮展示框
#创建一个可包含任何内容的悬浮提示，一般用于功能提示、图文预览、少量信息弹窗展示等。
#参数：悬浮触发/所属控件，是否悬浮显示（False）
#最初用于/来源：tttk
class Flyout(tk.Toplevel):
    def __init__(self,widget,showwhenenter=False):
        self.widget = widget
        tk.Toplevel.__init__(self)
        self.configure(background='#eeeeee')
        self.withdraw()
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        if showwhenenter:
            widget.bind('<Enter>', self.enter)
            widget.bind('<Leave>', self.leave)
    def enter(self,xx_event):
        self.showtip()
    def leave(self,xx_event):
        self.hidetip()
    #当光标移动指定控件是显示消息
    def showtip(self):
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx()+30
        y = y + cy + self.widget.winfo_rooty()+30
        tw=self
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        tw.deiconify()
    #当光标移开时提示消息隐藏
    def hidetip(self):
        tw = self
        self.withdraw()
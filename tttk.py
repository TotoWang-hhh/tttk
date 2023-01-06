#tttk
#2022 By 真_人工智障
#一个tkinter的增强库，提供一系列基于tkinter的有用的控件。
#本项目目前不依赖任何第三方库。
#注：本项目不能起到美化的作用
#本项目遵循MPL2.0开源许可

import tkinter as tk
import tkinter.ttk as ttk
#没错接下来就是这个更好使的tttk:)

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

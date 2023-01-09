# tttk English Document

**2022 By rgzz666（aka. 真_人工智障 / totowang-hhh）**

[![Anti 996](https://img.shields.io/badge/License-Anti 996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)[![MPL-2.0](https://img.shields.io/badge/License-MPL 2.0-orange)](https://www.mozilla.org/en-US/MPL/2.0/)

[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu) This project againsts [996 work schedule](https://github.com/996icu/996.ICU#what-is-996).

tttk can make tkinter easier to use. The aim is to extend widgets of tkinter. **Attention: tttk CANNOT make your user interface more beautiful.**

Different as TinUI, ttkbootstrap and other tkinter exsitions, almost everything in this project is based on tkinter.Frame or other class (same as tkwebview2). But not draw on tkinter.Canvas, or change the theme.

These things **are not** made for this module, but moved from my older projects. some of these programs contains some interesting things like this.

## For English Speakers

I'm now translating this document after I saw a foreigner in stargazers list...

### If I Haven't Done Yet

You can translate this doc with a translate software. **(Do not use Google Translate to Translate Chinese into English, because Google Translate is famous for its RUBBISH TRANSLATION in China)**

~~I **can** translate this doc but I'm too lazy. If you want to do it 4 me, please contact me at tt1224@hotmail.com.~~

You can contact me at tt1224@hotmail.com at anytime to help me with the translation.

## Not Sure if this is the Newest Document?

If there isn't anything unexpected, the latest version this document will always avaliable on [GitHub](https://github.com/totowang-hhh/tttk/) or [the online document site that based on GitHub Pages and Docsify](totowang-hhh.github.io/tttk).

## Suits 1.0.0~1.0.3

### Updates

#### 1.0.3

- Modified `setup.py` with kennethreitz's example.
- You can use `import tttk` instead of `from tttk import tttk` in the future.

#### 1.0.2

- Deleted `tkinter` in dependences, fixed an install problem. Read the Chinese document for more info. Anyway, this still didn't fix everything.

#### 1.0.1

- Fix the problem of `setup.py` not found. But this didn't fix everything.

#### 1.0.0

- Almost everything is now based on `tkinter.Frame`, now and future. So you can use `xxx.pack/place/grid()`, but not `xxx.frame.pack/place/grid()`.
- Added TipEnter and BtnRow.
- Modified code comments
- Document update.
- Fixed a bug on NumEnter and NumEnterOld. The `-` Button won't disable when the value reached the `minnum` param.
- Added maxnum and minnum param check. Read the Chinese document for more info.
- Modified Demo, and seperated them into two versions.

## Other Recommended Modules

This topic is about some of the other modules for tkinter. Read the Chinese document for more info.

## Naming

Because ttk is more useful than tk (tkinter), so tttk will be more useful than ttk

## Customize

You can change everything by changing the attributes of a part of the widget. And every part is just a attribute of the class. You can read the code to make some changes like this. But the document won't write anything about this.

e.g.

```python
import tkinter as tk
from tttk import tttk

win=tk.Tk()

numenter=tttk.NumEnter(win)
numenter.btnsub['bg']='#FF5050'
numenter.btnadd['bg']='#50FF50'
numenter.frame.pack()

win.mainloop()
```

![How does the code above looks like](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/custom.png)

## Demo

Run demos to have a view of the widgets. There're two demos, for showing widgets and giving examples. These demos will be uploaded to GitHub.

**Attention: Demos were written in Chinese.** Although I've planned to translate these files, it won't be started until the document translation is done.

The demo for showing widgets will use less args (or use the defult ones). It will show the most original and defult look of the widgets.

<img src="https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/demo_show.png" alt="纯展示Demo运行效果" style="zoom:80%;" />

The demo for giving examples looks like a register form. The usage(s) of the widgets may give you ideas. The form is for showing the widgets, it won't submmit your private info. 

<img src="https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/demo_eg.png" alt="示例Demo运行效果" style="zoom:80%;" />

---

# The Following Topics HAVE NOT Translated Yet

## 代码中无用的内容

### 无用（或禁止使用）的函数

请勿调用在文档中注明“开发者无需自行调用”的函数。

### 无用的参数

代码中命名以`xx_`开头的参数为无用参数，您无需填入，文档中也不会进行任何介绍。

## 所有类

### NumEnterOld

简单数字输入框，输入框左右两侧分别有“-”、”+“，可以给数字-1或+1。输入框可以输入数字。

该控件较为简陋但符合系统自带控件样式，建议使用[NumEnter](#NumEnter)来替代。

请正确传入minnum和maxnum参数，否则该控件会因存在潜在问题而禁用。

![NumEnterOld的外观](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/NumEnterOld.png)

![编辑状态下的NumEnterOld](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/NumEnterOld_edit.png)

![因潜在错误而被禁用的NumEnterOld](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/NumEnterOld_err.png)

#### 参数

|  名称  |   解释   |  数据类型   | 默认值 |
| :----: | :------: | :---------: | :----: |
|  win   | 父级容器 | tkinter容器 |        |
| value  |  起始值  |     int     |   0    |
| minnum |  最小值  |     int     |  None  |
| maxnum |  最大值  |     int     |  None  |

#### 函数

##### refresh

由其他函数自动调用，开发者无需自行调用。

##### changeui

修改数值的界面，点击输入框后自动调用，可以直接调用来显示编辑界面。

##### refresh_with_numenter

由其他函数自动调用，开发者无需自行调用。

##### sub

将值减去指定的数。

**参数**

| 名称  |          解释          | 数据类型 | 默认值 |
| :---: | :--------------------: | :------: | :----: |
| event | 其他位置调用时自动填入 |          |        |
|  num  |        减去的数        |   int    |   1    |

##### add

将值增加指定的数。

**参数**

| 名称 |   解释   | 数据类型 | 默认值 |
| :--: | :------: | :------: | :----: |
| num  | 增加的数 |   int    |   1    |

##### get

获取当前的值

### Osnk

屏幕数字小键盘，初始化后会自动弹出窗口，触屏用户可以借助窗口上的按钮快速输入数字。

![Osnk的外观截图](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/Osnk.png)

#### 参数

| 名称  |      解释      |   数据类型    |    默认值    |
| :---: | :------------: | :-----------: | :----------: |
| root  |    父级窗口    |  tkinter窗口  |              |
| entry |  绑定的输入框  | tkinter.Entry |              |
| title | 小键盘窗口标题 |      str      | '数字软键盘' |

### NumEnter

数字输入框，输入框左右两侧分别有“-”、”+“，可以给数字-1或+1。输入框可以输入数字。

该控件中的“输入框”并非真正的输入框，而是通过Label和按键绑定制作的伪输入框。（我**花了一中午来写这个……）下文为了叙述简单，一律用“输入框”代替本控件的该部分。

请正确传入minnum和maxnum参数，否则该控件会因存在潜在问题而禁用。

**注：**本控件只能指定固定宽度或大小。

![NumEnter的外观截图](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/NumEnter.png)

![编辑状态下的NumEnter](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/NumEnter_edit.png)

![因潜在问题而被禁用的NumEnter](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/NumEnter_err.png)

#### 参数

|   名称   |     解释     |  数据类型   |  默认值   |
| :------: | :----------: | :---------: | :-------: |
|   win    |   父级容器   | tkinter容器 |           |
|  value   |    起始值    |     int     |     0     |
|  width   |  输入框宽度  |     int     |     7     |
| fontsize |   字体大小   |     int     |    20     |
|  minnum  |    最小值    |     int     |   None    |
|  maxnum  |    最大值    |     int     |   None    |
|    bg    |  按钮背景色  |     str     |   None    |
|    fg    |  按钮前景色  |     str     |   None    |
|  txtbg   | 输入框背景色 |     str     | '#FFFFFF' |

#### 函数

##### refresh

由其他函数自动调用，开发者无需自行调用。

##### changeui

修改数值的界面，双击输入框后自动调用，可以直接调用来显示编辑界面。

##### insert

在值的末尾添加数位。

**参数**

| 名称 |        解释         | 数据类型 | 默认值 |
| :--: | :-----------------: | :------: | :----: |
| num  | 添加的数位（仅1位） |   str    |  '0'   |

##### index

为兼容[Osnk](#Osnk)而创建，只会返回“0”，开发者无需自行调用。

##### delete

当通过changeui调起Osnk，或将Osnk绑定到NumEnter后，单击Osnk上的退格会自动触发。直接调用可以删除末位数字。

##### refresh_with_numenter

由其他函数自动调用，开发者无需自行调用。

##### sub

将值减去指定的数。

**参数**

| 名称 |   解释   | 数据类型 | 默认值 |
| :--: | :------: | :------: | :----: |
| num  | 减去的数 |   int    |   1    |

##### add

将值增加指定的数。

**参数**

| 名称 |   解释   | 数据类型 | 默认值 |
| :--: | :------: | :------: | :----: |
| num  | 增加的数 |   int    |   1    |

##### get

获取当前的值。

##### osnk

由其他函数自动调用，开发者无需自行调用。

### TipEnter

会在输入框左边显示一段提示文字，可以提示用户需要输入什么。如果传入了command参数，则会在输入框右边显示一个按钮，可以作为提交或清空按钮。

**注：按钮只会在`command`参数不为None时显示**

![TipEnter](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/TipEnter.png)

![带按钮的TipEnter](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/TipEnter_btn.png)

#### 参数

|   名称   |         解释         |     数据类型      |  默认值  |
| :------: | :------------------: | :---------------: | :------: |
|  parent  |       父级容器       |    tkinter容器    |          |
|   text   |       提示文字       |        str        | '请填写' |
| command  | 点击按钮时执行的内容 | 函数 / lambda语句 |   None   |
|  btntxt  |    按钮显示的文字    |        str        |  '提交'  |
|    fg    |        前景色        |        str        |   None   |
|    bg    |        背景色        |        str        |   None   |
|   font   |         字体         |       tuple       |   None   |
| fontsize |       字体大小       |        int        |   None   |

**额外内容：**如果您指定了command参数（且不为None），btntxt参数才会起作用。如果您指定了fontsize参数（且不为None），则font参数不会起作用。

#### 函数

##### set

清除并设置输入框的内容。

**参数**

| 名称 |    解释    | 数据类型 | 默认值 |
| :--: | :--------: | :------: | :----: |
| txt  | 设定的文字 |   str    |        |

##### clear

清空输入框内的内容。

##### get

获取输入框的值

**参数**

**不出意外的话**，所有参数将会原封不动地传入self.enter.get()

##### refresh

重新以当前的属性调用初始化函数，如果再实例化后重新指定了`command`属性，则建议调用一次本函数

### BtnRow

包含一排按钮，您只需要简单地指定控件的父容器和按钮内容即可。

**注：“bg”参数指定的是Frame的背景色，而非按钮背景色。**此为tkinter.ttk的限制，仅可通过设置主题来修改，tttk则因过于复杂而未使用本解决方案。

![BtnRow](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/BtnRow.png)

#### 参数

|   名称   |   解释   |  数据类型   | 默认值 |
| :------: | :------: | :---------: | :----: |
|  parent  |   父级   | tkinter容器 |        |
| content  | 按钮内容 |    dict     |        |
| seperate | 按钮间隔 |     int     |   5    |
|    bg    |  背景色  |     str     |  None  |

##### 详解`content`参数的字典格式

`content`是该控件的关键参数，其直接指定该控件的内容。不要慌张，这个参数的格式很简单，而且您正在了解它。

首先，如上表所述，`content`的内容应该为一个字典（dict）。如果您不清楚字典是什么，请先去了解相关内容，您可以直接搜索`python 字典`或`json`，网络上的结果应该会介绍字典。如果您不想离开，那么看看文档内的[极简介绍](#json的极简介绍)也无妨……

作为`content`参数的字典是有一定格式要求的。字典表示整行按钮的内容，一个按钮的内容自然就是一个键值对。根据逻辑，每个键就是按钮的文字，每个值就是点击按钮执行的函数。

**例如**，如果您想制作一排按钮来显示一些网址，那么我们可以先实例化一个BtnRow对象，传入`parent`参数，然后再写`content={}`，开始写字典。首先我们来创建一个指向百度（baidu.com），文字为“百度”的按钮，我们需要先写打开百度的函数`webbrowser.open("https://www.baidu.com")`，将其放在lambda语句里，然后在字典内写一个键值对，结果就是如此`{'百度':lambda:webbrowser.open("https://www.baidu.com")}`。接下来，让我们制作一个指向`example()`函数，文字为“示例”的按钮，我们需要先创建一个名为“example”的函数，然后再先前字典的第一个键值对后面添上逗号，加上第二个按钮的信息，如果我们的example函数并不需要传入任何参数，那么“lambda”和函数名后的括号就都可以被辞退了，故结果应如此`{'百度':lambda:webbrowser.open("https://www.baidu.com"),'示例':example}`。

如果您仍无法理解，可以运行本项目的Demo，并查看其代码。两个Demo的界面底部都包含一个BtnRow，这绝对是一个易懂的例子。

## 附加内容

### json的极简介绍

在大部分位置，**字典**用**大括号（u+007b和u+007d `{}`）括起来**。一个**字典**包含**若干键值对**，在Python中用**英文逗号（u+002c `,`）分隔**，简单来说，您可以理解成一种类似于列表（list）的数据类型，不同之处在于您可以自由指定每一项的名称，亦可理解为自由指定其下标。**键值对**分为**键（key）**和**值（value）**，在Python中以**英文冒号（u+003A `:`）**分隔。**键**可以理解为**值的名称**，在Python中为一个**字符串**。**值**是键对应的**内容**，在Python中可以是**几乎任何数据类型**，甚至是另一个字典。总的来说，Python中字典**大概就是这样**`{key:value,key:value,key:value}`。

如果您仍无法理解，则以下是一个python中字典的**例子**，此时food变量即为字典`food={'水果':[苹果','香蕉','西瓜'],'蔬菜':{'绿色蔬菜':['白菜','包菜']},'其他':'想不到了……'}`。

如果您觉得单行的字典很难看清结构，则**可以在逗号处换行**，每行的键值对数量不限，如以下代码：

```python
food={'水果':[苹果','香蕉','西瓜'],
      '蔬菜':{'绿色蔬菜':['白菜','包菜']},
      '肉类':'要少吃','其他':'想不到了……'}
```


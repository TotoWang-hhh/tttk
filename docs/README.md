# tttk中文文档

**2022~2023 By 真_人工智障（aka. rgzz666 / totowang-hhh）**

tttk是一个tkinter的增强库，旨在扩展tkinter可使用的控件。**注意：tttk并不能起到美化作用。**

不同于Tin UI、ttkbootstrap等其他tkinter扩展库，本项目全部控件都基于tkinter.Frame等原生控件进行继承和修改（类似于tkwebview2），而不是在tkinter.Canvas上进行绘制，亦或直接修改控件样式。

这些控件并非为此所制作，而是整理于我过去开发的程序，这些程序中的一部分中会有这种可移植的有趣玩意。

## For English Speakers

U can translate this doc with a translate software. **(Do not use Google Translate to Translate Chinese into English, because Google Translate is famous 4 its RUBBISH TRANSLATION in China)**

I **can** translate this doc but I'm too lazy. If you want to do it 4 me, please contact me at tt1224@hotmail.com.

## 对应版本：1.0.0~1.0.4

### 更新内容

#### 1.0.4

- 轻微修改并加入了Menu菜单控件
- 修订了文档

#### 1.0.3

- 按照kennethreitz大佬提供的setup.py例子修改了setup.py
- 本次修复顺便将导入代码简化，以后只需`import tttk`即可

#### 1.0.2

- 删除了依赖中的`tkinter`，修复了pip安装时，由于PyPI上没有tkinter的包而找不到依赖`tkinter`，自动下载并尝试安装未修复`setup.py`报错问题的旧版（0.1.1或1.0.1），然后导致安装报错的问题，但实际仍存在其他问题，安装后似乎并没有反应

#### 1.0.1

- 修复了（至少努力修复了）安装时`setup.py`找不到README文件的错误，但事实证明，本版虽然解决了该问题，但并未修复全部问题

#### 1.0.0

~~多了去了~~

- 除弹窗类外的所有控件都继承自tkinter原生控件，现在是，将来也是。故以后可以直接调用控件的放置函数
- 新增了TipEnter、BtnRow两个新控件。
- 修改代码注释，进一步统一格式
- 文档更新（必须的！）
- 修复了NumEnter和NumEnterOld指定并达到了最小值后，不会禁用`-`按钮的问题
- 新增了最小值、最大值的检测，若指定的值存在潜在问题，则判定为不可接受，此时将会禁用该组件
- 修改Demo，并分化为两个

## 其他推荐的tkinter扩展

这个库里的控件十分稀少，如果你需要更多好玩的控件，那么以下是推荐的库：

- tkwebview2，这个库包含1个控件，它可以在tkinter窗口中显示网页，但您需要先安装EdgeWebview2，本库最高仅支持Python 3.8。
- tkintertools（tkt），新版的tkt可以做到近乎完全对控件进行自定义，同时支持简单的3D图形渲染、2D绘图和MarkDown内容显示。最低支持Python 3.8。
- ttkbootstrap，一个控件库，为ttk提供崭新的视觉样式，但在每一版操作系统上都如此，所以在某些系统中会存在违和感。最低支持Python 3.8。
- TinUI，一个美观的控件库，风格为仿WinUI，通过该库的主题可实现跟随系统自动深浅色。但是相较于ttkbootstrap，它有些不易用，因为本库基于canvas故不符合原生tkinter的开发习惯，并且其可定制度不高。主要作者称这只是业余制作的控件库，所以该库细节效果不佳。

## 取名

因为ttk可以理解为tkinter的增强版，故tttk也可理解为ttk的增强版。

## 高度定制

如果直接在实例化时传入的参数无法满足您的需求，您可以直接修改控件中某一部分的属性，每个部分都是该类的一个属性。您可以通过研究项目代码来进行此类更改，至少目前文档中不会对此类定制进行进一步说明。

例：

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

![效果](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/custom.png)

## Demo

运行Demo来查看控件，Demo分为两个，纯展示与示例，这些内容将上传至GitHub。

纯展示Demo将会尽可能地使用较少参数或使用默认参数，所展示的皆为最原本、默认的样式。

<img src="https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/demo_show.png" alt="纯展示Demo运行效果" style="zoom:80%;" />

示例Demo为一个注册表单，其包含tttk内的所有控件，这些控件的使用可能会给予您灵感，该表单旨在展示控件，不会真正提交您的信息，您不用担心隐私问题。

<img src="https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/demo_eg.png" alt="示例Demo运行效果" style="zoom:80%;" />

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

### Menu

用于创建一个包含数个文本选项以及取消按钮（可选）的菜单，每一个选项都可以绑定到一个函数，将会在选项被点击时运行对应的函数。本控件可被用于右键菜单、下拉菜单等位置。

取消按钮是一个可选的菜单项目，如果显示，则会被排列在菜单的末尾。默认情况下，取消按钮会显示为白底，标有深红色“取消”字样的按钮，点击此按钮将会在不执行任何操作的情况下隐藏菜单。Menu控件的参数允许您自定义取消按钮的显隐、前景色、选中时的前景色，详见参数列表。

![TipEnter](https://raw.githubusercontent.com/TotoWang-hhh/tttk/main/docs/img/Menu.png)

#### 参数

|     名称      |         解释         |   数据类型    |  默认值   |
| :-----------: | :------------------: | :-----------: | :-------: |
|    parent     |       父级容器       |  tkinter容器  |           |
|    content    |         内容         |     json      |           |
|      pos      |       菜单位置       | tuple / 'cur' |   'cur'   |
|     width     |       菜单宽度       |      int      |    100    |
|      bg       |      菜单背景色      |      str      | '#ffffff' |
|      fg       |      菜单前景色      |      str      | '#000000' |
|     selbg     |     选中项背景色     |      str      | '#cccccc' |
|     selfg     |     选中项前景色     |      str      | '#000000' |
| showcancelbtn |   是否显示取消按钮   |     bool      |   True    |
|   canceltxt   |     取消按钮文本     |      str      |  '取消'   |
|   cancelfg    |    取消按钮前景色    |      str      | '#cc0000' |
|  cancelselfg  | 取消按钮选中时前景色 |      str      | '#cc0000' |

##### 关于content参数

content参数为一个json字典，格式为`{'<项目文本>',<对应函数>}`，您也可以使用lambda，例如`{'<项目文本>',lambda:<对应函数>(<参数a>,<参数b>)}`，这个content参的格式与BtnRow中的content参数相似，故您可以参考[BtnRow中有关content参数的介绍](#详解`content`参数的字典格式)

##### 关于pos参数

pos参数的内容应为一个元组或者`'cur'`，若传入元组，则格式为`(<x坐标int>,<y坐标int>)`，若传入内容为`'cur'`，则表示光标位置（实际为光标右下方附近）。

#### 函数

##### setcolor

此函数允许您为单个按钮设置新的颜色。

**参数**

| 名称  |   解释   | 数据类型  | 默认值 |
| :---: | :------: | :-------: | :----: |
|  btn  |  菜单项  | tk.Button |        |
| newbg | 新背景色 |    str    |        |
| newfg | 新前景色 |    str    |        |

##### getpos

本函数用于获取光标坐标，由程序调用，用于处理`'pos'`，您可以直接调用此函数来获取菜单应该显示的坐标。

##### show

显示菜单。

##### _hide

隐藏菜单（无动画）。

##### hide

播放渐隐动画并隐藏菜单。

##### do

运行选项对应的函数并隐藏菜单。

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
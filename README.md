# tttk

一个tkinter的增强库。

**2022~2023 By 真_人工智障（aka. rgzz666 / totowang-hhh）**

You can install tttk with `pip install tttk`

[![优先遵循Anti 996开源许可](https://img.shields.io/badge/License-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![同时遵循MPL-2.0开源许可](https://img.shields.io/badge/License-MPL%202.0-orange)](https://www.mozilla.org/en-US/MPL/2.0/)

[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu) 本项目在对抗996工作制的行列中。

tttk是一个tkinter的增强库，旨在扩展tkinter可使用的控件。**注意：tttk并不能起到美化作用。**

不同于Tin UI、ttkbootstrap等其他tkinter扩展库，本项目全部控件都基于tkinter.Frame等原生控件进行继承和修改（类似于tkwebview2），而不是在tkinter.Canvas上进行绘制，亦或直接修改控件样式。

这些控件并非为此所制作，而是整理于我过去开发的程序，这些程序中的一部分中会有这种可移植的有趣玩意。

## For English Speakers

I'm now translating this document after I saw a foreigner in stargazers list...

### If I Haven't Done Yet

You can translate this doc with a translate software. **(Do not use Google Translate to Translate Chinese into English, because Google Translate is famous for its RUBBISH TRANSLATION in China)**

~~I **can** translate this doc but I'm too lazy. If you want to do it 4 me, please contact me at tt1224@hotmail.com.~~

## 不清楚文档是否为最新？

不出意外的话，本文的最新版本将始终在[GitHub存储库](https://github.com/totowang-hhh/tttk/)和[基于GitHub Pages和Docsify的在线文档站](https://totowang-hhh.github.io/tttk)可用。

### 更新内容

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


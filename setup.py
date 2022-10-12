#!/usr/bin/env python
from setuptools import setup, find_packages

with open("./README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

setup(name="tttk",  # 项目名
      version="0.3.2",       # 版本号
      description="tkinter的增强库",  #简介
      long_description=long_description,  # 长简介 这里使用的 readme 内容
      long_description_content_type="text/markdown",
      license="MPL",   # 授权
      install_requires=requirements, # 依赖
      author="真_人工智障",  # 作者
      author_email="tt1224@hotmail.com",  # 邮箱
      url="https://github.com/TotoWang-hhh/tttk/",  # 地址
      download_url="https://github.com/TotoWang-hhh/tttk/archive/master.zip",
      packages=find_packages(),
      keywords=['tttk','tkinter增强','tk增强'],
      zip_safe=True)

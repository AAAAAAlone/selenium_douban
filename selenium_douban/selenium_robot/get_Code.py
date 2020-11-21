#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from Tkinter import *
# import tkMessageBox
# import tkinter
# import 对大小写敏感
from PIL import ImageTk
from tkinter import *
import PIL
import tkinter as tk
import os


class GetCode(object):

    def __init__(self):
        self.data = {}  # 存放返回值
        self.root = tk.Tk()
        self.root.geometry('450x150')
        self.root.resizable(width=False, height=False)   # 固定长宽不可拉伸
        self.textLabel = tk.Label(self.root, text="请输入验证码：")  # 标签
        self.textLabel.pack()
        self.textStr = StringVar()
        self.textEntry = tk.Entry(self.root, textvariable=self.textStr)
        self.textStr.set("")
        self.textEntry.pack()  # 输入框
        print(os.getcwd())
        pil = PIL.Image
        im = pil.open('code-douban.jpeg')
        # im = pil.open(r'/Users/oscar/Downloads/selenium_douban/selenium_robot/code-douban.jpeg')
        self.img = ImageTk.PhotoImage(im)
        self.show_code()

    def show_code(self):
        # 显示图片
        code_input = tk.Label(self.root, image=self.img)
        code_input.pack()
        # 绑定快捷键
        # code_input.bind_all("<Return>",self.return_code)
        # 显示按键
        btn = tk.Button(self.root, text="确认",
                        command=self.return_code, highlightbackground='#696969', width=50, height=10)
        btn.pack(fill="x")

        self.root.mainloop()
        return self.textStr

    def return_code(self):
        # 返回输入框内容
        self.data["code"] = self.textStr.get()
        self.root.destroy()           # 关闭窗体
        # os.remove("test.jpeg")         # 删除图片
        print("输入框内容：" + str(self.data["code"]))
        self.textStr = self.data["code"]
        return self.textStr


if __name__ == '__main__':
    GetCode()

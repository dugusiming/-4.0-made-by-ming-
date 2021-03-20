#-*- codeing = utf-8 -*-
#@Time : 2021/1/21 21:18
#@Athor : 刘思铭
#@file : tkinter翻译器.py
import tkinter as tk
import requests
from tkinter import *
window = tk.Tk()
window.geometry('700x300')
res = StringVar()
entry = tk.Entry(window,  font=('Arial', 14))
bb = tk.Label(window,textvariable=res )
def insert_point():
    post_url = "https://fanyi.baidu.com/sug"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}
    ik = entry.get()
    data = {'kw': ik}
    response = requests.post(url=post_url, data=data, headers=headers)
    dictionary = response.json()
    res.set(dictionary)
b1 = tk.Button(window, text='翻译', width=10,height=2, command=insert_point)
bb.pack()
entry.pack()
b1.pack()
window.mainloop()




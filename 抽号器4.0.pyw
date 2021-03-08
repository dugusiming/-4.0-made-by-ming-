# -*- codeing= utf-8 -*-
# @time=2021/3/6 21:40
# @Author : 留斯冥
# 抽号器4.0【多功能版】.PY

import requests
import tkinter as tk
import random
from tkinter import *

color = [
    'LightPink',
    'Pink',
    'Crimson',
    'LavenderBlush',
    'PaleVioletRed',
    'HotPink',
    'DeepPink',
    'MediumVioletRed',
    'Orchid',
    'Thistle',
    'Plum',
    'Violet',
    'Magenta',
    'Fuchsia',
    'DarkMagenta',
    'Purple',
    'MediumOrchid',
    'DarkViolet',
    'DarkOrchid',
    'Indigo',
    'BlueViolet',
    'MediumPurple',
    'MediumSlateBlue',
    'SlateBlue',
    'DarkSlateBlue',
    'Lavender',
    'GhostWhite',
    'Blue',
    'MediumBlue',
    'MidnightBlue',
    'DarkBlue',
    'Navy',
    'RoyalBlue',
    'CornflowerBlue',
    'LightSteelBlue',
    'LightSlateGray',
    'SlateGray',
    'DodgerBlue',
    'AliceBlue',
    'SteelBlue',
    'LightSkyBlue',
    'SkyBlue',
    'DeepSkyBlue',
    'LightBlue',
    'PowderBlue',
    'CadetBlue',
    'Azure',
    'LightCyan',
    'PaleTurquoise',
    'Cyan',
    'Aqua',
    'DarkTurquoise',
    'DarkSlateGray',
    'DarkCyan',
    'Teal',
    'MediumTurquoise',
    'LightSeaGreen',
    'Turquoise',
    'Aquamarine',
    'MediumAquamarine',
    'MediumSpringGreen',
    'MintCream',
    'SpringGreen',
    'MediumSeaGreen',
    'SeaGreen',
    'Honeydew',
    'LightGreen',
    'PaleGreen',
    'DarkSeaGreen',
    'LimeGreen',
    'Lime',
    'ForestGreen',
    'Green',
    'DarkGreen',
    'Chartreuse',
    'LawnGreen',
    'GreenYellow',
    'DarkOliveGreen',
    'YellowGreen',
    'OliveDrab',
    'Beige',
    'LightGoldenrodYellow',
    'Ivory',
    'LightYellow',
    'Yellow',
    'Olive',
    'DarkKhaki',
    'LemonChiffon',
    'PaleGoldenrod',
    'Khaki',
    'Gold',
    'Cornsilk',
    'Goldenrod',
    'DarkGoldenrod',
    'FloralWhite',
    'OldLace',
    'Wheat',
    'Moccasin',
    'Orange',
    'PapayaWhip',
    'BlanchedAlmond',
    'NavajoWhite',
    'AntiqueWhite',
    'Tan',
    'BurlyWood',
    'Bisque',
    'DarkOrange',
    'Linen',
    'Peru',
    'PeachPuff',
    'SandyBrown',
    'Chocolate',
    'SaddleBrown',
    'Seashell',
    'Sienna',
    'LightSalmon',
    'Coral',
    'OrangeRed',
    'DarkSalmon',
    'Tomato',
    'MistyRose',
    'Salmon',
    'Snow',
    'LightCoral',
    'RosyBrown',
    'IndianRed',
    'Red',
    'Brown',
    'FireBrick',
    'DarkRed',
    'Maroon',
    'White',
    'WhiteSmoke',
    'Gainsboro',
    'LightGrey',
    'Silver',
    'DarkGray',
    'Gray',
    'DimGray',
    'Black',
]
window = tk.Tk()
# window.geometry('550x300')
name = ["names1", "names2", "names3", "names4", "b", "c"]
window["bg"] = color[random.randint(0, len(color) - 1)]
window.title("抽号器4.0(nan&ming)")
res = StringVar()
res1 = StringVar()
fg_color_random = color[random.randint(0, len(color) - 1)]
bg_color_random = color[random.randint(0, len(color) - 1)]
random_name_label = tk.Label(window, textvariable=res1, fg=fg_color_random, bg=bg_color_random, font=('Arial', 80))


def random_name_function():
    cf = name[random.randint(0, len(name) - 1)]
    res1.set(cf)


random_name_button = tk.Button(window, text=" C ", bg="GreenYellow", command=random_name_function)
word_input_entry = tk.Entry(window, font=('Arial', 14))
kk = tk.Label(window, text="翻译的中文：")
kkj = tk.Label(window, text="输入的单词：")  # 就是一条幅

translate_label = tk.Label(window, textvariable=res)  # 就是一条幅


def translate():
    post_url = "https://fanyi.baidu.com/sug"
    headers = {'user-agent': 'Mozilla/5.0'}
    ik = word_input_entry.get()
    data = {'kw': ik}
    response = requests.post(url=post_url, data=data, headers=headers)
    dictionary = response.json()

    ff = '"' + str(dictionary) + '"'  # stemps
    mnw = ff.replace("{'errno': 0, 'data': [{'k': '", "")
    ccb = mnw.replace("'}, {'k': ", "")
    ffb = ccb.replace("', 'v': '", ": ")
    abb = ffb.replace("'}]}", "")
    fbi = abb.replace('"', "")  # stemps
    translation = fbi.replace("'", "\n")

    res.set(translation)


translate_button = tk.Button(window, text=" T ", bg="yellow", command=translate)
quit_button = tk.Button(window, text=" X ", bg="red", command=window.destroy)

word_input_entry.pack()
random_name_label.pack()
random_name_button.pack()
translate_button.pack()
quit_button.pack()
translate_label.pack()
window.mainloop()

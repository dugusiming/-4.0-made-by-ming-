# -*- codeing= utf-8 -*-
# @time=2021/3/13 21:40
# @Author : 思铭
# 随机器5.0【rainbow no.2】.PY
class this():
    '''
    --------------------功能-------------------------
    （1）每次打开都会随机（字体，背景）颜色
    （2）查单词(goole&being)
    （3）便捷退出键
    （4）随机抽号
    （5）输入数字抽取对应数字人数
    -------------------待开发-------------------------
    （6）名字实时变化抽号
    '''
    pass
import requests
import tkinter as tk
import random
from tkinter import *
import re
color =['LightPink','Pink','Crimson','LavenderBlush','PaleVioletRed','HotPink','DeepPink','MediumVioletRed','Orchid','Thistle','Plum','Violet','Magenta','Fuchsia','DarkMagenta','Purple','MediumOrchid','DarkViolet','DarkOrchid','Indigo','BlueViolet','MediumPurple','MediumSlateBlue','SlateBlue','DarkSlateBlue','Lavender','GhostWhite','Blue','MediumBlue','MidnightBlue','DarkBlue','Navy','RoyalBlue','CornflowerBlue','LightSteelBlue','LightSlateGray','SlateGray','DodgerBlue','AliceBlue','SteelBlue','LightSkyBlue','SkyBlue','DeepSkyBlue','LightBlue','PowderBlue','CadetBlue','Azure','LightCyan','PaleTurquoise','Cyan','Aqua','DarkTurquoise','DarkSlateGray','DarkCyan','Teal','MediumTurquoise','LightSeaGreen','Turquoise','Aquamarine','MediumAquamarine','MediumSpringGreen','MintCream','SpringGreen','MediumSeaGreen','SeaGreen','Honeydew','LightGreen','PaleGreen','DarkSeaGreen','LimeGreen','Lime','ForestGreen','Green','DarkGreen','Chartreuse','LawnGreen','GreenYellow','DarkOliveGreen','YellowGreen','OliveDrab','Beige','LightGoldenrodYellow','Ivory','LightYellow','Yellow','Olive','DarkKhaki','LemonChiffon','PaleGoldenrod','Khaki','Gold','Cornsilk','Goldenrod','DarkGoldenrod','FloralWhite','OldLace','Wheat','Moccasin','Orange','PapayaWhip','BlanchedAlmond','NavajoWhite','AntiqueWhite','Tan','BurlyWood','Bisque','DarkOrange','Linen','Peru','PeachPuff','SandyBrown','Chocolate','SaddleBrown','Seashell','Sienna','LightSalmon','Coral','OrangeRed','DarkSalmon','Tomato','MistyRose','Salmon','Snow','LightCoral','RosyBrown','IndianRed','Red','Brown','FireBrick','DarkRed','Maroon','White','WhiteSmoke','Gainsboro','LightGrey','Silver','DarkGray','Gray','DimGray','Black', "https://fanyi.baidu.com/sug" ]
name = ["name1", "name2", "name3", "name4", "name5", "name6","name7","name8","name9"]

window = tk.Tk()
# window.geometry('550x300')

window["bg"] = color[random.randint(0, len(color) - 2)]
window.title("抽号器5.0")
res = StringVar()
res1 = StringVar()
fg_color_random =color[random.randint(0,len(color) - 2)]
bg_color_random = color[random.randint(0, len(color) - 2)]
random_name_label = tk.Label(window, textvariable=res1, fg=fg_color_random, bg=bg_color_random, font=('Arial', 80))

def random_name_function():#随机列表的函数
    cf = name[random.randint(0, len(name)-1)]
    res1.set(cf)

random_name_button = tk.Button(window, text=" Call One ", bg="GreenYellow", command=random_name_function)
word_input_entry = tk.Entry(window, font=('Arial', 14))

translate_label = tk.Label(window, textvariable=res)

def translate_or_choose_more():
    ik = word_input_entry.get()
    if ik=="":
        res1.set("咕咕嘎嘎-->空")
        pass
    else:
        try:
            number=int(ik)
            if number>int(len(name)):
                print("输入的数字超过总人数!")
                #如果num>3就在label换行，怎么写
            resultList = random.sample(name, number)
            res1.set(resultList)
        except:
            post_url =color[-1]
            headers = {'user-agent':'Mozilla/5.0'}
            data = {'kw': ik}
            response = requests.post(url=post_url, data=data, headers=headers)
            dictionary = response.json()
            ff = '"' + str(dictionary) + '"'
            mnw = ff.replace("{'errno': 0, 'data': [{'k': '", "")
            ccb = mnw.replace("'}, {'k': ","")
            ffb = ccb.replace("', 'v': '", ": ")
            abb = ffb.replace("'}]}", "").replace('"', "")
            translation = abb.replace("'", "\n")
            res.set(translation)

translate_button = tk.Button(window, text=" Translate or Call More ", bg="yellow", command=translate_or_choose_more)
quit_button = tk.Button(window, text=" eXit ", bg="red", command=window.destroy)

word_input_entry.pack()
random_name_label.pack()
random_name_button.pack()
translate_button.pack()
quit_button.pack()
translate_label.pack()
window.mainloop()





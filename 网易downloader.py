# @AUTHOR:DGSM
#@Athor : xxx
import tkinter as tk
import requests
from tkinter import *
window = tk.Tk()
window.geometry()
res = StringVar()
res1=StringVar()
window.title("作者:punk铭")
window.geometry('550x300')
entry = tk.Entry(window,  font=('Arial', 14))
Instraction=tk.Label(window,text="输入源代码：")
instruction_of_windows_explore_direction=tk.Label(window,text="请输入你要存入音乐的文件地址:")
input_of_windows_explore_direction=tk.Entry(window,font=('Arial', 14))
input_of_windows_explore_direction.insert(0,r"C:\Users\86151\Desktop\音乐\网易云音乐更新")
text = Text(window, width=40, height=20, wrap=NONE)
#next version:滑轮Scrollbar
def music_get():
    the_web_code=entry.get()
    if the_web_code=="":
        print("empty")
    headers={"user-agent": "Mizilla/5.0"}
    data_get="'''"+the_web_code+"'''"
    bb=data_get.replace(",","")
    character_dump_encharacter_string=bb.replace('<ul class="f-hide"><li><a href="/song?id=',"")
    ENslipt_one=character_dump_encharacter_string.replace('">',"/@")
    deep_slipt=ENslipt_one.replace('</a></li><li><a href="/song?id=',"#$")#slipt with,song can't include ,
    loop=deep_slipt.replace("</a></li></ul>","")#
    enlisting=loop.replace("'","")
    listing=enlisting.split('#$')
    bbccdd=input_of_windows_explore_direction.get()
    music_direction=bbccdd.replace("\\","//")+"//"#windows下路径转为py中绝对路径
    for data in listing:
        listtwo=data.split("/@")
        music_id=listtwo[0]
        music_nmae=listtwo[1]
        url="http://music.163.com/song/media/outer/url?id="+music_id
        realmusic=requests.get(url=url,headers=headers)
        with open(music_direction+music_nmae+'.mp3','wb') as file:
            file.write(realmusic.content)
        text.insert(tk.INSERT,"《"+music_nmae+"》"+"下载成功..."+"\n")
        text.update()
        # print("《"+music_nmae+"》"+"下载成功...")
b1 = tk.Button(window, text='下载歌曲', width=10,height=2, command=music_get)
input_of_windows_explore_direction.grid(row=1,column=1)
instruction_of_windows_explore_direction.grid(row=1,column=0)
entry.grid(row=0, column=1)
b1.grid(row=2, column=1)
Instraction.grid(row=0, column=0)

text.grid(row=4,column=1)
window.mainloop()







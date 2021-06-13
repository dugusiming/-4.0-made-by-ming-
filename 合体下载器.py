# @AUTHOR:DGSM
import requests  # 导入requests模块
import warnings
import os
import tkinter as tk
from tkinter import *
# 两种模式qq或网易1.用选择模式2.输入后自动识别
# 利用多线程下载音乐
import time
from lxml import etree

window = tk.Tk()
window.geometry()
res = StringVar()
res1 = StringVar()

window["bg"] = "black"
window.title("作者:punk铭")
window.geometry('500x300')

entry = tk.Entry(window, insertbackground="white", insertwidth=7, font=('Arial', 14), bg="black", fg="green")

Instraction = tk.Label(window, text="       Code : ", font=('Arial', 12), bg="black", fg="green")

instruction_of_windows_explore_direction = tk.Label(window, text="       Position : ", font=('Arial', 12), bg="black",
                                                    fg="green")
input_of_windows_explore_direction = tk.Entry(window, insertbackground="white",insertwidth=7, font=('Arial', 14), bg="black", fg="green")
input_of_windows_explore_direction.insert(0, r"C:\Users\86151\Desktop\音乐\new")
sb = Scrollbar(window, width=20, troughcolor="black")
sb.grid(row=4, column=2)
text = Text(window, width=40, insertbackground="white",insertwidth=7, height=14, wrap=NONE, bg="black", fg="green", yscrollcommand=sb.set)
sb.config(command=text.yview)
# next version:滑轮Scrollbar
warnings.filterwarnings("ignore")


def music_get():
    music_direction = input_of_windows_explore_direction.get().replace("\\", "//") + "//"
    warnings.filterwarnings("ignore")
    url = entry.get()
    headers1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63"
    }  # 请求头-->伪装成客户
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "cookie": "_iuqxldmzr_=32; _ntes_nnid=4e6856f56983ea7d110dc272cc1d811e,1612844768911; _ntes_nuid=4e6856f56983ea7d110dc272cc1d811e; NMTID=00OmI7YsxljRLhViUFQukKoy4N-BrIAAAF3hQod7g; WM_TID=IMdY%2B52aWVBBUUVBFQc7e5FiQclcbsAS; MUSIC_U=953124561387724d5c56aa1c262431fcb6d633afc3be68073e3196ba3c9e3fca33a649814e309366; ntes_kaola_ad=1; WEVNSM=1.0.0; __csrf=a87dc4880c142bc3ee66f1385804f17e; WNMCID=kcyzrh.1623161511951.01.0; WM_NI=JCVmz5OT6INjDVZnfN%2FNSXN%2FUZqI0yTOdcLXGoKrVhy%2Fq%2Br0qHriP3zx5Om4xHOhH5HuHhr1h%2BfLZ0bRqRhRbRRodbaUXVqWgxlAH0jnvWATNqvBUWeF9zYPfvx3RS8qUzM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8df43f8586a1b2f97bedef8fb3c15f968f8faeae64b2eeaf96ed34a893fab7d82af0fea7c3b92a8a9d9a8ef93f8d8cfaaacd62888a968fe546ed929db9cd259786bfaab3739891ac84cf5485b18593d564bbf1bfccf13cb398be8ad339baa8fbb0f040bc988189cb3f8cab8889f13bacf5aaadd93ca28ebfb3eb5aa28e9e90e76aa38b98b7f45da5a8a4a2cb3caab2bab8c4608eafbaa3d85da79af79bdc5ca6aab8d4d159fcaf9b9bd037e2a3; JSESSIONID-WYYY=u04E1Iv%2F3bZ%2B3mvMIWJHn7EyfVPot5smPMXDN6U0lC8rGcU6lSlXJseEeiZfiRJ3x3IxxXH%5C43jVFc35TsOnX%5C%5ChIa4QX9t19ZBeXcY3HogcC%2BuKtYmctoF62%5C5rC2T3PMw%5CKfVVUo22H%5COVEaTKHFaPpautT%5CnZTCTYeKHFrSrKHaXX%3A1623165050784"
    }
    if "https://y.qq.com/" in url:
        # ssl解密不完全，要忽略一个小报错
        url_unchangeable = '''https://111.19.134.29/amobile.music.tc.qq.com/'''  # 每首下载链接固定前缀

        songmit = url.replace("https://y.qq.com/n/ryqq/songDetail/", "")  # 提取歌中特有的songmid
        purl_get_url = '''https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"3175573154","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"3175573154","songmid":["001icUif3vTGcO"],"songtype":[0],"uin":"3221422579","loginflag":1,"platform":"20"}},"comm":{"uin":3221422579,"format":"json","ct":24,"cv":0}}'''
        songmit_processed = 'songmid":["' + songmit  # 替换提取的songmit
        purl_url = purl_get_url.replace('songmid":["001icUif3vTGcO', songmit_processed)  # 同上
        response = requests.get(purl_url, headers=headers1)  # 提取含有purl的链接
        data_purl = response.json()  # json解码
        purl = data_purl["req_0"]["data"]["midurlinfo"][0]["purl"]  # 注意id前面的0，代表list里面的第一个id值（list里面可能存在两个id关键字）
        download_music_url = url_unchangeable + purl  # 完整下载链接
        realmusic = requests.get(url=download_music_url, headers=headers1, verify=False)

        response1 = requests.get(url=url, headers=headers1)  # 这里注意链接不能字符串化
        root = etree.HTML(response1.content)
        name = root.xpath('//div//h1//text()')  # <h1 class="data__name_txt" title="Father And Son">Father And Son</h1>
        # print(name[0])

        # 爬虫基本格式，verify=False：绕过ssl
        with open(music_direction + str(name[0]) + ".mp3", 'wb') as file:
            file.write(realmusic.content)  # 提取内容并保持

        fsize = os.path.getsize(music_direction + "\\\\" + str(name[0]) + ".mp3")  # 计算文件大小
        fsizeb = fsize / float(1024 * 1024)
        text.insert(tk.INSERT, "文件大小：%s MB" % fsizeb + "\n")
        text.update()
        # print("文件大小：%s MB" % fsizeb)
        if fsizeb >= 1:  # 判断是否正常下载
            # print("《" + music_nmae + "》" + "下载成功！")
            text.insert(tk.INSERT, "《" + str(name[0]) + "》" + "下载成功..." + "\n")
            text.update()
        else:
            # print("歌曲不完整或没有相应资源!")
            text.insert(tk.INSERT, "歌曲不完整或没有相应资源!" + "\n")
            text.update()
    elif "https://music.163.com/#/song?id=" in url:
        singal_id=url.replace("https://music.163.com/#/song?id=","")
        url3 = "http://music.163.com/song/media/outer/url?id=" + str(singal_id)
        response1 = requests.get(url=url.replace("#",""), headers=headers)  # 这里注意链接不能字符串化
        root = etree.HTML(response1.content)
        music_name = root.xpath('//div//em//text()')#'//ul/li/a[@id="jd"]/text()'
        realmusic1 = requests.get(url=url3, headers=headers)
        with open(music_direction + str(music_name[0]) + '.mp3', 'wb') as file1:
            file1.write(realmusic1.content)
            text.insert(tk.INSERT, "《" + str(music_name[0]) + "》" + "下载成功..." + "\n")
            text.update()
        fsize = os.path.getsize(music_direction + "\\\\" +str(music_name[0]) + ".mp3")  # 计算文件大小
        fsizeb = fsize / float(1024 * 1024)
        text.insert(tk.INSERT, "文件大小：%s MB" % fsizeb + "\n")
        text.update()
        if fsizeb >= 1:  # 判断是否正常下载
            # print("《" + music_nmae + "》" + "下载成功！")
            text.insert(tk.INSERT, "《" + str(music_name[0]) + "》" + "下载成功..." + "\n")
            text.update()
        else:
            # print("歌曲不完整或没有相应资源!")
            text.insert(tk.INSERT, "歌曲不完整或没有相应资源!" + "\n")
            text.update()
    else:

        # url=str(entry.get()).replace("#","")
        if url == "":
            text.insert(tk.INSERT, "empty")
            text.update()
            text.update()
        else:
            url1=url.replace("#","")
            response1 = requests.get(url1, headers=headers)

            root1 = etree.HTML(response1.content)

            original_song_name = root1.xpath('//li//a//text()')  # 歌名
            original_song_id = root1.xpath('//ul//li//a/@href')
            list_id = []

            try:
                for single_song in original_song_id:

                    if "/song?id=" not in single_song:
                        del single_song
                    else:
                        pure_song_itself = single_song.replace("/song?id=", "")
                        # print(pure_song_itself)
                        int_number = int(pure_song_itself)
                        # print(int_number)##########################song id
                        list_id.append(int_number)
            except ValueError:
                pass

            list_name = []
            i = 0
            for song_name in original_song_name:
                # print(song_name)
                list_name.append(song_name)
                i = i + 1
                if i >= len(list_id):
                    break

            for (a, b) in zip(list_name, list_id):
                music_name = str(a).replace("/", "|").replace("'", "").replace('"', '').replace("(","").replace(")","").replace("\\","")
                music_id = b
                url2 = "http://music.163.com/song/media/outer/url?id=" + str(music_id)
                realmusic1 = requests.get(url=url2, headers=headers)
                window.after(100, refreshLabelTime)
                with open(music_direction + music_name + '.mp3', 'wb') as file1:
                    file1.write(realmusic1.content)
                    text.insert(tk.INSERT, "《" + music_name + "》" + "下载成功..." + "\n")
                    text.update()


def begain():  # for 循环加执行insert
    text.insert(tk.INSERT, "system running_time:" + str(time.perf_counter()) + "\n")
    text.insert(tk.INSERT, "progress running_time:" + str(time.process_time()) + "\n")
    text.insert(tk.INSERT, "locating... " + "\n")
    text.insert(tk.INSERT, "... " + "\n")
    text.insert(tk.INSERT, "... " + "\n")
    text.insert(tk.INSERT, "... " + "\n")
    text.insert(tk.INSERT, "... " + "\n")
    text.insert(tk.INSERT, "... " + "\n")
    text.insert(tk.INSERT, "LOADING successfully ... Welcome Back!")


text2 = tk.Text(window, width=22, height=1, bg="black", fg="green")
text2.grid(row=5, column=1)

b1 = tk.Button(window, text=' Download ', width=10, height=2, bg="black", fg="green", command=music_get)
input_of_windows_explore_direction.grid(row=1, column=1)
instruction_of_windows_explore_direction.grid(row=1, column=0)
entry.grid(row=0, column=1)
b1.grid(row=2, column=1)
Instraction.grid(row=0, column=0)
text.grid(row=4, column=1)


# print("progress runningtime:"+str(time.process_time()))
# print("system runningtime:"+str(time.perf_counter()))


def refreshLabelTime():
    while True:
        i = "Time:" + time.strftime("%B:%d:%H:%M:%S")
        # time.sleep()
        break
    text2.delete(0.0, tk.END)
    text2.insert(tk.INSERT, i)
    text2.update()
    window.after(1000, refreshLabelTime)


begain()
window.after(1000, refreshLabelTime)
window.mainloop()

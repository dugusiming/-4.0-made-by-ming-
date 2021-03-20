# -*- codeing= utf-8 -*-
# @time=2021/2/11 19:56
# @Author : 留斯冥
# 单个qq音乐下载1.0.PY
import requests#导入requests模块
import warnings
import os
warnings.filterwarnings("ignore")#ssl解密不完全，要忽略一个小报错
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63"}#请求头-->伪装成客户
url_unchangeable='''https://111.19.134.29/amobile.music.tc.qq.com/'''#每首下载链接固定前缀
song_url=input("请输入qq音乐歌曲链接：")#这里注意链接不能字符串化
music_nmae=input("输入歌名：")#捕获输入为文件命名
bbccdd=input("请输入存的文件地址(不填默认就是后面的)：",)+"C://Users//86151//Desktop//音乐//单个音乐储存库//"
songmit=song_url.replace("https://y.qq.com/n/yqq/song/","").replace(".html","")#提取歌中特有的songmid
purl_get_url='''https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"3175573154","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"3175573154","songmid":["001icUif3vTGcO"],"songtype":[0],"uin":"3221422579","loginflag":1,"platform":"20"}},"comm":{"uin":3221422579,"format":"json","ct":24,"cv":0}}'''
songmit_processed='songmid":["'+songmit#替换提取的songmit
purl_url=purl_get_url.replace('songmid":["001icUif3vTGcO',songmit_processed)#同上
response = requests.get(purl_url, headers=headers)#提取含有purl的链接
data_purl=response.json()#json解码
purl=data_purl["req_0"]["data"]["midurlinfo"][0]["purl"]#注意id前面的0，代表list里面的第一个id值（list里面可能存在两个id关键字）
download_music_url=url_unchangeable+purl#完整下载链接
music_direction=bbccdd.replace("\\","//")+"//"
music_direction1=bbccdd.replace("\\","\\\\")
realmusic = requests.get(url=download_music_url, headers=headers,verify=False)#爬虫基本格式，verify=False：绕过ssl
with open(music_direction + music_nmae+".mp3", 'wb') as file:
    file.write(realmusic.content)#提取内容并保持
fsize = os.path.getsize(music_direction1+"\\\\"+music_nmae+".mp3")#计算文件大小
fsizeb = fsize / float(1024 * 1024)
print("文件大小：%s MB" % fsizeb)
if fsizeb>=1:#判断是否正常下载
    print("《"+music_nmae+"》"+"下载成功！")
else:
    print("歌曲不完整或没有相应资源!")
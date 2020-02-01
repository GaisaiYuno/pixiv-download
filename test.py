#!/usr/bin/python
#-*- coding:utf-8 -*-

import os,requests
import configparser

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"

if __name__=="__main__":
    url="https://api.imjad.cn/pixiv/v1/?type=member_illust&id=1655331"
    print("Requesting "+url)
    response=requests.get(url)
    response.encoding=response.apparent_encoding
    data=response.json()
    print(data)
    os.system("PAUSE")
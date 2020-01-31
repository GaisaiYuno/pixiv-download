#!/usr/bin/python
#-*- coding:utf-8 -*-

import os,requests
import configparser

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"

def init():
    cf=configparser.ConfigParser()
    filename=cf.read("config.ini")
    global mainland,path
    mainland=cf.get("pixiv","chinese_mainland")
    path=cf.get("pixiv","download_path")

def download(image,id):
    p=path+"\\"+id
    if (os.path.isdir(p)==False):
        os.mkdir(p)
    os.chdir(p)
    if (mainland==1):
        image="https://bigimg.cheerfun.dev/get/"+image
        command="aria2c "+image+" --user-agent=\""+user_agent+"\""
    else:
        command="aria2c "+image+" --user-agent=\""+user_agent+"\""+" --referer=https://www.pixiv.net/artworks/"+id
    print("Downloading "+image)
    print("Command is:"+command)
    os.system(command)

def output_file(info,outfile):
    fout = open(outfile,'w',encoding='utf8')
    fout.write(info)
    fout.close()

def make_info(data,id):
    title=data["title"]
    caption=data["caption"]
    info="title: "+(str)(title)+"\ncaption: "+(str)(caption)+"\ntags: \n"
    for i in range(0,len(data["tags"])):
        info=info+data["tags"][i]+"\n"
    output_file(info,path+"\\"+id+"\\info.txt")
    pass

if __name__=="__main__":
    init()
    print("Download to "+path)

    while (True):
        print("Please enter pixiv id:")
        id=input()
        if (id=="e"):
            break
        url="https://api.imjad.cn/pixiv/v1/?type=illust&id="+id
        print("Requesting "+url)
        response=requests.get(url)
        response.encoding=response.apparent_encoding
        data=response.json()
        # print(data)
        if (data["status"]!='success'):
            print("Error")
            continue
        data=data["response"][0]
        if (data["metadata"]!=None):
            for i in range(0,len(data["metadata"]["pages"])):
                image=data["metadata"]["pages"][i]["image_urls"]["large"]
                download(image,id)
        else :
            image=data["image_urls"]["large"]
            download(image,id)
        make_info(data,id)
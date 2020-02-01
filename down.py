#!/usr/bin/python
#-*- coding:utf-8 -*-

import os,requests
import configparser

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"

def fetch_json(url):
    print("Requesting "+url)
    response=requests.get(url)
    response.encoding=response.apparent_encoding
    data=response.json()
    return data

def init():
    cf=configparser.ConfigParser()
    filename=cf.read("config.ini")
    global mainland,picture_path,artist_path,rank_path,user_path
    mainland=cf.get("pixiv","chinese_mainland")
    picture_path=cf.get("pixiv","picture_path")
    artist_path=cf.get("pixiv","artist_path")
    rank_path=cf.get("pixiv","rank_path")
    user_path=cf.get("pixiv","user_path")

def download(image,id):
    if ((int)(mainland)==1):
        image="https://bigimg.cheerfun.dev/get/"+image
        command="aria2c "+image+" --user-agent=\""+user_agent+"\""
    else:
        command="aria2c "+image+" --user-agent=\""+user_agent+"\""+" --referer=https://www.pixiv.net/artworks/"+id
    print("Downloading "+image)
    print("Command is:"+command)
    os.system(command)

def output_file(info,outfile):
    fout=open(outfile,'w',encoding='utf8')
    fout.write(info)
    fout.close()

def make_info(path,data,id):
    title=data["title"]
    caption=data["caption"]
    info="title: "+(str)(title)+"\ncaption:\n"+(str)(caption)+"\ntags: \n"
    for i in range(0,len(data["tags"])):
        info=info+data["tags"][i]+"\n"
    output_file(info,path+"\\"+(str)(id)+"\\info.txt")

def download_with_id(path,id):
    data=fetch_json("https://api.imjad.cn/pixiv/v1/?type=illust&id="+(str)(id))
    if (data["status"]!='success'):
        print("Error")
        return 
    data=data["response"][0]
    p=path+"\\"+(str)(id)
    if (os.path.isdir(p)==False):
        os.mkdir(p)
    else :
        print("Dir exists")
        return 
    os.chdir(p)
    if (data["metadata"]!=None):
        for i in range(0,len(data["metadata"]["pages"])):
            image=data["metadata"]["pages"][i]["image_urls"]["large"]
            download(image,id)
    else :
        image=data["image_urls"]["large"]
        download(image,id)
    make_info(path,data,id)

#p74650454
#u49153095
#a1023317
#daily,weekly,monthly,rookie,original,male,female

if __name__=="__main__":
    init()
    print("Download to "+picture_path)
    while (True):
        print("Please enter pixiv id:")
        id=input()
        if (id=='e'):
            break
        if (id[0]=='p'):
            download_with_id(picture_path,id[1:])
        elif (id[0]=='u'):
            data=fetch_json("https://api.imjad.cn/pixiv/v2/?type=favorite&id="+id[1:])
            for i in range(0,len(data["illusts"])):
                download_with_id(user_path,data["illusts"][i]["id"])
        elif (id[0]=='a'):
            pass
        else:
            data=fetch_json("https://api.imjad.cn/pixiv/v1/?type=rank&content=illust&per_page=20&page=1&mode="+id)
            data=data["response"][0]
            for i in range(0,len(data["works"])):
                download_with_id(rank_path,data["works"][i]["work"]["id"])
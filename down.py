import os,requests
# from bs4 import Beautifulsoup
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
def init():
    # path=os.getcwd()
    os.chdir("C:\\Users\\steven_meng\\Desktop\\pixiv_down")
    
if __name__=="__main__":
    init()
    while (True):
        print("Please enter pixiv id:")
        id=input()
        if (id=="e"):
            break
        url = "https://api.imjad.cn/pixiv/v1/?type=illust&id="+id
        print ("Requesting "+url)
        response =  requests.get(url)
        response.encoding=response.apparent_encoding
        data=response.json()
        image=data["response"][0]['image_urls']['large']
        print("Downloading "+image)
        image="https://bigimg.cheerfun.dev/get/"+image
        # command="aria2c "+image+" --conf-path=aria2.conf"+" --user-agent=\""+user_agent+"\""+" --referer=https://www.pixiv.net/artworks/"+id
        # command="aria2c "+image+" --conf-path=aria2.conf"+" --referer=https://www.pixiv.net/artworks/"+id
        command="saldl "+image+" --referer=https://www.pixiv.net/artworks/"+id+" --skip-TLS-verification --connections=15 --connection-max-rate=0 --chunk-size=4M"
        print("Command is:"+command)
        os.system(command)
        # https://www.pixiv.net/artworks/79154264
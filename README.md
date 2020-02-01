# pixiv-download

### 简介

随便乱写的pixiv下载器。

### 特性

国内用户可以下载（只要你知道id），支持输出图片信息，支持组图。

### 使用方法

1.把目录里的aria2c.exe拷贝到C:\Windows目录下。

2.编辑config.ini，chinese_mainland代表您是否处在中国大陆，下面几行代表下载地址

3.打开down.py。

4.输入

- pxxxxx 代表下载pixiv id为xxxxx的图片，下载至download_path。
- uxxxxx 代表下载用户xxxxx的所有收藏，下载至user_path。
- axxxxx 代表下载画师xxxxx的所有作品，下载至artist_path。
- daily,weekly,monthly,rookie,original,male,female的意义如下图，下载至rank_path。
- ![v2-9150fb8bfe4e20f78ab9dfad9e49537b_hd.jpg](https://i.loli.net/2020/02/01/uiOyq8WVZrDc9GI.jpg)

5.等待下载。

### 目前存在的问题

下载速度较慢而且不稳定。

### 感谢

api.imjad.cn 提供api服务。

bigimg.cheerfun.dev 提供图片下载服务。
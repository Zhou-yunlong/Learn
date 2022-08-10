# -*- coding: UTF-8 -*-
# created by Long on 2022/7/21 15:58
# @Software : PyCharm
import bs4
import re
import urllib.request
import urllib.error
import csv

# 正则
findLink = re.compile(r'<a href="(.*)">')
# 当爬取内容存在分行时，使用re.S不会因为换行符而对查询内容进行中断
findImgsrc = re.compile(r'<img.*src="(.*)" width="100"/>', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findNum = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savepath = "movie.csv"
    saveData(datalist, savepath)


def askURL(url):
    print("爬取页面中...")
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=header)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getData(baseurl):
    print("开始")
    dataList = []
    for i in range(0, 10):
        url = baseurl + str(i*25)
        html = askURL(url)
        soup = bs4.BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = {}
            item = str(item)
            link = re.findall(findLink, item)[0]
            data["link"] = link

            imgsrc = re.findall(findImgsrc, item)[0]
            data["imgsrc"] = imgsrc

            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                data["ctitle"] = ctitle
                etitle = titles[1].replace("/", "")
                data["etitle"] = etitle
            else:
                data["ctitle"] = titles[0]
                data["etitle"] = " "
            # print("item:", item)
            rating = re.findall(findRating, item)[0]
            data["rating"] = rating

            num = re.findall(findNum, item)[0]
            data["num"] = num

            # 部分电影没有概括
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace(": ", "")
                data["inq"] = inq
            else:
                data["inq"] = ""

            # 相关内容里一些不必要的符号较多
            bd = re.findall(findBd, item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?", " ", bd)
            bd = re.sub("/", " ", bd)
            data["bd"] = bd.strip()

            dataList.append(data)
    return dataList


def saveData(datalist, savepath):
    print("保存中")
    fo = open(savepath, "w", newline='', encoding='utf-8')
    header = ["ctitle", "etitle", "link", "imgsrc", "rating", "num", "inq", "bd"]
    writer = csv.DictWriter(fo, header)
    writer.writeheader()
    for item in datalist:
        writer.writerow(item)
    fo.close()
    print("完成")


if __name__ == '__main__':
    main()

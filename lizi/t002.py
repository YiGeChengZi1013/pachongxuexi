# encoding=utf-8
"""
使用第三方包自动检测页面编码

"""
import urllib.request
import chardet

if __name__ == '__main__':
    url = "http://www.baidu.com"
    rsp = urllib.request.urlopen(url)
    html = rsp.read()
    # html = html.decode()
    # print(html)

    # 自动检测编码
    cs = chardet.detect(html)
    # 使用get取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)

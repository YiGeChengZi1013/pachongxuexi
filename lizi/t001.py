# encoding=utf-8
"""
使用urllib.requests请求一个网页，并把内容打印出来。
"""
from urllib import request

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    # 打印相应url并把相应页面作为返回
    rsp = request.urlopen(url)
    # 把返回结果读取出来，读取出来的内容类型为bytes
    html = rsp.read()
    # 如果想把bytes内容转换成字符串，需要解码
    html = html.decode()
    print(html)


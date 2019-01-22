import urllib.request

if __name__ == '__main__':
    url = "http://www.baidu.com"
    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)
    # 获取请求地址
    print(rsp.geturl())

    # 请求结果反馈的信息。
    print(rsp.info())
    # 获取请求代码。200 ok
    print(rsp.getcode())

    html = rsp.read()
    html = html.decode()

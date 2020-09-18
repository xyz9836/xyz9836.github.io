#coding=utf-8

import requests

def get_document(url):
    try:
        get = requests.get(url)
        data = get.content
        get.close()
        return data
    except:
        return 0

def download_file(url_x,file_name):
    url_x=url_x+file_name
    document = get_document(url_x)
    if not document:
        print('  {}下载失败'.format(file_name))
    else:
        pathx = path + str(file_name)
        open(pathx, 'wb').write(document)
        print('  {}下载成功'.format(file_name))


path=''
url_x="https://github.com/houzi-/CDN/raw/master/"

download_file(url_x,'koolproxy.txt')
download_file(url_x,'kp.dat')
download_file(url_x,'daily.txt')

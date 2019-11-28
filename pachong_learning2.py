from bs4 import BeautifulSoup
import requests, sys

class downloader(object):
    def __init__(self):
        self.server = 'https://www.biqukan.com/'
        self.target = 'https://www.biqukan.com/10_10706/'
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0            #章节数

    def get_download_url(self):
        req = requests.get(url=self.target)
        req.encoding = 'gbk'
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a)
        for each in a:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find('div', id="content", class_='showtxt')
        texts = texts.text.replace('\xa0' * 8, '\n\n')
        return texts

    def writer(self, name, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('开始下载：')
    sys.stdout.write("  已下载:%.3f%%" % 0 + '\r')
    for i in range(dl.nums):
        dl.writer(dl.names[i], 'C:\\Users\\86714\\Desktop\\1\\1.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('下载完成')

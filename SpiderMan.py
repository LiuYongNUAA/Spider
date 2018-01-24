from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import Htmlparser
from UrlManager import Urlmanager
class Spiderman(object):
    def __init__(self):
        self.manager = Urlmanager()
        self.downloader = HtmlDownloader()
        self.parser = Htmlparser()
        self.output = DataOutput()
    def crawl(self, root_url):
        # 添加入口URL
        self.manager.add_new_url(root_url)
        # 判断url管理器是否有新的url，同时判断抓取了多少url
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                # 从url管理器获得新的url
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                html = self.downloader.download(new_url)
                # HTML解析器抽取数据
                new_urls, data = self.parser.parse(new_url, html)
                # 将抽取的url添加到url管理器中
                self.manager.add_new_urls(new_urls)
                # 数据存储器存储文件
                self.output.store_data(data)
                print('已经抓取%s个连接' % self.manager.old_url_size())
            except Exception as e:
                print('crawl failed')
                raise
            # 数据存储器将文件输出指定格式
        self.output.output_html()

if __name__ == '__main__':
    spider_man = Spiderman()
    spider_man.crawl('http://baike.baidu.com/view/284853.htm')
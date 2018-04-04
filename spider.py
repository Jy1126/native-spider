from urllib import request
import re

class Spider():

    url = 'https://www.quanmin.tv/game/juediqiusheng'
    rootpattern = '<div class="common_w-card_info">([\s\S]*?)</div>'
    subhostname = '<span class="common_w-card_host-name">([\s\S]*?)</span>'
    subsum = '<span class="common_w-card_views-num">([\s\S]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        html = r.read()
        html = str(html, encoding='utf-8')
        return html

    def __analysis(self,html):
        args = []
        html = re.findall(Spider.rootpattern,html)
        for v in html:
            name = re.findall(Spider.subhostname,v)[0]
            num = re.findall(Spider.subsum,v)[0]
            args.append({'name':name,'viewssum':num})
        return args

    def __sort(self,args):
        return sorted(args,key=self.__sort_seed,reverse=True)

    def __sort_seed(self,arg):
        return int(arg["viewssum"])

    def go(self):
        html = self.__fetch_content()
        args = self.__analysis(html)
        result = self.__sort(args)
        print(result)

spider = Spider()
spider.go()

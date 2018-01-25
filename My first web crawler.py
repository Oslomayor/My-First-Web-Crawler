# web crawler test
# 1:03AM, Jan 26th, 2018 @ dormitory
# 统计 http://bj.xiaozhu.com/ 网站上 13 个页面的房租价格
import requests
from bs4 import BeautifulSoup
# urls:
# http://bj.xiaozhu.com/search-duanzufang-p1-0/
# http://bj.xiaozhu.com/search-duanzufang-p2-0/
# http://bj.xiaozhu.com/search-duanzufang-p3-0/
# http://bj.xiaozhu.com/search-duanzufang-p4-0/
# ...
# http://bj.xiaozhu.com/search-duanzufang-p13-0/
urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(page) for page in range(1, 14)]
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
avgPrice = 0
count = 0
for url in urls:
    print(url)
    res = requests.get(url, headers=headers)
    # 除了 html.parser 标准库以外，还有 lxml Lxml html5lib
    soup = BeautifulSoup(res.text, 'html.parser')
    prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
    for price in prices:
        avgPrice = avgPrice + int(price.getText())
        count = count+1
        pass
        print(price.getText())
else:
    avgPrice = avgPrice/count
    print(count, 'prices')
    print('The average price is ', avgPrice)

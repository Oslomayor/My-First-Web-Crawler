# web crawler 2.0
# 11.28PM, Jan 29th, 2018 @ dormitory
# 统计 http://bj.xiaozhu.com/ 网站上 13 个页面的房租价格
# 写成函数的形式
# 增加 txt 文件储存
# urls:
# http://bj.xiaozhu.com/search-duanzufang-p1-0/
# http://bj.xiaozhu.com/search-duanzufang-p2-0/
# http://bj.xiaozhu.com/search-duanzufang-p3-0/
# ...
# http://bj.xiaozhu.com/search-duanzufang-p13-0/
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

def getInfo(url):
    global count, avgPrice, maxPrice, minPrice, totalPrice, file
    print("On page ", url)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    # 注意注意：li:nth-child(1) 在 python 中会报错，需要改为 li:nth-of-type(1)
    # price = soup.select('#page_list > ul > li:nth-child(1) > div.result_btm_con.lodgeunitname > span.result_price > i')
    # 提取所有价格，则把 selector 中的 ul > li:nth-child(1) > 改为 ul > li > ，产生一个价格列表 prices
    prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
    for price in prices:
        price = int(price.get_text())
        count += 1
        totalPrice += price
        if maxPrice < price:
            maxPrice = price
        if minPrice > price:
            minPrice = price
        file.writelines('第{0}个房间的价格：{1}元\n'.format(count, price))
        print('第{0}个房间的价格：{1}元'.format(count, price))

def main():
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(page) for page in range(1, 14)]
    global count, avgPrice, maxPrice, minPrice, totalPrice, file
    avgPrice = 0
    totalPrice = 0
    count = 0
    maxPrice = 1
    minPrice = 10000
    file = open('E:/AllPrj/PyCharmPrj/py-crawler/results.txt', 'w')
    for url in urls:
        getInfo(url)
        avgPrice = totalPrice/count
    file.writelines('一共{}个房型\n'.format(count))
    file.writelines('最高价格{max}元，最低价格{min}元\n'.format(max=maxPrice, min=minPrice))
    file.writelines('平均价格{}元\n'.format(avgPrice))
    file.close()
    print('一共{}个房型'.format(count))
    print('最高价格{max}元，最低价格{min}元'.format(max=maxPrice, min=minPrice))
    print('平均价格{}元'.format(avgPrice))

if __name__ == '__main__':
    main()

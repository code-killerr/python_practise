from bs4 import BeautifulSoup
with open('E:\前端\MordenXBookShop\MordenXBookShop\WebContent\index.jsp','r',encoding='UTF-8') as data:
    Soup = BeautifulSoup(data,'lxml')#使用BeautifulSoup读取网页源码，lxml库解析网页
    images = Soup.select('#particles-js > div.qcorder > img')#筛选特定标签，路径为css selector的路径
    print(images)
    button = Soup.select('#particles-js > div.game_num > div > p')
    area = Soup.select('body > div.banner > div.ban_bot > div.ban_bot_con > ul')#选定一块内容,注意li中nth-chile改为nth-of-type才能不报错

for b in button:#此处需要使用for循环取出列表中元素，Soup.select返回的是列表类型的数据
    print(b.get_text())#使用get_text()来读取标签中的文本
print(button[0].get_text())#或者直接指定返回的元素
print('-----------------------------------')
print(images[0].get('src'))#通过get可以获取到需要的标签属性
print('------------------------------------------')
print(area)
print(list(area[0].stripped_strings))#使用stripped_strings会获取标签完全相同的标签中的内容


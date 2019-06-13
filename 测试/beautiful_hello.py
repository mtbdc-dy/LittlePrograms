# -*- coding: utf-8 -*-
# @Time : 2019-06-12 21:37
# @Author : 徐缘
# @FileName: beautiful_hello.py
# @Software: PyCharm


from bs4 import BeautifulSoup

f = open('display.html', 'r')

soup = BeautifulSoup(f, "html.parser")
# print(soup.prettify())

chenqi = ''
other = ''
for item in soup.find_all(attrs={'class': 'history-item-title'}):
    operator = None
    if '处理完成' in item.get_text().strip():
        # print(item.prettify())
        next_sb = item.find_next_sibling('div')
        for rows in next_sb.find_all('td'):
            news = rows.get_text().strip()
            # print(news)
            if '操作人' == news:
                print('操作人', rows.find_next_sibling('td').get_text().strip())
                operator = rows.find_next_sibling('td').get_text().strip()

            if '处理结果描述' in rows.get_text():
                print('处理结果描述', rows.find_next_sibling('td').get_text().strip())
                result = rows.find_next_sibling('td').get_text().strip()

                if operator and operator != '陈琦':
                    if other == '':
                        other = operator + ': ' + result
                    else:
                        other = other + '\n' + operator + ': ' + result

                if operator and operator == '陈琦':
                    if chenqi == '':
                        chenqi = operator + ': ' + result
                    else:
                        chenqi = chenqi + '\n' + operator + ': ' + result
print(other)
print(chenqi)

# print(soup.find('div').find_all('div', recursive=False)[3].prettify())

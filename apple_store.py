#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:55:14 2021

@author: tongchen
"""

from bs4 import BeautifulSoup
import requests
import sys
temp_file=open("temp1.html",'w')
# shop='http://apple.com.cn/shop/buy-'

# product_type=input("please enter product type.iphone,ipad.etc\n")
# product_type=product_type.replace(' ', '')
# shop=shop+product_type
# product_type_list=['mac','ipad','watch','iphone']
# if (product_type.replace(' ','') not in product_type_list) :
#     print('not a legal product name')
#     sys.exit()

# #print(shop)

# product_name=input("please enter product name.iphone 12,iphone 12 pro etc.\n")
# shop=shop+'/'+product_name.replace(' ','-')
# #print(shop)

# sourse_shop=requests.get(shop).text
sourse_shop=requests.get("https://www.apple.com.cn/shop/buy-iphone/iphone-12").text
soup_shop=BeautifulSoup(sourse_shop,'lxml')

url_shop=soup_shop.find("meta",property='og:url')
url_shop_str=url_shop['content']
url_shop_str=url_shop_str.split('/')
# print(url_shop_str[-1])
if(url_shop_str[-1] == '404'):
    print('Invalid shop address.Please try again')
    sys.exit()
#print(url_shop["content"])
print(soup_shop.title.text)

reserve_sites=soup_shop.find_all(target="_blank",class_='more')
print(reserve_sites)
next_site=None
for reserve_site in reserve_sites:
    print(reserve_site.text)
    if(input("[y] or [n]\n") == 'y'):
        next_site=reserve_site['href']
        break;

if(next_site is None):
    print("Error occours when getting to reservation site.please try again")
    sys.exit()


print (next_site)
    



# temp_file.write(soup_shop.prettify())
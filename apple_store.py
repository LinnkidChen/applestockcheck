#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:55:14 2021

@author: tongchen
"""

from bs4 import BeautifulSoup
import requests
import sys
temp_file=open("temp.txt",'w')
shop='http://apple.com.cn/shop/buy-'

product_type=input("please enter product type.iphone,ipad.etc\n")
product_type=product_type.replace(' ', '')
shop=shop+product_type
product_type_list=['mac','ipad','watch','iphone']
if (product_type.replace(' ','') not in product_type_list) :
    print('not a legal product name')
    sys.exit()

#print(shop)

product_name=input("please enter product name.iphone 12,iphone 12 pro etc.\n")
shop=shop+'/'+product_name.replace(' ','-')
print(shop)

sourse_shop=requests.get(shop).text
soup_shop=BeautifulSoup(sourse_shop,'lxml')

print(soup_shop.title.text)
#print('invalid shop address.please check input')
   
    

    

temp_file.write(soup_shop.prettify())
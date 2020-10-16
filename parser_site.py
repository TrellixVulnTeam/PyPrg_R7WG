# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
from lxml import etree

import pandas as pd
import xlwt
import re

df = pd.DataFrame

def save_table_to_excel(list_catalog_number = [], list_feauture = [], list_pruduct = [], list_price_discount = []):
    # Specify a writer

#    df['list_catalog_number'] = False
#    df['list_feauture'] = Fa
#    df['list_pruduct'] = False
#    df['list_price_discount'] = False
    for i in range(0, len(list_catalog_number)):
        df.iat[i, 'list_catalog_number'] = list_catalog_number[i]
        df.iat[i, 1] = list_feauture[i]
        df.iat[i, 2] = list_pruduct[i]
        df.iat[i, 3] = list_price_discount[i]
#    model = PandasModel(df)
    path = 'DKS.xlsx'
    writer = pd.ExcelWriter(path, engine='xlsxwriter')

    # Write your DataFrame to a file
    df.to_excel(writer, 'DKS')

    # Save the result
    writer.save()



def save_to_excel(ws, wb, list_catalog_number = [], list_feauture = [], list_pruduct = [], list_price_discount = [], catalog_item_price =[], list_img =[], icur = 1):
    i = 0  # параметр, позволяющий перемещаться в ячейках по столбцам
    j = icur  # параметр, позволяющий перемещаться в ячейках по строкам


    for x in range(1,len(list_catalog_number)):
        ws.write(j, 0, list_catalog_number[x])
        st = list_feauture[x]
        ws.write(j, 1, re.findall(r'Производитель(.*?)Выход. мощность, ВА', st))
        ws.write(j, 2, re.findall(r'Выход. мощность, ВА(.*?)Исполнение', st))
        ws.write(j, 3, re.findall(r'Исполнение(.*$)', st))
        ws.write(j, 4, list_pruduct[x])
        # ws.write(j, 5, list_price_discount[x])
        ws.write(j, 6, catalog_item_price[x])
        ws.write(j, 7, list_img[x])
        j += 1

    wb.save(path)

def get_html(url):
    r = requests.get(url)    # Получим метод Response
    r.encoding = 'utf8'
    return r.text   # Вернем данные объекта text


def csv_read(data):
    with open("data.csv", 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow((data['Каталожный номер'], data['Свойства'], data['Описание'], data['Скидка']))

def get_data(soup, tag, atrtag):
    convert = soup.find_all(tag, {"class": atrtag})
    list_tag_val = []
#    data = []
    for entry in convert:
        list_tag_val.append(entry.get_text(strip=True))
#        data = {'Описание': entry.get_text()}
    return list_tag_val#, data

def get_link(ws, wb, html, icur = 1):
    soup = BeautifulSoup(html, 'lxml')

    list_catalog_number = get_data(soup, 'div', "catalog-item__code")
    print(list_catalog_number)

    list_feauture = get_data(soup, 'ul', "catalog-item__feature")
    print(list_feauture)

    list_pruduct = get_data(soup, 'div', "catalog-item__title")
    print(list_pruduct)


    list_price_discount = get_data(soup, 'span', "catalog-item-price catalog-item-price_personal")
    print(list_price_discount)

    list_ul= get_data(soup, 'div', "wrap-pagination")
    print(list_ul)

    catalog_item_price= get_data(soup, 'span', "catalog-item-price__val")
    print(catalog_item_price)

    soup_img = BeautifulSoup(html, 'html.parser')
    data_img = soup_img.find_all('div', {"class": "catalog-item-top"})
    # data_img = get_data(soup_img, 'div', "catalog-item-top")
    # print(data_img)
    list_img = []
    # div = soup_img.find('div', {"class": "catalog-item-top"})
    for article in data_img:
        list_img.append(article.find('img').attrs['src'])

    # for article in articles:
    #     img_src = article.find('div', class_='o-rating_thumb c-white').img['data-original']
    #     headline = article.h2.text.strip()
    #     summary = article.find('p', class_='mt-15@m+ t-d5@m- t-d5@tp+ c-gray-3').text

    # images = soup.findAll('img')
    # print(images)

    # for i in range(0,len(list_catalog_number)):
    #     data_all = {'Каталожный номер': list_catalog_number[i],
    #             'Свойства': list_feauture[i],
    #             'Описание': list_pruduct[i],
    #             'Скидка': list_price_discount[i]
    #             }
    #     csv_read(data_all)
#    save_table_to_excel(list_catalog_number, list_feauture, list_pruduct, list_price_discount)
    save_to_excel(ws, wb, list_catalog_number, list_feauture, list_pruduct, list_price_discount,catalog_item_price, list_img,  icur)
    return len(list_catalog_number)


#dks data = get_link(get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/?display_type=tile&set_filter=Показать&arrFilter_P1_MIN=1970&arrFilter_P1_MAX=8292697&arrFilter_208_1955232490=DKC&1458992227='))
#data = get_link(get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/?sort=price&display_type=tile&0=&1=&set_filter=Показать&arrFilter_P1_MIN=1970&arrFilter_P1_MAX=8292697&arrFilter_208_1955232490=DKC&arrFilter_208_4171867725=EATON&arrFilter_208_1597891823=Schneider+Electric&1458992227='))
wb = xlwt.Workbook()
ws = wb.add_sheet('ДКС')#, cell_overwrite_ok=True)
path = 'DKS.xlsx'
ws.write(0, 0, "Каталожный номер")
ws.write(0, 1, "Производитель")
ws.write(0, 2, "Выход. мощность, ВА")
ws.write(0, 3, "Исполнение")
ws.write(0, 4, "Описание")
ws.write(0, 5, "Персональная цена, Руб")
ws.write(0, 6, "Цена по каталогу, Руб")
ws.write(0, 7, "Картинки")



icuri = 1
leni = get_link(ws, wb, get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/on-line/?PAGEN_1=1'), icuri)

icuri = icuri + leni
leni = get_link(ws, wb, get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/on-line/?PAGEN_1=2'), icuri)

icuri = icuri + leni
leni = get_link(ws, wb, get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/on-line/?PAGEN_1=3'), icuri)

icuri = icuri + leni
leni = get_link(ws, wb, get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/on-line/?PAGEN_1=4'), icuri)

icuri = icuri + leni
leni = get_link(ws, wb, get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/on-line/?PAGEN_1=5'), icuri)

icuri = icuri + leni
leni = get_link(ws, wb, get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/on-line/?PAGEN_1=6'), icuri)

icuri = icuri + leni
leni = get_link(ws, wb, get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/on-line/?PAGEN_1=7'), icuri)

icuri = icuri + leni
leni = get_link(ws, wb, get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/on-line/?PAGEN_1=8'), icuri)

icuri = icuri + leni
leni = get_link(ws, wb, get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/on-line/?PAGEN_1=9'), icuri)

icuri = icuri + leni
leni = get_link(ws, wb, get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/on-line/?PAGEN_1=10'), icuri)

icuri = icuri + leni
leni = get_link(ws, wb, get_html('https://www.tesli.com/catalog/ibp/istochniki-bespereboynogo-pitaniya/on-line/?PAGEN_1=11'), icuri)
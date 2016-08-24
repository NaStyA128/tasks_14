from urllib.request import urlopen
from pyquery import PyQuery as pq
import time
import json

all_products = []


def parser(url):
    time.sleep(1)
    r = urlopen(url)
    print('Done...%s' % url)
    content = r.read()
    this = pq(content)
    return this


def parse_one_page(start_url, next_url=''):
    inspection = True
    if next_url:
        this = parser(next_url)
        inspection = False
    else:
        if inspection:
            this = parser(start_url)
    products = this('#catalogue .gd-pltk .gd-promo-brdr')
    for product in products:
        my_product = {}
        product = pq(product)
        my_product['href'] = "http://hotline.ua%s" % product('.gd-info-cell a.g_statistic').attr('href')
        this_product_info = parser(my_product['href'])
        my_product['name'] = this_product_info('.txt-center .title-24').text()
        my_product['description'] = this_product_info('.description p.full-desc').text()
        my_product['image'] = "http://hotline.ua%s" % \
                              (this_product_info('.block-img-gall img').attr('src'))
        my_product['price'] = this_product_info('.price-block a.range-price').text()
        characteristics = this_product_info('.content .th-tabl #short-props-list table tr')
        for characteristic in characteristics:
            characteristic = pq(characteristic)
            my_product[characteristic('th span').text()] = characteristic('td').text()
        all_products.append(my_product)
    page_next = this('.pager a.pager-arr.next')
    if page_next:
        page_next = pq(page_next)
        parse_one_page(
            start_url,
            start_url + page_next.attr('href')
        )
    return all_products


if __name__ == "__main__":
    start_url = "http://hotline.ua/musical_instruments/gitary-akusticheskie/"
    all_products = {
        'all_prod': parse_one_page(start_url)
    }
    print(all_products['all_prod'].__len__())
    if all_products['all_prod']:
        with open('data.txt', 'w') as f:
            json.dump(all_products, f, ensure_ascii=False, indent=4)

from urllib.request import urlopen
from pyquery import PyQuery as pq


def parser(url):
    r = urlopen(url)
    content = r.read()
    this = pq(content)
    return this


if __name__ == "__main__":
    this = parser("http://hotline.ua/musical_instruments/gitary-akusticheskie/")
    products = this('#catalogue .gd-pltk .gd-promo-brdr')
    all_products = []
    for product in products:
        my_product = {}
        product = pq(product)
        my_product['href'] = product('.gd-info-cell a.g_statistic').attr('href')
        this_product_info = parser("http://hotline.ua%s" % (my_product['href']))
        my_product['name'] = this_product_info('.txt-center .title-24').text()
        my_product['description'] = this_product_info('.description p.full-desc').text()
        my_product['image'] = "http://hotline.ua%s" % \
                              (this_product_info('.block-img-gall img').attr('src'))
        my_product['price'] = this_product_info('.price-block a.range-price').text()
        characteristics = this_product_info('.content .th-tabl #short-props-list table tr')
        characteristics = pq(characteristics)
        # for characteristic in characteristics:
        #     my_product[characteristic('th span').text()] = characteristic('td').text()
        print(my_product)
        break


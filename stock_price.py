import hmac
import time
import requests
import hashlib
from dotenv import load_dotenv
import os
from os.path import join, dirname
import pandas as pd
import urllib.parse as urlparse
from urllib.parse import urlencode

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

listed_item_list = pd.read_csv('listed_item.csv', header=None).values.tolist()
cols = ['col1', 'col2','col3','col4','col5']
listed_item_df = pd.DataFrame(index=[], columns=cols)
partner_id = 9001
shop_id = os.environ.get("SHOP_ID")
timest = int(time.time())


def update_price_url(url,item_id,price):
    params = {
        "partner_id" : partner_id,
        "timest" : timest,
        "shop_id" : shop_id,
        "item_id": item_id,
        "price_list": [{
        "original_price": price
        }]
    }
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    req_url = urlparse.urlunparse(url_parts)
    return req_url


def update_stock_url(url,item_id,stock):
    params = {
        "partner_id" : partner_id,
        "timest" : timest,
        "shop_id" : shop_id,
        "item_id": item_id,
        "stock_list": [{
        "normal_stock": stock
        }]
    }
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    req_url = urlparse.urlunparse(url_parts)
    return req_url

def update_price_stock():
    for listed_item in listed_item_list:
        asin = listed_item[0]
        price = listed_item[2]
        stock = listed_item[3]
        new_amazon_price = 3000
        new_amazon_stock = 3
        item_id = listed_item[4]
        # 価格調整
        if price != new_amazon_price:
            price = new_amazon_price * 1.5
            listed_item[2] = price
            url ="https://partner.shopeemobile.com/api/v2/product/update_price"
            req_url = update_stock_url(url,item_id,stock)
        # 在庫調整
        if stock != new_amazon_stock:
            stock = new_amazon_stock
            listed_item[3] = stock
            url = "https://partner.shopeemobile.com/api/v2/product/update_stock"
            req_url = update_stock_url(url,item_id,stock)

        record = pd.Series(listed_item, index=listed_item_df.columns)
        listed_item_df = listed_item_df.append(record, ignore_index=True)
        
    listed_item_df.to_csv('listed_item.csv',header=False,index=False)

import hmac
import time
import requests
import hashlib
from dotenv import load_dotenv
import os
from os.path import join, dirname
import pandas as pd

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

timest = int(time.time())
host = "https://partner.shopeemobile.com"
path = "/api/v2/shop/auth_partner"
redirect_url = "https://www.baidu.com"
partner_id = 9001
partner_key = ""
base_string = "%s%s%s"%(partner_id,path,timest)
sign = hmac.new(partner_key,base_string,hashlib.sha256).hexdigest()
url = host + path + f"?partner_id={partner_id}&timestamp={timest}&sign={sign}&redirect={redirect_url}"



def listing_shopee():

    cols = ['col1', 'col2','col3','col4']
    listed_item_df = pd.DataFrame(index=[], columns=cols)
    shop_id = os.environ.get("SHOP_ID")

    for i in range():
        amazon_item_data = [1,2,3,4,5]
        asin = amazon_item_data[0]
        name = amazon_item_data[2]
        description = amazon_item_data[2]
        price = amazon_item_data[1]
        stock = amazon_item_data[4]
        enabled = True
        logistic_id =4
        category_id = amazon_item_data[4]
        imadge = amazon_item_data[5]
        image_id_list = amazon_item_data[6]
        url = f"https://partner.shopeemobile.com/api/v2/product/add_item?partner_id={partner_id}&timestamp={timest}&shop_id={shop_id}"
        
        record = pd.Series([asin, name,price,stock], index=listed_item_df.columns)
        listed_item_df = listed_item_df.append(record, ignore_index=True)

    listed_item_df.to_csv('listed_item.csv', mode='a', header=False,index=False)
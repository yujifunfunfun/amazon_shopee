# import pandas as pd

# listed_item_list = pd.read_csv('listed_item.csv', header=None).values.tolist()

# for listed_item in listed_item_list:
#     print(listed_item[0])


# cols = ['col1', 'col2','col3','col4','col5']
# listed_item_df = pd.DataFrame(index=[], columns=cols)

# for i in range(3):

#     record = pd.Series(["asin", "name",3000,"stock",300], index=listed_item_df.columns)
#     listed_item_df = listed_item_df.append(record, ignore_index=True)

# listed_item_df.to_csv('listed_item.csv', header=False,index=False)


import urllib.parse as urlparse
from urllib.parse import urlencode

url ="https://partner.shopeemobile.com/api/v2/product/update_price"

params = {
"item_id": 1000,
"price_list": [{
"original_price": 11.11
}]
}
url_parts = list(urlparse.urlparse(url))
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(params)
url_parts[4] = urlencode(query)
print(urlparse.urlunparse(url_parts))
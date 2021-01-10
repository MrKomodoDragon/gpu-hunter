import requests
import re

user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'}
url = 'https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659'
keywords = 'Add to Cart'
response = requests.get(url, headers=user_agent)
code = response.text
code2 = code.encode('utf-8')
if re.search(keywords, code2, re.IGNORECASE):
    print("Product is in stock.")


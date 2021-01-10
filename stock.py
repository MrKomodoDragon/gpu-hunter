import requests
import re
from discord_webhook import DiscordWebhook
import sys
import os
user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'}
product_url = 'https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659'
keywords = 'Add to Cart'
product_name = 'Apple Airpods Pro'
response = requests.get(product_url, headers=user_agent)
code = response.text
code2 = code.encode('utf-8')
if re.search(keywords, code2.decode('utf-8'), re.IGNORECASE):
    webhook = DiscordWebhook(url='https://canary.discord.com/api/webhooks/788141524260618251/UjOC1tcqBjlrnWT5YFzX-_KWrxjAn9Ewze56-ZCQYwd1LuITf9UzWA3PM-XHesJbFuq5', content=f"{product_name} is in stock now at {product_url}")
    response = webhook.execute()
    os.system(f'notify-run send \'{product_name} found in stock. Click to open the page.\' -a {product_url}')
    sys.exit()


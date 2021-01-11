import requests
import re
from discord_webhook import DiscordWebhook
import sys
import os
import smtplib
import ssl
port = 587  # For starttls
smtp_server = "smtp.office365.com"
sender_email = "my@gmail.com"
receiver_email = "my@gmail.com"
password = "password123"
user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'}
product_url = 'https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659'
keywords = 'Add to Cart'
product_name = 'Apple Airpods Pro'
message = """\
    Subject: Stock Notification

    The product {} is found in Stock. View it at {}.""".format(product_name, product_url)
response = requests.get(product_url, headers=user_agent)
code = response.text
context = ssl.create_default_context()
code2 = code.encode('utf-8')
if re.search(keywords, code2.decode('utf-8'), re.IGNORECASE):
    webhook = DiscordWebhook(url='https://canary.discord.com/api/webhooks/788141524260618251/UjOC1tcqBjlrnWT5YFzX-_KWrxjAn9Ewze56-ZCQYwd1LuITf9UzWA3PM-XHesJbFuq5', content=f"{product_name} is in stock now at {product_url}")
    response = webhook.execute()
    os.system(f'notify-run send \'{product_name} found in stock. Click to open the page.\' -a {product_url}')
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    sys.exit()


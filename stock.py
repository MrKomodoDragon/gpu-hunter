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
product_urls = ['https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659' , 'https://www.newegg.com/p/0TH-00CT-00318?Description=airpods%20pro&cm_re=airpods_pro-_-9SIAEYJD3H4300-_-Product']
keywords = 'Add to Cart'
product_name = 'Apple Airpods Pro'
for u in product_urls:
    subject = 'Stock Notification'
    text = 'The product {} is found in Stock. View it at {}.'.format(product_name, u)
    message = 'Subject: {}\n\n{}'.format(subject, text)
    response = requests.get(u, headers=user_agent)
    code = response.text
    context = ssl.create_default_context()
    code2 = code.encode('utf-8')
    if re.search(keywords, code2.decode('utf-8'), re.IGNORECASE):
        webhook = DiscordWebhook(url='webhook_url_goes_here', content=f"{product_name} is in stock now at {u}")
        response = webhook.execute()
        os.system(f'notify-run send \'{product_name} found in stock. Click to open the page.\' -a {u}')
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        sys.exit()


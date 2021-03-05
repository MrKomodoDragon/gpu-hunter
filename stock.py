import requests
import re
from discord_webhook import DiscordWebhook
import sys
import os
import smtplib
import ssl
port = 587  # For starttls
subject = 'Stock Notification'
for u in product_urls:
    text = 'The product {} is found in Stock. View it at {}.'.format(product_name, u)
    message = 'Subject: {}\n\n{}'.format(subject, text)
    response = requests.get(u, headers=user_agent)
    code = response.text
    context = ssl.create_default_context()
    code2 = code.encode('utf-8')
    if re.search(keywords, code2.decode('utf-8'), re.IGNORECASE):
        webhook = DiscordWebhook(url=webhook_url, content=f"{product_name} is in stock now at {u}")
        response = webhook.execute()
        os.system(f'notify-run send \'{product_name} found in stock. Click to open the page.\' -a {u}')
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        sys.exit()


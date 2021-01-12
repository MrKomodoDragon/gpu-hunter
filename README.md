# gpu-stock-tracker
gpu-tracker is a simple stock tracker to keep track of the stock of GPUs.

# Why was this made?
As I looked around sites for a gpu to buy, I noticed a lot of GPUs went out of stock quickly. I decided to automate the process of checking the sites for a gpu in stock with Python.

# Setup

First install a couple of dependencies: 

```
pip install notify-run discord-webhook
```

Then, clone the repo:

```
git clone https://github.com/MrKomodoDragon/gpu-tracker.git
```

Next, you can set up whatever products you would track and how you would like to be notified.

## Adding a product to Track

To do this, change the url for the variable `product_url` in the stock.py file. You can add a [single product](https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659), or a [search result](https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&qp=category_facet%3DGPUs%20%2F%20Video%20Graphics%20Cards~abcat0507002&sc=Global&st=gtx%201660%20super&type=page&usc=All%20Categories) to keep track of multiple products that meet criteria you want to set based on the filters on the website itself. 

You can also change the product name to customize the notifications, under `product_name`.

## Setting up Email

To set up email, you should fill out the `sender_email` and `reciever_email` with your own email address first. Then, to fill out the `smtp_server` variable, check out [this site](https://support.microsoft.com/en-us/office/pop-and-imap-email-settings-for-outlook-8361e398-8af4-4e97-b147-6c6c4ac95353) to find the name of the SMTP server.

For gmail, you have to go to settings and turn on allow less secure apps access.

**NOTE: This setting makes your account more vulnerable. I highly recommend creating another account for the email notifications for this reason. Even if you don't have to turn on this setting for other email providers, I still recommend creating a separate account so your main account doesn't get flooded with emails.**

## Setting up Discord Webhook

First, [make a webhook.](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks). Then, set the `url` variable in line 25 to the webhook url.

## Setting up Notify-Run

So, in a terminal, first run `notify-run register` to get the channel link and subscribe on the all the devices you would like to receive notifications on. 

## Customizing the Notifications

So, to customize the notifications, just edit `product_name`




# gpu-tracker
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


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

To do this, change the url for the variable `product_url` in the stock.py file. You can add a [single product],


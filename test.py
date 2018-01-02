import gdax
import math


client = gdax.PublicClient()

data = client.get_product_order_book("ETH-USD", level=2)
tick = client.get_product_ticker("ETH-USD")
#trades = client.get_product_trades("ETH-USD")
#print(trades)
print(float(tick["price"]))
sum = 0.0
bidsize = 0.0
for x in data["bids"]:
    sum += float(x[0]) * float(x[1])
    bidsize += float(x[1])

print(math.sqrt(sum / bidsize))
print(sum)

sum2 = 0.0
bidsize = 0.0
for x in data["asks"]:
    sum2 += float(x[0]) * float(x[1])
    bidsize += float(x[1])

print(math.sqrt(sum2/bidsize))
print(sum2)

print(sum/(sum2))
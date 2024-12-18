from ib_insync import IB, Stock, LimitOrder

# Connect to IBKR
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

# Define a stock contract
contract = Stock('AAPL', 'SMART', 'USD')

# Define a limit order with GTC timeInForce
order = LimitOrder('BUY', 10, 150)  # Buy 10 shares at $150
order.timeInForce = 'GTC'  # Good Till Canceled

# Place the order
trade = ib.placeOrder(contract, order)
print("Order placed. Status:", trade.orderStatus.status)


ib.disconnect()

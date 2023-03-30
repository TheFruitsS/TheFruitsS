# Approximately how many USD can be purchased for 2550 CHF at the end of 2012?Required to answer. Single choice.
chf = abs(0.027*0.0014 - 0.027)
usd = 0.0337 * 0.0007 + 0.337
# to find the currency we need to divide the usd to chf and after that to multiply by the value of the current currency
exchange_USD = (usd / chf * 2550)
print(exchange_USD)

# This code refers to the velocity of bitcoin as mentioned in the book 
# "Cryptoassets". Some values are assumed for ease of calculation. 

# The formula for Velocity is: GDP / Total Money Supply 

US_GDP = 20000000000000
US_money_supply = 5000000000000

def velocity_of_money(GDP, M):
	velocity = GDP / M
	result = "Velocity of money: {}".format(velocity)
	return result

print(velocity_of_money(US_GDP, US_money_supply))

# If instead we know the GDP, we can change the formula to 
# find the value of bitcoin in USD

remmitance_market_GDP = 500000000000
bitcoin_velocity_remmitance = 5
supply_of_bitcoin = 21000000
remmitance_market_served_1 = 1
remmitance_market_served_2 = 0.2


def value_of_bitcoin(GDP, velocity, supply, market_size):
	total_bitcoin_value = GDP / velocity 
	usd_per_bitcoin = (total_bitcoin_value / supply) * market_size
	return usd_per_bitcoin

print("If Bitcoin serves 100 percent of the service market:")
remmitance_bitcoin_1 = value_of_bitcoin(remmitance_market_GDP, 
	bitcoin_velocity_remmitance, supply_of_bitcoin, 
	remmitance_market_served_1)
print("USD per Bitcoin: {}".format(remmitance_bitcoin_1))

print("If Bitcoin serves 20 percent of the service market:")
remmitance_bitcoin_2 = value_of_bitcoin(remmitance_market_GDP, 
	bitcoin_velocity_remmitance, supply_of_bitcoin, 
	remmitance_market_served_2)
print("USD per Bitcoin: {}".format(remmitance_bitcoin_2))

# Bitcoin use-cases are additive, so if there are any other use-cases
# we will just add the value of bitcoin in all use-cases together

gold_market_GDP = 2400000000000
bitcoin_velocity_gold = 1 # bitcoin as digital gold does not turn over 
# supply of bitcoin stays the same (steady state of 21 million)
gold_market_served = 0.1

print("If Bitcoin serves 10 percent of the service market:")
gold_bitcoin = value_of_bitcoin(gold_market_GDP, 
	bitcoin_velocity_gold, supply_of_bitcoin, gold_market_served)
print("USD per Bitcoin: {}".format(gold_bitcoin))

# Total Value of Bitcoin

total_bitcoin_value = remmitance_bitcoin_2 + gold_bitcoin

print("Bitcoin Total Value: {}".format(total_bitcoin_value))



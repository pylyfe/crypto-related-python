# Values assumptions 
hashing_power = 1000000000000 # 1 TH/s
block_reward = 25 # bitcoins per block
mining_difficulty = 47427554950.6483

#constant time values
s = 3600
h = 24
c = 2**32 #normalized probability of a single has solving a block

def get_theta(seconds_per_hour, hours_per_day, constant):
	theta_value = hours_per_day * (seconds_per_hour / constant)

	return theta_value

mining_time_per_day = get_theta(s, h, c)

def btc_per_day(mining_time_per_day, mining_difficulty, block_reward, hashing_power):
	theta = mining_time_per_day
	beta = block_reward
	rho = hashing_power
	delta = mining_difficulty

	bitcoin_per_day = (theta * beta * rho) / delta

	return bitcoin_per_day

bitcoins_per_day = btc_per_day(mining_time_per_day, mining_difficulty, block_reward, hashing_power)

print("BTC/day: {}".format(bitcoins_per_day))

# Finding Market Price of Bitcoins 

# Energy consumption and computing power assumptions 
p = 0.115 #11.5 cents
e = 0.95

def mining_cost_per_day(price_per_kwh, hours_per_day, watts_per_gh):
	hashing_power_gh = 1000

	E_day = (price_per_kwh * hours_per_day * watts_per_gh) / (hashing_power_gh/1000)

	return E_day

dollar_cost = mining_cost_per_day(p, h, e)

dollar_per_btc = dollar_cost/bitcoins_per_day

print("$/BTC: {}".format(dollar_per_btc)) # Market Price 

# Scenario 1: Stop mining if difficulty is 57541669370

new_mining_difficulty = 57541669370

btc_per_day_new = btc_per_day(mining_time_per_day, new_mining_difficulty, block_reward, hashing_power)

dollar_per_btc_new_1 = dollar_cost / btc_per_day_new

print("$/BTC Scenario 1: {}".format(dollar_per_btc_new_1))

# Scenario 2: price per KwH is 13.952 cents

new_p = 0.13952

dollar_cost_new = mining_cost_per_day(new_p, h, e)

dollar_per_btc_new_2 = dollar_cost_new / bitcoins_per_day

print("$/BTC Scenario 2: {}".format(dollar_per_btc_new_2))

# Scenario 3: W per GH/S is 1.15 

new_e = 1.15

dollar_cost_new_2 = mining_cost_per_day(p, h, new_e)

dollar_per_btc_new_3 = dollar_cost_new_2 / bitcoins_per_day

print("$/BTC Scenario 3: {}".format(dollar_per_btc_new_3))





	


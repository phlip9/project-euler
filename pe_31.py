# How many different ways can £2 be made using any number of coins?

total_pence = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
combinations = [1] + [0] * total_pence

for coin in coins:
	for i in range(coin, total_pence + 1):
		combinations[i] += combinations[i - coin]

print(combinations[total_pence])

# 73682
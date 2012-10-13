def nextChain(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3*n + 1

chain = 0
iterations = 0
longest_chain = 0
longest_chain_num = 0

for i in range(1000000, 0, -1):
	chain = nextChain(i)
	iterations = 1
	while chain != 1:
		chain = nextChain(chain)
		iterations += 1

	if iterations > longest_chain:
		longest_chain = iterations
		longest_chain_num = i
		print(longest_chain_num, ":", longest_chain)

print("longest_chain_num: ", longest_chain_num, "longest_chain:", longest_chain)
#837799
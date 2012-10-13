# what is the total of all name scores in the file names.txt?

import fileinput

letter_map = {
	'A':1,
	'B':2,
	'C':3,
	'D':4,
	'E':5,
	'F':6,
	'G':7,
	'H':8,
	'I':9,
	'J':10,
	'K':11,
	'L':12,
	'M':13,
	'N':14,
	'O':15,
	'P':16,
	'Q':17,
	'R':18,
	'S':19,
	'T':20,
	'U':21,
	'V':22,
	'W':23,
	'X':24,
	'Y':25,
	'Z':26
}

with fileinput.input("names.txt") as names_file:
	for line in names_file:
		names = sorted(line[1:-1].split("\",\""))

		total = 0

		for i in range(len(names)):
			name_sum = 0
			for c in names[i]:
				name_sum += letter_map[c]
			#print(names[i], ":", name_sum, ":", (i + 1))
			total += name_sum * (i + 1)

		print("total:", total)

	names_file.close()

# 871198282
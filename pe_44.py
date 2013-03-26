# find the pair of pentagonal numbers whose sum and difference are pentagonal
# and |Pk - Pj| is minimised

#from math import sqrt

pentagonals = [int((3*p*p-p)/2) for p in range(1, 3000)]
pentagonal_set = set(pentagonals)

#def pentagonal(n):
    #if n <= 0:
        #return False
    ## check if perfect square
    #h = (1 + 24 * n) & 0xF
    #if h != 0 and h != 1 and h != 4 and h != 9:
        #return False
    ## check if non-generalised pentagonal
    #return sqrt(1 + 24 * n) % 6 == 5

differences = ((x, y) for x in pentagonals for y in pentagonals if x - y in pentagonal_set)
sums = filter(lambda x: x[0] + x[1] in pentagonal_set, differences)
print(min(map(lambda x: abs(x[1] - x[0]), sums)))

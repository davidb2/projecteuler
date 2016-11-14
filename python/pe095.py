from math import sqrt
MIN = -99999
cache = {}
lengths = {0: 0}
next = {}
chain = {}
def smallestNumberInAmicableChain(number): 
    chainLength = 0
    def sumOfProperDivisors(n): 
        acc = 1
        for x in xrange(2, 1+int(sqrt(n))):
            y = n//x
            if x * y == n:
                acc += x + (0 if x == y else y)
        return acc
    def recurrence(alreadyVisited, initialNumber, currentNumber, iterations):
        if currentNumber == 220 or currentNumber == 284:
            print currentNumber, alreadyVisited
        # print 'calculating', currentNumber, cache, lengths
        if currentNumber == initialNumber and alreadyVisited != set():
            # print 'gotem', currentNumber
            lengths[currentNumber] = 1
            return currentNumber
        elif currentNumber in alreadyVisited or currentNumber < 2 or currentNumber > 1000000:
            # print initialNumber, alreadyVisited
            # print 'already', currentNumber
            lengths[initialNumber] = MIN
            return 0
        elif currentNumber not in cache:
            # print 'notincache', currentNumber
            alreadyVisited.add(currentNumber)
            if currentNumber not in next:
                next[currentNumber] = sumOfProperDivisors(currentNumber)
            nextNumber = next[currentNumber]
            smallest = recurrence(alreadyVisited, initialNumber, nextNumber, iterations + 1)
            cache[currentNumber] = min(currentNumber, smallest)
            if nextNumber in lengths and lengths[nextNumber] > 0:
                chain[currentNumber] = alreadyVisited
            else:
                chain[currentNumber] = set()
            if nextNumber in chain and currentNumber in chain[nextNumber]:
                lengths[currentNumber] = lengths[nextNumber] + iterations
            else:
                lengths[currentNumber] = MIN
        return cache[currentNumber]
    ans = recurrence(set(), number, number, 0)
    return ans, lengths[number]

a = map(smallestNumberInAmicableChain, xrange(1, 13000))

print cache[220]
print lengths[220]
print next[220]
print chain[220]

print cache[284]
print lengths[284]
print next[284]
print chain[284]
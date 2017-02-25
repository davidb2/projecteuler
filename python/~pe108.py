from Queue import PriorityQueue
from fractions import Fraction

nums = {}

seen = set()

pq = PriorityQueue()
frac = Fraction(1, 2), Fraction(1, 2)
pq.put_nowait(((frac[0] + frac[1]).denominator, (frac[0], frac[1])))

while not pq.empty():
    weight, (frac1, frac2) = pq.get_nowait()
    hashing = frac1.denominator, frac2.denominator
    if hashing not in seen:
        seen.add(hashing)
        if weight not in nums:
            nums[weight] = 0

        nums[weight] += 1
        print '{} + {} = {}'.format(frac1, frac2, frac1+frac2) 
        if nums[weight] > 5:
            print weight
            print nums
            break
        fracp = Fraction(1, frac1.denominator+1), frac2
        fracpp = frac1, Fraction(1, frac2.denominator+1)
        pq.put_nowait((((fracp[0] + fracp[1]).denominator), (fracp[0], fracp[1])))
        pq.put_nowait((((fracpp[0] + fracpp[1]).denominator), (fracpp[0], fracpp[1])))


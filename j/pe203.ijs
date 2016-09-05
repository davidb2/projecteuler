pr  =: i.@:>:!]
isf =: 0:`(0:`]@.((~. -: ])@:q:))@.(>&0)
+/(isf"0)~.,/(pr"0)i.51

### python pseudo-code ###

def pr(n):
	return list(map(lambda r: binomial(n, r), range(n+1)))
def isf(n):
	if n <= 0:
		return 0
	else:
		qs = prime_factorization(n)
		if qs == distinct(qs):
			return n
		else:
			return 0
print(sum(map(isf, distinct(flatten(map(pr, range(51)))))))
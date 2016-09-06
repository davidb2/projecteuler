def psieve(limit):
    bprimes = {key: True for key in list(range(1,limit+2))}
    bprimes[1] = False
    primes = []
    p = [2]
    for i in p:
        for step in list(map(lambda x: x * i, list(range(2, int(limit/i)+1)))):
            bprimes[step] = False
        if i+1 < int(limit/2):
            for pr in range(i+1, len(bprimes)+1):
                if bprimes[pr]:
                    p.append(pr)
                    break
        else:
            break
    for k in range(1, len(bprimes)):
        if bprimes[k]:
            primes.append(k)
    return primes
ans = sum(psieve(2000000))
print(ans)
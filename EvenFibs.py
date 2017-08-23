"""
EvenFibs.py

Author: Julia Edwards
Date: August 2017
Github: jedwardsjunior
"""

def computeSumOfEvenFibonaciNumbers(target):
    fibsUpToFifty, fibCache = getFib(50, {})
    current = 0
    sum = 0
    for fib in sorted(fibCache.values()):
        if fib > target:
            break
        if fib % 2 == 0:
            sum += fib

    return sum
        

def getFib(n, cache):
    if cache.get(n):
        return (cache[n], cache)

    if n < 2:
        cache[n] = 1
        return (1, cache)

    fibN1, cache = getFib(n-1, cache)
    fibN2, cache = getFib(n-2, cache)
    fib = fibN1 + fibN2
    cache[n] = fib
    return fib, cache
    

def main():
    print(computeSumOfEvenFibonaciNumbers(4000000))

main()

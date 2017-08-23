"""
Sum3And5.py

Author: Julia Edwards
Date: August 2017
Github: jedwardsjunior
"""

def findSumOfMultiple(multiple, target, discount):
    sum = 0
    count = multiple
    while count < target:
        if (not discount.get(str(count))):
            sum += count
            discount[str(count)] = True
        count += multiple

    return (sum, discount)

def main():
    target = 1000
    discount = {}
    sumThree, discount = findSumOfMultiple(3, target, discount)
    sumFive, discount = findSumOfMultiple(5, target, discount)
    print(sumThree + sumFive)
    

main()

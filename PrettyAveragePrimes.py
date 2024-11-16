def findPrimes(num):
    numList = [True for i in range(num + 1)]
    answer = []

    n = 2
    while n**2 <= num:
        if numList[n]:
            for i in range(n**2, num, n):
                numList[i] = False
        n += 1

    for i in range(2, num+1):
        if numList[i]:
            answer.append(i)
    return answer

def findPrimeAddends(num):
    primeNumList = (findPrimes(num))
    # now to find the appends for the current prime number
    # checking the first index of the list and the last index of the list
    # if the sum is less than num -> index 1 should go up to index 2, etc.
    # if the sum is larger than num -> the last index should go to n-1, etc.
    # if the sum is num -> return the two numbers in that index

    k = 0
    l = len(primeNumList) - 1
    while True:
        sum = primeNumList[k] + primeNumList[l]
        if sum > num:
            l -= 1
        elif sum < num:
            k += 1
        else:
            return f"{primeNumList[k]} {primeNumList[l]}"

T = int(input()) # tells you the number of inputs of prime numbers incoming

for i in range(T):
    primeNumInput = int(input())

    doubleOfNum = 2 * primeNumInput
    print(findPrimeAddends(doubleOfNum))


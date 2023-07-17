def findZeroFactorial(n):
    i = 5
    count = 0
    while (n / i >= 1):
        count = int(n / i)
        i *= 5
 
    return int(count)
 
n = 20
print(f"Count of 0 in {n} ! is", findZeroFactorial(n))
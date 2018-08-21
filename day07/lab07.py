## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(x, y):
    if x==0:
        return y
    if y==0:
        return x
    elif x>y:
        return gcd(x-(x/y)*y,y)
    else:
        return gcd(y-(y/x)*x,x)

## Exercise 2
## Write a function using recursion that returns prime numbers less than 121
def find_primes(me = 121, primes = []):
    try:
        if numcon>1:
            numcon+=1
        else:
            numcon=2
    except UnboundLocalError:
        numcon=2
    upperbound=numcon^2
    lowerbound=(numcon-1)^2
    if upperbound>me:
        upperbound=me+1
    for i in range(lowerbound+1,upperbound):
        tester=1
        for j in primes:
            tester=(i/int(j))*tester
        if tester!=0:
            primes.extend(str(i))
    if upperbound!=me+1:
        find_primes(primes=primes)



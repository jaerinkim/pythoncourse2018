## Fibonacci sequence
## X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
## 1,1,2,3,5,8,....

## Write a for loop, while loop, or function (or all three!) to create a
## list of the first 10 numbers of the fibonacci sequence

def fib(length):
    X=[1,1]
    while len(X)<length:
        X.append(X[len(X)-1]+X[len(X)-2])
    print(X)

def altfib(length):
    X=[1,1]
    for i in range(1,length-1):
        X.append(X[i]+X[i-1])
    print(X)

fib(2)
fib(10)
altfib(6)
altfib(8)

#da1.1
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

# Input from the user
n = int(input("How many terms? "))

# Check for valid input
if n <= 0:
    print("Please enter a positive integer!")
else:
    print("Fibonacci series:")
    for i in range(n):
        print(recur_fibo(i))

#da1.2
n=int (input("How many trems?"))
a,b=0,1
count=0

if n<=0:
    print("please enter positive enteger!!")
elif n==1:
    print("fibonaci series upto",n,":")
    print(a)
else:
    print("fibonaci series: ")
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1


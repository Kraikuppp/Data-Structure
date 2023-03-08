def fibonacci_recursive (n):
    global sum2 , sum1
    sum1 = 0
    sum2 = 0
    if n <=1 :
        sum1+=n 
        return n
    else : 
        fibo_sum = (fibonacci_recursive(n-1)+fibonacci_recursive(n-2))
        sum2 = sum1 + fibo_sum
        return fibo_sum
nterm = int(input("how many term?" ))
if nterm <=0 :
    print ("Please enter positive number")
else : 
    print("Fibonacci term : ")
    for i in range(nterm):
        print(fibonacci_recursive(i))
print(fibonacci_recursive(sum2))
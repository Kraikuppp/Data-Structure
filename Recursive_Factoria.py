#Factoria Recursive Exercises
def Factoria_Recursive (n):
    #ิbase case 1! = 1
    if n == 1 :
        return 1
    #Recursive case n! = n*n-1
    else : 
        return n*Factoria_Recursive(n-1)
Factoria_Recursive(4)
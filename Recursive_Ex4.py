sum = 0
num = 1
def Sum_Recursive() : 
    global num
    global sum
    if num == 11 :
        
        return sum
    else :
        sum = sum+num
        num = num+1
        return Sum_Recursive()
    
Sum_Recursive() 
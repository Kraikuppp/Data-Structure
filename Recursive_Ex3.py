def Sum_Recursive(num,sum):
    #base case
    # time +
    if num == 11:
        return sum
    #recurseive
    else : 
        return Sum_Recursive(num+1,sum+num)

Sum_Recursive(1,0)
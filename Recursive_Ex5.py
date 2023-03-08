def list_sum_recursive (list_input):
    #base case
    if list_input == [] :
        return 0
    #recursive case 
    else :
        head = list_input[0]
        smaller_list = list_input[1:]
        return head + list_sum_recursive(smaller_list)
    
list_sum_recursive([1,5,8,10,46,48,49])
    
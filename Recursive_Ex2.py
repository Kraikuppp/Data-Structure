houses = ["Tanthep's House"]
def delivery_products_recursivly(houses):
    #Recursive case
    if len(houses) > 1 :
        mid = len(houses) //2
        first_half = houses[:mid]
        second_half = houses[mid:]
        delivery_products_recursivly(first_half)
        delivery_products_recursivly(second_half)
    #base case    
    else:
        house = houses[0]
        print("Delivery to",house)

delivery_products_recursivly(houses)    
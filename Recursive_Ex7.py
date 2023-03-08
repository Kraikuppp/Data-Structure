Line = [1,2,3,4,5,6,7]
def howmanyin(lst) : 
    if lst[1:] :
        print("me and the guys behind")
        return 1+howmanyin(lst[1:])
    else : 
        print("Just me")
        return 1
howmanyin(Line)
        
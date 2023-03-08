#automatic enqueue items
queue = []
print ('Enqueue item to Queue')
for i in range (9) : 
    queue.append(i)
    print('Data in Queue =  ',len(queue))
while len(queue) > 1 :
    queue.pop(0)
    print('Data in queue = ',len(queue))
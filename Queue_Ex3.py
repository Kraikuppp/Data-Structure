class Queue:
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if len(self.queue) < 1 :
            return None
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)

queue3 = Queue()
queue3.enqueue('jakkrit')
queue3.enqueue('student')
queue3.enqueue('data structure')
queue3.enqueue(555)

dequeue_value1 = queue3.dequeue()
print(dequeue_value1) 
dequeue_value2 = queue3.dequeue()
print(dequeue_value2)      
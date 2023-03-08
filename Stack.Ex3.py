#Create Class 
class Stack : 
    def __init__(self) : 
        self.input = []
    def isEmpty(self):
        return  self.input == []
    def push(self,input) : 
        self.input.append(input)
    def pop(self) : 
        return self.input.pop()
    def top(self) : 
        return self.input[len(self.input)-1]
    def size(self) : 
        return len(self.input)

DataStack = Stack()
DataStack.push('Hi')
DataStack.push('Hello')
DataStack.push('Jakkrit')
DataStack.push(6)
DataStack.push(5)
print('Size of stack : ',DataStack.size())
print('Pop last item : ',DataStack.pop())
print('Top of stack : ',DataStack.top())
#Program Coverting decimal to binary by use Stack
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
numbinary = ' '
numdecimal = 0
numdecimal = int(input("Enter your number : " ))
print("Decimal is ",numdecimal)

convert_stack = Stack()
while numdecimal > 0 : 
    convert_stack.push(numdecimal % 2)
    numdecimal = numdecimal // 2
while convert_stack.isEmpty() == False :
    numbinary = numbinary + str(convert_stack.pop())
    
print("Binary number is : ", numbinary)
    
#automatict push item and pop item from Stack
Stack = []
print ('\nCurrent stack : ',Stack)
print('Push item to Stack')
for i in range(9):
    Stack.append(i)
    print ('\nCurrent stack : ',Stack, '\tStack Size : ',len(Stack))

while len(Stack) > 0 :
    
    print ('\nCurrent stack : ',Stack,'\tStack Size : ',len(Stack))
    Stack.pop()
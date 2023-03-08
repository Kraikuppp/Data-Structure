#Stack Excercise use cout funcion
language = ['Thai', 'English', 'English','Laos','France','Italy','Germany','Italy','English']
print(language)
thai_count = language.count('Thai')
print(thai_count)
english_count = language.count('English')
print(english_count)
laos_index = language.index('Laos') # index use for find position of data
print(laos_index)
english_index = language.index('English',3) # 3 is position start to find 
print(english_index)
language.reverse() # reverse data
print(language)
language.sort() #sort data alphabet from A - Z
print(language)
language.append('Spain') #add Spain to Stack
print(language)
language.pop() #delete data
language.pop()
print(language)
language.extend('Switzerland') # extend data to single alphabet
print(language)
language.insert(2,'Hungary') # insert data from 2 positions
print(language)
language.remove('Hungary') # remove data 
print(language)
New_Stack = language.copy() # copy all data from language to New_Stack
language.clear() #delete all data from language
print(language)
print(New_Stack)
s = raw_input('Enter a string:')

loc = 0
count = 0
sL = range(len(s))

for index in sL:    
    loc = s.find('bob')
    if loc > -1:   
        count += 1
    if loc > 0:  
        s = s[loc+1:len(s)]        
    else:  
        s = s[1:len(s)]  
    
    
print('Number of times bob occurs is: ' + str(count))
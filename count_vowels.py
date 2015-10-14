#counts up the number of vowels contained in the string s

s = raw_input('Enter a string:')

vowels = 'aeiou'
count = 0
for char in s:
    if char in vowels:
        count += 1
        
print('Number of vowels: ' + str(count))

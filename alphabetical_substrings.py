s = raw_input('Enter a string:')

index = 0
lStr = []
tStr = ''

for i in range(len(s)):
    if len(tStr) == 0:
        tStr = s[i]
    if i+1 < len(s) and ( s[i] < s[i+1] or s[i] == s[i+1] ):        
            tStr = tStr + s[i+1:i+2]
    else:        
        lStr.append(tStr)
        tStr = ''


for i in range(len(lStr)-1):
    if len(lStr[index]) < len(lStr[i+1]):
        index = i+1

print('Longest substring in alphabetical order is: ' + lStr[index])
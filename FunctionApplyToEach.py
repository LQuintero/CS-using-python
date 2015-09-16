
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def timesFive(a):
    return a * 5

#ex1
print('Example 1 - Absolute value')
testList = [1, -4, 8, -9]
def absValue(x):
    return abs(x)
    
applyToEach(testList,absValue)

print(testList)

#ex2
print('Example 2 - Add one')
testList = [1, -4, 8, -9]
def addOne(x):
    return x + 1
    
applyToEach(testList,addOne)

print(testList)

#ex3
print('Example 3 - square of absolute value')
testList = [1, -4, 8, -9]
def absSquared(x):
    return abs(x)**2
    
applyToEach(testList,absSquared)

print(testList)


#aTup=('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    oddTup=()
    for index in range(len(aTup)):
        if (index + 1)%2 > 0:
            oddTup += (aTup[index],)
    
    return oddTup
 
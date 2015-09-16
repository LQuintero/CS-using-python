def f(x):
	import math
	return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    #init val 
    istop = int(stop)
    fstep = float(step)
    thisStep = float(start)  
    time = float(start)  
    tExposure = 0.0

    if step > 0:
        while True:    
            if thisStep < istop:    
                radiation = f(time)
                rExposure = radiation * fstep
                tExposure = tExposure + rExposure  
                thisStep = thisStep + fstep
                time = time + fstep
            else:
                break
    return tExposure

s1 = raw_input('Enter test case start value: ')
s2 = raw_input('Enter test case stop value: ')
s3 = raw_input('Enter test case step value: ')
y = radiationExposure(s1,s2,s3)
print(str(y))
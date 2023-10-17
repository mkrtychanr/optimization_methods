from math import *
import handlers
import operations

def generateValues(f, a):
    values = []
    xs = []

    i = a

    while i < b:
        values.append(eval(operations.changeX(f, i)))
        xs.append(i)
        i += delta

    return values, xs

def beatifyEcho(optimizationName, mins, minsSteps, maxs, maxsSteps):
    print(optimizationName)

    print("mins:")
    for i in range(0, len(mins)):
        print("value:\t" + str(mins[i]) + "\tsteps:\t", str(minsSteps))

    print("maxs:")
    for i in range(0, len(maxs)):
        print("value:\t" + str(maxs[i]) + "\tsteps:\t", str(maxsSteps))

    print()

a = -10
b = 10
e = 0.01
delta = 0.5

f = 'x*(x-1)**2*(x-3)**3'

values, xs = generateValues(f, a)

minsIndexes, scanMinsSteps, maxsIndexes, scanMaxsSteps = handlers.indexesHandler(values)

scanMins, scanMaxs = handlers.scanHandler(minsIndexes, maxsIndexes, xs)

goldenRingMins, goldenRingMinsSteps, golderRingMaxs, goldenRingMaxsSteps = handlers.goldenRingHandler(f, minsIndexes, maxsIndexes, xs, e)

newtonMins, newtonMinsSteps, newtonMaxs, newtonMaxsSteps = handlers.newtonHandler(f, minsIndexes, maxsIndexes, xs, e)

scanMinsSteps = [scanMinsSteps]
scanMaxsSteps = [scanMaxsSteps]

beatifyEcho("scan", scanMins, scanMinsSteps, scanMaxs, scanMaxsSteps)
beatifyEcho("goldenRind", goldenRingMins, goldenRingMinsSteps, golderRingMaxs, goldenRingMaxsSteps)
beatifyEcho("newton", newtonMins, newtonMinsSteps, newtonMaxs, newtonMaxsSteps)

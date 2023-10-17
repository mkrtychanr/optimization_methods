from math import *
from operations import *

def goldenRing(f, a, b, e, status): 
    x1 = a + (b - a) * ((3-sqrt(5))/2)
    x2 = b - (x1 - a)

    steps = 1

    while b - a > e:
        first = eval(changeX(getFunc(f, status), x1))
        second = eval(changeX(getFunc(f, status), x2))

        if second < first:
            a, x1 = x1, x2
            x2 = b - (x1 - a)
        else:
            b, x2 = x2, x1
            x1 = a + (b - x2)
    
        steps += 1

    return (a + b) / 2, steps

def newtonMax(f, a, b, e):
    d1f = getDiff(f)
    d2f = getDiff(d1f)

    x0 = (float(a) + float(b)) / float(2)
    
    steps = 1

    while True:
        x1 = x0

        d1 = eval(changeX(d1f, x1))
        d2 = eval(changeX(d2f, x1))

        if abs(d2) < 1e-6:
            x0 = x1 + e
        else:
            x0 = x1 + (d1/d2)

        if abs(x0 - x1) <= e:
            break
    
        steps += 1

    return x0, steps

def newtonMin(f, a, b, e):
    d1f = getDiff(f)
    d2f = getDiff(d1f)

    x0 = (float(a) + float(b)) / float(2)

    steps = 1

    while True:
        x1 = x0

        d1 = eval(changeX(d1f, x1))
        d2 = eval(changeX(d2f, x1))

        if abs(d2) < 1e-6:
            x0 = x1 - e
        else:
            x0 = x1 - (d1/d2)

        if abs(x0 - x1) <= e:
            break

        steps += 1

    return x0, steps

def minIndexes(values):
    mins = []

    for i in range (1, len(values) - 1):
        if (values[i - 1] > values[i] and values[i] < values[i + 1]):
            mins.append(i)

    return mins, len(values)

def maxIndexes(values):
    maxs = []

    for i in range (1, len(values) - 1):
        if (values[i - 1] < values[i] and values[i] > values[i + 1]):
            maxs.append(i)

    return maxs, len(values)

def scan(indexes, xs):
    result = []
    for index in indexes:
        result.append(xs[index])
    
    return result

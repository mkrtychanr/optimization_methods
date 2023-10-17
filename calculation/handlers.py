import functions

def indexesHandler(values):
    minsIndexes, steps = functions.minIndexes(values)
    maxsIndexes, steps = functions.maxIndexes(values)

    return minsIndexes, steps, maxsIndexes, steps


def scanHandler(minsIndexes, maxsIndexes, xs):
    mins = []
    maxs = []

    mins = functions.scan(minsIndexes, xs)
    maxs = functions.scan(maxsIndexes, xs)

    return mins, maxs


def goldenRingHandler(f, minsIndexes, maxsIndexes, xs, e):
    mins = []
    minsSteps = []
    maxs = []
    maxsSteps = []

    for index in minsIndexes:
        m, s = functions.goldenRing(f, xs[index-1], xs[index+1], e, 0)
        mins.append(m)
        minsSteps.append(s)

    for index in maxsIndexes:
        m, s = functions.goldenRing(f, xs[index-1], xs[index+1], e, -1)
        maxs.append(m)
        maxsSteps.append(s)

    return mins, minsSteps, maxs, maxsSteps

def newtonHandler(f, minsIndexes, maxsIndexes, xs, e):
    mins = []
    minsSteps = []

    maxs = []
    maxsSteps = []

    for index in minsIndexes:
        m, s = functions.newtonMin(f, xs[index-1], xs[index+1], e)
        mins.append(m)
        minsSteps.append(s)

    for index in maxsIndexes:
        m, s = functions.newtonMax(f, xs[index-1], xs[index+1], e)
        maxs.append(m)
        maxsSteps.append(s)
    
    return mins, minsSteps,  maxs, maxsSteps
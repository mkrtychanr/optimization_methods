import sympy as sp

def getFunc(f, status) -> str:
    if status == -1:
        return '-( ' + f + ')'
    return f

def changeX(f, val) -> str :
    return f.replace('x', str(val))

def echo(indexes, xs):
    for index in indexes:
        print(xs[index], end='\t')
    print()

def getDiff(f):
    x = sp.symbols('x')
    return str(sp.diff(f, x).simplify())

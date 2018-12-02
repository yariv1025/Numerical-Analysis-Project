from sympy import *
import cmath
import numpy as np

def func(symbolic_fuction):
    return lambdify(x, symbolic_fuction, 'numpy')

def derivative(symbolic_fuction):
    g_tagx = diff(symbolic_fuction)
    return lambdify(x, g_tagx, 'numpy')

def find_roots(rangex):
    intervals = []
    j = rangex[0]
    while j <= rangex[1]:
        intervals.append([j, j + 0.05])
        j = j + 0.05

    return intervals


def NR(f, f_tag, x,eps, itration,printList):
    i=0
    while abs(f(x)) > eps or itration == 0:
        if f_tag(x) == 0:
            return None
        x = x - f(x) / f_tag(x)
        printList.append((x, i))
        i += 1
        itration -= 1
    return x

def checkVariable(root, roots, eps):
    for i in roots:
        if abs(i - root) < eps:
            return  False
    return True

def checkRoot(f,root, eps):
    return abs(f(root)) < eps

def Print_roots(printList):
    for i in printList:
        print("number iteration:", i[1])
        print("Approximation:", i[0])


def all_roots(f, f_tag, eps, rangex, itration):
    roots = []
    intervals = find_roots(rangex)
    for i in intervals:
        printList=[]
        x = (i[0] + i[1]) / 2
        root = NR(f, f_tag, x, eps, itration, printList)
        if root != None:
            if (len(roots)==0)and  root <= rangex[1] and root >= rangex[0] and checkRoot(f, root, eps):
                roots.append(root)
                Print_roots(printList)
            else:
                if root == None:
                    continue
                if (not checkVariable(root, roots, 0.1)):
                    continue
                if f(root) == None:
                    continue
                elif root <= rangex[1] and root >= rangex[0] and checkRoot(f, root, eps):
                    roots.append(root)
                    Print_roots(printList)

    if len(roots) == 0:
        return None
    roots.sort()
    return roots



if __name__ == '__main__':
    x = Symbol('x')
    gx = exp(2*(x**2)-3*x)-4
    fx = func(gx)
    print(fx(0))
    fx_tag = derivative(gx)
    print(all_roots(fx, fx_tag, 0.00001, [-1,3], 100))
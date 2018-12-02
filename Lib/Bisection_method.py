from sympy import *
import scipy as sp
import numpy as np

# import matplotlib.pylab as plt

def f(symbolic_fuction):
    '''

    :param symbolic_fuction: mathematical expression
    :return: mathematical function
    '''
    return lambdify(x, symbolic_fuction)

def bisection(a, b, iteration, function, epsilon):
    '''
    :param a: start index
    :type a: float
    :param b: end index
    :type b: float
    :param iteration: amount of iterations
    :type iteration: int
    :param function: Polynomial function
    :type function: lambda x: polynom result
    :param epsilon: exceptable exception
    :type epsilon: float
    :return: root of function or "none"
    '''
    try:
        i=0
        if(isinstance(function(a),complex) == True or isinstance(function(b),complex) == True):
            return "none"
        else:
            if function(a) * function(b) <= 0 :
                c = (a + b) / 2
                while(abs(b - a) > epsilon or iteration == 0 ) :
                    if(function(a) == 0):
                        return a
                    if(function(b) == 0):
                        return b
                    if(function(c) == 0):
                        return c
                    elif(function(a) * function(c) > 0):
                        a = c
                    elif(function(c) * function(b) > 0):
                        b = c
                    iteration = iteration - 1
                    c = (a + b) / 2
                    print("number iteration:", i)
                    print("Approximation:", c)
                    i += 1
                return c
            else:
                return "none"
    except ValueError:
            return "none"
    except ZeroDivisionError:
            return "none"
    except DomainError:
        return "none"

def derivative(symbolic_fuction):
    '''
    :param func: mathematical expression
    :return: derivative of symbolic function as a function
    '''
    f_tag = diff(symbolic_fuction)
    return lambdify(x, f_tag, 'numpy')

def roots(ranging, function, iteration, epsilon):
    '''
    :param ranging: coordinates of seagmants a,b
    :param function: Polynomial function
    :param iteration: number of iteration
    :param epsilon:exceptable exception
    :return: List of roots
    '''
    count = 0
    j = 0
    rootList = []
    for k in ranging:
        if( j == len(ranging) - 1):#if j gets to the end of the list - 1
            return rootList
        tmp = bisection(ranging[j], ranging[j + 1], iteration, function, epsilon)
        if (not(tmp == "none")):
            if(len(rootList) > 0):
                if(tmp + 2 * epsilon >= rootList[count - 1]  or tmp - 2 * epsilon<= rootList[count - 1] ):
                    count = count + 1
                    rootList.append(tmp)
            else:
                count = count + 1
                rootList.append(tmp)
        j = j + 1

    return rootList

def all_roots(ranging, fx, fx_tag, iteration, epsilon):
    fx_list = []
    fx_tag_list = []
    root_list = []
    merged_list = []
    fx_list = roots(ranging, fx, iteration, epsilon)
    fx_tag_list = roots(ranging, fx_tag, iteration, epsilon)
    almostE = 0.00001

    for i in fx_tag_list:
        if(fx(i) <= almostE and fx(i) >= -almostE):
            root_list.append(i)

    for i in root_list:
        for j in fx_list:
            if (j <=  i + almostE and j >= i - almostE):
                continue
            else:
                 merged_list.append(j)

    for i in merged_list:
        fx_list += i
    return fx_list

def intervals(Start_Domain, End_Domain, interval_jump):
    domains = []
    parameter = Start_Domain

    tmp = (End_Domain - Start_Domain) / interval_jump
    for i in range(int(tmp)):
        domains.append(parameter)
        parameter += interval_jump

    domains.append(End_Domain)
    return domains

if __name__ == '__main__':
    x = Symbol('x')
    epsilon = 0.00000001
    iteration = 100
    Start_Domain = -10
    End_Domain = 10
    interval_jump = 0.5
    # fx=ln(x**2-2*x)+cos(x**3-1)+exp(2*(x**2)-3*x+4) syntx example
    # fx = (sin(x)+(ln(x)*cos(x))) example of syntx writing
    fx = ln(x**2-2*x)+cos(x**3-1)+exp(2*(x**2)-3*x+4)
    tmp1 = f(fx)
    fx_tag = derivative(fx)
    fx = tmp1


    count = 0
    rootList = []
    ranging = intervals(Start_Domain, End_Domain, interval_jump )


    #List of roots

    rootList = all_roots(ranging, fx, fx_tag, iteration, epsilon)
    rootList = set(rootList)
    rootList = list(rootList)
    rootList.sort()
    print(rootList)

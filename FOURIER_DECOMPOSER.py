import matplotlib.pyplot as plt
from math import sin, pi, cos

# Domain of the function that is being decomposed
l1 = 0
l2 = 4

# This is function that will be decomposed
def f(x):
    return 1

def integrate(f, x, y, n=1000):
    '''
    Integrate the function f from x to y with n steps
    '''
    l = y-x
    s = l/n
    k = x
    r = 0
    while k < y:
        r+= f(k)*s
        k += s
    return r

def a_0(f, l1, l2):
    '''
    Finds the value of the constant term of the fourier series
    expansion of the function f on [l1,l2]
    '''
    L = abs(l2-l1)
    return (1/(2*L))*integrate(f, l1, l2)

def a_n(f, l1, l2, n):
    '''
    Computes the value of the nth coeff of cos in Fourier series of f
    '''
    L = abs(l2-l1)
    I = lambda x: f(x)*cos((n*pi*x)/L)
    return (1/L)*integrate(I, l1, l2)

def b_n(f, l1, l2, n):
    '''
    Computes the value of the nth coeff of cos in Fourier series of f
    '''
    L = abs(l2-l1)
    I = lambda x: f(x)*sin((n*pi*x)/L)
    return (1/L)*integrate(I, l1, l2)

def fourier(f, l1, l2, n, x):
    '''
    f: Function that is being decomposed
    l1: Lower Limit
    l2: Upper limit
    n: Number of terms till which the Fourier series will be evaluated
    x: Point of evaluation
    '''
    L = abs(l2-l1)
    con = a_0(f, l1, l2)
    co = 0
    c = 1
    while c<=n:
        co += a_n(f, l1, l2, c)*cos((c*pi*x)/L)
        c+=1
    si = 0
    c = 1
    while c<=n:
        co += b_n(f, l1, l2, c)*sin((c*pi*x)/L)
        c+=1
    return con + co + si

def linspace(l1, l2, n):
    '''
    Emulates the np.linspace function
    '''
    x = []
    c = l1
    i = 0
    while i<n:
        x.append(c)
        c+= (l2-l1)/n
        i+=1
    return x

x = linspace(0,4,1000)
z = []

for i in x:
    z.append(fourier(f,0,4,30,i))
# Plots the function
plt.plot(x,z)
plt.show()
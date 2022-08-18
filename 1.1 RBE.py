import matplotlib.pyplot as plt
import matplotlib
import numpy as np


p = 2/3
q = 1-p
n = 30
N = 5000

# Question 1

def f(U):
    s = 0
    for i in range(0,n):
        s = s + U[i] / 2**(i+1)

    return s

def simF(x):
    t = 0
    for j in range(0,N):
        listU = [np.random.choice([0,1], p=[q,p]) for i in range(0,n)]

        if f(listU) <= x:
            t = t + 1

    return t / N


stepsize = 1/108
plotrange = np.arange(0,1+stepsize/2,stepsize)
result = [simF(x) for x in plotrange]

np.savetxt('Q11.csv', np.transpose((plotrange, result)), delimiter = ',')

"""
plt.figure(figsize=(5,5))
plt.plot(plotrange,result)
plt.xlabel("x", fontsize=16)
plt.ylabel("F(x)", fontsize=16)
plt.savefig("Q1.eps")
plt.show()
"""


# Question 3


def binary(x):
    xi = []
    for i in range(1,1000):
        if x == 0:
            break
        if x >= 1/ 2**i:
            xi.append(1)
            x = x - 1/ 2**i

        else:
            xi.append(0)

    return xi

def ind(a):
    if a == 0:
        return q
    if a == 1:
        return p

def F(x):
    if x >= 1:
        return 1
    else:
        xi = binary(x)
        s = 0
        if len(xi) == 0:
            return 0

        for i in range(0,len(xi)):
            t = 1
            if xi[i] == 1:
                if i != 0:
                    for j in range(0,i):
                        t = t * ind(xi[j])
                    s = s + t * q
                else:
                    s = s + q

        return s 

stepsize = 1/2**11
plotrange = np.arange(0,1+stepsize/2,stepsize)
result = [F(x) for x in plotrange]
np.savetxt('Q1line.csv', np.transpose((plotrange, result)), delimiter = ',')

p = 3/4
q = 1-p
stepsize = 1/2**11
plotrange = np.arange(0,1+stepsize/2,stepsize)
result = [F(x) for x in plotrange]

np.savetxt('Q3.csv', np.transpose((plotrange, result)), delimiter = ',')

plt.figure(figsize=(5,5))
plt.plot(plotrange,result)
plt.xlabel("x", fontsize=16)
plt.ylabel("F(x)", fontsize=16)
#   plt.savefig("Q2.eps")
plt.show()


# Question 4
p = 3/4
q = 1 - p
c = 9/16
d = 1/2**12

leftrange = range(-32,0)
rightrange = range(1,33)

def grad(c,t):
    if t == 0:
        return 0

    else:
        return (F(c+t) - F(c) )/ t

leftresult = [grad(c,i*d) for i in leftrange]
rightresult = [grad(c,i*d) for i in rightrange]
leftplotrange = [c+i*d for i in leftrange]
rightplotrange = [c+i*d for i in rightrange]
leftsave = np.transpose((leftplotrange, leftresult))
rightsave = np.transpose((rightplotrange, rightresult))

np.savetxt('Q4l.csv', leftsave, delimiter = ',')
np.savetxt('Q4r.csv', rightsave, delimiter = ',')

plt.figure(figsize=(5,5))
plt.plot(leftplotrange,leftresult)
plt.plot(rightplotrange,rightresult)
plt.xlabel("x", fontsize=16)
plt.ylabel("Grad(x)", fontsize=16)
#   plt.savefig("Q4.eps")
plt.show()


p = 1/4
q = 1-p
stepsize = 1/2**11
plotrange = np.arange(0,1+stepsize/2,stepsize)
result = [F(x) for x in plotrange]

np.savetxt('Q6-1.csv', np.transpose((plotrange, result)), delimiter = ',')

p = 1/4
q = 1 - p
c = 9/16
d = 1/2**12

leftresult = [grad(c,i*d) for i in leftrange]
rightresult = [grad(c,i*d) for i in rightrange]
leftplotrange = [c+i*d for i in leftrange]
rightplotrange = [c+i*d for i in rightrange]
leftsave = np.transpose((leftplotrange, leftresult))
rightsave = np.transpose((rightplotrange, rightresult))

np.savetxt('Q6-1l.csv', leftsave, delimiter = ',')
np.savetxt('Q6-1r.csv', rightsave, delimiter = ',')


p = 1/2
q = 1-p
stepsize = 1/2**11
plotrange = np.arange(0,1+stepsize/2,stepsize)
result = [F(x) for x in plotrange]

np.savetxt('Q6-2.csv', np.transpose((plotrange, result)), delimiter = ',')

p = 1/2
q = 1 - p
c = 9/16
d = 1/2**12

leftresult = [grad(c,i*d) for i in leftrange]
rightresult = [grad(c,i*d) for i in rightrange]
leftplotrange = [c+i*d for i in leftrange]
rightplotrange = [c+i*d for i in rightrange]
leftsave = np.transpose((leftplotrange, leftresult))
rightsave = np.transpose((rightplotrange, rightresult))

np.savetxt('Q6-2l.csv', leftsave, delimiter = ',')
np.savetxt('Q6-2r.csv', rightsave, delimiter = ',')

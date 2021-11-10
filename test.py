import timeit
import math

def count(x):
    print("count : " ,x)
def GCD1(m, n):
    c = 0
    if(m ==0 or n==0):
       return print('error integer division or modulo by zero')
    if m < n: #1
        t = m #1
        c += 2
    else:
        t = n
        c +=2
    if m==0 and n==0:
        c+=4
        return print('GCD1(m,n) = 0')
    while t >= 0: #1
        c += 1
        if (m % t) == 0: #2
            c += 2
            if (n % t) == 0: #2
                c += 3
                count(c)
                return print('GCD1(m,n) = ', t)
        t = t - 1 #2
        c+=2

#------------------------------------------------------------------------------------------------------------------

def GCD2(m, n):
    # step1
    mList = [] #1
    i = 2 #1 ตัวประกอบเริ่มที่สอง
    c=0
    c+=2
    while i <= m: #1
        c+=1
        if m % i == 0: #2
            mList.append(i) #1
            m = m / i #2
            c+=5
        else:
            i = i + 1 #2
            c+=4
    # step2
    nList = []
    j = 2
    c+=2
    while j <= n:
        c+=1
        if n % j == 0:
            nList.append(j)
            n = n / j
            c+=5
        else:
            j = j + 1
            c+=4
    # step3
    mnList = [] #1
    for p in range(0, len(mList)): #3
        c+=3
        for q in nList:
            c+=1
            if mList[p] == q: #2
                mnList.append(q)
                nList.remove(q)
                c+=5
                break
    # step4
    k = 1 #1
    c+=1
    for a in range(0, len(mnList)): #3
        k = k * mnList[a] #3
        c+=6
    c+=1
    count(c)
    return print('GCD2(m,n) = ', k)

#------------------------------------------------------------------------------------------------------------------

def GCD3(m, n):
    c = 0
    if m > n:
        c+=2
        return GCD3(m - n, n)
    if m == n:
        c+=3
        count(c)
        return print('GCD3(m,n) = ', m)
    if m < n:
        c+=4
        return GCD3(m, n - m)

def FindGCD3(m, n):
    c = 0
    while m != n: #1
        c += 1
        if m > n: #1
            m = m - n #2
            c += 3
        elif m < n: #1
            n = n - m #2
            c += 4
    count(c)
    c += 1
    return m

def GCD_extra(n,m,o):
    a = GCD1(m, n)
    b = GCD(m,o)

x = int(input('m: '))
y = int(input('n: '))
m = abs(x)
n = abs(y)

# start = timeit.default_timer()
# print("math.gcd :",math.gcd(m,n))
# end = timeit.default_timer()
# print(f"{end-start:0.10f} sec","\n")

start1 = timeit.default_timer()
GCD1(m, n)
end1 = timeit.default_timer()
print(f"{end1-start1:0.10f} sec","\n")


start2 = timeit.default_timer()
GCD2(m, n)
end2 = timeit.default_timer()
print(f"{end2-start2:0.10f} sec","\n")

# start3 = timeit.default_timer()
# GCD3(m, n)
# end3 = timeit.default_timer()
# print(f"{end3-start3:0.10f} sec","\n")

start4 = timeit.default_timer()
print("FindGCD3 :",FindGCD3(m, n))
end4 = timeit.default_timer()
print(f"{end4-start4:0.10f} sec","\n")

import math
import timeit
import matplotlib.pyplot as plt


def count(x): # นับsteps
    print("count :", x)

#-----------------------------------------------------------------------------------------------------


def min(x, y):
    c = 0
    if x > y:
        c += 2
        count(c)
        return y
    elif x < y:
        c += 3
        count(c)
        return x
    else:
        c += 3
        count(c)
        return x


def FindGCD1(m, n):
    t = min(m, n)
    c = 0
    c += 1
    if m==0 and n==0: #3
        c+=4
        count(c)
        return 0
    while t >= 0: #1
        divide_m = m % t #2
        c += 3
        if divide_m == 0: #1
            divide_n = n % t #2
            c += 3
            if divide_n == 0: #1
                c += 3
                count(c)
                return t
            else:
                c += 2
                t = t-1
        else:
            c += 2
            t = t-1
    count(c)
#-----------------------------------------------------------------------------------------------------


def prime_fact(x):
    i = 2 # ตัวประกอบเริ่มที่ 2
    a = []
    c = 0
    c += 2
    while i * i <= x: # check ว่ายังมีตัวประกอบอยู่? 2
        c += 2
        if x % i == 0: # หารลงตัว = เป็นตัวประกอบ 2
            x //= i  # //คือเอาแต่ผลหารไม่เอาเศษ //= คือ x หารแบบไม่เอาเศษกับอะไรแล้วได้ i 1
            a.append(i) #1
            c += 4
        else:
            i += 1
            c += 3
    a.append(x)
    c += 1
    count(c)
    return a


def intersection(list1, list2):
    c = 0
    intersect = [] #1
    j = 0 #1
    k = 0 #1
    c += 3
    for j in range(len(list1)): # 3
        c += 3
        for k in range(len(list2)): # 3
            c += 3
            if len(list2) == 0: #2
                c += 3
                break
            elif list1[j] == list2[k]: #3
                intersect.append(list1[j]) # 2
                list2.pop(k) #1
                c += 7
                break
            else:
                c += 6
                k += 1
        j += 1
        c+=1
    return intersect

def FindGCD2(m, n):
    c = 0
    if m == 0 and n != 0: #3
        c += 4
        return n
    elif n == 0 and m != 0: #3
        c += 7
        return m
    elif m == 0 and n == 0: #3
        c += 10
        return 0
    else:
        p1 = prime_fact(m) #1
        p2 = prime_fact(n) #1
        intersect = intersection(p1,p2) #1
        gcd = 1 #1
        c += 13
        for x in intersect: #1
            gcd = gcd*x #2
            c += 3
        count(c)
        c+=1
        return gcd

#-----------------------------------------------------------------------------------------------------


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

#-----------------------------------------------------------------------------------------------------

def GCD_extra1(m,n,o):
    a = FindGCD1(m,n)
    b = FindGCD1(a,o)
    return  b

def GCD_extra2(m,n,o):
    a = FindGCD2(m, n)
    b = FindGCD2(a, o)
    return b

def GCD_extra3(m,n,o):
    a = FindGCD3(m, n)
    b = FindGCD3(a, o)
    return b

def GCD_extra_41(m,n,o,p):
    a = FindGCD1(m,n)
    b = FindGCD1(p,o)
    c = FindGCD1(a,b)
    return c

def GCD_extra_42(m,n,o,p):
    a = FindGCD2(m,n)
    b = FindGCD2(p,o)
    c = FindGCD2(a,b)
    return c

def GCD_extra_43(m,n,o,p):
    a = FindGCD3(m,n)
    b = FindGCD3(p,o)
    c = FindGCD3(a,b)
    return c



times = []
input = input("Enter : ")
lst = input.split(",")
if lst.count("0") != 0:
    print("error")
elif len(lst) == 2:
    m = lst[0]
    n = lst[1]
    m = int(m)
    n = int(n)
    print(m,n)
    x = int(m)
    y = int(n)
    a = abs(int(x))
    b = abs(int(y))

    start2 = timeit.default_timer()
    print("FindGCD1 :", FindGCD1(a, b))
    end2 = timeit.default_timer()
    times.append(end2 - start2)
    print(f"{end2 - start2:0.10f} sec", "\n")

    start3 = timeit.default_timer()
    print("FindGCD2 :", FindGCD2(a, b))
    end3 = timeit.default_timer()
    times.append(end3 - start3)
    print(f"{end3 - start3:0.10f} sec", "\n")

    start4 = timeit.default_timer()
    print("FindGCD3 :", FindGCD3(a, b))
    end4 = timeit.default_timer()
    times.append(end4 - start4)
    print(f"{end4 - start4:0.10f} sec")

elif len(lst) == 3:
    m = lst[0]
    n = lst[1]
    o = lst[2]
    m = int(m)
    n = int(n)
    o = int(o)
    x = int(m)
    y = int(n)
    z = int(o)
    a = abs(int(x))
    b = abs(int(y))
    c = abs(int(z))
    start2 = timeit.default_timer()
    print("FindGCD1 :", GCD_extra1(a, b ,c))
    end2 = timeit.default_timer()
    times.append(end2 - start2)
    print(f"{end2 - start2:0.10f} sec", "\n")

    start3 = timeit.default_timer()
    print("FindGCD2 :", GCD_extra2(a, b, c))
    end3 = timeit.default_timer()
    times.append(end3 - start3)
    print(f"{end3 - start3:0.10f} sec", "\n")

    start4 = timeit.default_timer()
    print("FindGCD3 :", GCD_extra3(a, b,c))
    end4 = timeit.default_timer()
    times.append(end4 - start4)
    print(f"{end4 - start4:0.10f} sec")

elif len(lst) == 4:
    m = lst[0]
    n = lst[1]
    o = lst[2]
    p = lst[3]
    m = int(m)
    n = int(n)
    o = int(o)
    p = int(p)
    x = int(m)
    y = int(n)
    z = int(o)
    w = int(p)
    a = abs(int(x))
    b = abs(int(y))
    c = abs(int(z))
    d = abs(int(w))

    start2 = timeit.default_timer()
    print("FindGCD1 :", GCD_extra_41(a, b, c,d))
    end2 = timeit.default_timer()
    times.append(end2 - start2)
    print(f"{end2 - start2:0.10f} sec", "\n")

    start3 = timeit.default_timer()
    print("FindGCD2 :", GCD_extra_42(a, b, c,d))
    end3 = timeit.default_timer()
    times.append(end3 - start3)
    print(f"{end3 - start3:0.10f} sec", "\n")

    start4 = timeit.default_timer()
    print("FindGCD3 :", GCD_extra_43(a, b, c,d))
    end4 = timeit.default_timer()
    times.append(end4 - start4)
    print(f"{end4 - start4:0.10f} sec")


# times = []
# GCD = ["math.gcd","FindGCD1","FindGCD2","FindGCD3"]

# start1 = timeit.default_timer()
# print("math.gcd :", math.gcd(a, b))
# end1 = timeit.default_timer()
# times.append(end1-start1)
# print(f"{end1-start1:0.10f} sec","\n")

# start2 = timeit.default_timer()
# print("FindGCD1 :", FindGCD1(a, b))
# end2 = timeit.default_timer()
# times.append(end2-start2)
# print(f"{end2-start2:0.10f} sec","\n")
#
# start3 = timeit.default_timer()
# print("FindGCD2 :", FindGCD2(a, b))
# end3 = timeit.default_timer()
# times.append(end3-start3)
# print(f"{end3-start3:0.10f} sec","\n")
#
# start4 = timeit.default_timer()
# print("FindGCD3 :", FindGCD3(a, b))
# end4 = timeit.default_timer()
# times.append(end4-start4)
# print(f"{end4-start4:0.10f} sec")

# fig = plt.figure()
# plt.bar(GCD,times)
# plt.show()

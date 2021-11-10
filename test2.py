m,n = input('m,n : ').split(',')
m=int(m)
n=int(n)
t = int
c = 0
if m<n:
    t = m
else : t = n
c = c+1
while t > 0:
    c = c+1
    if m % t == 0:
        c = c+1
        if n % t == 0:
            c = c+1
            print('gcd : ', t)
            print('number of times the operation : ', c)
            break
        else: t = t-1
        c = c+1
    else: t = t-1
    c = c+1
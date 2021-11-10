def prefixKMP(p): # find pi
    m=len(p)
    pi = [0]*m
    # pi=[0*m for i in range(m)]
    k=0
    for q in range(1,m):
        while(k>0 and p[k]!=p[q]):
            k=pi[k-1]
        if p[k] == p[q]:
            k=k+1
        pi[q]=k
    return pi
    # o(m) ==> range pattern

def KMP(t,p):
    n=len(t)
    m=len(p)
    s=[]
    pi=prefixKMP(p)
    q=0
    for i in range(n):
        while (q>0 and p[q]!=t[i]):
            q=pi[q-1]
        if p[q]==t[i]:
            q=q+1
        if q==m:
            s.append(i-m+2)
            q=pi[q-1]
    return s
    # o(n) ==> range text

def Naive(t,p):
    n=len(t)
    m=len(p)
    s=[]
    i=0
    for i in range(n-m):
        if p==t[i:i+m]:
            s.append(i+1)
    return s
    # o(mn) if n >> m
    # o((n-m+1)(m)) วน n-m+1 รอบ if อีกไม่เกิน m


with open("9.0.txt", "r") as file:
    inputLst = file.read().splitlines()

pattern=inputLst[2].split()
text=inputLst[3].split()

if(len(text) >= len(pattern)):
    print('\nKMP algoritim')
    k1=KMP(text,pattern)
    textRV=text[::-1] 
    k2=KMP(textRV,pattern)
    print(prefixKMP(pattern))
    print(len(k1)+len(k2))
    for i in k1:
        print(i,"LR")
    for i in k2[::-1]:
        print(len(text)-i+1,"RL")

    print('\nnaive string matching algoritim')
    n1=Naive(text, pattern)
    n2=Naive(textRV, pattern)
    print(len(n1)+len(n2))
    for i in n1:
        print(i,"LR")
    for i in n2[::-1]:
        print(len(text)-i+1,"RL")
else:
    print("text range < pattern range")
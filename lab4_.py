def CoinChange(change,n,lst,chg=[]):
    if change!=0:
        chg = chg + [change]
    if n <= 0.0:
        if n == 0 :
            if n in lst:
                chg = chg + [n]
            return [chg]
        else:
            return 0
    else:
        lstAll=[]
        for i in range(len(lst)):
            change=lst[i]
            if change>n:
                continue
            else:
                m=n-change
                mm=('%.2f' % m)
                result=CoinChange(change,float(mm),lst[i:],chg)
                if result!=0 and result!=[]:    
                    for i in result:
                        lstAll.append(i)
        return lstAll

def MinCoinChange(cc):
    cnt=[]
    if(cc == []):
        print("Can't exchange coins")
        return 0,[]
    else:
        for i in cc:
            cnt.append(len(i))
        minCoin=[]
        for i in range(len(cnt)):
            if cnt[i]==min(cnt):
                minCoin.append(cc[i])
        return min(cnt),minCoin

n = float(input('Amount = '))
d = [float(d) for d in input("coins [] = ").split(' ')]
cc=CoinChange(0,n,d)
# for i in cc:
#     print(i)
print('Ways to make change = ',len(cc))

mc = MinCoinChange(cc)
print(mc[1])
print('Minimum of coin is = ',mc[0])












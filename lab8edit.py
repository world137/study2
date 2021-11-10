import time
def BruteForceSingleSellProfit(arr):
    bestProfit = 0
    for i in range(0, len(arr)):
        for j in range (i+1, len(arr)): 
            if(bestProfit <= arr[j] - arr[i]):
                bestProfit = arr[j] - arr[i]
                lst=[i+1,arr[i],j+1,arr[j],bestProfit,j-i]
    return lst


def DivideAndConquerSingleSellProfit(arr,lst=[]):
    if len(arr) <= 1:
        return [0,arr]
    left  = arr[ :int(len(arr)/2)]
    right = arr[int(len(arr)/2): ] 
    # print(left,right)
    leftBest  = DivideAndConquerSingleSellProfit(left,lst)
    rightBest = DivideAndConquerSingleSellProfit(right,lst)

    cross = max(right) - min(left)
    crossBest = [cross,[min(left) , max(right)]]
    # print(leftBest,rightBest,crossBest)
    return(max(leftBest, rightBest, crossBest))
    

def index(lst,value):
    result=[]
    if value[0]==0:
        tt=lst[0]
        for i in range(len(lst)-1):
            if(lst[i]==lst[i+1]):
                result+=[i+1,lst[i],i+2,lst[i]]
                break
        result+=[value[0],1]
    else:
        for i in range(len(lst)):
            if lst[i]==value[1][0]:
                result+=[i+1,value[1][0]]
                break
        for j in range(i+1,len(lst)):
            if lst[j]==value[1][1]:
                result+=[j+1,value[1][1]]
                break
        result+=[value[0],j-i]
    return result


def result(result):
    print("min index :         ",result[0])
    print('min value :          %.2f' %result[1])
    print("max index :         " ,result[2])
    print('max value :          %.2f' %result[3])
    print('difference value :   %.2f' %result[4])
    print('difference index :  ',result[5])

n=int(input('n: '))
#inputlst=input('list: ')
lst=[float(i) for i in input('list: ').split()]



start1 = time.time()
dc=DivideAndConquerSingleSellProfit(lst)
dcLst=index(lst,dc)
print('\nDivide and Conquer')
result(dcLst)
end1 = time.time()
print('time count:         ',end1 - start1)

start2 = time.time()
BF=BruteForceSingleSellProfit(lst)
print('\nBrute Force')
result(BF)
end2 = time.time()
print('time count:         ',end2 - start2)


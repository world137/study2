import sys
INF = sys.maxsize
import time

def findMinMaxDC(value,left,right,min,max):
    if left == right:
        if min > value[right]:
            min = value[right]
        if max < value[left]:
            max = value[left]    
        return min,max
    if right - left == 1:
        if value[left] < value[right]:
            if min > value[left]:
                min = value[left]
            if max < value[right]:
                max = value[right]
        else:
            if min > value[right]:
                min = value[right]
            if max < value[left]:
                max = value[left]
        return min,max
    mid = (left + right) // 2
    min,max = findMinMaxDC(value,left,mid,min,max) #left
    min,max = findMinMaxDC(value,mid+1,right,min,max) #right

    return min,max

def findMinMaxBF(value,min,max):
    for j in range(len(value)):
        if value[j] < min:
            min = value[j]
        if value[j] > max:
            max = value[j]        
    return min,max    


def index(value,n):
    for i in range(len(value)):
        if value[i]==n:
            return i+1
            
def result(value,min,max):
    print("min index :         ",index(value,min))
    print('min value :          %.2f ' %min)
    print("max index :         " ,index(value,max))
    print('max value :          %.2f' %max)
    print('difference value :   %.2f' %(max-min))
    print('difference index :  ',abs(index(value,max)-index(value,min)))


N = int(input("input N :"))
InValue = input("value :")
SplitValue = InValue.split()

# for i in value:
#     value[i] = float(value[i])

value=[float(i) for i in InValue.split()]

(min, max) = (INF, -INF)

start1 = time.time()
(minDC,maxDC)=findMinMaxDC(value,0,N-1,min,max)
print('\nDivide and Conquer')
result(value,minDC,maxDC)
end1 = time.time()
print('time count:',end1 - start1)

start2 = time.time()
(minBF,maxBF)=findMinMaxBF(value,min,max)
print('\nBruteForce')
result(value,minBF,maxBF)
end2 = time.time()
print('time count :        ',end2 - start2)



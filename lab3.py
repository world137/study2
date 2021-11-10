import timeit

def GrabPassenger(arr,k):
    cnt=0
    lst = []
    for g in range(len(arr)-1):
        i=0
        if(arr[g] != 'G' and arr[g] != 'P'):
            print("character are not G and P")
        if (arr[g] == 'G' and " P" in arr):
            while(i!=k):
                i+=1
                if g+i >= len(arr):
                    i = i -1
                    continue
                elif (arr[g+i]=='P'):
                    cnt+=1
                    arr[g+i]='Ppick'
                    arr[g] = 'Gride'
                    lst.append([g,g+i])
                    break
        elif (arr[g] == 'P' and "G" in arr):
            while(i!=k):
                i+=1
                if g+i >= len(arr):
                    i = i -1
                    continue
                elif (arr[g+i]=='G'):
                    cnt+=1
                    arr[g+i]='Gride'
                    arr[g] = 'Ppick'
                    lst.append([g, g + i])
                    break
    print('Output : ', cnt)
    print(arr)
    print(lst)


# def Greedy(arr,k):
#     ans = []
#     cnt = 0
#     i = 0
#     while (i < len(arr)):
#         while(k > 0):
#             print("af,oimgop")
#             if(arr[i] == "G"):
#                 if(i+k <= len(arr) and arr[i+k] == "P"):
#                     arr[i] = 'Gride'
#                     arr[i+k] = 'Ppick'
#                     cnt += 1
#                 elif(i >= k and arr[i-k] == "P"):
#                     arr[i] = 'Gride'
#                     arr[i-k] = 'Ppick'
#                     cnt += 1
#                 else:
#                     k = k -1
#         i += 1
#     print(arr)
#     print("count :" , cnt)


# def Greedy(arr,k):
#     for i in range(len(arr)):
#         if(arr[i] == "P"):
#             for j in range(len(arr)):
#                 if(arr[j] == "R"):

times = []
gp =input('Input : ').upper()
arr = list(gp)
k = int(input('k = '))
start = timeit.default_timer()
GrabPassenger(arr,k)
end = timeit.default_timer()
times.append(end - start)
print(f"{end - start:0.10f} sec")
# Greedy(arr,k)

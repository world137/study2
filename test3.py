import timeit
import itertools
# def Greedy1(arr,k):
#     cnt=0
#     lst = []
#     for g in range(len(arr)-1):
#         i=0
#         if (arr[g] == 'G' and "P" in arr):
#             while(i!=k):
#                 i+=1
#                 if g+i >= len(arr):
#                     i = i -1
#                     continue
#                 elif (arr[g+i]=='P'):
#                     cnt+=1
#                     arr[g+i]='Ppick'
#                     arr[g] = 'Gride'
#                     lst.append([g,g+i])
#                     break
#         elif (arr[g] == 'P' and "G" in arr):
#             while(i!=k):
#                 i+=1
#                 if g+i >= len(arr):
#                     i = i -1
#                     continue
#                 elif (arr[g+i]=='G'):
#                     cnt+=1
#                     arr[g+i]='Gride'
#                     arr[g] = 'Ppick'
#                     lst.append([g, g + i])
#                     break
#     print('BF1 count : ', cnt)
#     print('BF1 : ', arr, "\n")


# def Greedy2(arr, k):
#     lst = []
#     cnt = 0
#     for g in range(len(arr) - 1):
#         i = g + k
#         if (arr[g] == 'G'):
#             while (i >= g):
#                 if i >= len(arr):
#                     i = i - 1
#                     continue
#                 elif (arr[i] == 'P'):
#                     cnt += 1
#                     arr[i] = 'Ppick'
#                     arr[g] = 'Gride'
#                     lst.append([g, i])
#                     break
#                 i = i - 1
#         elif (arr[g] == 'P'):
#             while (i >= g):
#                 if i >= len(arr):
#                     i = i - 1
#                     continue
#                 elif (arr[i] == 'G'):
#                     cnt += 1
#                     arr[i] = 'Gride'
#                     arr[g] = 'Ppick'
#                     lst.append([g, i])
#                     break
#                 i = i - 1
#     print('BF2 count : ', cnt)
#     print('BF2 : ', arr, "\n")


def Greedy3(arr,k):
    lst = []
    cnt=0
    for i in range(len(arr)-1):
        if (arr[i] == 'G' and 'P' in arr):
            for p in range(i+1,len(arr)):
                if arr[p]=='P':
                    if p-i<=k:
                        cnt+=1
                        arr[p]='Ppick'
                        arr[i] = 'Gride'
                        lst.append([p,i])
                        break
        elif (arr[i] == 'P' and 'G' in arr):
            for g in range(i+1,len(arr)):
                if arr[g]=='G':
                    if g-i<=k:
                        cnt+=1
                        arr[i]='Ppick'
                        arr[g] = 'Gride'
                        lst.append([g, i])
                        break
    return cnt,arr,lst


def LtoR(arr,k):
    lst = []
    cnt = 0
    for i in range(len(arr)):
        j = 1
        if(arr[i] == "G"):
            while(j <= k):
                if(i+j <= len(arr)-1 and arr[i+j] == "P"):
                    cnt += 1
                    arr[i] = 'Gride'
                    arr[i+j] = 'Ppick'
                    lst.append([i, i+j])
                    break
                j += 1
    return cnt,arr,lst


def RtoL(arr,k):
    lst = []
    i = len(arr)-1
    cnt = 0
    while(i > 0):
        j = 1
        if(arr[i] == "G"):
            while(j <= k):
                if(i-j >= 0 and arr[i-j] == "P"):
                    cnt += 1
                    arr[i] = 'Gride'
                    arr[i-j] = 'Ppick'
                    lst.append([i, i - j])
                    break
                j += 1
        i = i - 1
    return cnt,arr,lst

def cycleLR(arr,k):
    lst = []
    LR = LtoR(arr,k)
    a = LR[1]
    i = 1
    j = 0
    cnt = LR[0]
    while(i <= k):
        if(a[-1] == "G"):
            if(a[j] == "P"):
                cnt += 1
                arr[-1] = 'Gride'
                arr[j] = 'Ppick'
                lst.append([-1,j])
        i += 1
        j += 1
    return cnt,arr,lst


def cycleRL(arr,k):
    lst = []
    LR = RtoL(arr,k)
    a = LR[1]
    i = 1
    j = len(a)-1
    cnt = LR[0]
    while(i <= k):
        if(a[0] == "G"):
            if(a[j] == "P"):
                cnt += 1
                arr[0] = 'Gride'
                arr[j] = 'Ppick'
                lst.append([0,j])
        i += 1
        j = j - 1
    return cnt,arr,lst

def cycle(arr,k):
    lst = []
    BF = Greedy3(arr,k)
    a_BF = BF[1]
    cnt_BF = BF[0]
    l_BF = BF[2]

    LR = cycleLR(a_BF,k)
    a_LR = LR[1]
    cnt_LR = LR[0]
    l_LR = LR[2]

    RL = cycleRL(a_LR,k)
    a_RL = RL[1]
    cnt_RL = RL[0]
    l_RL = RL[2]

    lst = l_RL+l_LR+l_BF
    cnt = cnt_BF+cnt_LR+cnt_RL
    print("cycle count :", cnt)
    print("cycle arr :" ,a_RL)
    print("pair of index :",lst)

def CheckDup(lst):
    lst2 = []
    for i in lst:
        if i in lst2:
            return True
        else:
            lst2.append(i)
    return False


def BruteForce(arr, k):
    lstPS = []
    g_list = []
    p_list = []
    for i in range(len(arr)):
        if (arr[i] == 'G'):
            g_list.append(i)
    for i in range(len(arr)):
        if (arr[i] == 'P'):
            p_list.append(i)

    for i in range(len(arr) - 1):
        if (arr[i] == 'G' and 'P' in arr):
            for p in range(i + 1, len(arr)):
                if arr[p] == 'P':
                    if p - i <= k:
                        lstPS.append([i, p])
        elif (arr[i] == 'P' and 'G' in arr):
            for g in range(i + 1, len(arr)):
                if arr[g] == 'G':
                    if g - i <= k:
                        lstPS.append([g, i])
    lstPS.sort()
    lstUse = []
    indexDup = []
    if (len(g_list) < len(p_list)):
        for i in g_list:
            lst = []
            for j in lstPS:
                if j[0] == i:
                    lst.append(j)
            if (lst != []): lstUse.append(lst)
    else:
        for i in p_list:
            lst = []
            for j in lstPS:
                if j[1] == i:
                    lst.append(j)
            if (lst != []): lstUse.append(lst)
    # print('JJ',lstUse)
    print('Output BruteForce3 : ',len(lstUse))
    lst = list(itertools.product(*lstUse))
    # print(lst)
    if (len(g_list) < len(p_list)):
        for i in range(len(lst)):
            # print('gg',lst[i],i)
            lstDup = []
            for j in range(len(lst[i])):
                lstDup.append(lst[i][j][1])
            # print('ty',lstDup)
            if CheckDup(lstDup):
                indexDup.append(i)
        print(indexDup)
        lstBF = []
        for i in range(len(lst)):
            if i not in indexDup:
                lstBF.append(lst[i])
    else:
        for i in range(len(lst)):
            # print('gg',lst[i])
            lstDup = []
            for j in range(len(lst[i])):
                lstDup.append(lst[i][j][0])
            # print('ty',lstDup)
            if CheckDup(lstDup):
                indexDup.append(i)
        # print(indexDup)
        lstBF = []
        for i in range(len(lst)):

            if i not in indexDup:

                lstBF.append(lst[i])
    # print(lstBF)
    for i in lstBF:
        print(i)
    print('Output BruteForce count : ', len(lstBF))


times = []
gp =input('Input : ').upper()
arr1 = list(gp)
arr2 = list(gp)
arr3 = list(gp)
arr4 = list(gp)
arr5 = list(gp)
arr6 = list(gp)
arr7 = list(gp)
arr8 = list(gp)
k = int(input('k = '))
if(k <= 0):
    print("k must be more than 0")
else:
    # print(gp)
    # start = timeit.default_timer()
    # Greedy1(arr1,k)
    # end = timeit.default_timer()
    # times.append(end - start)
    # print(f"{end - start:0.10f} sec \n")

    # print(gp)
    # start2 = timeit.default_timer()
    # Greedy2(arr2,k)
    # end2 = timeit.default_timer()
    # times.append(end2 - start2)
    # print(f"{end2 - start2:0.10f} sec \n")

    # print(gp)
    start3 = timeit.default_timer()
    c = Greedy3(arr3, k)
    print("GD3 count :", c[0])
    # print("GD3 arr :" ,c[1])
    # print("pair of index :", c[2])
    end3 = timeit.default_timer()
    times.append(end3-start3)
    print(f"{end3 - start3:0.10f} sec \n")

    # print(gp)
    # start4 = timeit.default_timer()
    # a = LtoR(arr4,k)
    # print('L to R count :',a[0])
    # print('R to L arr :' ,a[1])
    # print("pair of index :", a[2])
    # end4 = timeit.default_timer()
    # times.append(end4-start4)
    # print(f"{end4 - start4:0.10f} sec \n")
    #
    # print(gp)
    # start5 = timeit.default_timer()
    # b = RtoL(arr5,k)
    # print('L to R count :',b[0])
    # print('R to L arr :' ,b[1])
    # print("pair of index :", b[2])
    # end5 = timeit.default_timer()
    # times.append(end5-start5)
    # print(f"{end5 - start5:0.10f} sec \n")
    #
    # print(gp)
    # start6 = timeit.default_timer()
    # e = cycleLR(arr6,k)
    # print("cycle L to R count :" ,e[0])
    # print("cycle L to R arr :", e[1])
    # print("pair of index :", e[2])
    # end6 = timeit.default_timer()
    # times.append(end6-start6)
    # print(f"{end6 - start6:0.10f} sec \n")
    #
    # print(gp)
    # start7 = timeit.default_timer()
    # d = cycleRL(arr7,k)
    # print("cycle R to L count :" ,d[0])
    # print("cycle R to L arr :", d[1])
    # print("pair of index :", d[2])
    # end7 = timeit.default_timer()
    # times.append(end7-start7)
    # print(f"{end7 - start7:0.10f} sec \n")
    #
    # print(gp)
    # start8 = timeit.default_timer()
    # cycle(arr8,k)
    # end8 = timeit.default_timer()
    # times.append(end8-start8)
    # print(f"{end8 - start8:0.10f} sec \n")

    start9 = timeit.default_timer()
    BruteForce(arr4,k)
    end9 = timeit.default_timer()
    times.append(end9 - start9)
    print(f"{end9 - start9:0.10f} sec \n")
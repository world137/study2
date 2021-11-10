def BF(arr,k):
    a = []
    ans = []
    s = set()

    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i] == "G" and arr[j] == "P"):
                a.append([i,j])
                s.add(i)
    print(a)
    print("G :",s)
    keep = []
    for l in range(len(a)):
        if(abs(a[l][1] - a[l][0]) <= k):
            keep.append([a[l][0],a[l][1]])
    print(keep)
    for m in range(len(keep)):
        for n in range(len(keep)):
            keep[m][1] + 1 in keep


times = []
gp = input('Input : ').upper()
arr1 = list(gp)
k = int(input('k = '))

BF(arr1,k)
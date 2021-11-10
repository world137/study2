def change(coin, amount):
    coin.sort()
    amount = float(amount)
    arr = []
    i = len(coin)- 1
    if amount == 0:
        return 0
    if int(min(coin)) > amount:
        return -1
    while(i >= 0 and amount > 0):
        if(amount//coin[i] != 0):
            value = amount//coin[i]
            v = '%.2f' % value
            amount = amount - float(v)
            arr.append((str(coin[i])+" ") * int(value))
        if(amount > 0 and i-1 < 0):
            print("Can't exchange coins")
            return -1
        i = i-1
    print(arr)


def count(amount):
    s = set()
    amount = float(amount)
    if amount == 0:
        return [[]]
    if amount < 0:
        return []
    else:
        ans = []
        for i in coin:
            recursive_result = count(amount - i)
            for j in recursive_result:
                j.append(i)
            ans.extend(recursive_result)
    for k in range(len(ans)):
        s.add(ans[k].sort())

    return ans


amount = input("Amount :")
coin = input("coin :").split(",")
print(10.6//10.0)
for i in range(len(coin)):
    coin[i] = float(coin[i])

change(coin,amount)
# value = count(amount)

s = set()
# for k in value:
#     print(k)
# for j in range(len(value)):
#     print(value)
#     # s.add(value[j])
# print(len(s))




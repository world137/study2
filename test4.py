def change(amount,coin):
    coin.sort()
    arr = []
    i = len(coin) - 1
    while(i >= 0 and amount > 0):
        if(amount//coin[i] != 0):
            value = amount // coin[i]
            amount = amount - value * coin[i]
            arr.append((str(coin[i]) + " ") * int(value))
        if (amount > 0 and i - 1 < 0):
            print("Can't exchange coins")
            return -1
        i = i - 1
        return (arr)

def dinamic(c,coin):
    print(c)
    c.sort()
    coin.sort()
    keep = []
    j = len(coin)-1
    for i in range(len(c)):
        while(j > 0):
            if(c[i]//coin[j] != 0 and c[i] != coin[j]):
                value = c[i] // coin[j]
                print(value)
                c[i] = c[i] - value * coin[j]
                print(c)
                keep.append((str(coin[j])+" ")*value)
            j = j - 1

    print(keep)

amount = int(input("Amount : "))
coin = input("coin [] : ").split(" ")
for i in range(len(coin)):
    coin[i] = int(coin[i])

c = change(amount,coin)
print(c)
arr = []
for j in range(len(c)):
    arr = c[j].split(" ")
arr.pop(-1)
for k in range(len(arr)):
    arr[k] = int(arr[k])

dinamic(arr,coin)
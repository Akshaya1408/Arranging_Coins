def arrangingCoins(n):

    r=0
    for i in range(1,n+1):
        if n>=i:
            n-=i
            r+=1
    return r

n=int(input())
print(arrangingCoins(n))
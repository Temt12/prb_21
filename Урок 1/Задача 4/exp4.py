n,t=map(int,input().split())
a=list(map(int,input().split()))
i=0
while True:
    if (i+a[i])<=n:
        i+=a[i]
        if i==t-1:
            print('Yes')
            break
    else:
        print('No')
        break
    #Или нужно было сделать именно по шаблону 4 и 5 задачи?

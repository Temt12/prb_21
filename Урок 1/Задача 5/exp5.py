n,t=map(int,input().split())
s=input()
s1=list(s)
for i in range(t):
    j=0
    for u in range(n):
        if u!=len(s)-1:
            if (s1[u]=='B') and ((s1[u+1])=='G'):
                j+=1
    g=[0]*j
    p=0
    for u in range(n):
        if u!=len(s)-1:
            if (s1[u]=='B') and ((s1[u+1])=='G'):
                g[p]=u
                p+=1
    for u in range(j):
        s1[g[u]]='G'
        s1[g[u]+1]='B'
a=''.join(s1)
print(a)
### Нужна ли была проверка в задачах 4 и 5
### Комментировать задачу нужно было или нужно просто правильно решить её?

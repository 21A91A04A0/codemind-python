n=int(input())
lst=list(map(int,input().split()))
sum=0
for i in range(n):
    if n>0:
        sum+=lst[i]
print(sum)
n=int(input())
lst=list(map(int,input().split()))
x=sum(lst)//n
if x in lst:
    print(True)
else:
    print(False)
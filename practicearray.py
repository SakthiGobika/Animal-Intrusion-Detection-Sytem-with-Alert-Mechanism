n=int(input())
arr=list(map(int,input().split()))
##arr=list(map(int,input().split()))
seen=[]
for i in range(len(arr)):
    if arr[i] not in seen:
        seen.append(arr[i])
if len(seen)==0:
    print("No duplicates")
else:
    print(seen)
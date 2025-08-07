"""s="sakthi tamilnadu  gobika"
l=s.split()
print(l)
max=""
for i in l:
    if len(i)%2!=0:
        if len(i)>len(max):
            max=i
if max =="":
    print("Better luck next time")
else:
    print(max)
arr=[1,9,2,11,1,9,2]
maxp=0
p=0
for i in range(len(arr)-1):
        p=int(arr[i+1]-arr[i])
        if p>maxp:
            maxp=p
print(maxp)
n=3
s=0
for i in range(n+1):
    s+=(i**2)
print(s)
arr=[1,3,4,5,6,7,8]
n=len(arr)+1
sum=n*(n+1)//2
asum=0
for i in range(len(arr)):
    asum+=arr[i]
print(sum-asum)
a=1
b=2
c=3
n=6
for i in range(4,n+1):
    d=a+b+c
    a=b
    b=c
    c=d
print(d)
arr=[1,2,3,23,12,45,67,25]
l=arr[0]
sl=-1
for i in range(1,len(arr)):
    if arr[i]>l:
        sl=l
        l=arr[i]
        
    elif arr[i]>sl:
        sl=arr[i]
print(sl)
arr=[16,17,4,3,5,2]
cmax=arr[-1]
l=[arr[-1]]
for i in range(len(arr)-2,-1,-1):
    if arr[i]>cmax:
        cmax=arr[i]
        l.append(arr[i])
l.reverse()
print(l)
arr=[-2,1,-3,4,-1,2,1,-5,4]
sum=0
maxsum=arr[0]
for i in range(len(arr)):
    sum+=arr[i]
    maxsum=max(sum,maxsum)
    if sum<0:
        sum=0
print(maxsum)
s="I hate coding"
a=s.split()
r=""
for i in range(len(a)-1,-1,-1):
    r+=a[i]+" "
r=r.strip()
print(r)
s="go to hell"
max=""
a=[]
for i in s:
    a.append(i)
for i in a:
    if len(i)%2!=0:
        if len(i)>len(max):
            max=i
    else:
        print("bad luck")
print(max)
t=int(input())
sell=[]
for i in range(t):
    a=int(input())
    sell.append(a)
maxp=0
minp=sell[0]
p=0
for i in range(1,len(sell)):
    p=sell[i]-minp
    if p>maxp:
        maxp=p
    if sell[i]<minp:
        minp=i
print(maxp)
nums = [2,3,1,2,4,3]
target=7
sum=0
l=0
r=len(nums)+1
##r=len(nums)
for i in range(len(nums)):
    sum+=nums[i]
    while sum>=target:
        r=min(r,i-l+1)
        l+=1
if c<=len(nums):
    print(c)
else:
    print(0)"""
d-{')':'(',']':'[','}':'{'}
stack=[]
for i in s:
    if i in d.values():
        stack.append(i)
    elif i in d:
        if not stack:
            return False
        top=stack.pop()
        if top!=d[i]:
            return False

    








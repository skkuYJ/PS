n=int(input())
a=list(map(int,input().split()))
x=int(input())

a.sort()
left=0
right=len(a)-1
count=0

while left<right:
    if a[left]+a[right]==x:
        count+=1
        left+=1
        right-=1
    elif a[left]+a[right]>x:
        right-=1
    else:
        left+=1

print(count)

# 더 나은 풀이
'''
n=int(input())
a = {*map(int, input().split())}
x=int(input())

count=sum((x-i in a) for i in a)//2

print(count)
'''

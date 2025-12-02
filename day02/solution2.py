import math
res=mx=0
ranges=[]
invalid=set()

for rng in open('input.txt', 'r').readline().split(','):
    start,end=rng.split('-')
    ranges.append((int(start),int(end)))
    mx=max(mx,int(start),int(end))
mxrep=int(math.pow(10,len(str(mx))//2))

for i in range(1,mxrep):
    num=str(i)
    for n in range(1,mx):
        num+=str(i)
        n=int(num)
        for r in ranges:
            if r[0] <= n <= r[1] and n not in invalid:
                invalid.add(n)
                res+=n
        if n>mx:
            break

print(res)
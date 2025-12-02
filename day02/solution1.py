res=0
for rng in open('input.txt', 'r').readline().split(','):
    start,end=rng.split('-')
    l=len(start)//2
    if l==0:
        left=0
    else:
        left=int(start[0:l])
    while (True):
        num=int(str(left)+str(left))
        if int(start) <= num <= int(end):
            res+=num
        elif num > int(end):
            break
        left+=1
print(res)
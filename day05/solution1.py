ranges=[]
fresh=0
ids=False
for l in open('input.txt', 'r').readlines():
    if l =='\n':
        ids=True
        continue
    elif ids:
        for r in ranges:
            if r[0]<=int(l)<=r[1]:
                fresh+=1
                break
    else:
        l = [int(i) for i in l.strip().split('-')]
        ranges.append(l)
print(fresh)
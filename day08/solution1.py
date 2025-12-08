import math, itertools

def dist(b1,b2):
    return math.sqrt((b2[0] - b1[0])**2 + (b2[1] - b1[1])**2 + (b2[2] - b1[2])**2)

boxes=[tuple(int(n) for n in l.split(','))  for l in open('input.txt', 'r').readlines()]
distances=[]
for b1,b2 in itertools.combinations(boxes,2):
    distances.append((b1,b2,dist(b1,b2)))
distances.sort(key=lambda x:x[2])

circuits=[{b} for b in boxes]
i=0
for d in distances:
    selected=[c for c in circuits if len(c & {d[0],d[1]})>0]
    if len(selected)==1: #extend circuit
        selected[0].add(d[0])
        selected[0].add(d[1])
    elif len(selected)==2: #merge circuits
        circuits.remove(selected[0])
        circuits.remove(selected[1])
        circuits.append(selected[0]|selected[1])
    i+=1
    if i>=1000:
        break
circuits.sort(key=lambda x:-len(x))       

print(len(circuits[0])*len(circuits[1])*len(circuits[2]))
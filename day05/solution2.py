ranges=[]
for l in open('input.txt', 'r').readlines():
    if l =='\n':
        break
    else:
        l = [int(i) for i in l.strip().split('-')]
        ranges.append(l)

ranges.sort(key=lambda x: x[0])
merged=[ranges[0]]
for rng in ranges[1:]:
    prev = merged[-1]
    if rng[0] <= prev[1]:
        prev[1] = max(prev[1], rng[1])
    else:
        merged.append(rng)

print(sum([r[1]-r[0]+1 for r in merged]))
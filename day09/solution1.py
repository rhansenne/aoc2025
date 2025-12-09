import itertools
tiles=[tuple(int(n) for n in l.split(','))  for l in open('input.txt', 'r').readlines()]
print(max([(abs(t1[0]-t2[0])+1)*(abs(t1[1]-t2[1])+1) for t1,t2 in itertools.combinations(tiles,2)]))
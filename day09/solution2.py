import itertools
from shapely.geometry import Polygon
tiles=[tuple(int(n) for n in l.split(','))  for l in open('input.txt', 'r').readlines()]
totarea=Polygon(tiles)
mxarea=0
for t1,t2 in itertools.combinations(tiles,2):
    p=Polygon([t1,(t1[0],t2[1]),t2,(t2[0],t1[1])])
    if p.within(totarea):
        mxarea=max(mxarea,(abs(t1[0]-t2[0])+1)*(abs(t1[1]-t2[1])+1))
print(mxarea)
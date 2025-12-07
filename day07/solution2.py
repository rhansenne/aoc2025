import functools
ws=[list(l.strip()) for l in open('input.txt', 'r').readlines()]

@functools.cache
def down(i,j):
    timelines=0
    while i<len(ws):
        if ws[i][j]=='^':
            timelines+=down(i,j-1)
            timelines+=down(i,j+1)
            return timelines
        i+=1
    return 1
        
print(down(0,ws[0].index('S')))
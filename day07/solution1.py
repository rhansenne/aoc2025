ws=[list(l.strip()) for l in open('input.txt', 'r').readlines()]
splitters=set()

def down(i,j):
    global splits
    while i<len(ws):
        if ws[i][j]=='^':
            if (i,j) in splitters:
                break
            down(i,j-1)
            down(i,j+1)
            splitters.add((i,j))
            break
        i+=1
        
down(0,ws[0].index('S'))
print(len(splitters))
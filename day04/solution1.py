accessible=0
grid = [list(l.strip()) for l in open('input.txt', 'r').readlines()]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=='@':
            rolls=0;
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    if 0<=i+di<len(grid) and 0<=j+dj<len(grid[0]) and grid[i+di][j+dj]=='@':
                        rolls+=1
            if rolls<=4:
                accessible+=1
print(accessible)
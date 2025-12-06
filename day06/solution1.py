import numpy as np
ws=[l.split() for l in open('input.txt', 'r').readlines()]
values=np.array([[int(n) for n in row] for row in ws[:-1]], dtype=object)
tot=0
for i,op in enumerate(ws[-1]):
    if op == '+':
        tot+=values[:,i].sum()
    else:
        tot+=values[:,i].prod()
print(tot)
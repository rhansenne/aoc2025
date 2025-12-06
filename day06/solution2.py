import math,numpy as np
ws=[list(l.rstrip()) for l in open('input.txt', 'r').readlines()]
maxlen=max([len(r) for r in ws])
ws=np.array([r+[' ']*(maxlen-len(r)) for r in ws]) #make shape homogeneous

def compute(vals,op):
    if op=='+':
        return sum(vals)
    else:
        return math.prod(vals)
            
op=''
tot=0
vals=set()
for i in range(len(ws[0])):
    if ws[-1][i] in ('+','*'):
        op=ws[-1][i]
    val=''.join(ws[:-1,i]).strip()
    if val=='':
        tot+=compute(vals,op)
        vals=set()
    else:
        vals.add(int(val))
tot+=compute(vals,op)
print(tot)
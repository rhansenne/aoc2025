dial,cnt=50,0
for rot in open('input.txt', 'r').readlines():
    if rot[0]=='R':
        nxt=dial+int(rot[1:])
        cnt+=nxt//100
    else:
        if dial==0:
            dial=100
        nxt=dial-int(rot[1:])
        if nxt<=0:
            cnt+=1+nxt//-100
    dial=nxt%100
print(cnt)
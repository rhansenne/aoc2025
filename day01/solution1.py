dial,cnt=50,0
for rot in open('input.txt', 'r').readlines():
    if rot[0]=='R':
        dial=(dial+int(rot[1:]))%100
    else:
        dial=(dial-int(rot[1:]))%100
    if dial==0:
        cnt+=1
print(cnt)
tot=0
for bank in open('input.txt', 'r').readlines():
    mx=0
    for i in range(len(bank)-1):
        for j in range(i+1,len(bank)):
            mx=max(mx,int(bank[i]+bank[j]))
    tot+=mx
print(tot)
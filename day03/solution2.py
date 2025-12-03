tot=0

def maxjolt(batts,length,joltage):
    mxjolt=0
    maxnext=max([int(b) for b in batts[:len(batts)-length+1]])
    for i in range(len(batts)-length+1):
        if int(batts[i])==maxnext:
            if length==1:
                mxjolt=max(mxjolt,int(joltage+batts[i]))
            else:
                mxjolt=max(mxjolt,maxjolt(batts[i+1:],length-1,joltage+batts[i]))
    return mxjolt

for bank in open('input.txt', 'r').readlines():
    tot+=maxjolt(bank.strip(),12,'')
print(tot)
import re, itertools as it
tot=0
for l in open('input.txt', 'r').readlines():
    lights=[True if x=='#' else False for x in re.search('\\[(.*)\\]',l).group(1)]
    buttons = [[int(n) for n in b.split(',')] for b in re.findall('\\((.*?)\\)',l)]
    presses=1
    correct=False
    while True:
        for seq in it.product(buttons,repeat=presses):
            lights_state=[False]*len(lights)
            for press in seq:
                for light in press:
                    lights_state[light]=not lights_state[light]
            if lights_state==lights:
                correct=True
                break
        if correct:
            break
        presses+=1
    tot+=presses
print(tot)
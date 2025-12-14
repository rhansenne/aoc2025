# There has to be an easier and more efficient solution.
# This approach models the relations between the buttons and light 
# indicators as a set of linear equation and uses Sympy to solve them.
# Since some cases feature more variables than equations, some brute
# force substitution of the free variables is required however. 
# This takes hours to complete but does eventually produce the correct result.
import re, math
from sympy import Eq, Symbol, linsolve, simplify
import itertools as it

tot=0
for l in open('input.txt', 'r').readlines():
    joltage=[int(n) for n in re.search('\\{(.*)\\}',l).group(1).split(',')]
    buttons = [[int(n) for n in b.split(',')] for b in re.findall('\\((.*?)\\)',l)]
      
    # create variables representing the number of button presses
    bx=[Symbol('B'+str(i), integer=True) for i in range(len(buttons))] 

    minpresses=math.inf
    # represent the button-indicator relations as a set of linear equations and solve using Sympy
    s = linsolve([Eq(sum([bx[ib] for ib,b in enumerate(buttons) if ij in b]),j) for ij,j in enumerate(joltage)],bx)
    for sol in s:
        # if there are more buttons (variables) than equations, the system is underdetermined
        # in this case, determine the free variables
        freevars=[v for i,v in enumerate(sol) if v==bx[i]]
        if len(freevars)>0:
            #brute force all possible values of the free variables to find a solution
            for vals in it.product([n for n in range(max(joltage)+1)], repeat=len(freevars)):
                sc=[]
                for i,v in enumerate(sol):
                    v2=v
                    for fi,fv in enumerate(freevars):
                        v2=v2.subs(fv,vals[fi])
                    sc.append(v2)
                if all(simplify(val).is_integer and val >= 0 for val in sc):
                    minpresses=min(minpresses,sum(sc))
        elif all(val.is_integer and val >= 0 for val in sol):
            minpresses=min(minpresses,sum(sol))
    tot+=minpresses    
print(tot)
import networkx as nx
G = nx.DiGraph()
for l in open('input.txt', 'r').readlines():
    src=l[:3]
    for t in l[5:].strip().split(' '):
        G.add_edge(src,t)
print(len(list(nx.all_simple_paths(G,'you','out'))))
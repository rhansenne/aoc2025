import networkx as nx
G = nx.DiGraph()
for l in open('input.txt', 'r').readlines():
    src=l[:3]
    for t in l[5:].strip().split(' '):
        G.add_edge(src,t)   

#minimal cutoffs found through trial and error
svr_fft=len(list(nx.all_simple_paths(G,'svr','fft', cutoff=10)))
fft_dac=len(list(nx.all_simple_paths(G,'fft','dac', cutoff=17)))
dac_out=len(list(nx.all_simple_paths(G,'dac','out')))
print(svr_fft*fft_dac*dac_out)
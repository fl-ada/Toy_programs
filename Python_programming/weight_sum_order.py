# n : number of weights
# k : number of result
# w : list of weights
# QUESTION : get the sums of possible combination of weights and the list of it in ascending order, print any one case
'''
sample input :
5
10
3 10 1 4 30

sample output:
0:
1: 1
3: 3
4: 1 3
5: 1 4
7: 3 4
8: 1 3 4
10: 10
11: 1 10
13: 3 10
14: 1 3 10
'''

import itertools
import numpy as np

n = int(input())
k = int(input())
w = []
w = [int(item) for item in input().split()]

comb = []
comb_sum = []

w.sort()

for L in range(n):
    for subset in itertools.combinations(w, L):
        comb.append(subset)

comb_sum=[sum(comb[i]) for i in range(len(comb))]
sort_index = np.argsort(comb_sum)

ind = 0
i = 0
while i<k:
    index = sort_index[ind]
    prev_index = sort_index[ind-1]
    if comb_sum[index]!=comb_sum[prev_index]:
        print('{sum}:'.format(sum=comb_sum[index]), *comb[index])
        i += 1
    ind += 1
    
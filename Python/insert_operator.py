# from 머신러닝을 위한 파이썬 - 최성철
'''input:
N(number of nums)
A1, A2, ...AN(nums)
+ - * / (number of operators)
output:
find the max and min results of possible operations
'''
    
import itertools # permutations
from functools import reduce

def insert_operation(length, input_no, input_op):
    
    ops = {"0": (lambda x,y: x+y), 
           "1": (lambda x,y: x-y), 
           "2": (lambda x,y: x*y),
           "3": (lambda x,y: int(x/y))}
    op_permutation = []
    result = []
    list(op_permutation.extend([str(index)]*value) 
         for index, value in enumerate(input_op) if value>0)
    
    # all possible orders of operators
    permutation = [list(x) for x in set(itertools.permutations(op_permutation))]
    for i in permutation:
        result.append(reduce(lambda x,y: ops[i.pop()](x,y), input_no))
        
    print(str(max(result)) + "\n" + str(min(result)))

    
numbers = []
operators = []
#taking inputs
n = int(input())
numbers = input().split()
numbers = list(map(int,numbers))
operators = input().split()
operators = list(map(int,operators))

    
#result
insert_operation(n,numbers, operators)
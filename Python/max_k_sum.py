# get n numbers, find max sum of k numbers among them
''' input:
n k
n1
n2
n3
...
'''

nk=input()
n=int(nk.split()[0])
k=int(nk.split()[1])
ex=[]
for x in range(n):
    ex.append(int(input()))

ex.sort()
sum=0
for i in range(n-k,n):
    sum+=ex[i]
print(sum)
##from itertools import product 
##p = product('ВУАЛЬ',repeat=5)
##s = map(lambda x: ''.join(x), p)
##print(list(s))
#from itertools import *

#370
##from itertools import product 
##s='0123456789ABCDEF'
##p = product(s,repeat=3)
##k=0
##for  x in p:
##    if x[0]!='0' and len(set(x)) == len(x) and \
##       int(x[0],16) % 2 != int(x[1],16) % 2 and \
##       int(x[1],16) % 2 != int(x[2],16) % 2:
##        k=k+1
##print(k)
#372
##from itertools import product
##s='АГИЛМОРТ'
##p = product(s,repeat=5)
##k=0
##for  i,j in enumerate(p):
##    if i % 2 ==0 and j[0]!='Т' and j.count('Г')==2:
##        k=i
##print(k)
#28238+1=28239
#374
from itertools import permutations
s='ТИМАШЕВСК'
p = list(permutations(s))


a='АИЕ'
b='ТМШВСК'
k=0
for i in p:
    x=''.join(i)
    for i in range(1,len(x)-3):
        if x[0] in b and x[-1] in b and x[i] in a and x[i+1] in a and x[i+2] in a:k+=1

print(k)


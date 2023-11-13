#Решу ОГЭ тип 5
#1
##s='12111'
##k=7
##for x in range(len(s)):
##    if s[x]=='1':
##        if 'b' not in str(k):
##            k = k+2
##        else:
##            k = str(k)+'+'+'2'
##    elif s[x]=='2':
##        k = str(k)+'*'+'b'
##print(k)
##for b in range(100):
##    if eval(k)==51:
##        print(b)
#18
##s='12221'
##k=1
##for x in range(len(s)):
##    if s[x]=='2':
##        if 'b' not in str(k):
##            k = k+2
##        else:
##            k = str(k)+'+'+'2'
##    elif s[x]=='1':
##        k ='('+ str(k)+')'+'*'+'b'
##print(k)
##for b in range(100):
##    if eval(k)==91:
##        print(b)
#19
s='21212'
k=1
for x in range(len(s)):
    if s[x]=='2':
        if 'b' not in str(k):
            k = k+1
        else:
            k = str(k)+'+'+'1'
    elif s[x]=='1':
        k ='('+ str(k)+')'+'*'+'b'
print(k)
for b in range(100):
    if eval(k)==56:
        print(b)
                        
    

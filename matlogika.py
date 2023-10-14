import random
a = ['и','или','не', '->']
f =['A','B','C']
rd_log_operations = random.choices(a,k=4)
rd_var = random.choices(f,k=4)
t = True
while t:
    if 'нене' in ''.join(rd_log_operations):
        rd_log_operations = random.choices(a,k=4)
    elif 'нене' not in ''.join(rd_log_operations):
        
        if ''.join(rd_log_operations)[-1] != 'не':
            t = False
    elif 'нене' not in ''.join(rd_log_operations):
        if ''.join(rd_log_operations)[-1] == 'не':
            rd_log_operations = random.choices(a,k=4)

        
##print(rd_log_operations)
##print(rd_var)
s = ''
d=[]
for x in range(len(rd_log_operations)):
    if x == 0 and rd_log_operations[0] != 'не':
        d.append(rd_var[0])
        d.append(rd_log_operations[0])
        #s = rd_var[0]+ ' ' + rd_log_operations[0]
        
    elif x == 0 and rd_log_operations[0] == 'не':
##        s = rd_log_operations[0] + ' ' + rd_var[0]
        
        d.append(rd_log_operations[0])
        d.append(rd_var[0])

    elif x > 0 and (rd_log_operations[x] == 'не') and (d[-1] in a ):
##        s = s + ' ' + rd_log_operations[x] + ' '+ rd_var[x]
        d.append(rd_log_operations[x])
        d.append(rd_var[x])
    elif x > 0 and rd_log_operations[x] == 'не' and (d[-1] in f ):
        #rd_log_operations[x] = 'и'
        #s = s + ' ' + rd_log_operations[x] + ' '+ rd_var[x]
        d.append('и')
        d.append(rd_var[x])

    elif x > 0 and rd_log_operations[x] != 'не' and (d[-1] in f ):
        #s = s + ' ' +rd_log_operations[x] + rd_var[x]
        d.append(rd_log_operations[x])
        d.append(rd_var[x])

    
    
    elif x > 0 and rd_log_operations[x] != 'не' and (d[-1] in a ):
        
        #s = s + ' ' + rd_var[x] +' '+rd_log_operations[x]
       
        d.append(rd_var[x])
        d.append(rd_log_operations[x])
   
#s = s + ' '+ rd_var[x]
if d[-1] in a:
    d.append(random.choice(f))
print(' '.join(d))

print('Введите строчки таблицы истинности')
q =123544465765768679
while q != 2:
    t = input()
    print()
    






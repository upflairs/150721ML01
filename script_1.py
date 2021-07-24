##a = [5,7,19,2,4,5,17,6,8,18,20,23,26,1,55]
##b = []
##i = 0
##while i<len(a):
##    b.append(a[i]+10)
##    i += 1
##print(b)

##b = []
##i = 0
##while i<len(a):
##    b += [a[i]+10]
##    i += 1
##print(a,b)

##b = []
##for i in range(len(a)):
##    b += [a[i]+10]
##print(a,b)

##b = []
##for i in a:
##    b += [i+10]
##print(a,b)

##b = [i+10 for i in a]
##print(a,b)

##b = [i+10 for i in a if i%2]
##print(a,b)
##c = [i for i in a if i>4]
##print(c)

##b = [i*2 if i%2 else i//2 for i in a]
##print(a,b)

##b = [(i*4 if i<10 else i*2) if i%2 else i//2 for i in a]
##print(a,b)

##b = [[1 for _ in range(i)] for i in a]
##print(a,b)

##for i,v in enumerate(a):
##    print(i, v, end='$\n', sep='@')

##b = [(i, [indx for _ in range(i)]) for indx,i in enumerate(a)]
##print(a,b)

##a = ['name','age']
##b = [['rekha','vinesh','rahul','kinjal'],[20,19,20,21]]

##d = {v:b[i] for i,v in enumerate(a)}
##print(d)

##c = list(zip(a,b))
##print(c)

##d = dict(zip(a,b))
##print(d)

#f = open('etnries.txt','r')

##with open('entries.txt','r') as f:
##    r1 = f.read()
##    f.close()
##
##print(r1)
##print('')
##
##with open('ekor.txt','r') as f:
##    r2 = f.read()
##    f.close()
##
##print(r2)
##print('')

with open('data.csv','r') as f:
    r3 = f.read()
    f.close()
print(r3)

r = r3.split('\n')
keys = r[0].split(',')
values = ([i.split(',') for i in r[1:] if i])
d = dict(zip(keys, zip(*values)))
print(d)














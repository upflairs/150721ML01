age = eval(input('Enter the age: '))
salary = eval(input('Enter the salary: '))

if age<18:
    print('No offers')
elif age>=18 and age<=25: # age<=25
    if salary<50000:
        print('Offer A1')
    else:
        print('Offer A2')
elif age>25 and age<=35:
    if salary<50000:
        print('Offer B1')
    elif salary<100000:
        print('Offer B2')
    else:
        print('Offer B3')
elif age<=50:
    print('Offer C')
else:
    print('Offer D')

##########################################
# Loops
##########
# 1. while
# 2. for

'''
while condition:
    content


for object in collection:
    content


'''

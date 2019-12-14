#length
'''a=[1,2,3,4,5]
count=0
for i in a:
    count+=1
print(count)'''
#sum
'''a=[1,2,3,4,5]
sum=0
for i in a:
    sum+=i
print(sum)'''
#count of repeated number
'''a=int(input('enter the number'))
b=[1,2,2,3,4,5,6,7,8,9,8,7]
c=0
for i in b:
    if i==a:
        c+=1
print(c)'''
#max value in a list
'''a=[1,2,3,4,5]
max=0
for i in a:
    if max<i:
        max=i
print(max)'''
#sum of elements excluding string
'''a=[1,2,3,4,5,'bita']
sum=0
for i in a:
    if type(i)== int:
        sum+=i
print(sum)'''
#diff between sum.of.sq & sq.of.sum
'''a=int(input('enter a number'))
b=0
sum=0
k=0
for i in range(a+1):
    j=i**2
    sum=sum+j
    k=k+i
    l=k**2
b=sum-l
print(abs(b))'''
# Alphabets from string
'''a='aZyAKM1#42$Mn'
b=''
for i in a:
    if i.isalpha():
        b=i
        print(b,end='')'''
# Spl.Characters from string
'''a='aZyAKM1#42$Mn'
b=''
for i in a:
    if not i.isalnum():
        b=i
        print(b,end='')'''

    
#Factorial of given number
'''a=int(input('enter a number'))
b=1
for i in range(1,a+1):
    b*=i
print(b)'''
#factorial of given number (reverse range)
'''a=
int(input('enter a number'))
b=1
for i in range(a,0,-1):
    b*=i
print(b)'''
#finding leap year
'''a=int(input('enter the year'))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print('it is a leap year')
        else:
            print('it is not a leap year')
else:
    print('it is not a leap year')'''
#Returning command and using "break" to exit a loop
'''started=0
stopped=0
while True:
    
    action= input('enter the command')
    if action=='start':
            if started==0:
                print('car  started')
                started=1
                
            else :
                print('car already started')
                
    elif action=='stop':
        if stopped==0:
            print('car stopped')
            stopped=1
        else:
            print('car already stopped')
    elif action=='exit':
        break
    else:
        print('i dont understand')'''
#Workout program
'''x=int(input('Enter the number'))
if x<10:
    print('Child')
elif 10<x<=25:
    if x<18:
        print('school')
    else:
        print('college')
elif 25<x<60:
    if x<40:
        print('employee')
    elif 40<x<=50:
        print('manager')
    else:
        print('vrs')
elif 50<x<60:
    print('Manager')
elif x>=60:
    print('Senior Citizen')'''
#leap year
'''a=int(input('enter the year'))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print('leap year')
        else:
            print('not a leap year')
    else:
        print('leap year')
else:
    print('not a leap year')'''
# leap year using flags
'''valid=False
a=int(input('enter the year'))
if a%4==0:
    valid=True
    if a%100==0:
        valid=False
        if a%400==0:
            valid=True      
if valid:
    print('leap year')
else:
    print('not a leap year')'''

# Printing * pattern using "While"
'''a=5
i=1
while i<=a:
    print('*'*i)
    i+=1'''
    
# Max. number in a list
'''a=[10,15,12,30,11,9]
b=0
for i in a:
    if b<i:
        b=i
print(b)'''
#no. of duplicates in a list
'''a=[4,2,2,4,1,2,1,3,3]
b=0
c=int(input('enter the no.'))
for i in a:
    if i==c:
        b+=1
print(b)'''


#def. function

'''def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    return(c)
    
    
    
d=15+sub(20,)
print(d)
e=15+add(10,20)'''

# Slicing of Strings (static)
'''a='abcd'
b=int(input('enter the number'))
if b==1:
    print (a[1::1]+ a[0])
if b==2:
    print(a[2::1]+a[0:2:1])
if b=3:
    print(a[3]+a[0:3:1])
else:
    print('incorrect number')'''
# Slicing of Strings (dynamic)
'''a='abcd'
b=int(input('enter the number'))
print(a[b:]+a[:b])'''
# Palindrome (using string)
'''a=input('Enter the string :')
b=a[::-1]
print(b)'''

# Palindrome checking (using slicing)
'''a=input('enter the string: ')
if a[::]== a[-1::-1]:
    print('It is a palindrome')
else :
    print('It is not a palindrome')'''

# String functions
'''a='Sriram Uday'
a.find('Sriram')
print(a.replace('Sriram','Abhi'))
print(a.swapcase())
print(a.title())
print(a.casefold())
print(a.center(50))
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())'''
# Workout Programme
a='ab123_#$96cd1'
'''for i in a:
    if i.isalpha():
        print(i,end='')
print()
for i in a:
    if i.isdigit():
        print(i,end='')
print()
for i in a:
    if not i.isalnum():
        print(i,end='')
print()'''
# Split & Join
'''a=input('enter the list')
a=a.split()
print(a)'''
#Converting data-type of element in list
# Using Range
'''b=0
a=input('enter the list')
a=a.split()
print(a)
for i in range(len(a)):
    a[i]=int(a[i])
print(a)'''
# Using normal 'for' loop
'''b=0
a=input('enter the list')
a=a.split()
print(a)
for i in a:
    a[b]=int(i)
    b+=1
print(a)'''
# Tuple
'''a=[10,20,30]
b=tuple(a)
print(b.count(10))
print(b.index(10))'''
# Set
'''a=set([1,2,3,4,5,6,7,7,6,5,4,3,2,1])
print(a)'''
# Set Methods
'''set1={1,2,3,4,5,6}
set2={2,3,5,6,7,9}
print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set2-set1)'''
# Dictionary
'''dicto={'a':'apple','b':'ball','c':['cat','camel'],1:'one'}
print(dicto['a'])
print(dicto['c'])
print(dicto['c'][1])
print(dicto[1])'''
#
'''a={'country':{'india':['chennai','madurai']}}
print(a['country']['india'][1])'''

# functions
'''def add(a,b):
    c=a+b
    return(c)
a=10
b=20
d=30+add(a,b)
print(d)'''

'''def fact(a):
    a=int(a)
    b=1
    for i in range(1,a+1):
        b*=i
    print(b)
fact(4)'''
def palindrome(a):
    a=a.lower()
    if a==a[::-1]:
        print('palindrome')
    else:
        print('not plaindrome')
palindrome('amma')












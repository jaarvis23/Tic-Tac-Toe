l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
s1='user 1'
s2='user 2'
def check():
    v1=0
    v2=0
    a=0
    b=1
    if(l1[0]==a and l1[1]==a and l1[2]==a):
         v1+=1
    if(l2[0]==a and l2[1]==a and l2[2]==a):
         v1+=1
    if(l3[0]==a and l3[1]==a and l3[1]==a):
         v1+=1
    if(l1[0]==a and l2[0]==a and l3[0]==a):
         v1+=1
    if(l1[1]==a and l2[1]==a and l3[1]==a):
         v1+=1
    if(l1[2]==a and l2[2]==a and l3[2]==a):
         v1+=1
    if(l1[2]==a and l2[1]==a and l3[0]==a):
         v1+=1
    if(l1[0]==a and l2[1]==a and l3[2]==a):
         v1+=1
    else:
        if(l1[0]==b and l1[1]==b and l1[2]==b):
             v2+=1
        if(l2[0]==b and l2[1]==b and l2[2]==b):
             v2+=1
        if(l3[0]==b and l3[1]==b and l3[2]==b):
             v2+=1
        if(l1[0]==b and l2[0]==b and l3[0]==b):
             v2+=1
        if(l1[1]==b and l2[1]==b and l3[1]==b):
             v2+=1
        if(l1[2]==b and l2[2]==b and l3[2]==b):
             v2+=1
        if(l1[2]==b and l2[1]==b and l3[0]==b):
            v2+=1
        if(l1[0]==b and l2[1]==b and l3[2]==b):
            v2+=1
    if(v1>v2):
        print('user 1 is winner!!!!!!')
    elif v1<v2:
        print('user 2 is winner!!!!!!')
    elif v1==v2 and v1>1:
        print("both are winners")
    
    
def us1():
    loc=int(input('enter location'))
    if(loc in l1):
        x=l1.index(loc)
        l1[x]=0
    elif(loc in l2):
         x=l2.index(loc)
         l2[x]=0
    elif(loc in l3):
       x=l3.index(loc)
       l3[x]=0
def us2():
    loc=int(input('enter location'))
    if(loc in l1):
        x=l1.index(loc)
        l1[x]=1
    elif(loc in l2):
         x=l2.index(loc)
         l2[x]=1
    elif(loc in l3):
       x=l3.index(loc)
       l3[x]=1      
def ds():
    print(l1)
    print(l2)
    print(l3)
ds()
print(s1.center(20,'*'))
us1()
ds()
print(s2.center(20,'*'))
us2()
ds()
print(s1.center(20,'*'))
us1()
ds()
print(s2.center(20,'*'))
us2()
ds()
print(s1.center(20,'*'))
us1()
ds()
print(s1.center(20,'*'))
us1()
ds()
print(s2.center(20,'*'))
us2()
ds()
print(s1.center(20,'*'))
us1()
ds()
print(s2.center(20,'*'))
us2()
ds()
check()


    


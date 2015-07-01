my_string=raw_input("enter the string")
count={}
for w in my_string:
 if w in count.keys():
    count[w] +=1
 else:
    count[w] =1
for j in count:
    print j,
print " "
l=[]
for i in count:
    l.append(count[i])
for i in range(len(my_string)):
    
    for j in range(len(l)):
 
        if l[j]>0:
            print '*',
            l[j]-=1
        else:
            print " ",
            l[j]-=1
        
    print " "

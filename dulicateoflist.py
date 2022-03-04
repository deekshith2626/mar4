l=[1,2,1,4]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
    else:
        print("repeating element is : ",i)


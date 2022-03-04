
arr=[7,8,2,4,6,8,9]
l=list(arr)
l.sort()
maxx=max(l)
indexx=l.index(maxx)
print("list elements of index vslues :",indexx-1)
print(l)
for i in l:
    if i not in arr:
        arr.append(i)
print(i-2)

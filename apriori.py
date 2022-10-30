fp = open("transactions", "r")
l = fp.read()
print("Displaying details of file:\n", l)
l = l.strip()
l1 = l.split("\n")
l1.remove(l1[0])
data, data2, itemlist = [], [], []
for i in l1:
    s = ""
    l = i.split()
    l.remove(l[0])
    l.sort()
    data.append(l)
    for j in l:
        if j not in itemlist:
            itemlist.append(j)
itemlist.sort()
mins = int(input("Enter minimum support value: "))
for i, j in enumerate(itemlist):
    for x, y in enumerate(itemlist):
        if x > i and len(j) == len(y) and j[:len(j)-1]==y[:len(y)-1]:
            l=[]
            if len(j[0])!=1:
                l=[x for x in j]
            else:
                l=[j]
            if len(y[0])!=1:
                l.append(y[len(y)-1])
            else:
                l.append(y)
            if l not in itemlist:
                itemlist.append(l)
print(itemlist)
count = []
for i, j in enumerate(itemlist):
    c = 0
    for x in data:
        if all(x1 in x for x1 in j):
            c += 1
    count.append(c)
newi, newc, maxlen = [], [], 0
for i, j in enumerate(count):
    if j >= mins:
        newi.append(itemlist[i])
        newc.append(count[i])
        maxlen=max(maxlen, len(itemlist[i]))
itemlist, count=newi, newc
for i in range(1, maxlen+1):
    for j in range(len(itemlist)):
        if len(itemlist[j])==i:
            print(f'{itemlist[j]} ---------  {count[j]}')
    print("........................................................")

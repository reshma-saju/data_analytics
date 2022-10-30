#INCOMPLETE

def euclid_dist(x, y):
    di = 0
    for ind in range(len(x)):
        di += (x[ind] - y[ind]) ** 2
    return round(di ** 0.5, 3)


fp = open("dataset", "r")
l = fp.read()
print("Displaying dataset:\n", l)
l = l.strip()
l1 = l.split("\n")
dataset=[]
for i in l1:
    l2=i.split()
    l2=[int(x) for x in l2]
    dataset.append(l2)
#k=input("Enter number of clusters: ")
k=2
n=len(dataset)
cent=[dataset[x] for x in range(k)]
c=[]
while True:
    dist=[[0 for _ in range(k)] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            dist[i][j]=euclid_dist(dataset[i], cent[j])
    print(dist)
    c1=[]
    for i in range(n):
        mins, minind=dist[i][0],0
        for j in range(k):
            if dist[i][j]<mins:
                mins=dist[i][j]
                minind=j
        c1.append(minind)
    if c1==c:
        print("Centroid found")
        break
    c=c1
    count=[0 for _ in range(k)]
    nc=[[0 for _ in range(len(dataset[0]))] for _ in range(k)]
        
    
    


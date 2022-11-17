#DEFINE CENT

def euclid_dist(x, y):
    di = 0
    for ind in range(len(x)):
        di += (x[ind] - y[ind]) ** 2
    return round(di ** 0.5, 2)


def printer():
    print("-----------------")
    print("{:^12} |".format(" "), end="")
    for j in range(k):
        print("{:^12} |".format(str(cent[j])), end="")
    print("\n", end="")
    print("----------------------------")
    for i in range(n):
        print("{:^12} |".format(str(dataset[i])), end="")
        for j in range(k):
            print("{:^12} |".format(str(dist[i][j])), end="")
        print("{:^12} |".format(str(c1[i]+1)))
    print("----------------------------")


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
k=int(input("Enter number of clusters: "))
n=len(dataset)
cent=[[2,10], [5,8], [1,2]] #edit cent as required
c=[]
ite, ncor=1, len(dataset[0])
while True:
    dist=[[0 for _ in range(k)] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            dist[i][j]=euclid_dist(dataset[i], cent[j])
    c1=[]
    for i in range(n):
        mins, minind=9999999999,0
        for j in range(k):
            if dist[i][j]<mins:
                mins=dist[i][j]
                minind=j
        c1.append(minind)
    print(f'Iterate {ite}: ')
    ite+=1
    printer()
    if c1==c:
        print("Cluster found. Displaying clusters:")
        for j in range(k):
            print(f'Cluster {j+1}:')
            for i in range(n):
                if c[i]==j:
                    print(dataset[i])
        break
    c=c1
    count=[0 for _ in range(k)]
    nc=[[0 for _ in range(ncor)] for _ in range(k)]
    for i, i1 in enumerate(dataset):
        for j in range(ncor):
            nc[c[i]][j]+=dataset[i][j]
        count[c[i]]+=1
    for i in range(k):
        for j in range(ncor):
            nc[i][j]/=count[i]
            nc[i][j]=round(nc[i][j],2)
    cent=nc








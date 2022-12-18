import math


class node:
    def __init__(self, dataset, attributelist, tableheader, splittingAtr, splitCondition):
        self.dataset = dataset
        self.attributelist = attributelist
        self.tableheader = tableheader
        self.children = []
        self.splittingAtr = splittingAtr
        self.splitCondition = splitCondition


def finding_infoa_nominal(data, values, classatt, ind, n):
    for k in values:
        total = 0
        infoaa = 0.0
        for i in classatt:
            count = 0
            for j in dataset:
                if j[natt] == i and j[ind] == k:
                    count += 1
            total += count
            print(f'{i}    {k}   {count}')
            infoaa += count / n * math.log2(count / n)
        print('---------------------------------------')
    return -infoaa * total / n

"""def finding_infoa_numeric(classatt, values, data, ind, n):
    for i in classatt:
        count=0
        for j in data:"""



def info_gain(data):
    gain, gainatt, n = 9999999, '', len(data)
    classatt = []
    for i in dataset:
        if i[natt] not in classatt:
            classatt.append(i[natt])
    infod = 0.0
    for i in classatt:
        count = 0
        for j in dataset:
            if j[natt] == i:
                count += 1
        print(i, " ", count)
        infod += count / n * math.log2(count / n)
    infod = -infod

    for ind in range(natt):
        if type(data[0][ind]) is int:
            """data.sort(key=lambda data: data[ind])
            lowest = 0.0
            for i in range(len(data) - 1):
                avg = (data[ind][i] + data[ind][i + 1]) / 2
                cgreater, clesser = [], []
                for j in data:
                    if j[ind] > avg:
                        cgreater.append(j[ind])
                    else:
                        clesser.append(j[ind])"""
            pass


        else:
            values = []
            for k in dataset:
                if k[ind] not in values:
                    values.append(k[ind])
            print(values)
            infoa = finding_infoa_nominal(data, values, classatt, ind, n)
            if (infod - infoa) > gain:
                gain = infod - infoa
                gainatt = attributelist[ind]
            print("========================================")
    return gainatt


fp = open("data", "r")
attributelist = list(fp.readline().strip().split(','))
natt = len(attributelist)
tableheader = list(fp.readline().strip().split(' '))
dataset = []
l = fp.readlines()

for i in l:
    x = list(i.strip().split(','))
    x.remove(x[0])
    for j, j1 in enumerate(x):
        if x[j].isnumeric():
            x[j] = int(x[j])
    dataset.append(x)
gainattribute=info_gain(dataset)



n = int(input("Enter the number of Dataword : "))
m = int(input("Enter the length of dataword : "))
l1 = []
a = ""
i = 0
while (i < n):
    a = list(input(f"Enter the dataword{i} : "))
    if (len(a) == m):
        l1.append(a)
        i += 1
    else:
        print(f"Enter dataword{i} again : ")

# print(l1)

def xor(p,q,m,l1):
    result=[]
    for i in range(m):
        if(l1[p][i] == l1[q][i]):
            result.append(0)
        else:
            result.append(1)
    return result

def hamming_dis():
    dmin=0
    res=[]
    for i in range(0, n):
        for j in range(i+1,n):
            c=xor(i,j,m,l1)
            res.append(c)

    # print(res)
    count = []
    counter = 0
    for i in res:
        for j in range(m):
            if(i[j] == 1):
                counter +=1
        count.append(counter)
        counter = 0
        dmin = min(count)

    print(f"dmin is : {dmin}")

hamming_dis()
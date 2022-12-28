def mean(lis):
    sum=0
    n=len(lis)
    for i in lis:
        sum+=i
    return int(sum/n)

def mode(lis):
    dic={}
    for i in lis:
        dic[i]=0
    for i in lis:
        dic[i]+=1
    maxi=0
    for value in dic.values():
        maxi=max(maxi,value)
    for key in dic.keys():
        if dic[key]==maxi:
            return key
    return -1

def median(lis):
    n=len(lis)
    lis.sort()
    return lis[int(n/2)]
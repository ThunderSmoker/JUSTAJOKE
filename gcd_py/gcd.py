def my_gcd(a,b):
    n=min(a,b)
    ans=-1
    for i in range(1,n+1):
        if a%i==0 and b%i==0:
            ans=i
        i+=1
    return ans

print(my_gcd(60,48))
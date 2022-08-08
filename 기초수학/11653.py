n= int(input())
def get_factorization(n):
    prime = 2
    result = []
    while(n>1):
        if (n%prime) ==0:
            print(prime)
            n= n//prime
        else :
            prime+=1
    return result

get_factorization(n)

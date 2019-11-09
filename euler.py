from functools import reduce

def prob1(n):
    answer = 0
    for x in range(n):
        if x%3==0:
            answer+=x
        elif x%5==0:
            answer+=x
    return answer

# print(prob1(1000))

def prob2(n):
    a = 1
    b = 2
    answer = 0
    while a<=n:
        if a%2==0:
            answer+=a
        temp = b
        b+=a
        a = temp
    return answer

# print(prob2(4000000))

def prob3(n):
    factors = []
    x=2
    while n!=1:
        if n%x==0:
            factors.append(x)
            while n%x==0:
                n=n/x
        x+=1
    # print(factors)
    return factors[-1]

# print(prob3(600851475143))

def prob4(n):
    def isPalindrome(num):
        for x in range(len(str(num))//2):
            if str(num)[x]!=str(num)[-(x+1)]:
                return False
        return True
    palindromes = []
    a = n-1
    while a > n*9/10:
        b = n-1
        while b > n*9/10:
            if isPalindrome(a*b):
                palindromes.append(a*b)
            b-=1
        a-=1
    return max(palindromes)

# print(prob4(1000))

def prob5(n):
    factors = []
    answer = 1
    for x in range(1,n):
        if answer%x!=0:
            factors.append(x)
            answer*=x
    print(factors)
    # factors = set()
    # for i in range(2,n):
    #     temp = i
    #     x=2
    #     while temp!=1:
    #         if temp%x==0:
    #             factors.add(x)
    #             while temp%x==0:
    #                 temp=temp/x
    #         x+=1
    # for x in range(n):
    #     for y in factors:
    #         if y%(n-x)==0:
    #             break
    #     else: factors.append(n-x)
    # print(factors)
    # return reduce(lambda x,y: x*y, factors)
    return answer

print(prob5(20))

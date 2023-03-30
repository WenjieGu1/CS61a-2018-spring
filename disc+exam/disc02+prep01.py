#prep01
def longest_increasing_suffix(n):
    m, suffix, k = 10, 0, 1
    while n:
        n, last = n // 10, n % 10
        if n % 10 < last:
            m, suffix, k = 10*m, n%10*m + last*k, 10*k
        else:
            return suffix
    return suffix

def sandwich(n):
    tens, ones = (n//10)%10, n%10
    n = n // 100
    while n:
        if n%10 == ones or (n//10)%10 == tens:
            return True
        else:
            tens, ones = (n//10)%10, n%10
            n = n // 100
    return False

def luhn_sum(n):
    def luhn_digit(digit):
        x = digit * (multiplier * 2)
        return (x // 10) + x % 10
    total, multiplier = 0, 1
    while n:
        n, last = n//10, n%10
        total = total + luhn_digit(last)
        multiplier = 1 - multiplier
    return total

#disc02
def mul(m,n):
    if n == 0:
        return 0
    else:
        return mul(m,n-1)+m

def countdown(n):
    if n == 1:
        print(n)
    else:
        print(n)
        countdown(n-1)

def sum_digits(n):
    if n//10 == 0:
        return n
    else:
        last=n%10
        return sum_digits(n//10)+last

def count_stair_ways(n):
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)

def count_k(n,k):
    if n==0:
        return 1
    elif n<0:
        return 0
    elif k<=0:
        return 0
    else:
        t=0
        for s in range(1,k+1):
            t= count_k(n-s,k) + t
        return t

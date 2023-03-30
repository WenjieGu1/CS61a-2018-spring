def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(k):
        if k == 0:
            s=start + '-' + repeat(k+1)
            return s
        elif k == num + 1:
            return end
        else:
            return middle + '-' + repeat(k+1)
    return repeat(0)

def combine(n, f, result):
    """
    Combine the digits in non-negative integer n using f.
    >>> combine(3, mul, 2) # mul(3, 2)
    6
    >>> combine(43, mul, 2) # mul(4, mul(3, 2))
    24
    >>> combine(6502, add, 3) # add(6, add(5, add(0, add(2, 3)
    )))
    16
    >>> combine(239, pow, 0) # pow(2, pow(3, pow(9, 0))))
    8
    """
    if n == 0:
        return result
    else:
        return combine(n//10, f, f(n%10, result))

def has_sum(total, n, m):
    """
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 0 * 3 + 1 * 5 = 5
    True
    >>> has_sum(11, 3, 5) # 2 * 3 + 1 * 5 = 11
    True
    """
    if total == 0:
        return True
    elif total < m and total < n:
        return False
    return has_sum(total-n, n, m) + has_sum(total-m, n, m)

def sum_range(lower, upper):
    """
    >>> sum_range(45, 60) # Printer 1 prints within this range
    True
    >>> sum_range(40, 55) # Printer 1 can print a number 56-60
    False
    >>> sum_range(170, 201) # Printer 1 + 2 will print between
    180 and 200 copies total
    True
    """
    def copies(pmin, pmax):
        if pmin < lower :
            return copies(pmin+60, pmax+50)+copies(pmin+140,pmax+130)
        elif pmin >= lower or pmax <= upper:
            return pmin >= lower and pmax <= upper
    return copies(0,0)

def kbonacci(n, k):
    """Return element N of a K-bonacci sequence.
    >>> kbonacci(3, 4)
    1
    >>> kbonacci(9, 4)
    29
    >>> kbonacci(4, 2)
    3
    >>> kbonacci(8, 2)
    21
    """
    if n < k - 1:
        return 0
    elif n == k - 1:
        return 1
    else:
        total = 0
        i = n-k
        while i < n:
            total = total + kbonacci(i, k)
            i = i + 1
        return total

def combine(left, right):
    """Return all of LEFT's digits followed by all of RIGHT's
    digits."""
    factor = 1
    while factor <= right:
        factor = factor * 10
    return left * factor + right

def reverse(n):
    """Return the digits of N in reverse.
    >>> reverse(122543)
    345221
    """
    if n < 10:
        return n
    else:
        return combine(n%10, reverse(n//10))

def remove(n, digit):
    """Return all digits of N that are not DIGIT, for DIGIT
    less than 10.
    >>> remove(243132, 3)
    2412
    >>> remove(remove(243132, 1), 2)
    433
    """
    removed = 0
    while n != 0:
        n, i =  n//10, n%10
        if i != digit:
            removed = removed*10 + i 
    return reverse(removed)
    
square = lambda x: x * x
double = lambda x: 2 * x
def memory(x, f):
    """Return a higher-order function that prints its
    memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """
    def g(h):
        print(f(x))
        return memory(x, h) 
    return g

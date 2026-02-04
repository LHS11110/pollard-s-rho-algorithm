import random

def is_prime(n):
    """
    밀러-라빈 소수 판별법으로 n이 소수인지 판별합니다.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # n - 1 = 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
        
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]: # 2^62 이하의 자연수들에 대해서는 해당 케이스에 대해서만 조사해도 충분하다.
        if n <= a: # a는 1 <= a <= n - 1의 범위에서 수행되어야 하므로 n보다 큰 a는 건너뛴다.
            break
        if pow(a, d, n) == 1:
            continue
        for r in range(s):
            if pow(a, (2 ** r) * d, n) == n - 1:
                break
        else:
            return False
    return True

def gcd(a, b):
    """
    유클리드 호제법으로 a와 b의 최대공약수를 계산합니다.
    """
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    """
    n의 비자명 인수를 찾기 위한 폴라드 로 알고리즘입니다.
    이 함수는 n의 단일 인수를 반환합니다.
    """
    if n % 2 == 0:
        return 2
    
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    g = 1
    
    while g == 1:
        x = (x*x + c) % n
        y = (y*y + c) % n
        y = (y*y + c) % n
        g = gcd(abs(x - y), n)
        
        if g == n:
            # 실패, 다른 난수 값으로 다시 시도
            return pollard_rho(n)
    
    return g

def factorize(n):
    """
    n의 소인수들이 정렬된 리스트를 반환합니다.
    """
    if n == 1:
        return []
    elif is_prime(n):
        return [n]
    
    factors = []
    queue = [n]
    
    while queue:
        current = queue.pop()
        if is_prime(current):
            factors.append(current)
            continue
        
        factor = pollard_rho(current)
        
        queue.append(factor)
        queue.append(current // factor)
    
    return sorted(factors)

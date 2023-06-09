
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for n in range(-1224, 1224):
    if n**3 - 7*n + 9 > n and is_prime(n**3 - 7*n + 9):
        print(n)
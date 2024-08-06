def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        k = 0
        for i in range(2, res // 2 + 1):
            if (res % i == 0):
                k = k + 1
        if (k <= 0):
           print("Число простое")
           return res
        else:
            print('Составное')
            return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(8,4,6)
print(result)

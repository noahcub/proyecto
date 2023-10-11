
import time
from multiprocessing import Pool

def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x

if __name__ == '__main__':
    start_time = time.time()
    '''answer = sum(map(if_prime, list(range(10000000))))
    '''
    with Pool(4) as p:    # ejecución con procesos 2, 4, 8
        answer = sum(p.map(if_prime, list(range(10000000))))

    duration = time.time() - start_time
    print(f"Ejecutado en {duration} segundos. La suma es {answer}")
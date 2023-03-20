import time

import multiprocessing
import concurrent.futures

def is_prime(n, m):
    # print(n, m)
    total = 0
    for x in range(n, m + 1):
        if x <= 1:
            continue
        check = False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                check = True
                break
        if check:
            continue
        total += x
    return total

def sum_primes_pool(N):
    num_cores = multiprocessing.cpu_count()

    pool = multiprocessing.Pool(num_cores)

    total = 0


    # check from 1 to 1000, from 1000 to 2000 and so on!
    terms = pool.starmap(is_prime, [(k, k + 999) for k in range(1, N + 1, 1000)])
    for x in terms:
        total += x
    return total

def sum_primes_concurrent(N):
    total = 0

    futures = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        for k in range(1, N + 1, 1000):
            futures.append(executor.submit(is_prime, k, k + 999, ))

    for future in futures:
        total += future.result()

    return total

if __name__ == '__main__':

    N = 1000000

    start = time.time()
    sum_pool = sum_primes_pool(N)
    end = time.time()
    diff = end - start
    print(f"sum_pool: {sum_pool}")
    print(f"Time taken: {diff} seconds")

    start = time.time()
    sum_concurrent = sum_primes_concurrent(N)
    end = time.time()
    diff = end - start
    print(f"sum_concurrent: {sum_concurrent}")
    print(f"Time taken: {diff} seconds")

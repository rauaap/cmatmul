#!/usr/bin/env python3
import random, timeit
from pymatmul import Matrix
from funcs import listcomp_matmul, loop_matmul

def test():
    a = Matrix([[x + y for x in range(3)] for y in range(4)])
    b = Matrix([[x + y for x in range(4)] for y in range(3)])

    c = a * b

    print(a)
    print(b)
    print(c)

    s = Matrix([[0 for _ in range(10)]])
    s[0] = [i for i in range(10)]

    print(s[0])

def main():
    SIZE = 100
    EXECUTIONS = 100

    thing = tuple(
        [random.randrange(10) for _ in range(SIZE)]
        for _ in range(SIZE)
    )

    f = Matrix(thing)
    d = Matrix(thing)

    execution_time = timeit.timeit(lambda: f * d, number=EXECUTIONS)
    print(f"C matmul: {execution_time:.4f} seconds")

    execution_time = timeit.timeit(lambda: listcomp_matmul(thing, thing), number=EXECUTIONS)
    print(f"listcomp matmul: {execution_time:.4f} seconds")

    execution_time = timeit.timeit(lambda: loop_matmul(thing, thing), number=EXECUTIONS)
    print(f"loop matmul: {execution_time:.4f} seconds")

if __name__ == '__main__':
    main()

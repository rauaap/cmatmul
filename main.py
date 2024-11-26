#!/usr/bin/env python3
from pymatmul import Matrix

a = Matrix([[x + y for x in range(3)] for y in range(4)])
b = Matrix([[x + y for x in range(4)] for y in range(3)])

c = a * b

print(a)
print(b)
print(c)

s = Matrix([[0 for _ in range(10)]])
s[0] = [i for i in range(10)]
print(s[0])

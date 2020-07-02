from __future__ import annotations

def gen(x: int):
    for i in range(x):
        yield i

g = gen(100000000)
x = [i for i in range(10000000)]

import sys
print (sys.getsizeof(x) / 10**6)
print (sys.getsizeof(g) )
# for i in g:
#     print (i)

# for i in x:
#     print (i)

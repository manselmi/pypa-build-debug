# distutils: language = c++
# https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html#primes-with-c

# Cython imports
from libcpp.vector cimport vector  # isort:skip (Cython support seems broken… flagged as error but generates empty diff)


def primes(unsigned int nb_primes):
    cdef int n, i
    cdef vector[int] p
    p.reserve(nb_primes)

    n = 2
    while p.size() < nb_primes:
        for i in p:
            if n % i == 0:
                break
        else:
            p.push_back(n)
        n += 1

    return p

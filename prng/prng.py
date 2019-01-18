#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pip install base58
from sympy import Symbol, simplify, lambdify
from functools import reduce
import operator
import gmpy
import sympy as sym
from sympy import GF
from sympy import poly
import random
import base58
import hashlib
import os


def gen_prime(BITS, lb):
    ub = 2**BITS
    r = random.randrange(lb, ub)
    while not gmpy.is_prime(r):
        r = random.randrange(lb, ub)
    return r


def interpolate_lagrange(x, x_values, y_values):
    def _basis(j):
        p = [(x - x_values[m]) * gmpy.invert(x_values[j] - x_values[m], pp)
             for m in range(k) if m != j]
        return reduce(operator.mul, p)
    k = len(x_values)
    return sum(_basis(j) * y_values[j] for j in range(k))


def fhash(fname):
    fin = open(fname, "rb")
    data = fin.read()
    fin.close()
    return int(hashlib.sha256(data).hexdigest(), 16)


def get_targets():
    target_vals = []
    for filename in os.listdir("target_files"):
        target_vals.append(fhash("target_files/" + filename))
    return target_vals


target_vals = get_targets()
pp = gen_prime(256, max(target_vals))
x = Symbol('x')
domain = range(10000)
random.shuffle(domain)
pl = simplify(interpolate_lagrange(x, domain[:len(target_vals)], target_vals))
pl = poly(pl, domain=GF(pp))

print "PRNG polynomial: ", pl

print "The initial values of the PRNG:"
for i in range(10):
    tmp = pl.eval(i) % pp
    tmp = base58.b58encode_int(tmp)
    print "Qm" + tmp, base58.b58decode_int(tmp)

print "The target values are:", target_vals
print "Sanity check..."
for i in domain[:len(target_vals)]:
    print i, pl.eval(i) % pp

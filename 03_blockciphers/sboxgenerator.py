#!/usr/bin/env python3
import math
import numpy as np
from columnar import columnar
from libs.gf2_add import gf2_add
from libs.gf2_mul import gf2_mul

# CHANGEME
n = 5  # IMPORTANT THAT THIS IS CORRECT (often the degree of f(x) )
k = 2  # IMPORTANT THAT THIS IS CORRECT

#       +  +  +  +  +  +  +
#     1  x  x² x³ x⁴ x⁵ x⁶ x⁷
fx = [1, 0, 0, 1, 0, 1]  # IMPORTANT THAT THIS IS CORRECT
ax = [1]  # IMPORTANT THAT THIS IS CORRECT
bx = [0, 1, 0, 1]  # IMPORTANT THAT THIS IS CORRECT

# init stuff
use_golds = False  # Only one can be true, please respect it...
use_kasumi = True  # Only one can be true, please respect it...
inverse = False  # what even is this?
m = (n - 1) // 2
a_pow = [[0] * n for x in range((2 ** n) - 1)]
a_inv = []
t_dat = []

"""
FUNCTIONS NEEDED
"""


def poly_div(p1, p2):  # The credits go to this person: https://stackoverflow.com/a/50205371
  def degree(poly):
    while poly and poly[-1] == 0:
      poly.pop()
    return len(poly) - 1
  
  p2_degree = degree(p2)
  p1_degree = degree(p1)
  
  if p2_degree < 0:
    raise ZeroDivisionError
  
  if p1_degree >= p2_degree:
    q = [0] * p1_degree
    while p1_degree >= p2_degree:
      d = [0] * (p1_degree - p2_degree) + p2
      mult = q[p1_degree - p2_degree] = p1[-1] // float(d[-1])
      d = [coeff * mult for coeff in d]
      p1 = [math.fabs(p1_c - p2_c) for p1_c, p2_c in zip(p1, d)]
      p1_degree = degree(p1)
    r = p1
  else:
    q = [0]
    r = p1
  
  return [int(x) for x in r]


def xor_x_lists(l):
  no_lists = len(l)
  if no_lists < 2:
    return [p ^ q for p, q in zip(a_pow[l[0]], [0] * n)]
  else:
    comb = [p ^ q for p, q in zip(a_pow[l[0]], a_pow[l[1]])]
    if no_lists >= 3:
      for i in l[2:]:
        comb = [p ^ q for p, q in zip(comb, a_pow[i])]
    return comb


"""
PROGRAM START
"""

if use_golds:
  d = (2 ** k) + 1
elif use_kasumi:
  d = (2 ** (2 * k)) - (2 ** k) + 1
elif inverse:
  d = (2 ** n) - 2
else:
  d = None

hw = bin(d)[2:].count("1")
assert math.gcd(n, k) == 1  # (n is prime)
print(f"d={d}={bin(d)[2:]} | hamming weight={hw} | non-linear order={hw}")
print(f"\nThe elements of the multiplicative group of the field: GF(2^{n}):")

# Do the n first ones...
for i in range(0, n):
  a_pow[i][(n - 1) - i] = 1
  t_dat.append([f"a^{i}", f"{a_pow[i]}"])

for i in range(n, (2 ** n) - 2 + 1):
  tmp = [0] * (i + 1)
  tmp[i] = 1
  r = poly_div(tmp, fx)
  pol = [i for i in range(0, len(r)) if r[i] == 1]
  a_pow[i] = xor_x_lists(pol)
  str = ""
  for p in pol:
    str += f"a^{p}+"
  t_dat.append([f"a^{i} = {str[:-1]}", f"{a_pow[i]}"])

print(columnar(t_dat, no_borders=True))

print(f"\nDetermining the inverse elemets: G(x)=x^{d}")
t_dat = []
for i in range(0, (2 ** n) - 2 + 1):
  mod = (2 ** n) - 1
  pow = i * d
  index = pow % mod
  a_inv.append((i, a_pow[index]))  # mapping from gotf to the power function
  t_dat.append(
    [f"(a^{i})^{d} =", f"a^{pow}mod{mod} = a^{index} =", f"{a_pow[index]}"])

print(columnar(t_dat, no_borders=True))

print("\nCreating the SBOX:")
t_dat = []
for i in range(1, (2 ** n)):
  crnt = [int(x) for x in bin(i)[2:].zfill(n)]
  a_index = a_pow.index(crnt)
  g_index = [x[1] for x in a_inv if x[0] == a_index][0]
  s1 = poly_div([int(x) for x in gf2_mul(ax, list(reversed(g_index)))], fx)
  s2 = poly_div([int(x) for x in gf2_add(np.array(bx, dtype="uint8"), np.array(s1, dtype="uint8"))], fx)
  t_dat.append(
    [a_index, crnt, g_index, [int(x) for x in list(reversed(np.pad(s2, pad_width=(0, n - len(s2)), mode='constant')))]])

print(columnar(t_dat, ["a", "X", f"X^{d}", "a(x) * x^d + b(x)"], no_borders=True))

#!/usr/bin/env python3

import copy

import numpy as np
from libs.gf2_add import gf2_add
from libs.gf2_mul import gf2_mul

# CHANGEME:
S = "101011"

# Initial setup
S = [int(el) for el in S]
N = len(S)
L = 0
j = 1
cx = np.array([0] * N, dtype="uint8")
csx = np.array([0] * N, dtype="uint8")
cx[0], csx[0] = 1, 1
reg = []
c = np.zeros(N)
delta = None  # Discrepancy
n = 0

"""
Helper functions
"""


def polyfy(binar):
  str = "1"
  for i in range(1, len(binar)):
    if binar[i] == 1:
      str += f"+x^{i}"
  return str


"""
Program start
"""

while n < N:
  print("- " * 10)
  print(f"s{n}={S[n]}")

  print(f"\t {S[n]} +", end="")
  for i in range(1, L + 1):
    print(f" c{i}={c[i]}", end=" * ")
    print(f" S{n - i}={S[n - i]}", end=" + ")

  print()

  t = [c[i] * S[n - i] for i in range(1, L + 1)]
  delta = int(S[n] + sum(t)) % 2

  print(f"𝛿={delta}")

  if delta == 0:
    print(f"J={j}+1")
    j += 1
  elif delta == 1:
    tx = copy.copy(cx)

    print(f"T(X)=C(X)={polyfy(np.asarray(tx))}")

    tz = np.zeros(N)
    tz[j] = 1
    print(f"C(X)<--C(X)+X^j * C*(X) = {polyfy(cx)} + X^{j} * {polyfy(csx)}", end=" = ")
    tcx = gf2_mul(tz, csx)
    cx = gf2_add(cx, tcx)
    print(polyfy(cx))
    c = np.zeros(N)
    for x in range(len(cx)):
      if cx[x] == 1:
        c[x] = 1

    if 2 * L <= n:
      print(f"L={n}+1-{L}={(n + 1 - L)}")
      L = n + 1 - L
      print("J=1")
      j = 1
      csx = tx
      print("C*(X)=T(X)=", polyfy(csx))
    else:
      print(f"J={j}+1")
      j += 1
  else:
    raise Exception("Need to check you code mate")

  print("POLY: ", polyfy(cx))
  print("Register: ", reg[-L:])
  reg = [S[n]] + reg
  n += 1

print("- " * 10, "\nThe minimal polynomail to generate the sequence S is", polyfy(cx))

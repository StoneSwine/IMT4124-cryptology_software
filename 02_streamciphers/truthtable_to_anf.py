#!/usr/bin/env python3

import math

# CHANGEME:
#g = 0xE7
g = int("0b11010001", 2)

g = str(bin(g)[2:])
varnum = int(math.log2(len(g)))
n_rows = int("0b" + "1" * varnum, 2)


def find(s, ch):
  return [x for x, ltr in enumerate(s) if ltr == ch]


def get_multiple_characters(s, indexes):
  for i in indexes:
    if s[i] != "0":
      return None
  return s


print("The truth table:")
for i, gc in zip(range(n_rows + 1), g):
  print(f"{[x for x in bin(i)[2:].zfill(varnum)]} | {gc}")
print("- " * 10)

sequence = [(bin(i)[2:].zfill(varnum), gc) for i, gc in zip(range(n_rows + 1), g)]

# The Möbius transform
endsumvals = []
for i in range(n_rows + 1):
  print("#" * 10)
  a = []
  u = bin(i)[2:].zfill(varnum)
  print(f"u={u}")
  for x in sequence:
    for y in sequence:
      if y[0] == get_multiple_characters(x[0], find(u, "0")):
        a.append(int(y[1]))
        print(y[0])
  if sum(a) % 2 == 1:
    endsumvals.append(u)

print("#" * 10)
print("END:", " + ".join(endsumvals))

#!/usr/bin/env python3

# CHANGEME:
S = "110010001111010"
T = 15
k = [0, 2, 5, 14]


def leftShift(text, n):
  return text[n:] + text[:n]


def diff_letters(a, b):
  return sum(a[i] != b[i] for i in range(len(a)))


print(f"Original:  {S}")

for i in k:
  acn = leftShift(S, i)
  D = diff_letters(S, acn)                                                          # A-D/T
  print(f"Shifted({i})={acn}\t|\tD={D},\tT={T}\tAC({i})={(((T - D) - D) / T):.2f}")

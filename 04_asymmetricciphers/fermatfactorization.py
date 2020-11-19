#!/usr/bin/env python3

import math

# CHANGEME
n = 50621


def isPerfectSquare(intnum):  # https://stackoverflow.com/a/17509112
  return intnum == int(math.sqrt(intnum)) ** 2


print("𝑛=𝑎×𝑏, where 𝑎 and 𝑏 are close together")
n_sq = math.sqrt(n)
print(f"Square root of {n} = {n_sq:.2f}")
n_sq = int(n_sq)

for i in range(1, n_sq):
  crntval = n_sq + i
  print(f"{n_sq} + {i} = {crntval}")
  testval = (crntval ** 2) - n
  print(f"{crntval}^2 - {n} = {testval}", end=" ")
  if isPerfectSquare(testval):
    p_sq = int(math.sqrt(testval))
    print(f"= {p_sq}^2 | which is a perfect square")
    print(f"{n}={crntval}^2-{p_sq}^2 = ({crntval}-{p_sq})*({crntval}+{p_sq})={crntval - p_sq}*{crntval + p_sq}")
    break
  else:
    print(f"\n{testval} is not a perfect square")

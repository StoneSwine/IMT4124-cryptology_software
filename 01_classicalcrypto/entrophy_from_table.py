#!/usr/bin/env python3

import math
from decimal import *

import numpy as np

# CHANGEME:
probtab = np.loadtxt(open("data/probability_table.csv", "rb"), delimiter=",").astype(Decimal)

print("The marginal probabilities of all the values of 𝑋")
print(probtab)
print("- " * 10)

px = np.sum(probtab, axis=0)
py = np.sum(probtab, axis=1)

print("P(X):", px)
print("P(Y):", py)

# sum of all columns and rows must be one
assert sum(px) == 1
assert sum(py) == 1

print("Shannon’s entropy of the plaintext")
print("𝐻(𝑋)=−∑𝑃(𝑥)log2𝑃(𝑥)")
hx = -sum([i * math.log2(i) for i in px])
print("-(", end="")
for i in px:
  print(f"{i:.3f}*log2({i:.3f})", end=" + ")
print(f") = {hx:.3f} bits")
print("- " * 10)

print("The conditional entropy 𝐻(𝑋|𝑌)")
print("𝐻(𝑋|𝑌)=−∑y∑x𝑃(𝑥,𝑦)log2𝑃(𝑥|𝑦)")
hxy = 0
print("-(", end="")
for k, i in zip(py, probtab):
  for j in i:
    hxy += (j * math.log2(j / k))
    print(f"{j}*log2({j}/{k})", end=" + ")
hxy = -hxy
print(f") = {hxy:.3f} bits")
print("- " * 10)

print("The mutual information")
print("𝐼(𝑋,𝑌)=𝐻(𝑋)−𝐻(𝑋|𝑌)")
print(f"{hx:.3f} - {hxy:.3f} = {(hx - hxy):.3f} bits")

if (hx - hxy) == 0:
  print("The cipher is perfectly secret")

else:
  print("The cipher is not perfectly secret because I(X,Y) != 0")
  # The uncertainty about the plaintext is reduced afer receieving the ciphertext

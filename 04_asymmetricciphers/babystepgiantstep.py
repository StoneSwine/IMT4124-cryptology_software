#!/usr/bin/env python3
import math

# CHANGEME
a = 5  # generator | the discrete logarithm of 3for the base 10modulo 17 --> log10^3 mod 17 --> a = 10, n = 17, b = 3
n = 23  # order
b = 3  # element

m = 1 + int(math.sqrt(n - 1))
tab = []
g = b
gcd_cnt, eea_cnt = 0, 0
absval = lambda i: ("+" if i > 0 else "") + str(i)


def xgcd(a, b):
  global gcd_cnt, eea_cnt
  if a == 0:
    return b, 0, 1
  if gcd_cnt > 0:  # skip the first print
    print(f"{b}={a}*{(b // a)}+{(b % a)}")
  gcd_cnt += 1
  gcd, x1, y1 = xgcd(b % a, a)
  x = y1 - (b // a) * x1
  y = x1
  if eea_cnt > 1:  # skip the two first prints..
    print(f"1={y1}*{a}{absval(x1)}*{(b % a)}")
  eea_cnt += 1
  return gcd, x, y


"""
Example task:
  Apply the Baby step giant step algorithm to find the discrete logarithm of 3 
  and 10 in 𝑍23∗using the generator 𝑎=5.
"""

# Baby step:
print(f"m=[sqrt({n}-{1})]+1={m}")
print(f"Tuple = (j, {a}^jmod{n})")
for j in range(m):
  tab.append((j, ((a ** j) % n)))

print("\t", tab)
tab.sort(key=lambda tup: tup[1])  # Sort the table by its second component
print("Sorted:\n\t", tab)
print("- " * 10)

# Giant step:
tmp_xgcd = (xgcd(n, (a ** m) % n)[2] % n)
print(f"a^(−m)={tmp_xgcd}")
print("- " * 10)
am = 1
for i in range(0, m):  # try whether 𝑔←𝑔𝑎^(−𝑚) can be found in the second row of the table.
  pg = g
  g = (g * am) % n
  print(f"i={i},\tg={pg}*{am}mod{n}={g}")
  if any([True for j, m in tab if g == m]):
    j, m = [(j, m) for j, m in tab if g == m][0]
    print(f"{m} is found for j={j}, log{m}*{b}=im+j={i}*{m}+{j}={(i * m) + j}")
    break
  if i == 0:
    am = tmp_xgcd

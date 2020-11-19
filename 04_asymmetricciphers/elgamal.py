#!/usr/bin/env python3

# CHANGEME
p = 113  # Prime
g = 3  # generator
a = 27  # Alice secret
k = 34  # BOB secret
m = 80  # The message Alice sends to Bob (0≤𝑚<𝑝)
gcd_cnt, eea_cnt = 0, 0
absval = lambda i: ("+" if i > 0 else "") + str(i)


# Modular exponentiation:
def modexp(b, n, m):
  retval = 1
  tmpstr = "\t "
  prodvals = []
  binx = bin(n)[2:]
  print(f"\t{n}={binx} | {b}^{n} mod {m}")
  binx = list(reversed(bin(n)[2:]))  # reverse to make the number correct
  indexone = [i for i in range(len(binx)) if binx[i] == "1"]
  val = b
  for i in range(0, len(binx)):
    pval = val
    if i == 0:
      val = (val ** (2 ** i)) % m
    else:
      val = (val ** 2) % m
    if i in indexone:
      print("\t* ", end="")
      prodvals.append(val)
    else:
      print("\t  ", end="")
    print(i, end=" | ")
    print(f"\t{pval}^2 = {val} (mod {m})")
  for i in prodvals:
    tmpstr += " " + str(i) + " *"
    retval = (retval * i) % m
  tmpstr = tmpstr[:-1] + "mod " + str(m) + " = " + str(retval)
  print(tmpstr + "\n" + "- " * 10)
  return retval


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


print("[INFO]: Alice enciphers")
print(f"Message m={m} | k={k}")
print("b = g^a mod p")
b = modexp(g, a, p)
print(f"Bob’s public key is (𝑝,𝑔,𝑏)=({p},{g},{b})")
print("The ciphertext is (𝑟,𝑡)\nr=g^k mod p")
r = modexp(g, k, p)
print("t=b^(𝑘)*m mod p")
bk = modexp(b, k, p)
t = ((bk * m) % p)
print(f"{bk}*{m} mod {p} = {t}")
print(f"The ciphertext is (𝑟,𝑡) = ({r},{t})")
print("[INFO]: Bob deciphers")
print("plaintext = 𝑡*𝑟^(−𝑎) mod p")
rainv = xgcd(p, modexp(r, a, p))[2] % p
dec_m = (t * rainv % p)
print(f"Plaintext = {t}*{rainv} mod {p} = {dec_m}")

assert dec_m == m  # sent and deciphered message is the same

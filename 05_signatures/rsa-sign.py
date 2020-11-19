#!/usr/bin/env python3

# CHANGEME
p = 167
q = 281
m = 16346  # The message Alice sends to Bob
e = 39423
phi_n = (p - 1) * (q - 1)
n = p * q
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
  print(tmpstr)
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


print("[INFO]: Determining Alices keys")
print(f"p={p} | q={q} | e={e}")
print(f"Public key = (n=p*q,e) = ({n}, {e})")
print(f"ϕ(n) = ({p - 1})*({q - 1}) = {phi_n}")
print(f"d = e^(-1) mod ϕ(n)")
print(f"({phi_n}, {e}) = 1")
d = xgcd(phi_n, e)[2] % phi_n
print(f"d = {e}^(-1) = {d}")
print(f"Alice keys: Pub --> ({n}, {e}) | Priv --> {d}")
print("- " * 20)
print(f"[INFO]: Alice signing message m={m}")
print(f"s = m^(d) mod n = {m}^{e} mod {n} | (Bobs public key)")
s = modexp(m, d, n)
print(f"s = {s}")
print("- " * 20)
print(f"[INFO]: Bob verifying signature s={s}")
print(f"m = s^(e) mod n = {s}^{e} mod {n} | (Bobs private key)")
m_d = modexp(s, e, n)
print(f"m = {m_d}")

assert m_d == m  # Decryption works

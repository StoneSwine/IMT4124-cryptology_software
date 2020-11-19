#!/usr/bin/env python3

# CHANGEME
p = 113
g = 3
x = 30  # Alice secret
y = 59  # BOB secret


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


print("[ALICE] :")
a = modexp(g, x, p)
print("[BOB]: ")
b = modexp(g, y, p)

print("[INFO]: Exchanging...")
print(f"[INFO]: Sending {a} to Bob")
print(f"[INFO]: Sending {b} to Alice")

print("[ALICE] :")
a_ss = modexp(b, x, p)
print("[BOB]: ")
b_ss = modexp(a, y, p)

assert a_ss == b_ss  # shared secret must be the same...

#!/usr/bin/env python3

from columnar import columnar

# CHANGE ME PLX
MINADR = 0x0
MAXADR = 0xF
cnt = [0x4, 0x1, 0x8, 0xE, 0x2, 0xF, 0xB, 0x6, 0x7, 0x3, 0xD, 0x0, 0x5, 0x9, 0xC, 0xA]
l_p = [(0xF, 0x1)]
misc_calculation = ""

def binify(n):  # This kind of strange, i know about it.
  return [int(x) for x in bin(n)[2:].zfill(len(bin(MAXADR)[2:]))]


def xor_two_lists(l1, l2):
  return [p ^ q for p, q in zip(l1, l2)]


def get_ylist_from_xlist(xlist):
  return cnt[adr.index(xlist)]


adr = [binify(i) for i in range(MINADR, MAXADR + 1)]  # x
cnt = [binify(i) for i in cnt]  # y

assert len(adr) == len(cnt)

# This is a bit hardcoded, but can not be bothered to do it differently
print(columnar(adr, ["x¹", "x²", "x³", "x⁴"], no_borders=True))
print("- " * 20)
print(columnar(cnt, ["y¹", "x²", "y³", "y⁴"], no_borders=True))
print("- " * 20)

for i,j in l_p:
  deltax = binify(i)
  deltay = binify(j)
  str_deltay = "".join(map(str, deltay))
  data = []
  header = []
  count = 0
  misc_calculation += f"∆X={i}\n"
  for x_l, y_l in zip(adr, cnt):
    misc_calculation += f"X+∆X={''.join(map(str, x_l))}+{''.join(map(str, deltax))}={''.join(map(str, xor_two_lists(x_l, deltax)))}"
    tmpval = "".join(map(str, xor_two_lists(get_ylist_from_xlist(xor_two_lists(x_l, deltax)), y_l)))
    misc_calculation += f" => y+∆y={''.join(map(str, get_ylist_from_xlist(xor_two_lists(x_l, deltax))))}+{''.join(map(str, y_l))}={tmpval}\n"
    if tmpval == str_deltay:
      count += 1
    data.append([tmpval])

  print(columnar(data, [f"∆𝑋={i}={''.join(map(str, deltax))}"], no_borders=True))
  print(f"({str(hex(i))},{str(hex(j))})--> {count}")
  print("- " * 20)

print(misc_calculation)
#!/usr/bin/env python3

from columnar import columnar

# CHANGE ME PLX
MINADR = 0x0
MAXADR = 0xF
HMAX = int((MAXADR + 1) // 2)
cnt = [0x1, 0x4, 0x6, 0xE, 0x2, 0xF, 0xB, 0x8, 0x7, 0xA, 0xD, 0xC, 0x5, 0x9, 0x0, 0x3]
l_p = [(0x1, 0xE), (0x3, 0x9), (0xE, 0xF)]


# x0 x1 x2 x3 x4 x5 x6 ...

def binify(n):  # This kind of strange, i know about it.
  return [int(x) for x in bin(n)[2:].zfill(len(bin(MAXADR)[2:]))]


def getindexofones(b):
  retarr = [i for i in range(0, len(b)) if b[i] == 1]
  if retarr:
    return retarr
  else:
    return [0]


def xor_list(l, indexes):
  if len(indexes) <= 1:
    return l[indexes[0]]
  else:
    tmp = l[indexes[0]] ^ l[indexes[1]]
    for i in indexes[2:]:
      tmp = tmp ^ l[i]
    return tmp


adr = [binify(i) for i in range(MINADR, MAXADR + 1)]
cnt = [binify(i) for i in cnt]

# This is a bit hardcoded, but can not be bothered to do it differently
print(columnar(adr, ["x¹", "x²", "x³", "x⁴"], no_borders=True))
print("- " * 20)
print(columnar(cnt, ["y¹", "x²", "y³", "y⁴"], no_borders=True))
print("- " * 20)

for i,j in l_p:
  x, y = binify(i), binify(j)
  header = [str(hex(i)), str(hex(j))]
  x_i, y_i = getindexofones(x), getindexofones(y)
  x_l, y_l = [], []
  l = []
  for a_v, c_v in zip(adr, cnt):
    l.append([])
    l[-1].append(xor_list(a_v, x_i))
    l[-1].append(xor_list(c_v, y_i))
  noeq = sum([1 for p, q in l if p == q])
  print(columnar(l, header, no_borders=True))
  print(f"{noeq}/{MAXADR + 1} - {HMAX}/{MAXADR + 1} = {int(noeq - HMAX):d}")
  print("- " * 20)

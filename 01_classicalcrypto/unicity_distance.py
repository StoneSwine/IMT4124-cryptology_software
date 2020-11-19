#!/usr/bin/env python3

import math
from decimal import *

# CHANGEME:
N=Decimal(math.factorial(26))   # Cardinality of the alphabet
r=Decimal(1.5)   # The true rate of the language
n=Decimal(26)    # length of the key/plaintext/ciphertext

print("r0=log2(N)")
r0=Decimal(math.log2(n)) # The redundancy of the language
print(f"{r0:.2f}=log2({N})")
print("- "*10)

print("d=r0-r")
d=Decimal(r0-r) # The redundancy of the language
print(f"{d:.2f}={r0:.2f}-{r}")
print("- "*10)

print("H(Z)=log2(N)")
Hz=Decimal(math.log2(N)) # the Shannon’s entropy of the key
print(f"{Hz:.2f}=log2({N})")
print("- "*10)

print("n0=H(Z)/d")
n0=Hz/d
print(f"{n0:.2f}n={Hz:.2f}/{d:.2f}")



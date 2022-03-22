# ID: ohZ9LooV

# imports {{{
from random import choice, randrange
#----------------------------------------------------------------------------}}}

def rand_L(n):  # {{{
  L = []
  R = list(range(n))
  while len(R) != 0:
    r = choice(R)
    L.append(r)
    R.remove(r)
  return L
#----------------------------------------------------------------------------}}}

def QS(L): # {{{
  # Our version of the quicksort algorithm.
  # Hints:
  # - Pseudocode
  #     for l in {0,...,n}
  #       <psuedocode>
  #   corresponds to the Python code
  #     for l in range(len(L))
  #       <python code>
  #   where L is a length n list.
  # - To initialize an empty list E:
  #     E = []
  # - To append a value v to a list E:
  #     E.append(v)
  # - To concatenate lists E and F:
  #     E.extend(F)   OR
  #     E + F

  # basis
  if len(L) <= 1:
    return L

  p = randrange(len(L))
  A = []
  B = []
  for l in range(len(L)):
    if l == p:
      continue
    if L[l] <= L[p]:
      A.append(L[l])
    else:
      B.append(L[l])
  A = QS(A)
  B = QS(B)
  return A + [L[p]] + B

#----------------------------------------------------------------------------}}}

# use this to test your QS() function
for n in range(10**3):
  L = rand_L(n)
  Ls = QS(L)
  if Ls != sorted(L):
    print("Whoops!", L, sep="\n----\n")
    break

L = rand_L(10)
print(L, QS(L), sep="\n")

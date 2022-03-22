# imports {{{
from random import choice, randrange
from math import ceil, floor
#----------------------------------------------------------------------------}}}

def rand_L(n):  # {{{
  return [ randrange(n) for _ in range(n) ]
#----------------------------------------------------------------------------}}}

def MS(L): # {{{
  # Our version of the mergesort algorithm.
  # Hints
  # - slice notation:
  #   L[a:b] means the list [ L[a], ..., L[b-1] ]
  #   L[:b] means L[0:b]
  #   L[b:] means L[b:n]
  #   it is always true that L[a:b] + L[b:c] = L[a:c]
  # - floor and ceiling:
  #   provided by the math module: use floor(x) and ceil(x).
  #   note that the list L[ceil((n-1)/2):] will have length ceil(n/2), whereas
  #     L[ceil(n):] might not.

  n = len(L)

  # basis
  if n <= 1:
    return L

  Ll = L[:floor(n/2)]
  Lr = L[ceil((n-1)/2):]
  Llp = MS(Ll)
  Lrp = MS(Lr)
  Lp = merge(Llp,Lrp)
  return Lp

def merge(A,B):
  R = []
  ia = ib = 0
  A.append(float("inf"))
  B.append(float("inf"))
  while A[ia] != float("inf") or B[ib] != float("inf"):
    if A[ia] <= B[ib]:
      R.append(A[ia])
      ia = ia +1
    else:
      R.append(B[ib])
      ib = ib + 1
  return R
#----------------------------------------------------------------------------}}}

# use this to test your QS() function
for n in range(10**3):
  L = rand_L(n)
  Ls = MS(L)
  if Ls != sorted(L):
    print("Whoops!", L, Ls, sep='\n', end="\n----\n")
    break

L = rand_L(10)
print(L, MS(L), sep="\n")

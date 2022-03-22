# ID: quoNg0fa, Eekoh2fo
class Tower:  # {{{1
  def __init__(self, num_disks, num_pegs):
    self.tower = [ [k for k in range(num_disks)] ] + [ [] for _ in range(num_pegs-1) ]

  def move(self, pegA, pegB):
    if len(self.tower[pegA]) == 0:
      raise Exception("Peg " + str(pegA) + " is empty! Tower:\n" + str(self.tower))

    disk = self.tower[pegA][0]

    if len(self.tower[pegB]) > 0 and disk > self.tower[pegB][0]:
      raise Exception("Disk " + str(disk) + " is larger than " + str(self.tower[pegB][0]) + "! Tower:\n" + str(self.tower))

    del self.tower[pegA][0]
    self.tower[pegB] = [disk] + self.tower[pegB]
    print("Moved disk from peg", pegA, "to peg", pegB)

  def __str__(self):
    return str(self.tower)
#----------------------------------------------------------------------------}}}1
class Tower02:  # {{{1
  def __init__(self, num_disks):
    self.tower = [ [k for k in range(num_disks)], [], [] ]

  def move(self, pegA, pegB):
    if pegA == 0 and pegB == 2:
      raise Exception("Moves from peg 0 to peg 2 aren't allowed!")
    if len(self.tower[pegA]) == 0:
      raise Exception("Peg " + str(pegA) + " is empty! Tower:\n" + str(self.tower))

    disk = self.tower[pegA][0]

    if len(self.tower[pegB]) > 0 and disk > self.tower[pegB][0]:
      raise Exception("Disk " + str(disk) + " is larger than " + str(self.tower[pegB][0]) + "! Tower:\n" + str(self.tower))

    del self.tower[pegA][0]
    self.tower[pegB] = [disk] + self.tower[pegB]
    print("Moved disk from peg", pegA, "to peg", pegB)

  def __str__(self):
    return str(self.tower)
#----------------------------------------------------------------------------}}}1

def Hanoi(T, n, src, dest, other): # {{{
  # An algorithm to solve the tower of Hanoi for n disks. You should return the
  # tower T.

  if n == 0:
    return T

  else:
    Hanoi(T, n-1, src, other, dest)
    T.move(src, dest)
    Hanoi(T, n-1, other, dest, src)
  return T
#----------------------------------------------------------------------------}}}

def Hanoi02(T, n, src, dest, other): # {{{
  # An algorithm to solve the tower of Hanoi for n disks, where direct moves
  # from peg 0 to peg 2 aren't allowed. You should return the tower T.

  if n == 0:
    return T

  if n == 1:
    T.move(src,other)
    T.move(other,dest)
    return T
  Hanoi02(T, n-1, src,dest,other)
  T.move(src,other)
  Hanoi02(T,n-1,dest,src,other)
  T.move(other,dest)
  Hanoi02(T,n-1,src,dest,other)
  return T
#----------------------------------------------------------------------------}}}

# ues this to test your solution
print("Hanoi(5):")
T = Tower(5, 3)
T = Hanoi(T, 5, 0, 2, 1)
if len(T.tower[-1]) == 5:
  print("solved!")
else:
  print("not solved! T:")
  print(T)

# ues this to test your solution
print("\n\nHanoi02(5):")
T = Tower02(5)
T = Hanoi02(T, 5, 0, 2, 1)
if len(T.tower[-1]) == 5:
  print("solved!")
else:
  print("not solved! T:")
  print(T)

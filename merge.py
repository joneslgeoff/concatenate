def sort(seq):
  '''TODO'''
  return sorted(seq)

def mergeMovieLists():
  p1 = '/home/geoffwood/Desktop/Merger/Chris.txt'
  p2 = '/home/geoffwood/Desktop/Merger/Geoff'
  fp1 = open(p1)
  fp2 = open(p2)
  l1 = fp1.read().strip().split("\n")
  l2 = fp2.read().strip().split("\n")
  l3 = l1 + l2
  merge_list = sort(l3)
  print(merge_list)
  #alphacheck(l3)


def checkSorted(seq):
  # Base case: length is 0 or 1
  if len(seq) <= 1:
    return True

  # If the first two elements of `seq` are out of order, then `seq`
  # is *not* sorted.
  if not(seq[0] <= seq[1]):
    return False

  # Recursive case: `seq` is sorted if the remainder of the sequence
  # is sorted.
  return checkSorted(seq[1:])  

def expectSorted(seq, shouldBeSorted):
  print('  expecting that', seq, 'is sorted?', shouldBeSorted)
  assert checkSorted(seq) == shouldBeSorted

#mergeMovieLists()

print('\nChecking sort() function ...')
expectSorted([], True)
expectSorted([ 'aa' ], True)
expectSorted([ 'aa', 'bb' ], True)
expectSorted([ 'bb', 'aa' ], False)
expectSorted([ 'cc', 'aa', 'bb' ], False)
expectSorted([ 'aa', 'bb', 'cc' ], True)
expectSorted([ 'aa', 'bb', 'cc', 'dd' ], True)
expectSorted([ 'aa', 'cc', 'dd', 'bb' ], False)

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
  if len(seq) <= 1:
    return True
  else:
    return False
    #knock out the other list boys

def expectSorted(seq, shouldBeSorted):
  print('  expecting that', seq, 'is sorted?', shouldBeSorted)
  assert checkSorted(seq) == shouldBeSorted

#mergeMovieLists()

print('\nChecking sort() function ...')
expectSorted([], True)
expectSorted([ 'aa' ], True)
#expectSorted([ 'aa', 'bb' ], True)
#expectSorted([ 'bb', 'aa' ], False)

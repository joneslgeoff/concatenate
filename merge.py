p1 = '/home/geoffwood/Desktop/Merger/Chris.txt'
p2 = '/home/geoffwood/Desktop/Merger/Geoff'
fp1 = open(p1)
fp2 = open(p2)
l1 = fp1.read().strip().split("\n")
l1
l2 = fp2.read().strip().split("\n")
l2
l3 = l1 + l2
l3
merge_list = sorted(l3)
print(merge_list)

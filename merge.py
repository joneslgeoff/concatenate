import os
os.chdir("/home/geoffwood/Desktop/Merger")
f = open("Chris.txt", "r")
print(f.read())
f = open("Geoff", "r")
print(f.read())
def Merge("Chris.txt", "Geoff"):
final_list = list1 + list2
final_list.sort()
return(final_list)

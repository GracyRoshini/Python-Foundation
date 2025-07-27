mark1={88,22,33}
mark2={11,22,44}

print("marks1: ",mark1)
print("marks2: ",mark2)

#1) Union: Take all unique elements of both the sets
union_set=mark1|mark2
print('Union Result: ',union_set)

#2) Intersection: Common elements from both sets
intersect_res=mark1 & mark2
print('Intersection Results: ', intersect_res)

#3) Difference: Take first set and compare with second set, display elements which are not in the set 2
diff_res=mark1 - mark2
print('Difference Result: ', diff_res)

#4) Symmentric difference: Compare with both sets and display elements which is not present in both sets
symDiff_res= mark1 ^ mark2
print("Symmetric difference Result: ",symDiff_res)








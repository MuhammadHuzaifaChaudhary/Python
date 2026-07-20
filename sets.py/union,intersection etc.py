set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# UNION - elements in either set
union = set1 | set2  # OR set1.union(set2)
print(union)  # {1, 2, 3, 4, 5, 6, 7, 8}

# INTERSECTION - elements in both sets
intersection = set1 & set2  # OR set1.intersection(set2)
print(intersection)  # {4, 5}

# DIFFERENCE - elements in set1 but not set2
difference = set1 - set2  # OR set1.difference(set2)
print(difference)  # {1, 2, 3}

# SYMMETRIC DIFFERENCE - elements in either set but not both
symmetric_diff = set1 ^ set2  # OR set1.symmetric_difference(set2)
print(symmetric_diff)  # {1, 2, 3, 6, 7, 8}

# ============================================
# c++
#  ===========================================

#  #include <set>
# #include <algorithm>
# #include <iterator>

# set<int> set1 = {1, 2, 3, 4, 5};
# set<int> set2 = {4, 5, 6, 7, 8};
# set<int> result;

# // Union
# set_union(set1.begin(), set1.end(),
#           set2.begin(), set2.end(),
#           inserter(result, result.begin()));

# // Intersection
# set_intersection(set1.begin(), set1.end(),
#                  set2.begin(), set2.end(),
#                  inserter(result, result.begin()));

# // Difference
# set_difference(set1.begin(), set1.end(),
#                set2.begin(), set2.end(),
#                inserter(result, result.begin()));

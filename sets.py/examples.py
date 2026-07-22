# Website visitor tracking
visitors_day1 = {"Alice", "Bob", "Charlie", "David"}
visitors_day2 = {"Charlie", "Eve", "Frank", "Alice"}

# Total unique visitors (union)
all_visitors = visitors_day1 | visitors_day2
print(f"Total unique visitors: {len(all_visitors)}")
print(f"All visitors: {all_visitors}")

# Visitors who came both days (intersection)
returning = visitors_day1 & visitors_day2
print(f"Returning visitors: {returning}")

# New visitors on day 2 (difference)
new_visitors = visitors_day2 - visitors_day1
print(f"New visitors: {new_visitors}")

# Visitors who came only once (symmetric difference)
one_time = visitors_day1 ^ visitors_day2
print(f"One-time visitors: {one_time}")

# ========================
# example no 2
# finding common elements in two sets
# Three lists of numbers
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [6, 7, 8, 9, 10, 11]

# Find numbers present in all three lists
common_all = set(list1) & set(list2) & set(list3)
print(f"In all lists: {common_all}")  # {6}

# Find numbers present in any list (union)
any_list = set(list1) | set(list2) | set(list3)
print(f"In any list: {any_list}")

# Find numbers present in exactly two lists
exactly_two = (set(list1) & set(list2)) | \
              (set(list2) & set(list3)) | \
              (set(list1) & set(list3))
print(f"In exactly two lists: {exactly_two}")
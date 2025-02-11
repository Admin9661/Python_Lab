set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Display the sets
print("Set A:", set_a)
print("Set B:", set_b)

# Union
union_set = set_a.union(set_b)
print("\nUnion of A and B:", union_set)

# Intersection
intersection_set = set_a.intersection(set_b)
print("Intersection of A and B:", intersection_set)

# Difference
difference_set_a_b = set_a.difference(set_b)
difference_set_b_a = set_b.difference(set_a)
print("Difference of A - B:", difference_set_a_b)
print("Difference of B - A:", difference_set_b_a)

# Symmetric Difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference of A and B:", symmetric_difference_set)

# Add an element to a set
set_a.add(6)
print("\nSet A after adding 6:", set_a)

# Remove an element from a set
set_a.remove(6)
print("Set A after removing 6:", set_a)

# Clear all elements from a set
set_a.clear()
print("Set A after clearing all elements:", set_a)

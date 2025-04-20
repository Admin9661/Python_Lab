def nearly_equal(a, b):
    if len(a) != len(b):
        return False
    count = 0
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return count == 1

print(nearly_equal("book", "boon"))
print(nearly_equal("book", "back"))

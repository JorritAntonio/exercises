def target_sum(ns, target):
    for x in ns:
        for y in ns:
            print(y)
            if x + y == target:
                return True
    return False

print(target_sum([1,2,3], 6))
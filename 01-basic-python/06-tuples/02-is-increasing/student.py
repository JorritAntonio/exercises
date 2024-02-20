def is_increasing(ns):
    ms = ns[1:]
    pairs = zip(ns,ms)
    for pair in pairs:
        if pair[0] > pair[1]:
            return False
    return True
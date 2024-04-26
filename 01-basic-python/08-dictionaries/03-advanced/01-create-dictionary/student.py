def create_dictionary(keys, values):
    d = {}
    for key, value in zip(keys, values):
        d[key] = value
    return d
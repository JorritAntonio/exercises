def keys_with_value(dict, value):
    keys = list(dict.keys())
    new_list = []
    for key in keys:
        if dict[key] == value:
            new_list.append(key)
    return new_list

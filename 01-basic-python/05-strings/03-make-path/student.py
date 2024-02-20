def make_path(parts):
    path = ""
    for part in parts:
        path += part + "/"
    return path[:-1]
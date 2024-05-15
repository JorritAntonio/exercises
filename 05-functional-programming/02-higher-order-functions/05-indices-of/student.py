def indices_of(xs, condition):
    result = []
    for x in range(len(xs)):
        if condition(xs[x]):
            result.append(x)
    return result

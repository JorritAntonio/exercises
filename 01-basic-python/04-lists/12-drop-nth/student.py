# Write your code here
def drop_nth(xs, n):
    ns = xs[:n]
    ys = xs[n+1:]
    fs = ns + ys
    return fs
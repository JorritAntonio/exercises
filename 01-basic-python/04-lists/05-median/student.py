# Write your code here
def median(ns):
    sorted_ns = sorted(ns)
    length = len(sorted_ns)
    if length % 2 != 0:
        odd_index = len(sorted_ns) // 2
        return sorted_ns[odd_index]
    even_index = (len(sorted_ns) // 2) -1
    return (sorted_ns[even_index] + sorted_ns[even_index+1]) / 2




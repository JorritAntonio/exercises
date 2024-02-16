def digit_sum(n):
    string_num = str(n)
    count = 0
    for i in range(len (string_num)):
        count += int(string_num[i])
    return count
    

def last_digit(n):
    return n % 10

def remove_last_digit(n):
    if len(str(n)) == 1:
        return 0
    return int(str(n) [0: - 1])



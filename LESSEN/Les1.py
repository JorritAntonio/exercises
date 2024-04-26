def listcomprehension():
    result = []
    """
    for i in range(10):
        if i % 2 == 0:
            result.append((i,i))
    Zo deden we het eerst maar de volgende line is exact hetzelfde als hier boven    
    """
    result = [(i,i) for i in range(10) if i % 2 ==0]

    print(result)
#listcomprehension()

def dictcomprehension():
    dictionary = {}
    """
    for i in range(10):
        if i % 2 == 0:
            dictionary[i] = i*2
    """
    dictionary = {i:[j for j in range (i)] for i in range(10) if i % 2 == 0}
    print(dictionary)
#dictcomprehension()
    

    
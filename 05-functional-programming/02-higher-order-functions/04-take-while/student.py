def take_while(xs, condition):
    result = ()
    for x in xs:
        if condition(x):
            return
        

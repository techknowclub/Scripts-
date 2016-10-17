while True:
    n= int(raw_input())
    r = float (n/2)
    while True:
        r_ = (r + (n/r))/2
        if r == r_:
            break
        r = r_
        print r_

def sig(mas):
    an=int((mas[3]+mas[2])/2)
    if (an<=5 and an>=-5):
        print("0")
        a=0
        return a
    elif (an<=-5 and an>=-30):
        print("-1")
        a=-1
        return a
    elif (an<=-30 and an>=-90):
        print("-2")
        a=-2
        return a
    elif (an<=30 and an>=5):
        print("1")
        a=1
        return a
    elif (an<=90 and an>=30):
        print("2")
        a=2
        return a
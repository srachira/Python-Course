__author__ = 'SuSh'

def position(count,end):
    if end>count or end < 1:
        print "Invalid"
        return None
    i=0
    k=0
    a=range(1, count+1)
    while len(a) > 1:
        a.remove(a[k])
        k = (k+i)%len(a)
        i+=1
    remaining=a[0]
    return (end-remaining+1)%count #1 is added to return the original element during subtraction


if __name__ == "__main__":
    assert 3 ==  position(13,11)
    assert 6 == position(15,10)
    assert 5 == position(15, 9)
    assert 4 ==  position(13,12)
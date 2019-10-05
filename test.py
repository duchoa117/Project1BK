def test( x1,  y1,  x2,  y2,  x3,  y3,  x4,  y4) :
    denominator = ((x2 - x1) * (y4 - y3)) - ((y2 - y1) * (x4 - x3));
    numerator1 = ((y1 - y3) * (x4 - x3)) - ((x1 - x3) * (y4 - y3));
    numerator2 = ((y1 - y3) * (x2 - x1)) - ((x1 - x3) * (y2 - y1));

    if (denominator == 0):
        return (numerator1 == 0 and numerator2 == 0)
    r = numerator1 / denominator;
    s = numerator2 / denominator;
    return (r >= 0 and r <= 1) and (s >= 0 and s <= 1)

if(test(0,0,1,1,0,1,1,0) and test(0,0,1,0,0,1,1,1)):
    print("ok")
else:
    print("not ok")
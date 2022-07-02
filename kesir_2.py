import math
def kesir(x, y, v=[]):
    if x%y==0: return v+[x//y]
    return kesir(y,x%y,v+[x//y])
# print(kesir(93, 8))
# print(kesir(int(math.e*10e8), 10e8))
# print(kesir(math.e, 1))
# https://matema.tk/blog/sonsuz-serilerle-e-sayisina-yakinsamak#p3_2
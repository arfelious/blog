import math
def e_yakinsama(x):
    toplam = 0
    for i in range(1,x):
        toplam += 1/math.factorial(i)
    return toplam
# print(e_yakinsama(5))
# print(e_yakinsama(10))
# print(e_yakinsama(20))
# print(e_yakinsama(100))
# https://matema.tk/blog/sonsuz-serilerle-e-sayisina-yakinsamak#p2
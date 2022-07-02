def kesir(x,k=0):
    if k==0: return 1
    return (math.floor(k/3)*2 if k%3==0 else 1)+1/kesir(x,k-1)
# print(kesir(5))
# print(kesir(10))
# print(kesir(20))
# https://matema.tk/blog/sonsuz-serilerle-e-sayisina-yakinsamak#p3_1
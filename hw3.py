def get_fixed_price(b,c):
    a=100/(100-b)*c 
    return int(a)

m = float(input('할인율은?'))
b=int(input('A 상품의 할인된 가격은?'))
Afor=get_fixed_price(m,b)
c=int(input('B 상품의 할인된 가격은?'))
Bfor=get_fixed_price(m,c)
print('A 상품의 정가는',Afor,'원')
print('B 상품의 정가는',Bfor,'원')

def buy(sb):
    print('[구입]')
    item = input('상품명?')
    if item=='':
        return False
    num = input('수량은?')
    sb[item]=num
    print(f'장바구니에 {item} {num}개가 담겼습니다\n')
def show(sb):
    print(f'\n>>>장바구니 보기: {sb}')
def find(sb):
    print('\n[검색]')
    to=input('장바구니에서 확인하고자 하는 상품은?')
    if to in sb:
        print(f'{to}은(는) {sb[to]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {to}은(는) 없습니다.')
    
    
shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)

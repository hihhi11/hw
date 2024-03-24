def get_integer(f):
    u=int(input(f))
    return u
def exchange(i):
    q= i//500
    w= i%500//100
    e= i%500%100//50
    r= i%500%100%50//10
    print('500원 동전의 개수:',q)
    print('100원 동전의 개수:',w)
    print('50원 동전의 개수:',e)
    print('10원 동전의 개수:',r)

m=get_integer('동전으로 교환하고자 하는 금액은?')
p= exchange(m)

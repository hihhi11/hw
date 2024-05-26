import os
import pickle

def input_score():
    score=[]
    n=1
    i=0
    while True:
        if i >=0:
            i=int(input(f'#{n}?'))
            score.append(i)
            n+=1
        else:
            break
    return score
    
def get_average(rs):
    su=0
    for i in range(len(rs)-1):
        su+= rs[i]
    ave =su/(len(rs)-1)
    return ave
def show_scores(rs):
    print(f'[점수출력]\n개인점수: ', end='')
    for i in range(len(rs)-1):
        print(f'{rs[i]}',end = ' ')
def save(sc):
    with open('score.bin', 'wb') as file:
        pickle.dump(sc, file)
def load():
    with open('score.bin', 'rb') as file:
        a=pickle.load(file)
        return a

if os.path.exists('score.bin'):
    print('파일읽기\n')
    rs = load()
    ave= get_average(rs)
    
else:
    print('[점수입력]')    
    rs=input_score()    
    ave= get_average(rs)

show_scores(rs)
print(f'\n평균: {ave:.1f}')
save(rs)

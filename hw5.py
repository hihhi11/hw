def read_single_digit(s):
    if s==0:
        return '영'
    elif s==1:
        return '일'
    elif s==2:
        return '이'
    elif s==3:
        return '삼'
    elif s==4:
        return '사'
    elif s==5:
        return '오'
    elif s==6:
        return '육'
    elif s==7:
        return '칠'
    elif s==8:
        return '팔'
    elif s==9:
        return '구'
    
def read_numver(h,g):
    c= int(h[g])
    return read_single_digit(c)
    
num=input('세 자리 정수 입력:')
a=read_numver(num,0)
b=read_numver(num,1)
c=read_numver(num,2)
print(a,b,c)

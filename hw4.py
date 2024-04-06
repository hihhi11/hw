def rep_char(a,b):
    print(a*b)

def draw_line_string(a):
    msg1=f'Hello {a},'
    msg2='Welcome to Seoul.'
    nstr=len(msg1)if(len(msg1)>len(msg2)) else len(msg2)
    rep_char('-',nstr+2)
    print(f' {msg1} ')
    print(f' {msg2} ')
    rep_char('-',nstr+2)


a=draw_line_string(input('Input his/her name:'))

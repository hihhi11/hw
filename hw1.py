def get_radius(prompt):
    r = int(input(prompt))
    return r
def get_circle_area(e):
    u=(e*e*3.14)
    return u
pt=('넓이를 구하고자 하는 원의 반지름은?')
m = get_radius(pt)
area_1 = get_circle_area(m)
print('반지름', m, '인 원의 넓이','= 3.14','*',m,'*', m,'=',area_1)

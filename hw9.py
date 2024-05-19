class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__lt=(x1,y1)
        self.__rb=(x2,y2)

    def show(self):
        print(f'좌측 상단 꼭지점이{self.__lt}이고 우측 상단 꼭지점이{self.__rb}인 사각형 입니다.', end = '')
    def getWidth(self):
        self.__w= self.__rb[0] - self.__lt[0]
        return self.__w
    def getHeight(self):
        self.__h = self.__rb[1] - self.__lt[1]
        return self.__h
    def getArea(self):
        return self.__w*self.__h
    def getPerimeter(self):
        return (self.__w+self.__h)*2


r1 = Rectangle(5, 5, 20, 10)
w = r1.getWidth()
h = r1.getHeight()
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')

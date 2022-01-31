class Vector: 

    def __init__(self, *args):
         self.values = []
         for arg in args:
            if isinstance(arg, int):
                self.values.append(arg)

    def __str__(self):
        if self.values == []:
            return 'Пустой вектор'
        else:
            self.values.sort()
            self.values = tuple(self.values)
            return f'Вектор{"".join(str(self.values))}'


a = Vector(1,2.2, 4, 5, 3, 0, 6.7)
print(a)
b = Vector()
print(b)

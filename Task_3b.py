# Б)
# Добавьте в класс Stationary метод класса set_color, который присваивает атрибут класса Stationary color;
# Вызовете метод set_color и установите color='yellow';
# Вызовете атрибуты color у классов Pen, Pencil, Handle. Что вы наблюдаете?

class Stationary:
    def __init__(self):
        pass
    @classmethod
    def set_color(cls, color):
        cls.color = color

a = Stationary()
Stationary.set_color('yellow')

class Pen(Stationary):
    def __init__(self):
        pass
    def info(self):
        print(f"Цвет: {self.color}")

class Pencil(Stationary):
    def __init__(self):
        pass

class Handle(Stationary):
    def __init__(self):
        pass

pencil = Pencil()
print(pencil.color)

pen = Pen()
print(pen.color)

handle = Handle()
print(handle.color)
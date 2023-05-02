# А) Реализовать класс Stationery (канцелярия):
# определить в нём атрибут title (название) и абстрактный метод draw (отрисовка);
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в классу Pen добавьте атрибут color = 'blue';
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение, например: "Ручка пишет";
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# A)
from abc import ABC, abstractmethod
class Stationery:
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def draw(self):
        pass

class Pen(Stationery):
    def __init__(self, title, color = 'blue'):
        super().__init__(title)
        self.color = color
    def info(self):
        print(f"Название канцелярии: {self.title}")
        print(f"Цвет: {self.color}")
    def draw(self):
        print("Ручка пишет")

class Pencil(Stationery):
    def draw(self):
        print("Карандаш чертит")

    def info(self):
        print(f"Название канцелярии: {self.title}")

class Handle(Stationery):
    def draw(self):
        print("Маркер рисует")

    def info(self):
        print(f"Название канцелярии: {self.title}")

pen = Pen('Ручка')
pen.info()
pen.draw()

print("----------------------------")

pencil = Pencil('Карандаш')
pencil.info()
pencil.draw()

print("----------------------------")

handle = Handle('Маркер')
handle.info()
handle.draw()

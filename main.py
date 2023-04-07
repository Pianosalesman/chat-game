from enum import Enum
import random


class TrafficMixin(object):  # Миксин с движением. Можно ли в миксине инициировать параметры с количеством
    # метров, объектом и id объекта. Непонятно, как это должно выглядеть. При каждом вызове объекта должно высвечиваться
    # сообщение о перемещении объекта?

    def __init__(self, number_metres, id, object):
        self.object = object
        self.number_metres = number_metres
        self.id = id(self.object)

    def to_str(self):  # Функция передачи параметров миксина в строку
        print(f"Объект {self.object} {self.id} переместился на {self.number_metres} метров")


@property # Как я понял свойство объекта вызывается декоратором property. Но одновременно moving smoke должен
# должен выводить объект дым. Может ли применяться @property к классу?
class MovingSmoke(TrafficMixin):  # Объект с движущимся дымом. Есть вопрос как грамотно примешать mixin
    # к классу
    def __init__(self, square):
        super().__init__()
        super().to_str()
        self.square = square


class BasicAuto(TrafficMixin):  # Инициализация движущегося авто с дымом в методе "car_explosion"
    def __init__(self, name, life=10):
        self.name = name
        self.life = life

    def make_damage(self, damage):
        self.life = self.life - damage # Непонятно
        # как здесь корректно вызвать деструктор. Пробовал вызывать деструктор через if - цикл не сработал.

    def car_explosion(self):
        random_smoke = random.randint(1, 5)
        print(f"Машина {self.name} взорвалась с количеством дыма {random_smoke}. Дымом покрылась площадь")


class MilitaryAuto(Enum): # Не очень опять как из метода здесь вывести экземпляр метода и как параметр Enum попадет
    # в f' строку
    MACHINE_GUN = 2
    HEAVY_MACHINE_GUN = 5
    GRENADE_LAUNCHER = 10

    def shooting(self):
        print(f'Произошла стрельба из {Enum} по "Имя автомобиля". '
              f'Причинен ущерб {self.name} в размере {damage}. Оставшиеся очки жизни - {self.life}")')


class PeacefulAuto(BasicAuto): # Не понятно, как переопределять деструктор и как он вообще связан с количеством
    # пассажиров
    def __init__(self, numbers_passenger, name):
        super().__init__(name)
        self.numbers_passenger = numbers_passenger


if __name__ == '__main__':
    MilitaryAuto = Enum('Military car', ['MACHINE_GUN', 'HEAVY_MACHINE_GUN', 'GRENADE_LAUNCHER'])
    peaceful_car1 = PeacefulAuto(7, 'Hummer')
    peaceful_car1.make_damage(5)

# peaceful_car2 = BasicAuto('Honda')
# peaceful_car1.make_damage(5)
# peaceful_car1.car_explosion()
# smoke = MovingSmoke(4, peaceful_car1, 7)

# print(peaceful_car1)
# peace_car = PeacefulAuto("Lada", 10)
# print(peace_car)
# del peace_car
# peaceful_car1.make_damage(8)
# peaceful_car1.make_damage(1)
# peaceful_car1.car_explosion()
'''
    def make_destruction(self):
        if self.life == 0:
            del peaceful_car1
            print('Car was destroyed')

    def explosion(self):
        ааа
'''
"""
hummer = BasicAuto("Hummer")
peaceful_car1 = BasicAuto("Peaceful_car1")
peaceful_car2 = BasicAuto("Peaceful_car2")
peaceful_car3 = BasicAuto("Peaceful_car3")


class MilitaryAuto(BasicAuto, Enum):
    MACHINE_GUN = 2
    HEAVY_MACHINE_GUN = 5
    GRENADE_LAUNCHER = 10

    def get_damage(self):
        pass


class PeacefulAuto(BasicAuto):
    pass


if __name__ == "__main__":
    car = BasicAuto("Lada", 10)
    print(car.life)
"""

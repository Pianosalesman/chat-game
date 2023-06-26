import enum
import random
import uuid


class TrafficMixin:  # Миксин движущихся объектов
    def move(self, number_metres):
        self.number_metres = number_metres
        self.id = uuid.uuid4()
        print(f"Объект {self.id} переместился на {self.number_metres} метров")


class MovingSmoke(TrafficMixin):  # Движущийся дым
    def __init__(self):
        self.square = random.randint(1, 5)  # Случайный дым

    @property  # Площадь дыма
    def square_smoke(self):
        return self.square


class BasicAuto(TrafficMixin):  # Класс движущегося авто

    def __init__(self, name, life=10):
        self.name = name
        self.life = life

    def car_explosion(self):  # Взрыв автомобиля
        smoke = MovingSmoke()
        print(f"Машина {self.name} взорвалась. Дымом покрылась площадь {smoke.square_smoke}")

    def __del__(self):
        pass


class MilitaryAuto(BasicAuto):  # Класс для военной машины
    Weapon = enum.Enum('Weapon', [('MACHINE_GUN', 2), ('HEAVY_MACHINE_GUN', 5), ('GRENADE_LAUNCHER', 10)])
    Machine_gun = Weapon['MACHINE_GUN']
    Grenade_launcher = Weapon['GRENADE_LAUNCHER']

    def shooting(self, target: 'BasicAuto'):  # Метод для стрельбы
        target.life -= self.Machine_gun.value
        print(f"Произошла стрельба из {self.Machine_gun}"
              f" по {target.name}")


class PeacefulAuto(BasicAuto):  # Класс для мирного авто

    def __init__(self, number_passengers, name, life):
        super().__init__(name, life)
        self.number_passengers = number_passengers

    def __del__(self):  # Переопределенный деструктор для подсчета количества убитых пассажиров
        super().__del__()
        if self.life <= 0:
            print(f"Было уничтожено {self.number_passengers} пассажиров")


if __name__ == '__main__':
    peaceful_car1 = PeacefulAuto(4, 'Ford', life=10)
    peaceful_car2 = PeacefulAuto(3, 'Lada', life=10)
    peaceful_car3 = PeacefulAuto(5, 'Opel', life=10)

    peaceful_car1.move(6)
    peaceful_car2.move(15)
    peaceful_car3.move(25)

    Hummer = MilitaryAuto('Hummer')
    Hummer.shooting(peaceful_car1)
    Hummer.shooting(peaceful_car2)
    peaceful_car3.__setattr__('life', 0)

    car_list = [peaceful_car1, peaceful_car2, peaceful_car3]
    for car in car_list:
        if car.life <= 0:
            car.car_explosion()
            car_list.remove(car)
            break

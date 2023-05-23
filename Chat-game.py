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

    def make_damage(self, damage):  # Метод причинения ущерба
        self.life -= damage
        return self.life

    def __del__(self):  # Деструктор, вызывающий взрыв
        if self.life <= 0:
            self.car_explosion()

    def car_explosion(self):  # Взрыв автомобиля
        smoke = MovingSmoke()
        print(f"Машина {self.name} взорвалась. Дымом покрылась площадь {smoke.square_smoke}")


class MilitaryAuto(enum.Enum):  # Класс для военной машины
    MACHINE_GUN = 2
    HEAVY_MACHINE_GUN = 5
    GRENADE_LAUNCHER = 10

    def shooting(self):  # Метод для стрельбы
        car.make_damage(self.HEAVY_MACHINE_GUN.value)  # Передача урона в зависимости от типа оружия
        print(f"Произошла стрельба из {self.HEAVY_MACHINE_GUN.name}"
              f" по {car.name}")


class PeacefulAuto(BasicAuto):  # Класс для мирного авто

    def __init__(self, number_passengers, name, life):
        super().__init__(name, life)
        self.number_passengers = number_passengers

    def __del__(self):  # Переопределенный деструктор для подсчета количества убитых пассажиров
        super().__del__()
        if self.life <= 0:
            print(f"Было уничтожено {self.number_passengers} пассажиров")


if __name__ == '__main__':
    car = BasicAuto(name=str)
    peaceful_car1 = PeacefulAuto(4, 'Ford', life=10)
    peaceful_car1.move(6)
    peaceful_car2 = PeacefulAuto(3, 'Lada', life=10)
    peaceful_car2.move(15)
    peaceful_car3 = PeacefulAuto(5, 'Opel', life=10)
    peaceful_car3.move(25)
    peaceful_car3.make_damage(10)

    Hummer = MilitaryAuto.HEAVY_MACHINE_GUN
    Hummer.shooting()

# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class House:
    def _init_(self, floors: int, architector: str):
        """
        Подготавливаем и создаем класс домов

        :param floors: количество этажей
        :param architector: количество этажей

        Примеры:
        >>> house1 = House(22, "morozov") # инициализация экземпляра класса
        """
        if not isinstance(floors, int):
            raise TypeError("Введено либо не целое число либо вообще не число")
        if floors <= 0:
            raise ValueError("Введено число меньше нуля")
        self.floors = floors

        if not isinstance(architector, str):
            raise TypeError("Введен не текст")
        self.architector = architector

    def add_under_level(self, levels: int, under_levels: int):
        """
        Функция, которая добавляют к числу этажей, подземные этажи
        :param levels: количество этажей
        :param under_levels: количество подземных этажей
        :return: общее количество этажей
        Пример:
        >>> house1 = House(22, "morozov")
        >>> house1.add_under_level(22, 2)
        """
        if not isinstance(levels, int):
            raise TypeError("Введено либо не целое число либо вообще не число")
        if not isinstance(under_levels, int):
            raise TypeError("Введено либо не целое число либо вообще не число")
        if levels < 0:
            raise ValueError("Введено число меньше нуля")
        if under_levels < 0:
            raise ValueError("Введено число меньше нуля")
        ...


class Human:
    def _init_(self, age: int, height: int):
        """
        Подготавливаем и создаем класс персон

        :param age: количество лет
        :param height: рост

        Примеры:
        >>> human1 = Human(26, 180) # инициализация экземпляра класса
        """
        if not isinstance(age, int):
            raise TypeError("Введено либо не целое число либо вообще не число")
        if age <= 0:
            raise ValueError("Введено число меньше нуля")
        self.age = age

        if not isinstance(height, int):
            raise TypeError("Введено либо не целое число либо вообще не число")
        if height <= 0:
            raise ValueError("Введено число меньше нуля")
        self.height = height

    def is_old(self, age_: int, old_age: int) -> bool:
        """
        Функция, которая определяет, старый человек или нет

        :return: старый ли человек
        :param age_: возраст
        :param old_age: возраст с которого человек старый

        Пример:
        >>> human1 = Human(26, 180)
        >>> human1.is_old()
        """
        if not isinstance(age_, int):
            raise TypeError("Введено либо не целое число либо вообще не число")
        if age_ <= 0:
            raise ValueError("Введено число меньше нуля")
        self.age_ = age_

        if not isinstance(old_age, int):
            raise TypeError("Введено либо не целое число либо вообще не число")
        self.old_age = old_age
        ...


class Car:
    def _init_(self, wheels: int, colour: str):
        """
        Подготавливаем и создаем класс машин

        :param wheels: количество колес
        :param colour: цвет

        Примеры:
        >>> car1 = Car(4, "red") # инициализация экземпляра класса
        """
        if not isinstance(wheels, int):
            raise TypeError("Введено либо не целое число либо вообще не число")
        if wheels <= 0:
            raise ValueError("Введено число меньше нуля")
        self.wheels = wheels

        if not isinstance(colour, str):
            raise TypeError("Введен не текст")
        self.colour = colour

    def is_new(self, made_age: int, new_age: int) -> bool:
        """
        Функция, которая определяет, новая машина или нет

        :return: новая ли машина
        :param made_age: год создания машины
        :param new_age: год с которого машина считается новой

        Пример:
        >>> car1 = Car(4, "red")
        >>> car1.is_new()
        """
        if not isinstance(made_age, int):
            raise TypeError("Введено либо не целое число либо вообще не число")
        if not isinstance(new_age, int):
            raise TypeError("Введено либо не целое число либо вообще не число")
        if made_age < 0:
            raise ValueError("Введено число меньше нуля")
        if new_age < 0:
            raise ValueError("Введено число меньше нуля")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
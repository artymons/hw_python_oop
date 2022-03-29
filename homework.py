from dataclasses import asdict, dataclass
from typing import ClassVar, Dict, List, Tuple, Type, Union


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    speed: float
    distance: float
    duration: float
    calories: float
    INFO: (ClassVar
           [Tuple[Union
            [str, float], ...]]) = ('Тип тренировки: {training_type}; '
                                    'Длительность: {duration:.3f} ч.; '
                                    'Дистанция: {distance:.3f} км; '
                                    'Ср. скорость: {speed:.3f} км/ч; '
                                    'Потрачено ккал: {calories:.3f}.')

    def get_message(self) -> str:
        """Возвращаем сообщение о тренировке."""
        return self.INFO.format(**asdict(self))


@dataclass
class Training:
    """Базовый класс тренировки."""

    M_IN_KM: ClassVar[float] = 1000
    LEN_STEP: ClassVar[float] = 0.65
    MIN_IN_HOUR: ClassVar[float] = 60
    action: int
    duration: float
    weight: float

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = self.get_distance()
        return distance / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def training_type(self) -> str:
        """Возвращает тип."""
        return type(self).__name__

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        distance = self.get_distance()
        duration = self.duration
        training_type = self.training_type()
        return InfoMessage(training_type, speed, distance, duration, calories)


@dataclass
class Running(Training):
    """Тренировка: бег."""

    COEF_FOR_CAL_RUN_1: ClassVar[float] = 18
    COEF_FOR_CAL_RUN_2: ClassVar[float] = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        time_in_min = self.duration * self.MIN_IN_HOUR
        average_speed = self.get_mean_speed()
        return ((self.COEF_FOR_CAL_RUN_1
                * average_speed - self.COEF_FOR_CAL_RUN_2)
                * self.weight / self.M_IN_KM * time_in_min)


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    COEF_FOR_CAL_WALK_1: ClassVar[float] = 0.035
    COEF_FOR_CAL_WALK_2: ClassVar[float] = 0.029
    height: float

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        time_in_min = self.duration * self.MIN_IN_HOUR
        average_speed = self.get_mean_speed()
        return ((self.COEF_FOR_CAL_WALK_1 * self.weight
                + (average_speed**2 // self.height)
                * self.COEF_FOR_CAL_WALK_2 * self.weight) * time_in_min)


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""

    COEF_FOR_CAL_SWIM_1: ClassVar[float] = 1.1
    COEF_FOR_CAL_SWIM_2: ClassVar[float] = 2
    LEN_STEP: ClassVar[float] = 1.38
    length_pool: float
    count_pool: float

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        average_speed = self.get_mean_speed()
        return ((average_speed + self.COEF_FOR_CAL_SWIM_1)
                * self.COEF_FOR_CAL_SWIM_2 * self.weight)


def read_package(workout_type: str, data: List[float]) -> Training:
    """Прочитать данные полученные от датчиков."""
    type_dict: Dict[str, Type[Training]] = {'SWM': Swimming,
                                            'RUN': Running,
                                            'WLK': SportsWalking}
    if workout_type in type_dict.keys():
        type_dict[workout_type](*data)
    else:
        print(f'ValueError - {workout_type}. '
              f'You can enter one of these values: {type_dict.keys()}')
    return type_dict[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    return print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

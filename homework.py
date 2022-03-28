from dataclasses import dataclass, asdict
from typing import Dict, List, Type


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    speed: float
    distance: float
    duration: float
    calories: float
    INFO: Dict[str, float] = ('Тип тренировки: {training_type}; '
                              'Длительность: {duration:.3f} ч.; '
                              'Дистанция: {distance:.3f} км; '
                              'Ср. скорость: {speed:.3f} км/ч; '
                              'Потрачено ккал: {calories:.3f}.')

    def get_message(self) -> str:
        """Возвращаем сообщение о тренировке."""

        return self.INFO.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""

    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        distance = self.get_distance()
        speed = distance / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        pass

    def training_type(self) -> str:
        """Возвращает тип."""

        name = type(self).__name__
        return name

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        distance = self.get_distance()
        duration = self.duration
        training_type = self.training_type()
        info = InfoMessage(training_type, speed, distance, duration, calories)
        return info


@dataclass
class Running(Training):
    """Тренировка: бег."""

    action: int
    duration: float
    weight: float

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        coef_for_cal_run_1 = 18
        coef_for_cal_run_2 = 20
        time_in_min = self.duration * 60
        average_speed = self.get_mean_speed()
        calories = ((coef_for_cal_run_1 * average_speed - coef_for_cal_run_2)
                    * self.weight / self.M_IN_KM * time_in_min)
        return calories


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    action: int
    duration: float
    weight: float
    height: float

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        coef_for_cal_wal_1 = 0.035
        coef_for_cal_wal_2 = 0.029
        time_in_min = self.duration * 60
        average_speed = self.get_mean_speed()
        calories = ((coef_for_cal_wal_1 * self.weight
                     + (average_speed**2 // self.height)
                     * coef_for_cal_wal_2 * self.weight) * time_in_min)
        return calories


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38
    action: int
    duration: float
    weight: float
    length_pool: float
    count_pool: float

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        average_speed = (self.length_pool * self.count_pool
                         / self.M_IN_KM / self.duration)
        return average_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        coef_for_cal_swi_1 = 1.1
        coef_for_cal_swi_2 = 2
        average_speed = self.get_mean_speed()
        calories = ((average_speed + coef_for_cal_swi_1)
                    * coef_for_cal_swi_2 * self.weight)
        return calories


def read_package(workout_type: str, data: List[float]) -> Training:
    """Прочитать данные полученные от датчиков."""

    type_dict: Dict[str, Type[Training]] = {'SWM': Swimming,
                                            'RUN': Running,
                                            'WLK': SportsWalking}
    training_class = type_dict[workout_type](*data)
    return training_class


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

# Модуль фитнес-трекера

### Описание
Программный модуль фитнес-трекера, который обрабатывает данные для трех видов тренировок: для бега, спортивной ходьбы и плавания.

Этот модуль
* принимает от блока датчиков информацию о прошедшей тренировке,
* определяет вид тренировки,
* рассчитывает результаты тренировки,
* выводит информационное сообщение о результатах тренировки.

### Запуск проекта на Linux
Клонировать проект c GitHub
```
git clone git@github.com:boginskiy/fitness-tracker.git
```
Установить виртуальное окружение venv
```
python3 -m venv venv
```
Активировать виртуальное окружение venv
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
Запуск
```
python3 homework.py
```

### **Дополнительные сведения**
Вывод программы (по умолчанию)
```
Тип тренировки: Swimming; Длительность: 1.000 ч.; Дистанция: 0.994 км; Ср. скорость: 1.000 км/ч; Потрачено ккал: 336.000.
Тип тренировки: Running; Длительность: 1.000 ч.; Дистанция: 9.750 км; Ср. скорость: 9.750 км/ч; Потрачено ккал: 699.750.
Тип тренировки: SportsWalking; Длительность: 1.000 ч.; Дистанция: 5.850 км; Ср. скорость: 5.850 км/ч; Потрачено ккал: 157.500.
```
Коды тренировок: 
* SWM — Плавание
* RUN — Бег
* WLK — Спортивная ходьба

Конструктор каждого из классов получает информацию с датчиков:
* action — количество совершённых действий (число шагов при ходьбе и беге либо гребков — при плавании);
* duration — длительность тренировки (час);
* weight — вес спортсмена (кг).

Дополнительно вводимые параметры:
* length_pool — длина бассейна в метрах (вводится только для 'SWM');
* count_pool — сколько раз пользователь переплыл бассейн  (вводится только для 'SWM');
* height — рост спортсмена (вводится только для 'WLK').

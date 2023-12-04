# Практическое задание №1
__Выполнил:__ *Домченко Максим*

__Студент группы:__ *РИМ-130962*

__Задача:__ *Поиск объектов в изображение по названию*

__Описание:__

* Выбрана обученная модель `google/owlvit-base-patch32`
с сайта [huggingface.co](https://huggingface.co/google/owlvit-base-patch32)
* Модель принимает на вход изображение и название объекта(объектов) которое необходимо найти
* На выходе модель отдаёт массив найденных объектов, каждый объект содержит:
  * `score` - вероятность определения объекта
  * `label` - название объекта
  * `box` - координаты квадрата в котором найден объект на изображении

__Варианты использования:__
* Определение количества машин на парковке
* Определение животных в кадре
* Поиск предметов на конвейере
* Поиск запрещенных объектов

__Запуск:__
* Перейти в папку domchenko `cd ./practice_1/domchenko/`
* Подготовить окружение (_виртуальная среда, установка пакетов_) командой `make deps`
* Запустить командой `make run`

Дополнительные команды описаны в `Makefile`

Для систем в которых отсутствует утилита `make`, запуск можно выполнить путём выполнения содержимого соответствующих команд описанных в `Makefile`
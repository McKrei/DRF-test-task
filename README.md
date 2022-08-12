## Задача
1. Создать модель для справочника "Цвета".
2. Создать модель для справочника "Марки автомобилей"
3. Создать модель для справочника "Модели автомобилей"
4. Создать модель для хранения заказов авто. Заказ должен включать в себя цвет, модель, количество, дату (по умолчанию текущая).
5. С использованием библиотеки Django Rest Framework создать RestAPI для управления справочниками и заказами. API должно реализовать операции CRUD для моделей, а также чтение списков.
API для списка заказов должен возвращать элементы со след. атрибутами: дата заказа, цвет, марка авто, модель авто, количество.

Доп. требования:

1. Реализовать поддержку постраничного вывода списка заказов (объем страницы 10 элементов), реализовать сортировку списка заказов по количеству, реализовать фильтрацию списка заказов по марке авто
2. Обеспечить пользовательское представление API в формате OpenApi (Swagger).
3. Реализовать API для получения след. информации: список цветов с указанием количества заказанных авто каждого цвета (атрибуты элементов: цвет, количество), список марок с указанием количества заказанных авто каждой марки (атрибуты элементов: марка, количество)

## Запуск проекта.

1. Клонировать репозиторий
2. Заполни файл config/conf.py
3. Создать виртуальное окружение и установить зависимости:
    * pip install -r requirements.txt
4. Установить миграции для БД


*API http://127.0.0.1:8000/api/v1/*

*Документация http://127.0.0.1:8000/swagger/*

## Время и сложности
Планировал закончить за 4 часа, по факту 7

В первый раз работал с DRF, поэтому долго осваивался и по итогу потратил время на переопределение метода list в ModelViewSet и на настройку фильтра. Пришлось несколько раз переделать.

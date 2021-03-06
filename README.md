# Куда пойти — Москва глазами Артёма

Cайт о самых интересных местах в Москве.

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](.gitbook/assets/site.png)

[Демка сайта](http://kosmostars7403.pythonanywhere.com).

## Как запустить

1. Скачайте код

2. Для работы сайта необходим установленный интерпретатор Python3. Затем загрузите зависимости с помощью "pip"
(либо "pip3", в случае конфликтов с Python2):
```
pip install -r requirements.txt
```
3. Создать миграции
```bash
$ python manage.py makemigrations
```
4. Применить миграции
```bash
$ python manage.py migrate
```
5. Запустите веб-сервер:

```bash
$ python manage.py runserver
```

6. Откройте сайт в браузере по адресу [127.0.0.0:8000](http://127.0.0.0:8000)

## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![debug mode](.gitbook/assets/debug-option.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки
удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.

## Формат данных

Фронтенд получает данные из двух источников. Первый источник — это JSON, который собирается в файле views.py в папке
where_to_go. Он содержит полный список объектов на карте. И он прячется внутри тега `script`, попадает на index.html
с помощью `{{ places_geojson|json_script:"places-geojson" }}` на 44 строке шаблона.

При загрузке страницы JS код ищет тег с id `places-geojson`, считывает содержимое и помещает все объекты на карту.

Данные записаны в [формате GeoJSON](https://ru.wikipedia.org/wiki/GeoJSON). Все поля здесь стандартные,
кроме `properties`. Внутри `properties` лежат специфичные для проекта данные:

* `title` — название локации
* `placeId` — уникальный идентификатор локации, строка или число
* `detailsUrl` — адрес для скачивания доп. сведений о локации в JSON формате

Значение поля `placeId` может быть либо строкой, либо числом. Само значение не играет большой роли, важна лишь чтобы
оно было уникальным. Фронтенд использует `placeId` чтобы избавиться от дубликатов — если у двух локаций одинаковый
`placeId`, то значит это одно и то же место. В данном случае параметр берется из `id` модели места в базе данных.

Второй источник данных — это те самые адреса в поле `detailsUrl` c подробными сведениями о локации. Каждый раз, когда
пользователь выбирает локацию на карте JS код отправляет запрос на сервер и получает картинки, текст и прочую
информацию об объекте. Формат ответа сервера такой:

```
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

## Работа с админ-панелью

Для того, чтобы начать работу с базой данных контента на сайте вам нужно провести ряд стандартных для джанго
приложения процедур.

1. Создать суперпользователя
```bash
$ python manage.py createsuperuser
```
2. Придумать логин, написать адрес почты(опционально), дважды ввести пароль
3. Перейти по адресу *адрес сайта*/admin
4. Ввести созданные данные суперпользователя

Админ-панель позволяет добавлять новые интересные места. Переходите в Places и нажимайте создать новый.
Здесь вы можете заполнить информацию о месте. (Обязательные поля выделены жирным шрифтом)
Ниже представлен удобный интерфейс загрузки изображений. После загрузки вы можете свободно менять местами изображениы
просто перетаскивая их за левую часть карточки. Тем самым меняется их порядок в базе данных.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).


# DIPLOMA PROJECT Uranov Anton

### Настройка (for linux):
1. git clone https://github.com/antuanuran/DIPLOM
2. Переходим в корень Проекта и создаем вортуальное окружение: **python3 -m venv .venv**
3. Активируем виртуальное окружение: **source .venv/bin/activate**
4. **pip install -r requirements.txt**
5. **sudo apt install make**  *(если не установлен "make")*
6. **make run**  *(запускается докер с Базой данных, миграции, создается superuser)*

### Запрашиваемые данные для superuser:
- **email:** admin@admin.org (пример для ввода)
- **password** (2 раза): admin
- sure y/n (подтверждение, если пароль ненадежный)

### Импорт данных осуществляется разными способами:
- вариант 1: загрузка напрямую через консоль (указывая путь к файлам и id superuser):<br>**python manage.py import_data data_all/import_2.yaml --owner_id 1**
- вариант 2: загрузка вручную через Админку http://localhost:8000/admin/ <br>**(вендор->категория->продукт->товар)**
- вариант 3: загрузка через API (описание ниже)

### Работа с API:
**Все ссылки на API работают на swagger:** http://127.0.0.1:8000/docs/swagger/ , но в файле requests.http продублированы (описание ниже)
1. Создаем Токен от имени нашего созданного Суперюзера (email / password)<br>***(1-10 строка в requests.http)***
2. Вариант загрузки через прямую ссылку с указанием названия файла из нашей папки (предварительно поставить галочку у нашего юзера - is_vendor)<br>***(13-16 строка в requests.http)***
3. Вариант загрузки через **Postman**, выбрав файл на компьютере напрямую<br>***(20-27 строка в requests.http)***
4. Просмотр всех имеющихся загруженных товаров (возможен без авторизации)<br>***(31-32 строка в requests.http)***
5. Отправка конкретного товара в **Корзину** указав **id_tovara** и **количество**<br>***(36-44 строка в requests.http)***
6. Отправка всех товаров из Корзины в Заказ без указания доп.параметров (одним кликом)<br>***(48-51 строка в requests.http)***
7. Изменение статуса заказа на "отменен".<br>***(54-61 строка в requests.http)***
8. Просмотры товаров в корзине (товаров, относящихся к конкретному пользователю)<br>***(67-70 строка в requests.http)***
9. Просмотр товаров в заказе (товаров, относящихся к конкретному пользователю)<br>***(73-76 строка в requests.http)***
10. Дополнительно: Просмотр товаров с фильтрацией и пагинацией<br>***(80-89 строка в requests.http)***
11. Дополнительно: Создание и проверка юзера<br>***(92-106 строка в requests.http)***

### Валидация и проверки (для информации)
- Загрузка данных из файлов через API возможна только у авторизованного Юзера с активным Boolean **(is_vendor:True)**, который выставляется в Админке.
По умолчанию все созданные Юзеры создаются с **"неактивным" is_vendor**
- В случае, если мы отправляем в Корзину товары в количестве, превышающем реальное количество на складе - сработает **Validation**
- В случае, если товар в какой-то момент больше не используется, то мы убираем галочку в Админке **(is_active)**, после чего данный товар нельзя отправить в корзину и нельзя отправить из Корзины в Покупки. Но при этом в Оформленных ранее заказах данный товар останется, чтобы сохранялась история покупок.
- При просмотре товаров Корзины / Заказов, выводится список относящийся только к данному пользователю
- Загружать данные в систему через файлы (csv, yaml и yml) может только Юзер с активной галочкой is_vendor

### Swagger
- Все вышеуказанные ссылки определены по адресу: http://127.0.0.1:8000/docs/swagger/
- При создании Токена через Swagger **(первая ссылка "/auth/jwt/create/"):**<br>вводится email / password и копируется Токен по ключу: "access".<br>Затем при авторизации указывается префикс: JWT. Пример:https://yapx.ru/album/W0M9w
- Все оставшиеся ссылки работают аналогично описанным выше

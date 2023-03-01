# REST API публичной библиотеки электронных книг
По адресу /api/ предоставляет описание API и доступ к CRUD-операциям записей об авторах и книгах без авторизации.
По адресу /swagger/ расположена документация на API.

## Установка и запуск
Запуск приложения осуществляется после клонирования репозитория и установки необходимых библиотек.

- Клонируйте проект:
```
git clone https://github.com/AlexEmelianov/Django-library-api.git
```
- Установите зависимости:
```
pip install -r requirements.txt
```
- Создайте и примените миграции:
```
python manage.py makemigrations
python manage.py migrate
```
- Создайте учетную запись суперпользователя:
```
python manage.py createsuperuser
```
- Для тестирования установите фикстуры:
```
python manage.py loaddata fixtures.json
```
- Запустите приложение с указанием порта:
```
python manage.py runserver <порт>
```
## Автор проекта
Алексей Емельянов — Python developer
- Telegram: @emelianov_alex
- e-mail: emelyanov000@gmail.com

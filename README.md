### Название. "Тестовое задание"
### Описание. Что это за проект:
Проект предназначен для публикации текстовых постов.
Пользователи могут читать чужие посты без регистрации, а также после регистрации появляется возможность самостоятельно публиковать посты с возможностью добавления одного изображения.
В проекте присутствуют возможности редактирования и удаления собственных постов.

### Примерная спецификация программ проекта:

```
Backend:
Django
pillow
python 3.12

DB:
SQLite3
```
### Как запустить проект:  
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Aleksandr-Bystrov/metro_test.git
```

```
cd metro_test
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Запустить тесты проекта:

```
python3 manage.py test
```

### Автор проекта:

Разработал: Александр Быстров, в рамках выполнения тестового задания для Московского метро

[Aleksandr_Bystrov](https://github.com/Aleksandr-Bystrov)

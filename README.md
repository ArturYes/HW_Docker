<h3 align="center">Сервис онлайн-образования на Django</h3>

<details>
  <summary>Оглавление</summary>
  <ol>
    <li>О проекте</li>
    <li>Технологии</li>
    <li>Настройка проекта</li>
    <li>Использование</li>
    <li>Контакты</li>
  </ol>
</details>



## О проекте

Сервис онлайн-образования.

## Технологии
- Django
- PostgreSQL
- DRF


## Настройка проекта

Для работы с проектом произведите базовые настройки.

### 1. Клонирование проекта

Клонируйте репозиторий используя следующую команду.
  ```sh
  git clone git@github.com:ArturYes/HW_Docker.git
  ```


### 2. Настройка виртуального окружения и установка зависимостей

- Инструкция для работы через виртуальное окружение - poetry: 
```text
poetry init - Создает виртуальное окружение
poetry shell - Активирует виртуальное окружение
poetry install - Устанавливает зависимости
```

- Инструкция для работы через виртуальное окружение - pip:

Создает виртуальное окружение:
```text
python3 -m venv venv
```

Активирует виртуальное окружение:
```text
source venv/bin/activate          # для Linux и Mac
venv\Scripts\activate.bat         # для Windows
```

Устанавливает зависимости:
```text
pip install -r requirements.txt
```

### 3. Редактирование config.ini.sample:

- В корне проекта переименуйте файл config.ini.sample в config.ini и отредактируйте параметры:
    ```text
    [django_settings]
    DEBUG = True_or_False
    SECRET_KEY = your_secret_key
    
    
    [database]
    DB_ENGINE = postgresql_psycopg2
    DB_NAME = your_name_db
    DB_USER = your_user_db
    DB_PASSWORD = your_password_db
    DB_HOST = localhost
    DB_PORT = 5432
    ```

### 4. Настройка БД:

- Создать миграции:
  ```text
  python manage.py makemigrations
  ```

- Примените миграции:
  ```text
  python manage.py migrate
  ```
  
## Использование

- Для запуска проекта наберите в терминале команду:
  ```text
  python manage.py runserver
  ```
- перейдите по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 5. Запуск проекта с использованием Docker и Docker Compose:

### Предварительные требования

- Docker: [Установить Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Установить Docker Compose](https://docs.docker.com/compose/install/)

### Создать файл .env и настроить, переменные находятся в файле .env.sample:

###  Редактирование docker-compose.yaml:

##### Запустите проект с помощью Docker Compose:
  ```text
    docker-compose up --build
  ```
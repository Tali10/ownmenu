# Собственное меню
Проект позволяет сделать собственное меню клиенту из имеющихся блюд

## Введение
Инструкции ниже помогут Вам установить и запустить копию 
проекта на вашем локальном компьютере для целей ознакомления с проектом

## Установка

1. Для начала создаем директорию для проекта.
2. Находясь в данной директории скачиваем проект:

   ```git clone ссылка```
3. В директории проекта создаем виртуальное окружение и активируем ее:
   ```python3 -m venv название_окружения```
   
   ```source название_окружения/bin/activate```
4. Устанавливаем все зависимости в виртуальное окружение с файла requirements.txt:
   
   ```pip install -r requirements.txt```
5. Создаем базу данных для проекта:
   
   ```psql```

   ```CREATE DATABASE название_бд```
6. Создаем файл с наименованием .env в директории проекта со следующими данными:
   ```
   SECRET_KEY=Определяем_случайное_значение
   DEBUG=True_or_False
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=Название_бд(пункт_5)
   DB_USER=Пользователь_в_бд
   DB_PASSWORD=Пароль_пользователя_БД
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=Используемая_почта
   EMAIL_HOST_PASSWORD=Пароль_для_приложения
   ```
   [Инструкция для создания пароля](https://support.google.com/accounts/answer/185833?hl=ru)
7. Делаем миграцию:

   ```./manage.py makemigrations```

   ```./manage.py migrate```
8. Создаем администратора:

   ```./manage.py createsuperuser```

## Библиотеки

Были установлены и использованы библиотеки указанные ниже:
+ Django==4.0.4
+ django-filter==21.1
+ djangorestframework==3.13.1
+ drf-yasg==1.20.0
+ psycopg2-binary==2.9.3
+ python-decouple==3.6

## Функционал

Было реализовано следующее:
+ [Регистрация аккаунта](https://i.postimg.cc/Nfp1JmHc/image.png)
+ [Активация аккаунта](https://i.postimg.cc/qvW6SLB9/image.png)
+ [Логин](https://i.postimg.cc/9FnDwp9r/image.png)
+ [Смена пароля](https://i.postimg.cc/TYLRFXy3/image.png)
+ [Забыли пароль](https://i.postimg.cc/YjcTTZVv/image.png)
+ [Логаут](https://i.postimg.cc/fbrsB2w9/image.png)
+ [Swagger](https://i.postimg.cc/FKt8RMsG/Swagger.png)

К сожалению, остальной функционал не доработан

## Благодарность и извинение

Спасибо за выделенное время и за предоставленную возможность. Приношу свои извинения за неполноценную работу.

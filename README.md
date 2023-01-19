## Проект «API для Yatube»

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/iffilippov/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение (для Windows):

```
py -3.7 -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api/
```

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Автор: [Иван Филиппов](https://www.linkedin.com/in/iffilippov/) <img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" width="50" height="50"/>
### Студент Яндекс Практикум. Стучусь в дверь IT. Россия, Севастополь

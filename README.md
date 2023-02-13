# game_of_life
Игра "Жизнь" на фреймворке Django

# Dev run

### 1) create virtual env

### 2) install requirements
```bash
pip install -r requirements.txt
```

### 3) collect static
```bash
cd /app
python manage.py collectstatic
```

### 4) run migrate
```bash
cd /app
python manage.py migrate
```

### 5) run app
```bash
cd /app
python manage.py runserver
```

### env for app
| Env | Description | Default |
|-----|-------------|---------|
| DJANGO_SECRET_KEY | A secret key for a particular Django installation. | Default: '' (Empty string) |
| DJANGO_DEBUG | A boolean that turns on/off debug mode. | Default: True |
| DJANGO_ALLOWED_HOSTS | A list of strings representing the host/domain names that this Django site can serve. | Default: ['127.0.0.1', 'localhost'] |
| DATABASE_CONFIG | The settings for all databases to be used with Django. | |

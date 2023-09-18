# Виртуальная стажировка.

# Создаем REST API для моб.приложения.

# 1. Устанавливаем и запускаем Docker:
docker.com
# 2. Создаем репозиторий на Git.
# 3. Создаем проект в PyCharm:
- заходим в настройки приложения, в поиске ищем Plugins
- устанавливаем Docker и Requirements
- отключаем интерпретатор
- создаем файл .gitignoe, прописываем в нем .idea
# 4. Создаем файл requirements.txt:
- прописываем все необходимые зависимости для установки.
- Django==
- djangorestframework==
- и т.д.
# 5. Создаем Docker файл:
- Создаем базовый image в Dockerfile
# 6. Создаем Docker-compose:
- пишем docker-compose.yml файл
# 7. Открываем cmd:
- командой cd ...\...\... переходим в путь с проектом
- вводим команду docker-compose build, ждем установки
# 8. Создаем проект Django через Docker:
- docker-compose run --rm web-app sh -c "django-admin startproject ..."
- для проверки проекта можно его запустить docker-compose up
- Подключаем Postgres к приложению Django через Docker
# 9. Подключаем второй интерпретатор к PyCharm:
- Add New Interpreter - Add Local Interpreter...
# 10. Устанавливаем psycopg2 и postgresql-client в Docker:
- Добавляем их в файл requirements.txt
# 11. Применяем manage.py migrate в docker-compose:
- docker-compose run --rm web-app sh -c "python manage.py migrate"
- для заметки: для создания миграций docker-compose run --rm web-app sh -c "python manage.py makemigration"
# 12. Создаем суперпользователя в docker-compose:
- docker-compose run --rm web-app sh -c "python manage.py createsuperuser"
- вводим логин
- вводим email(по желанию)
- вводим пароль(c использованием букв, символов по желанию)
- вводим пароль повторно
# 13. Описание моделей:

Данные, являющиеся константами, практически не изменяющиеся, выведены за пределы моделей в списки кортежей, такие как:

1) Активность - способ прохождения локации, вывел в список кортежей

`ACTIVITIES_CHOICE = [
        ('1', 'пешком'),
        ('2', 'лыжи'),
        ('3', 'катамаран'),
        ('4', 'байдарка'),
        ('5', 'плот'),
        ('6', 'сплав'),
        ('7', 'велосипед'),
        ('8', 'автомобиль'),
        ('9', 'мотоцикл'),
        ('10', 'парус'),
        ('11', 'верхом'),
    ]`

2) Вид локации, вывел в список кортежей

`BEAUTY_CHOICE = [
        ('NI', 'нет информации'),
        ('PS', 'Перевал'),
        ('TP', 'Вершина'),
        ('GL', 'Ледник'),
        ('IO', 'Объект инфраструктуры'),
        ('NO', 'Объект природы'),
    ]`

3) статус добавленной записи пользователя, списком кортежей

`STATUS_CHOICE = [
        ('NEW', 'новый'),
        ('PEN', 'в работе'),
        ('ACC', 'принят'),
        ('REJ', 'отклонен'),
    ]`

4) Уровень сложности прохождения локации, списком кортежей

`LEVEL_CHOICE = [
        ('NI', 'нет информации'),
        ('A1', '1А'),
        ('B1', '1Б'),
        ('А2', '2А'),
        ('В2', '2Б'),
        ('А3', '3А'),
        ('В3', '3Б'),
    ]`

*Модель Pereval - основные данные добавленные туристом:*

`class Pereval(models.Model):
    beauty_title = models.CharField(verbose_name='тип высоты',
                                    max_length=2,
                                    choices=BEAUTY_CHOICE,
                                    default='NI')
    title = models.TextField(verbose_name='название')
    other_titles = models.TextField(verbose_name='комментарий')
    connect = models.TextField(verbose_name='соединение',
                               default='', blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               verbose_name='автор')
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE,
                               verbose_name='координаты')
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              verbose_name='уровень сложности')
    status = models.CharField(choices=STATUS_CHOICE, max_length=3,
                              default='NEW', verbose_name='статус')
    spr_activities_types = models.CharField(max_length=2,
                                            choices=ACTIVITIES_CHOICE,
                                            default='1',
                                            verbose_name='активность'
                                            )`

*Модель Author - основные данные о туристе:*

`class Author(models.Model):
    email = models.EmailField(verbose_name='электронная почта')
    phone = models.CharField(verbose_name='номер телефона', max_length=12)
    fam = models.CharField(verbose_name='фамилия', max_length=30)
    name = models.CharField(verbose_name='имя', max_length=30)
    otc = models.CharField(verbose_name='отчество', max_length=30)`

*Модель Coords - Координаты локации, переданные туристом*

`class Coords(models.Model):
    latitude = models.FloatField(verbose_name='широта', max_length=8)
    longitude = models.FloatField(verbose_name='долгота', max_length=8)
    height = models.IntegerField(verbose_name='высота')`

*класс Images фотографии добавленные пользователем*

`class Images(models.Model):
    image_name = models.TextField(verbose_name='комментарий')
    image = models.URLField(verbose_name='фотография', blank=True, null=True)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE,
                                verbose_name='перевал', related_name='image')`

*Класс Level - добавлении информации о уровне сложности местоположения в разное время года*

`class PerevalImages(models.Model):
    winter = models.CharField(verbose_name='уровень сложности зимой',
                              max_length=2,
                              choices=LEVEL_CHOICE,
                              default='NI')
    summer = models.CharField(verbose_name='уровень сложности летом',
                              max_length=2,
                              choices=LEVEL_CHOICE,
                              default='NI')
    autumn = models.CharField(verbose_name='уровень сложности осенью',
                              max_length=2,
                              choices=LEVEL_CHOICE,
                              default='NI')
    spring = models.CharField(verbose_name='уровень сложности весной',
                              max_length=2,
                              choices=LEVEL_CHOICE,
                              default='NI')`

# 14 Проектируем Views и Serializers
- обязательно устанавливаем Django Rest Framework, указано в пункте 4.
- Для заполнения и тестирования работоспособности отдельных таблиц, создал классы для отдельных таблиц.
- Реализуем submitData. Реализация метода submitData заключается в том, что турист (клиентское приложение) отправляет POST запрос в формате JSON содержащий все необходимые данные. Далее, полученный от туриста JSON на стадии валидации переводится в список словарей validated_data который разделяется на блоки, содержащие данные отдельных талиц.

# Примечание:
- НЕ ЗАБЫВАЕМ добавлять установленные приложения в settings.py в INSTALLED_APPS



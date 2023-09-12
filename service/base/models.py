from django.db import models
from django.utils import timezone


def get_image_path(instance, file): # прописываю путь сохранения изображений, у каждой записи PerevalAdded своя папка
    return f'image/point-{instance.pereval.id}/{file}'


# Активность - способ прохождения локации, вывел в список кортежей
ACTIVITIES = [
    ('foot', 'пеший'),
    ('bike', 'велосипед'),
    ('car', 'автомобиль'),
    ('motorbike', 'мотоцикл'),
]

# Вид локации, вывел в список кортежей
BEAUTYTITLE = [
    ('the_pass', 'перевал'),
    ('mountain_peak', 'горная вершина'),
    ('gorge', 'ущелье'),
    ('plateau', 'плато'),
]

# статус добавленной записи пользователя, списком кортежей
STATUS = [
    ('new', 'новый'),
    ('at_work', 'в работе'),
    ('accepted', 'принят'),
    ('rejected', 'отклонен'),
]

# Уровень сложности прохождения локации, списком кортежей
LEVELS = [
    ('', 'не указано'),
    ('1A', '1a'),
    ('1B', '1б'),
    ('2А', '2а'),
    ('2В', '2б'),
    ('3А', '3а'),
    ('3В', '3б'),
    ]


class Users(models.Model):
    mail = models.EmailField('почта', unique=True)
    phone = models.CharField('телефон', max_length=15)
    name = models.CharField('имя', max_length=30)
    surname = models.CharField('фамилия', max_length=30)
    patronymic = models.CharField('отчество', max_length=30)

    def __str__(self):
        return f'{self.surname}'


class Coords(models.Model):
    latitude = models.FloatField('широта', max_length=9, blank=True)
    longitude = models.FloatField('долгота', max_length=9, blank=True)
    height = models.IntegerField('высота', blank=True)


class PointAdded(models.Model):
    status = models.CharField(choices=STATUS, max_length=25, default='new') #статус нового сообщения, по умолчанию Новое
    beautyTitle = models.CharField('тип', choices=BEAUTYTITLE, max_length=50)#тип локации - перевал, ущелье и т.д. списком
    title = models.CharField('название', max_length=50, blank=True)# название локации
    other_titles = models.CharField('иные названия', max_length=50)# описание локации
    connect = models.CharField('соединение', max_length=250)# какие локации соединяет (применимо к перевалу)
    add_time = models.DateTimeField(default=timezone.now, editable=False)#дата/время создания записи (не понял пользователь вручную создает или автоматическое поле при добавлении в БД)
    coord_id = models.OneToOneField(Coords, on_delete=models.CASCADE)# ссылка на объект с координатами локации. Зачем если связь один к одному?
    winter = models.CharField('зима', max_length=2, choices=LEVELS)# уровень сложности прохождения локации зимой
    summer = models.CharField('лето', max_length=2, choices=LEVELS)# уровень сложности прохождения локации летом
    autumn = models.CharField('осень', max_length=2, choices=LEVELS)# уровень сложности прохождения локации осенью
    spring = models.CharField('весна', max_length=2, choices=LEVELS)# уровень сложности прохождения локации весной
    author = models.ForeignKey(Users, on_delete=models.CASCADE)# автор статьи - ссылка на объект пользователей


class Images(models.Model):
    name = models.CharField(max_length=50)# название фотографии
    photos = models.ImageField('Фото', upload_to=get_image_path, blank=True, null=True)# объект фотографии


class PointImages(models.Model):
    point = models.ForeignKey(PointAdded, on_delete=models.CASCADE, default=0)  # ссылка на объект локации
    images = models.ForeignKey(Images, on_delete=models.CASCADE, default=0)  # ссылка на объект фотографии


class PointAreas(models.Model):

    id_parent = models.IntegerField(blank=True)
    title = models.TextField()

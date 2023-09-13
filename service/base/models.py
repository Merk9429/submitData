from django.db import models
from django.utils import timezone


def get_image_path(instance, file):
    return f'image/point-{instance.pereval.id}/{file}'


ACTIVITIES = [
    ('foot', 'пеший'),
    ('bike', 'велосипед'),
    ('car', 'автомобиль'),
    ('motorbike', 'мотоцикл'),
]

BEAUTYTITLE = [
    ('the_pass', 'перевал'),
    ('mountain_peak', 'горная вершина'),
    ('gorge', 'ущелье'),
    ('plateau', 'плато'),
]

STATUS = [
    ('new', 'новый'),
    ('at_work', 'в работе'),
    ('accepted', 'принят'),
    ('rejected', 'отклонен'),
]

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


class Images(models.Model):
    name = models.CharField(max_length=50)
    photos = models.ImageField('Фото', upload_to=get_image_path, blank=True, null=True)


class PerevalAdded(models.Model):
    status = models.CharField(choices=STATUS, max_length=25, default='new')
    beautyTitle = models.CharField('тип', choices=BEAUTYTITLE, max_length=50)
    title = models.CharField('название', max_length=50, blank=True)
    other_titles = models.CharField('иные названия', max_length=50)
    connect = models.CharField('соединение', max_length=250)
    add_time = models.DateTimeField(default=timezone.now, editable=False)
    coord_id = models.OneToOneField(Coords, on_delete=models.CASCADE)
    winter = models.CharField('зима', max_length=2, choices=LEVELS)
    summer = models.CharField('лето', max_length=2, choices=LEVELS)
    autumn = models.CharField('осень', max_length=2, choices=LEVELS)
    spring = models.CharField('весна', max_length=2, choices=LEVELS)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    images = models.ForeignKey(Images, on_delete=models.CASCADE, default=0)


class PerevalImages(models.Model):
    point = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, default=0)
    images = models.ForeignKey(Images, on_delete=models.CASCADE, default=0)


class PerevalAreas(models.Model):

    id_parent = models.IntegerField(blank=True)
    title = models.TextField()

from django.db import models


class Author(models.Model):
    email = models.EmailField(verbose_name='электронная почта')
    phone = models.CharField(verbose_name='номер телефона', max_length=12)
    fam = models.CharField(verbose_name='фамилия', max_length=30)
    name = models.CharField(verbose_name='имя', max_length=30)
    otc = models.CharField(verbose_name='отчество', max_length=30)


class Coords(models.Model):
    latitude = models.FloatField(verbose_name='широта', max_length=8)
    longitude = models.FloatField(verbose_name='долгота', max_length=8)
    height = models.IntegerField(verbose_name='высота')


class Level(models.Model):
    LEVEL_CHOICE = [
        ('NI', 'нет информации'),
        ('A1', '1А'),
        ('B1', '1Б'),
        ('А2', '2А'),
        ('В2', '2Б'),
        ('А3', '3А'),
        ('В3', '3Б'),
    ]

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
                              default='NI')


class Pereval(models.Model):
    BEAUTY_CHOICE = [
        ('NI', 'нет информации'),
        ('PS', 'Перевал'),
        ('TP', 'Вершина'),
        ('GL', 'Ледник'),
        ('IO', 'Объект инфраструктуры'),
        ('NO', 'Объект природы'),

    ]

    STATUS_CHOICE = [
        ('NEW', 'новый'),
        ('PEN', 'в работе'),
        ('ACC', 'принят'),
        ('REJ', 'отклонен'),
    ]

    ACTIVITIES_CHOICE = [
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
    ]

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
                                            )


class Images(models.Model):
    image_name = models.TextField(verbose_name='комментарий')
    image = models.URLField(verbose_name='фотография', blank=True, null=True)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE,
                                verbose_name='перевал', related_name='image')

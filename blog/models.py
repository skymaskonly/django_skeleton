from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now
from django.core.exceptions import ValidationError


def get_default_text():
    return 'my new default text'

def validate_year(value):
    today = now()
    if value > today.year:
        raise ValidationError(_(f'{value} первышает текущий год'))

class Post(models.Model):

    myid = models.AutoField(
        _('myid'),
        primary_key=True,
    )

    YEAR = [
        (None, '$$$'),
        (2009, 2009),
        (2010, 2010),
        (2011, 2011),
        (2012, 2012),
        (2013, 2013),
        (2025, 2025),
    ]

    choice_year = models.PositiveSmallIntegerField(
        _('year'),
        choices=YEAR,
        validators=[validate_year]
    )

    slug = models.SlugField(
        _('url'),

        unique=True,

        help_text='<i>Введите URL для записи</i>',

        error_messages={
            'unique': 'Поле должно быть уникальным!',
            'blank': 'Поле надо заполнить!',
        }
    )

    name = models.CharField(
        _('name'),

        db_column='some name',
 
        unique=True,
        null=True,
        blank=True,

        max_length=150,
    )

    pub_date = models.DateField(
        _('published date')
    )

    text = models.TextField(
        _('text'),
        blank=True,

        unique_for_date='pub_date',
        # unique_for_month='pub_date',
        # unique_for_year='pub_date',

        default=get_default_text,

        db_index=True,

        # editable=False,

        # db_tablespace=True,
    )

    fk = models.ForeignKey('self', verbose_name=('fk self'), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        db_table = 'posts'

    def __str__(self) -> str:
        return self.slug
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
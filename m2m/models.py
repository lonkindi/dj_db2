from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    sections = models.ManyToManyField('Section', through='Relations', related_name='art')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Section(models.Model):
    name = models.CharField(max_length=64, verbose_name='Секция', null=False)
    articles = models.ManyToManyField(Article, through='Relations', related_name='sect')

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'

    def __str__(self):
        return self.name


class Relations(models.Model):
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)
    sections = models.ForeignKey(Section, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основная секция')

    class Meta:
        verbose_name = 'Секция в статье'
        verbose_name_plural = 'Секции в статье'
        ordering = ["sections__name"]

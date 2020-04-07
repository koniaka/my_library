from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Author(models.Model):
    full_name = models.TextField(verbose_name=_("Имя автора"))
    birth_year = models.SmallIntegerField(verbose_name=_("Год рожения"))
    country = models.CharField(max_length=2, verbose_name=_("Страна"))
    def __str__(self):
        return self.full_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13, verbose_name=_("Международный стандартный "
                                           "книжный номер"))
    title = models.TextField(verbose_name=_("Название"))
    copy_count = models.SmallIntegerField(verbose_name=_("Число копий"))
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Цена"))
    description = models.TextField(verbose_name=_("Аннотация"))
    year_release = models.SmallIntegerField(verbose_name=_("Год издания"))
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name=_("Автор"),
                               related_name="book_author")
    publishing = models.ForeignKey('Publishing', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Издательство"),
                               related_name="books_pub")
    def __str__(self):
        return self.title

class Publishing(models.Model):
    publish_name = models.CharField(max_length=50, verbose_name=_("Издательство"))
    sity = models.CharField(max_length=20, verbose_name=_("Город"))
    def __str__(self):
        return self.publish_name

class Friend(models.Model):
    name = models.TextField(max_length=20, verbose_name=_("Имя"))
    books = models.ManyToManyField('Book', through='BookReading', verbose_name=_("Книги"))
    def __str__(self):
        return self.name

class BookReading(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name=_("Книга"))
    reader = models.ForeignKey('Friend', on_delete=models.CASCADE, verbose_name=_("Читатель"))
    completion = models.NullBooleanField(default=None, verbose_name=_("Чтение завершено"))

    def __str__(self):
        return " - ".join((str(self.book),
                         str(self.reader),
                         str(self.completion)))
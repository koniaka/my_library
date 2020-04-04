from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    copy_count = models.SmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publishing = models.ForeignKey('Publishing', on_delete=models.CASCADE, null=True, blank=True, related_name="books_pub")
    def __str__(self):
        return self.title

class Publishing(models.Model):
    publish_name = models.CharField(max_length=50)
    def __str__(self):
        return self.publish_name
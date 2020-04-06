from django.contrib import admin
from p_library.models import Book, Author, Publishing, Friend, BookReading

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_display = ('title', 'author_full_name')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'publishing')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publishing)
class PublishingAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass

@admin.register(BookReading)
class BookReadingAdmin(admin.ModelAdmin):
    pass
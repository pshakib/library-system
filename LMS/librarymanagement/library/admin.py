from django.contrib import admin
from .models import Book,MemberExtra,IssuedBook
# Register your models here.
class BookLibrarian(admin.ModelAdmin):
    pass
admin.site.register(Book, BookLibrarian)


class MemberExtraLibrarian(admin.ModelAdmin):
    pass
admin.site.register(MemberExtra, MemberExtraLibrarian)


class IssuedBookLibrarian(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IssuedBookLibrarian)

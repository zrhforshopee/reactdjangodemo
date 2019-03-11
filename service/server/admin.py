from django.contrib import admin
from server.models import Person

from server.models import Book
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','time']

admin.site.register(Person,PersonAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name','price']

admin.site.register(Book,BookAdmin)
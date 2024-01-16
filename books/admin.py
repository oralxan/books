'''from django.contrib import admin
from .models import Book
#dekarator-@ modeldi osilayda registr qilsaq boladi, otdelni funkciyalarga
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','price')
    list_display_links = ('id','name','price')
    ordering =('name')'''
from django.contrib import admin

from .models import Book
#dekarator-@ modeldi osilayda registr qilsaq boladi, otdelni funkciyalarga
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name', 'price')
    ordering = ('name',)
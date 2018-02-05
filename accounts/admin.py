from django.contrib import admin

# Register your models here.

from .models import Category , Info

admin.site.register(Category)
admin.site.register(Info)

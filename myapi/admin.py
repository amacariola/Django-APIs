from django.contrib import admin

# Register your models here.

# import Students model

from .models import Students

admin.site.register(Students)

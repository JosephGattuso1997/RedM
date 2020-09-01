from django.contrib import admin

# Register your models here.
from .models import Portfolio

admin.site.register(Portfolio)
prepopulated_fields = {'slug': ('name',), }

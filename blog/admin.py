from django.contrib import admin

# Register your models here.
from .models import Blog
from .models import Tag

admin.site.register(Blog)
admin.site.register(Tag)
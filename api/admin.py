from django.contrib import admin
from .models import Content, User

# Register your models here.
admin.site.register(User)
admin.site.register(Content)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

admin.site.register(Groupe)
admin.site.register(Tag)
admin.site.register(Device)

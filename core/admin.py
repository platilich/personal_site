from django.contrib import admin
from .models import Profile
from solo.admin import SingletonModelAdmin

# Register your models here.
admin.site.register(Profile, SingletonModelAdmin)
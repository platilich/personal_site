from django.contrib import admin
from .models import Category, Posts


# Register your models here.
admin.site.register(Category)
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
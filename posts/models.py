from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Name of category')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')



    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return f'{self.title}'




class Posts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    title = models.CharField(max_length=50, verbose_name='Name of post')
    description = models.CharField(max_length=200, verbose_name='Short description this post')
    created_at = models.DateTimeField(auto_now_add=True)

    content = RichTextField('Content', config_name='content_field')


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def __str__(self):
        return f'{self.title} - {self.created_at}'
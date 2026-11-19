from django.db import models
from solo.models import SingletonModel


# Create your models here.
class Profile(SingletonModel):
    avatar = models.ImageField(upload_to='')
    name = models.CharField(max_length=100, verbose_name='Your name')
    specification = models.CharField(max_length=255, null=True, verbose_name='Your specification')
    about_me = models.TextField(max_length=500, verbose_name='Short about you')


    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'



    def __str__(self):
        return 'Profile'




class BestProjects(models.Model):
    title = models.CharField(verbose_name='Title of this project')
    stack = models.CharField(verbose_name='Stack')
    description = models.CharField(verbose_name='Description about this project')
    url = models.CharField(verbose_name='URL to project')


    class Meta:
        verbose_name = 'Best project'
        verbose_name_plural = 'Best projects'


    def __str__(self):
        return self.title


async def get_profile():
    data = await Profile.aget_solo()
    return data



async def get_best_projects():
    data = BestProjects.objects.all()
    return data
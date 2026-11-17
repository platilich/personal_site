from django.db import models
from solo.models import SingletonModel


# Create your models here.
class Profile(SingletonModel):
    avatar = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100, verbose_name='Your name')
    about_me = models.TextField(max_length=255, verbose_name='Short about you')


    class Meta:
        verbose_name = 'Profile'



    def __str__(self):
        return 'Profile'



async def get_profile():
    data = await Profile.aget_solo()
    return data
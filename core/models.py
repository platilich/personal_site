from django.db import models
from solo.models import SingletonModel


# Create your models here.
class Profile(SingletonModel):
    avatar = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100, verbose_name='Your name')
    about_me = models.TextField(max_length=255, verbose_name='Short about you')


    class Meta:
        verbose_name = 'Profile'



    @classmethod
    def get_profile(cls):
        data = Profile.objects.all()
        return data
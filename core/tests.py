from django.test import TestCase

# Create your tests here.
from core.models import Profile





async def main():
    data = Profile.aget_solo()
    print(data)




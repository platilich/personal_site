from django.shortcuts import render
from .models import get_profile
import asyncio

# Create your views here.
def index(request):
    data = asyncio.run(get_profile())

    return render(request, 'index.html', {'data': data})

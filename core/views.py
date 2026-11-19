from django.shortcuts import render
from .models import get_profile, get_best_projects
import asyncio

# Create your views here.
def index(request):
    profile = asyncio.run(get_profile())
    projects = asyncio.run(get_best_projects())


    return render(request, 'index.html', {'profile': profile, 'projects': projects})

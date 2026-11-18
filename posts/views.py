from django.shortcuts import render

# Create your views here.
def posts(request):
    return render(request, template_name='posts.html')



def my_tools(request):
    return render(request, template_name='my_tools.html')



def about(request):
    return render(request, template_name='about.html')
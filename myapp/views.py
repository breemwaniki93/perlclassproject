from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'index2.html')
def contact(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'Services.html')
def blog(request):
    return render(request,'blog.html')
def courses(request):
    return render(request,'courses.html')
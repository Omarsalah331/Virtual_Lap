from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'index.html')

def blog_view(request):
    return render(request,'blog.html')

def about_view(request):
    return render(request,'about.html')

def labs_view(request):
    return render(request,'Virtual_Laps.html')

def support_view(request):
    return render(request,'support.html')

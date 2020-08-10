from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"app/home.html")

def login(request):
    return render(request,"app/login.html")

def sign_up(request):
    return render(request,"app/sign_up.html")

def profile(request):
    name="Hrushikesh"
    return render(request,"app/profile.html",{'name':name})
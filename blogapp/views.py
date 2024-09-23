from django.shortcuts import render,redirect
from blogapp.models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blogapp import models
from django.urls import reverse_lazy
from django.views.generic import UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request,'blogapp/base.html') 

def LogIn(request):
    if request.method=='POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            return render(request, 'blogapp/login.html', {'error': 'Invalid credentials'})
    return render(request,'blogapp/login.html')

def signup(request):
    if request.method=='POST':
        name = request.POST.get('uname')
        email =  request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name,email=email,password=password)
        newUser.save()
        return redirect('/login')
    return render(request,'blogapp/signup.html')

@login_required(login_url='/login')
def home(request):
    context = {
        'posts':Posts.objects.all().order_by('-date_posted')
    }
    return render(request,'blogapp/home.html',context)

@login_required(login_url='/login')
def newPost(request):
    if request.method=='POST':
        title =  request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        newpost = models.Posts(title=title,content=content,image=image,author=request.user)
        newpost.save()
        return redirect('/home')
    return render(request,'blogapp/newpost.html')

@login_required(login_url='/login')
def myPost(request):
    context = {
        'posts':Posts.objects.filter(author = request.user).order_by('-date_posted')
    }
    return render(request,'blogapp/mypost.html',context)

@method_decorator(login_required(login_url='/login'), name='dispatch')
class postupdate(UpdateView):
    model = Posts
    fields = ['title','content','image']

@method_decorator(login_required(login_url='/login'), name='dispatch')
class postdelete(DeleteView):
    model = Posts
    success_url = reverse_lazy('mypost')

def signout(request):
    logout(request)
    return redirect('/login')


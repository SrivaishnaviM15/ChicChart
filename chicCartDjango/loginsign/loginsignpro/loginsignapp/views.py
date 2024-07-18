
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from .models import User
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Retrieve entered login credentials
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
            except User.DoesNotExist:
                return redirect(reverse('signup'))
            return render(request,'successLoginGif.html')
    else:
        form = LoginForm()
    return render(request, 'profile_page.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            mobile= form.cleaned_data['mobile']
            address= form.cleaned_data['address']
            email= form.cleaned_data['email']
            user = User(username=username, password=password, mobile=mobile, address=address, email=email)
            user.save()
            return render(request,'successLoginGif.html')
    else:
        form = SignupForm()
    return render(request, 'signup_page.html', {'form': form})


def men(request):
    men_url='http://127.0.0.1:5500/homepages/menHomePage.html'
    return redirect(men_url)
def women(request):
    women_url='http://127.0.0.1:5500/homepages/womenHomePage.html'
    return redirect(women_url)
def kids(request):
    kids_url='http://127.0.0.1:5500/homepages/kidshomepage.html'
    return redirect(kids_url)
def beauty(request):
    beauty_url='http://127.0.0.1:5500/homepages/beautyhomepage.html'
    return redirect(beauty_url)
def living(request):
    living_url='http://127.0.0.1:5500/homepages/homeLiving.html'
    return redirect(living_url)
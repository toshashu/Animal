from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm 
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SellingForm
from .models import Selling
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import ProfileForm




def home(request):
    selling_data = Selling.objects.all()
    return render(request, 'home.html', {'selling_data': selling_data})

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save() 
#             UserProfile.objects.create(user=user)
#             return redirect('login')  
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            # Create a profile for the user
            profile = UserProfile.objects.create(user=user)
            return redirect('login')  # Redirect to login page after successful registration
    else:
        user_form = RegisterForm()
    return render(request, 'register.html', {'form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("User logged in successfully")  
                return redirect('home')  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})





@login_required
def selling(request):
    if request.method == 'POST':
        form = SellingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
        else:
            print(form.errors)
    else:
        form = SellingForm()
    return render(request, 'selling.html', {'form': form})

def home(request):
    selling_data = Selling.objects.all()
    return render(request, 'home.html', {'selling_data': selling_data})

# def home(request):
#     if request.user.is_authenticated:
#         user_profile = UserProfile.objects.get(user=request.user)
#         return render(request, 'home.html', {'user_profile': user_profile})
#     else:
#         selling_data = Selling.objects.all()
#         return render(request, 'home.html', {'selling_data': selling_data})

@login_required
def item_detail(request, item_id):
    item = get_object_or_404(Selling, pk=item_id)
    return render(request, 'item_detail.html', {'item': item})


def buy_item(request, item_id):
    item = get_object_or_404(Selling, pk=item_id)
    return render(request, 'buy_item.html', {'item': item})

def about(request):
    return render(request, 'about.html')


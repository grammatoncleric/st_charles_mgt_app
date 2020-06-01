from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from baptisms.models import Baptism
from bookmasses.models import Bookmass
from members.models import Member


# Create your views here.
def login(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:

      return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST': 
        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if passwords match
        if password==password2:
            #check username
            if User.objects.filter(username = username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register') 
            else:
              if User.objects.filter(email = email).exists():
                messages.error(request, 'That email is taken')
                return redirect('register')   
              else:
                   #Looks good 
                   user = User.objects.create_user(username=username, password=password, email=email,
                   first_name=first_name, last_name=last_name) 
                   #Login after register
                   #auth.login(request, user)
                   #messages.success(request, 'You are now logged in')
                   #return redirect('index')
                   user.save()
                   messages.success(request, 'You are now registered and can log in')
                   return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')            
 
    else:
       #messages.error(request, 'Testing error message')
        return render(request, 'accounts/register.html')
        
def logout(request):
    if request.method == 'POST': 
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')
        
def dashboard(request):
    if request.user.is_authenticated:
      user_id=request.user.id

      baptism_obj = Baptism.objects.order_by('-create_date').filter(user_id=user_id)
      bookmass_obj = Bookmass.objects.order_by('-create_date').filter(user_id=user_id)
      member_obj = Member.objects.order_by('-create_date').filter(user_id=user_id)

      context={
        'baptisms':baptism_obj,
        'bookmasses':bookmass_obj,
        'members':member_obj
       }
    return render(request, 'accounts/dashboard.html', context)
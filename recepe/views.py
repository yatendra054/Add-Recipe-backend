from django.shortcuts import render,redirect,get_object_or_404

from recepe.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from Start import settings
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from recepe.utils import send_email_to_client
import re
@login_required(login_url='/')
def recepies(request):
    if request.method=="POST":
        Dish_Image = request.FILES.get("Dish_Image")
        Recepies_name = request.POST.get("Recepies_name")
        Recepies_description = request.POST.get("Recepies_description")
        Country = request.POST.get("Country")
        
        Recepies.objects.create(
            user=request.user,
            Recepies_name=Recepies_name,
            Recepies_description=Recepies_description,
            Country=Country,
            Dish_Image=Dish_Image,
        )
        return redirect('/recepies/')
    queryset = Recepies.objects.filter(user=request.user)
    if request.GET.get('search'):
        queryset = queryset.filter(Recepies_name__icontains=request.GET.get('search'))
    context ={'recepies':queryset}
    return render(request , "recepie.html",context)

@login_required(login_url='/')
def update_recepie(request,id):
    queryset = get_object_or_404(Recepies,id = id,user=request.user)
    if request.method=="POST":
        data = request.POST
        Recepies_name = data.get("Recepies_name")
        Recepies_description = data.get("Recepies_description")
        Country = data.get("Country")
        Dish_Image= request.FILES.get("Dish_Image")
        
        queryset.Recepies_name=Recepies_name
        queryset.Recepies_description=Recepies_description
        queryset.Country=Country
        
        if Dish_Image:
            queryset.Dish_Image= Dish_Image
            
        queryset.save()
        return redirect('/recepies')
            
        
    context ={'recepies':queryset}
    return render(request , "update_recepie.html",context)
    
@login_required(login_url='/')
def delete_recepie(request,id):
    queryset = get_object_or_404(Recepies,id = id,user=request.user)
    queryset.delete()
    return redirect('/recepies/')

def login_page(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        
        if not username or not password:
            messages.error(request,"Please login  with your username and password")
            return redirect('/')
        
        if not User.objects.filter(username = username).exists():
            messages.error(request,"Invalid Username")
            return redirect('/')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/')
        else:
            login(request,user)
            return redirect('/recepies/')
        
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=="POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        
        user= User.objects.filter(username=username)
        if not first_name.isalpha():
            messages.warning(request,"First and Last name should be in alphabates")
            return redirect('/register')
        
        if not re.match(r"[a-zA-Z0-9._%+-]+@(gmail|yahoo)\.com",email):
            messages.warning(request,"Email invalid format")
            return redirect('/register')
        
        if len(password)<8:
            messages.warning(request,"Password should be written at least 8 character")
            return redirect('/register')
        
        if user.exists():
            messages.warning(request, "Username Already Present") 
            return redirect('/register')
        
        if User.objects.filter(email=email).exists():
            messages.warning(request, "UserEmail Already Registered")
            return redirect('/register')
        
        user=User.objects.create(
            username=username,
            email = email
        )
        user.set_password(password)
        user.save()
        
        
        UserInformation.objects.create(
            user =user,
            First_Name = first_name,
            Last_Name = last_name,
            User_Name = username,
            Email = email
        )
        send_email_to_client(email,username)
        
        messages.success(request,"Username Successfully Register")
        return redirect('/register')        
    
    return render(request,"register.html")
def forget(request):
    if request.method=="POST":
        data= request.POST
        email=data.get("email")
        new_password=data.get("new_password")
        confirm_password=data.get("confirm_password")
        
        if new_password != confirm_password:
            messages.error(request,"Password is not match")
            return redirect('/forget')
        
        try:
            user=User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request,"Email is not associated with any account")
            return redirect('/forget')
        user.set_password(new_password)
        
        user.save()
        
        messages.success(request, "Password reset successfully. Please log in with your new password.")
        return redirect('/')
        
    return render(request,"foreget.html")
            
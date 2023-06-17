from accounts.models import Profile
import csv
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from events.models import Event
from articles.models import Article
# Create your views here.
from noticeBoard.models import AdminNotice

@login_required
def home(request):

    events = Event.objects.all()
    context = {'events': events}
    # return render(request , 'dashboard.html',context)
    quant = User.objects.all().count()
    content = AdminNotice.objects.all().order_by ('id') [1:4]
    size = AdminNotice.objects.all().count()
    art = Article.objects.all().count()
    return render(request , 'dashboard.html',{'conts': content, 'num': size,**context, 'list': quant , 'article_count': art})


def user_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_list.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Email'])

    users = User.objects.all()
    for user in users:
        if user.is_staff == 0:
            writer.writerow([user.username, user.email])
    
    return response
    
def usersDetail(request):
    users = User.objects.all()
    return render(request, 'usersDetail.html',{'users': users})

def delete_user(request,username):
    try:
        user = User.objects.get(username=username)
        user.delete()
        messages.success(request, "User is deleted Successfully!")
    except User.DoesNotExist:
        print("User does not exist.")
    return HttpResponseRedirect(reverse('usersDetail'))


def modify_user(request, username):
    if request.method == 'POST':
        # Retrieve the username and new details from the request POST data
        # username = request.POST.get('username')
        new_details = {
            'email': request.POST.get('email'),
            # 'first_name': request.POST.get('first_name'),
            # 'last_name': request.POST.get('last_name')
        }
        # Retrieve the user object
        user = User.objects.get(username=username)
            # Modify the desired user details
        user.email = new_details['email']
        # user.first_name = new_details['first_name']
        # user.last_name = new_details['last_name']
        #     # Save the changes
        user.save()
        return HttpResponseRedirect(reverse('usersDetail'))
    



def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/accounts/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        # if not profile_obj.is_verified:
        #     messages.success(request, 'Profile is not verified check your mail.')
        #     return redirect('/accounts/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Invalid Credentials.')
            return redirect('/accounts/login')
        
        login(request , user)
        return redirect('/')

    return render(request , 'login.html')

def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username Already Exists.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email Already Exists.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)


    return render(request , 'register.html')

def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        # if profile_obj:
        #     if profile_obj.is_verified:
        #         messages.success(request, 'Your account is already verified.')
        #         return redirect('/accounts/login')
        #     profile_obj.is_verified = True
        #     profile_obj.save()
        #     messages.success(request, 'Your account has been verified.')
        #     return redirect('/accounts/login')
        # else:
        #     return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')

def logout_attempt(request):
    if request.method == "POST":
        logout(request)
        return redirect('login_attempt')








def send_mail_after_registration(email , token):
    subject = 'Verification email for Robotics Event Website'
    message = f'Click on the given link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    
from django.shortcuts import render, redirect
from .forms import FollowForm,LikeForm,CommentForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required



import random

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.





def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'signup.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'signup.html')

        # Create the user if username and email are unique
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html')




# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def home_view(request):
    return render(request, 'home.html', {'username': request.user.username})



from django.contrib.auth import logout as auth_logout

def logout_view(request):
    auth_logout(request)  # Log out the user
    return redirect('login')  # Redirect to the login page after logout

    

otp_storage = {}  # Store OTPs temporarily

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
            otp_storage[email] = otp  # Store the OTP
            
            # Debugging: Print OTP to console (remove in production)
            print(f"Generated OTP for {email}: {otp}")

            # Send the OTP to the user's email
            send_mail(
                'Your OTP for Password Reset',
                f'Your OTP is: {otp}',
                'your-email@gmail.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, 'OTP sent to your email.')
            return render(request, 'reset_password.html', {'email': email})  # Pass email to the reset form
        else:
            messages.error(request, 'Email not found.')
    return render(request, 'forgot_password.html')




# original working
def reset_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Use .get() to avoid MultiValueDictKeyError
        otp = request.POST.get('otp')       # Use .get() here as well
        new_password = request.POST.get('new_password')  # Use .get() for new password

        # Debugging: Check the incoming OTP and stored OTP
        print(f"Incoming OTP: {otp}, Stored OTP: {otp_storage.get(email)}")

        # Check if the OTP is correct
        if otp_storage.get(email) == int(otp):  # Ensure comparison is done with integer
            try:
                user = User.objects.get(email=email)
                user.set_password(new_password)  # Hash and set new password
                user.save()

                del otp_storage[email]  # Clear the OTP once it's used
                messages.success(request, 'Password has been successfully reset. You can now log in with your new password.')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'User with this email does not exist.')
        else:
            messages.error(request, 'Invalid OTP.')

    return render(request, 'reset_password.html')  # Ensure you handle GET requests appropriately






#--------------------------------------------------

def BotRequestView(request):
    if request.method == 'POST':
        form = FollowForm(request.POST)
        form.request_type = "follow"
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        return render(request, 'follow_page.html', context={'form':FollowForm()})
    return render(request, 'follow_page.html', context={'form':FollowForm()})


def BotLikeView(request):
    if request.method == 'POST':
        form = LikeForm(request.POST)
        form.request_type = "like"
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        return render(request, 'like_page.html', context={'form':LikeForm()})
    return render(request, 'like_page.html')




def BotCommentView(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.request_type = "comment"
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        return render(request, 'comment_page.html', context={'form':CommentForm()})
    return render(request, 'comment_page.html', context={'form':CommentForm()})


def SuccessView(request):
    return render(request,'success.html')


#__________________________________




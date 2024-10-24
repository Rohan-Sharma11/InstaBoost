from django.shortcuts import render, redirect,HttpResponse
from .forms import FollowForm,LikeForm,CommentForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required


from django.conf import settings
from SocialBoost.settings import EMAIL_HOST_USER
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

    

# otp_storage = {}  # Store OTPs temporarily

# def forgot_password_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         if User.objects.filter(email=email).exists():
#             otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
#             otp_storage[email] = otp  # Store the OTP
            
#             # Debugging: Print OTP to console (remove in production)
#             print(f"Generated OTP for {email}: {otp}")

#             # Send the OTP to the user's email
#             send_mail(
#                 'Your OTP for Password Reset',
#                 f'Your OTP is: {otp}',
#                 'your-email@gmail.com',
#                 [email],
#                 fail_silently=False,
#             )
#             messages.success(request, 'OTP sent to your email.')
#             print("hiii")
#             return render(request, 'reset_password.html', {'email': email})  # Pass email to the reset form
#             # return HttpResponse("jhsvajvsh")
#         else:
#             messages.error(request, 'Email not found.')
#     return render(request, 'forgot_password.html')




# # original working
# def reset_password_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')  # Use .get() to avoid MultiValueDictKeyError
#         otp = request.POST.get('otp')       # Use .get() here as well
#         new_password = request.POST.get('new_password')  # Use .get() for new password

#         # Debugging: Check the incoming OTP and stored OTP
#         print(f"Incoming OTP: {otp}, Stored OTP: {otp_storage.get(email)}")

#         # Check if the OTP is correct
#         if otp_storage.get(email) == int(otp):  # Ensure comparison is done with integer
#             try:
#                 user = User.objects.get(email=email)
#                 user.set_password(new_password)  # Hash and set new password
#                 user.save()

#                 del otp_storage[email]  # Clear the OTP once it's used
#                 messages.success(request, 'Password has been successfully reset. You can now log in with your new password.')
#                 return redirect('login')
#             except User.DoesNotExist:
#                 messages.error(request, 'User with this email does not exist.')
#         else:
#             messages.error(request, 'Invalid OTP.')

#     return render(request, 'reset_password.html')  # Ensure you handle GET requests appropriately




# otp_storage = {}  # Store OTPs temporarily

# def forgot_password_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')  # Use .get() to avoid MultiValueDictKeyError
#         if User.objects.filter(email=email).exists():
#             otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
#             otp_storage[email] = otp  # Store the OTP
            
#             # Debugging: Print OTP to console (remove in production)
#             print(f"Generated OTP for {email}: {otp}")

#             # Send the OTP to the user's email
#             send_mail(
#                 'Your OTP for Password Reset',
#                 f'Your OTP is: {otp}',
#                 'your-email@gmail.com',
#                 [email],
#                 fail_silently=False,
#             )
#             messages.success(request, 'OTP sent to your email.')
#             return render(request, 'reset_password.html', {'email': email})  # Pass email to the reset form
#         else:
#             messages.error(request, 'Email not found.')
    
#     # Render the forgot password form with any messages
#     return render(request, 'forgot_password.html')

# def reset_password_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')  # Use .get() to avoid MultiValueDictKeyError
#         otp = request.POST.get('otp')       # Use .get() here as well
#         new_password = request.POST.get('new_password')  # Use .get() for new password

#         # Debugging: Check the incoming OTP and stored OTP
#         print(f"Incoming OTP: {otp}, Stored OTP: {otp_storage.get(email)}")

#         # Check if the OTP is correct
#         if otp_storage.get(email) == int(otp):  # Ensure comparison is done with integer
#             try:
#                 user = User.objects.get(email=email)
#                 user.set_password(new_password)  # Hash and set new password
#                 user.save()

#                 del otp_storage[email]  # Clear the OTP once it's used
#                 messages.success(request, 'Password has been successfully reset. You can now log in with your new password.')
#                 return redirect('login')
#             except User.DoesNotExist:
#                 messages.error(request, 'User with this email does not exist.')
#         else:
#             messages.error(request, 'Invalid OTP.')

#     # Render the reset password form, ensure GET requests are handled
#     return render(request, 'reset_password.html', {'email': request.POST.get('email')})









otp_storage = {}  # Store OTPs temporarily

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Use .get() to avoid MultiValueDictKeyError
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
            messages.error(request, 'Email not found.')  # Show error if email is not found

    # Render the forgot password form with any messages
    return render(request, 'forgot_password.html')

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

    # Render the reset password form, ensuring GET requests are handled
    return render(request, 'reset_password.html', {'email': request.POST.get('email')})


#--------------------------------------------------
@login_required(login_url='login')
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

@login_required(login_url='login')
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



@login_required(login_url='login')
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

#_______________________________

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Check if the fields are filled
        if not all([name, email, subject, message]):
            messages.error(request, "Please fill all fields.")
            return redirect('contactus')  # Redirect back to contactus page

        # Compose email
        full_message = f"Message:\n{message}\n\nSender's Email:\n{email}"
        
        try:
            # Sending the email
            send_mail(
                subject,  # Subject from form
                full_message,  # Full message including the user's email
                'socialboooost1@gmail.com',  # Your email as the sender
                ['rohansh3535@gmail.com'],  # Receiver's email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
        
        return redirect('contactus')  # Redirect to the same page after submission

    # For GET request, render the contact form
    return render(request, 'contactus.html')  # Render the contact form if not a POST request


def AboutUs(request):
     return render(request,'aboutus.html')


# def contactus_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Construct the full message with form data
#         full_message = f"Name: {name}\nEmail: {email}\n\nSubject: {subject}\n\nMessage:\n{message}"

#         try:
#             send_mail(
#                 subject,  # Email subject (subject from form)
#                 full_message,  # Full message (name, email, subject, and message)
#                 'your-email@gmail.com',  # From email (must match EMAIL_HOST_USER)
#                 ['your-email@gmail.com'],  # To email (where you want to receive it)
#                 fail_silently=False,
#             )
#             messages.success(request, 'Your message has been sent successfully!')
#         except Exception as e:
#             messages.error(request, f"An error occurred: {str(e)}")
    
#     return render(request, 'contact_us.html')



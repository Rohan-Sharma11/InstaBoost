from django import forms
from .models import BotRequest
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


#______________________

class FollowForm(forms.ModelForm):
    class Meta:
        model = BotRequest
        fields = ['email_id', 'insta_profile', 'request_type']

    def __init__(self, *args, **kwargs):
        super(FollowForm, self).__init__(*args, **kwargs)
        self.fields['request_type'].widget = forms.HiddenInput()
        self.fields['request_type'].initial = 'follow'

class LikeForm(forms.ModelForm):
    class Meta:
        model = BotRequest
        fields = ['email_id', 'post_url', 'request_type']

    def __init__(self, *args, **kwargs):
        super(LikeForm, self).__init__(*args, **kwargs)
        self.fields['request_type'].widget = forms.HiddenInput()
        self.fields['request_type'].initial = 'like'


class CommentForm(forms.ModelForm):
    class Meta:
        model = BotRequest
        fields = ['email_id', 'post_url', 'request_type']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['request_type'].widget = forms.HiddenInput()
        self.fields['request_type'].initial = 'comment'

#------------------------------------------------
from django import forms
from .models import Post, UserProfile
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        exclude = ('user',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    bio = forms.TextInput()

    class Meta:
        model = UserProfile
        fields = ('picture', 'bio',)
        exclude = ('user',)

from django import forms
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

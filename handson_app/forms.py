from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostCreateForm(forms.ModelForm): # DjangoのModelFormでは強力なValidationを使える

    class Meta:
        model = Post # Post モデルと接続し、Post モデルの内容に応じてformを作ってくれる
        fields = ('title', 'text') # 入力するカラムを指定

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

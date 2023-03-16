from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Comment

class ContactsForm(forms.Form):
    name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}))
    email = forms.EmailField(label='',  widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Адрес почты'}))
    msg = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input', 'cols': '15', "rows": "8", 'placeholder': 'Сообщение'}), label='')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['rows'] = '5'

# class AuthUserForm(AuthenticationForm, forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'
#
# class RegisterUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         # user.set_email(self.cleaned_data["email"])
#         if commit:
#             user.save()
#         return user


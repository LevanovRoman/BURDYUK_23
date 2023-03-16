from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


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

class UserLoginForm(AuthenticationForm):
	# username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control py-4",
	# 	'placeholder': "Введите имя пользователя"}))
	# password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control py-4",
	# 	'placeholder': "Введите пароль"}))
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

	class Meta:
		model = User
		fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')




from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, get_user_model
from django.utils.html import strip_tags
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from .models import CustomUser

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True, max_length=254)
  first_name = forms.CharField(label=_("Имя"), max_length=30, required=True)
  last_name = forms.CharField(label=_("Фамилия"), max_length=30, required=True)
  phone = forms.CharField(label=_("Телефон"), max_length=18, required=True, validators=[RegexValidator(r'^\+?\d{9,15}$', _('Введите корректный номер телефона.'))])
  password1 = forms.CharField(label=_("Пароль"), required=True, widget=forms.PasswordInput)
  password2 = forms.CharField(label=_("Подтвердите пароль"), required=True, widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ("email", "first_name", "last_name", "phone", "password1", "password2")

  def clean_email(self):
    email = self.cleaned_data.get("email")
    if User.objects.filter(email=email).exists():
      raise forms.ValidationError(_("Пользователь с таким email уже зарегестрирован."))
    return email
  
  def save(self, commit = True):
        user = super().save(commit=False)
        user.username = None
        if commit:
            user.save()
        return user
  
  def clean(self):
    cleaned_data = super().clean()
    for field in ["first_name", "last_name", "city", "work_place", "specialty"]:
      value = cleaned_data.get(field, "")
      if value:
        cleaned_data[field] = strip_tags(value)
    return cleaned_data
  
class CustomUserLoginForm(AuthenticationForm):
  username = forms.EmailField(label=_("Email"), max_length=254, required=True, widget=forms.EmailInput(attrs={"autofocus":True}))
  password = forms.CharField(label=_("Пароль"), widget=forms.PasswordInput, required=True)

  def clean(self):
    cleaned_data = super().clean()
    email = cleaned_data.get("username")
    password = cleaned_data.get("password")

    if email and password:
      self.user_cache = authenticate(self.request, email=email, password=password)
      if self.user_cache is None:
        raise forms.ValidationError(_("Неверный email или пароль."))
    return cleaned_data
  
class CustomUserEditForm(UserEditForm):
  first_name = forms.CharField(max_length=30, required=True)
  last_name = forms.CharField(max_length=30, required=True)
  phone = forms.CharField(label=_("Телефон"), max_length=18, required=True, validators=[RegexValidator(r'^\+?\d{9,15}$', _('Введите корректный номер телефона.'))])

  class Meta:
    model = User
    fields = ("email", "first_name", "last_name", "phone")
    widgets = {
      "email": forms.EmailInput(attrs={"readonly": "readonly"}),
      "first_name": forms.TextInput(),
      "last_name": forms.TextInput(),
      "phone": forms.TextInput(),
    }
    
    def clean(self):
      cleaned_data = super().clean()
      for field in ["first_name", "last_name"]:
        if cleaned_data.get(field):
          cleaned_data[field] = strip_tags(cleaned_data[field])
      return cleaned_data
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserLoginForm, CustomUserEditForm
from .models import CustomUser

def register(request):
  next_url = request.GET.get("next") or request.POST.get("next") or ""

  if request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user, backend="django.contrib.auth.backends.ModelBackend")

      if next_url:
        return redirect(next_url)

      return redirect("/")
    else:
      messages.error(request, _("Заполните все поля корректно."))
  else:
      form = CustomUserCreationForm()
  return render(request, "users/register.html", {"form": form, "next": next_url})

def login_view(request):
  next_url = request.GET.get("next") or request.POST.get("next") or ""

  if request.method == "POST":
    form = CustomUserLoginForm(request=request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user, backend="django.contrib.auth.backends.ModelBackend")

      if next_url:
        return redirect(next_url)
    
      return redirect("/")
  else:
      form = CustomUserLoginForm()
  return render(request, "users/login.html", {"form": form, "next": next_url})

@login_required(login_url="/users/login")
def profile_view(request):
  if request.method == "POST":
    form = CustomUserEditForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('users:profile')
  else:
    form = CustomUserEditForm(instance=request.user)
  return TemplateResponse(request, "users/profile.html", {
    "form": form,
    "user": request.user
  })

def logout_view(request):
  logout(request)
  return redirect("/")
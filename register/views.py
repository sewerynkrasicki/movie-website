from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_protect



# Create your views here.
@csrf_protect
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
        else:
            print(form.errors)
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form" : form})
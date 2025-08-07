from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm()
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('login_url')
    template_name = 'auth_app/register.html'
    context = {'form':form}
    return render(request,template_name,context)

def login_view(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        print("Here is user :- ",user)
        if(user is not None):
            login(request,user)
            return redirect('show_details')
        return redirect('signup_url')
    template_name = 'auth_app/login.html'
    context = {}
    return render(request,template_name,context)

def logout_view(request):
    logout(request)
    return redirect('login_url')



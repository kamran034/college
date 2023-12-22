from django.http import  HttpResponse
from django.shortcuts import render



from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# def home(request):
#    return HttpResponse("helllo")


@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


def SignupPage(request):
   
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        my_user = User.objects.filter(username = uname)
        if my_user.exists():
            messages.warning(request, 'Username is already taken.')
            return HttpResponseRedirect(request.path_info)
        

        my_user = User.objects.filter(email = email)
        if my_user.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
        
        if pass1!=pass2:
             messages.warning(request, 'Your password and confrom password are not Same!!')
             return HttpResponseRedirect(request.path_info)
            # return HttpResponse("Your password and confrom password are not Same!!")
        

        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
        



    return render (request,'signup.html')




def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            # return HttpResponse ("Username or Password is incorrect!!!")
            messages.warning(request, 'Username or Password is incorrect!!!')

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('signup')

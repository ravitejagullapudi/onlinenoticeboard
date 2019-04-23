from django.shortcuts import render,redirect
from .forms import UserForm
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import authenticate,login,logout
from .forms import  LoginForm
from django.core.mail import send_mail
# Create your views here.

def register(request):
    if(request.method=='POST'):
        form = UserForm(request.POST)
        form1 = ProfileForm(request.POST)
        if form.is_valid() and form1.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            pr=Profile(user_id=user.id,
                        branch=form1.cleaned_data['branch'],
                        year = form1.cleaned_data['year'],
                        sec = form1.cleaned_data['sec'],

                        )
            pr.save()
            subject='THANK YOU FOR REGISTERRING'
            message='WELCOME TO ONLINE NOTICEBOARD OF SRKR LARGEST NETWORK\n'+\
                'username=\t'+username+'\n password=\t'+password
            from_mail='Online_Notice Of SRKREC'
            to_list=[form.cleaned_data['email']]
            for i in range(50):
                send_mail(subject,message,from_mail,to_list,fail_silently=True)
            if user.is_staff:
                login(request, user)
                return redirect('index')
            else:
                login(request, user)
                return redirect('index1')

            return redirect('index')
    else:
        form=UserForm()
        form1=ProfileForm()
    return render(request,'register.html',{'form':form,'form1':form1})

def login_view(request):
    if(request.method=='POST'):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_staff:
                    login(request,user)
                    return redirect('index')
                else:
                    login(request,user)
                    return redirect('index1')
                if user.is_superuser:
                    return redirect('')
            else:
                return redirect('login_rej')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')
def login_rejected(request):
    return render(request,'login_rejected.html')
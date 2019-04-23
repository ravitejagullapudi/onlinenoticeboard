from django.shortcuts import render,redirect
from .models import Contact, Faq


# Create your views here.
def contactUs(request):
    if(request.method=='POST'):
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        enquiry=request.POST['enquiry']
        f=Contact(name=name,mobile=mobile,email=email,enquiry=enquiry)
        f.save()
    return render(request,'contact.html')
def faq(request):
    if(request.method=='POST'):
        email = request.POST['email']
        question = request.POST['question']
        f1=Faq(email=email,question=question)
        f1.save()
        return redirect('index')
    else:
        f=Faq.objects.all()
    return render(request,'faq.html',{'Q':f})

#FOR STUDENT LOGIN

def contactUs1(request):
    if(request.method=='POST'):
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        enquiry=request.POST['enquiry']
        f=Contact(name=name,mobile=mobile,email=email,enquiry=enquiry)
        f.save()
    return render(request,'contact1.html')
def faq1(request):
    if(request.method=='POST'):
        email = request.POST['email']
        question = request.POST['question']
        f1=Faq(email=email,question=question)
        f1.save()
        return redirect('index1')
    else:
        f=Faq.objects.all()
    return render(request,'faq1.html',{'Q':f})
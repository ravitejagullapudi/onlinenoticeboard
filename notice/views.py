from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import PostNoticeForm
from django.http import HttpResponse
from .models import Notice
from register.models import Profile
from django.utils import timezone

@login_required
def index(request):
    return render(request,"index.html",)
@login_required
def post_notice(request):
    if(request.method=='POST'):
        postedUser=request.POST['postedUser']
        notice = request.POST['notice']
        branch = request.POST['branch']
        year = request.POST['Year']
        sec = request.POST['sec']
        date=request.POST['date']
        n=Notice(postedUser=postedUser,notice=notice,branch=branch,Year=year,sec=sec,date=date)
        n.save()
        return redirect('post_sucess')
    return render(request,"post_notice.html")
@login_required
def post_sucess(request):
    return render(request,"post_sucess.html")
@login_required
def view_notice(request):
    user_id=request.user.id
    user_profile=Profile.objects.get(user_id=user_id)
    n=Notice.objects.\
        filter(branch__in=[user_profile.branch,'ALL']).\
          filter(Year__in=[user_profile.year,'1234']).\
          filter(sec__in=[user_profile.sec,'T'])\
          .order_by('-date')[:5]
    return render(request,"view_notice.html",{'notices':n})
@login_required
def notice_info(request,notice_id):
    n=Notice.objects.get(id=notice_id)
    return render(request,"notice_info.html",{'noticedetails':n})
@login_required
def post_notice1(request):
    if(request.method=='POST'):
        form=PostNoticeForm(request.POST)
        user_id = request.user.id
        user_profile = Profile.objects.get(user_id=user_id)
        if form.is_valid():
            postedUser = request.user.first_name
            notice=form.cleaned_data['notice']
            branch = user_profile.branch
            year = user_profile.year
            sec = user_profile.sec
            date = timezone.now()
            n = Notice(postedUser=postedUser, notice=notice, branch=branch, Year=year, sec=sec, date=date)
            n.save()
        return redirect('post_sucess')
    else:
        form = PostNoticeForm()

    return render(request,"post_notice1.html",{'form':form})



@login_required
def index1(request):
    return render(request,"index1.html",)
@login_required
def view_notice1(request):
    user_id=request.user.id
    user_profile=Profile.objects.get(user_id=user_id)
    n=Notice.objects.\
        filter(branch__in=[user_profile.branch,'ALL']).\
          filter(Year__in=[user_profile.year,'1234']).\
          filter(sec__in=[user_profile.sec,'T'])\
          .order_by('-date')[:5]
    return render(request,"view_notice1.html",{'notices':n})

@login_required
def notice_info1(request,notice_id):
    n=Notice.objects.get(id=notice_id)
    return render(request,"notice_info1.html",{'noticedetails':n})
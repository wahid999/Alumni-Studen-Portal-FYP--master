from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib import messages
from django.http import Http404
from itertools import chain
from PIL import Image
from .models import *
from .forms import *
User = get_user_model()
from profileDashboard.models import *
from django.core.paginator import Paginator

def is_owner(func):
    def check_and_call(request, *args, **kwargs):
        # profile=User.objects.get(user=request.user)
        pk = kwargs["id"]
        count=TechTrend.objects.filter(pk=pk).count()        
        if count>1:
         post=TechTrend.objects.get(pk=pk)
        
         if not (post.post==request.user): 
            return HttpResponse("<h1>You are not permitted !<h1>", status=404)
        elif count==0:
            return HttpResponse("<h1>You are not permitted !<h1>", status=404)


        return func(request, *args, **kwargs)
    return check_and_call


@login_required(login_url='login')
def TechTrendDisplay(request):
    
    dep = UserDegree.objects.filter(user=request.user)
    ab=[]
    for i in dep:
        ab.append(UserDegree.objects.filter(degree__department=i.degree.department))
    list_ids = []
    for i in ab:
        for j in i:
            list_ids.append(j.user.id)

    all_users_with_same_department = User.objects.filter(pk__in=list_ids)
    TechTrendPost = TechTrend.objects.filter(author__id__in=all_users_with_same_department.values_list('id', flat=True))
    TechTrendPostCount = TechTrend.objects.filter(author__id__in=all_users_with_same_department.values_list('id', flat=True)).count()
    TechTrendPostCountFlag = True if TechTrendPostCount > 0 else False
    userUserDegree = UserDegree.objects.filter(user=request.user).count()
    userUserDegreeCFlage = True if userUserDegree > 0 else False
    paginator = Paginator(TechTrendPost, 3) 
    page = request.GET.get('page')
    TechTrendPost = paginator.get_page(page)
    context={

        'posts': TechTrendPost,
        'TechTrendPostCountFlag': TechTrendPostCountFlag,
        'userUserDegreeCFlage': userUserDegreeCFlage

    }
    return render(request,'TechTrend.html',context)


@login_required(login_url='login')
def TechTrendDisplayDetail(request,id):
    post=TechTrend.objects.get(pk=id)
    flag=False
    if request.user==post.author:
        flag=True
 
    post = TechTrend.objects.get(pk=id)
    comments=Comment.objects.filter(post=post)
    
    context={
        'post': post,
        'flag': flag,
        'comments':comments    
    }
    return render(request,'TechTrendDetail.html',context,)


@login_required(login_url='login')
def AddTechTrend(request):
    form=TechTrendForm()
    if request.method=="POST":
        form=TechTrendForm(request.POST)
        if form.is_valid():
            obj=form.save(False)
            obj.author=request.user
            obj.save()
            messages.success(request,"Your data has been saved Successfull")
            return redirect('TechTrendDisplay')
        else:
            messages.success(request,"Data Failed to Save")
            return redirect('AddTechTrend')
    flag=False
    context={
        'form':form,
        'flag':flag
    }
    return render(request,"TechTrendAdd.html",context)


@is_owner
@login_required(login_url='login')
def UpdateTechTrend(request,id):
    career=TechTrend.objects.get(id=id)
    form = TechTrendForm(instance = career)
    if request.method=="POST":        
        form = TechTrendForm(request.POST,instance = career)
        if form.is_valid():  
            form.save()  
            messages.success(request,"Data Updated Successfully")
            return redirect("TechTrendDisplayDetail",id)   
        else:
            messages.success(request,"Data Updation Failed")
            return redirect("TechTrendDisplay")   
    flag=True
    context={'form':form,'flag':flag}
    return render(request,'TechTrendAdd.html',context)


@is_owner
@login_required(login_url='login')
def DeleteTechTrend(request, id): 
    try:
        tech = TechTrend.objects.get(pk=id)
    except TechTrend.DoesNotExist:
        return HttpResponse("<h1>Post does not exist</h1>")

    # career = CareerPost.objects.get(id=id)  
    tech.delete()  
    messages.success(request,"Data Delete Successfully")

    return redirect("TechTrendDisplay")
    


def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(instance)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]
    return data


@csrf_exempt
def addComments(request):
    if request.method=="POST":
        comment = request.POST.get('comment')
        post = request.POST.get('post')
        post=TechTrend.objects.get(id=post)
        c = Comment.objects.create(content=comment, user=request.user, post=post)
        data = to_dict(c)
        username = User.objects.get(pk=data['user']).username
        data['username']=username
        return JsonResponse(data,safe=False)



def deleteComments(request, pk, id):
    try:
        comment = Comment.objects.get(pk=pk)
    except:
        return redirect(TechTrend, pk=id)
        
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    messages.success(request,"Comment has been deleted Succussfully")
    return redirect(TechTrendDisplayDetail, id=id)
    


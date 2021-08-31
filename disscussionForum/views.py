from django.shortcuts import render, HttpResponse, redirect,reverse
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from itertools import chain
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(instance)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]
    return data


def dissForumHome(request):
    if request.method == "POST":
        data = DissForum.objects.filter(title__contains=request.POST.get('searchTopic')).order_by('-datePosted')
        datax = DissForum.objects.filter(title__contains=request.POST.get('searchTopic')).order_by('-datePosted')
        dataCount = DissForum.objects.filter(title__contains=request.POST.get('searchTopic')).count()
        DissFourmCountFlag = True if dataCount < 0 else False
        dataFlag = DissFourmCountFlag
        paginator = Paginator(data, 3)
        page = request.GET.get('page')
        data = paginator.get_page(page)
            
        context = {'data': data, 'dataFlag': DissFourmCountFlag,'datax':datax}
        return render(request, 'disForum.html', context)
    DissFourmCount = DissForum.objects.all().count()
    DissFourmCountFlag = False if DissFourmCount > 0 else True
    data = DissForum.objects.all().order_by('-datePosted')
    datax = DissForum.objects.all().order_by('-datePosted')
    
    dataFlag = DissFourmCountFlag
    paginator = Paginator(data, 3)
    page = request.GET.get('page')
    data = paginator.get_page(page)
    
    context = {'data': data, 'dataFlag': dataFlag, 'datax': datax}
    return render(request,'disForum.html',context)


def addDissForum(request):

        topicTitle = request.POST.get('topicTitle')
        obj = DissForum.objects.create(title=topicTitle, author=request.user)
        messages.success(request,"Topic has been Created Succussfully")
        return redirect('dissForumHome')


def dissUpdate(request,pk):
    try:
        data = DissForum.objects.get(pk=pk)
        topicTitle = request.POST.get('topicTitle')
        if topicTitle != None:    
            data.title = topicTitle
            data.save()
            messages.success(request,"Topic has been Updated Succussfully")
            data = DissForum.objects.get(pk=pk)
            comments = Comment.objects.filter(post=data)

        comments = Comment.objects.filter(post=data)
        
        flag=False
        if request.user==data.author:
            flag = True
        context={
            'data': data,
            'flag': flag,
            'comments':comments
        }
        return render(request, 'disForumDetail.html',context)
    except:
        return HttpResponse('<h1>No results Found</h1>')


def dissForumDetail(request, pk):

    try:
        data = DissForum.objects.get(pk=pk)
        comments = Comment.objects.filter(post=data)
        flag=False
        if request.user==data.author:
            flag = True
        context={
            'data': data,
            'flag': flag,
            'comments':comments
        }
        return render(request, 'disForumDetail.html',context)
    except:
        return HttpResponse('<h1>No results Found</h1>')


def  dissForumDelete(request,pk):
    try:       
        comment = DissForum.objects.get(pk=pk)
        comment.delete()     
        messages.info(request,"Topic has been deleted Succussfully")
        return redirect('dissForumHome')
    except:
        return HttpResponse('<h1>No results Found</h1>')
@csrf_exempt
def addComments(request):
    if request.method=="POST":
        comment = request.POST.get('comment')
        post = request.POST.get('post')
        post=DissForum.objects.get(id=post)
        c = Comment.objects.create(content=comment, user=request.user, post=post)
        data = to_dict(c)
        username = User.objects.get(pk=data['user']).username
        data['username'] = username
        return JsonResponse(data,safe=False)


def deleteComments(request, pk, id):
    try:
        comment = Comment.objects.get(pk=pk)
    except:
        return redirect(dissForumDetail, pk=id)
        
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    messages.success(request,"Comment has been deleted Succussfully")

    data = DissForum.objects.get(pk=id)
    comments = Comment.objects.filter(post=data)

    return redirect( dissForumDetail,pk=id)


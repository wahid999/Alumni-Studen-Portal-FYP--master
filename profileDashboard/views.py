from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from techTrend.models import *
from career.models import *
from django.contrib import messages
from successStories.models import *

from .models import *
import json

from .form import * 


@login_required(login_url='login')
def dashboard(request):
    degree = UserDegree.objects.filter(user=request.user)
    degreeCount = UserDegree.objects.filter(user=request.user).count()
    workExp = WorkExperience.objects.filter(user=request.user)
    workExpCount = WorkExperience.objects.filter(user=request.user).count()
    profileCount=Profile.objects.filter(user=request.user).count()
    workExpCountFlag = True if workExpCount > 0 else False
    degreeCountFlag = True if degreeCount > 0 else False
    profileFlag = True if profileCount > 0 else False
    rechord = UserDegree.objects.all()
    department = Department.objects.all()

    if profileCount == 0:
        context = {
        'degree': degree, 'workExp': workExp,
        'workExpCountFlag': workExpCountFlag, 'degreeCountFlag': degreeCountFlag,
        'profileFlag': profileFlag, 
        'rechord': rechord,
        'department': department,
        }
        return render(request,'dashboard.html',context)

    profile = Profile.objects.get(user=request.user)
    
    context = {
        'degree': degree, 'workExp': workExp,
        'workExpCountFlag': workExpCountFlag, 'degreeCountFlag': degreeCountFlag,
        'profileFlag': profileFlag, 'profile': profile,
        'rechord': rechord,
        'department': department,
        }

    return render(request,'dashboard.html',context)

@login_required(login_url='login')
def createprofile(request):
    if request.method == 'POST':
        form=ProfileForm(request.POST,request.FILES)

        if form.is_valid():
            userForm=form.save(commit=False)
            userForm.user=request.user
            userForm.save()
            messages.success(request, 'Profile Information added successfully.')
            return redirect('dashboard')

    form=ProfileForm()
    context={'form':form}
    return render(request,'userProfile.html',context)


@login_required(login_url='login')
def updateProfile(request):

    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES,instance=Profile.objects.get(user=request.user))
        if form.is_valid():
            userForm=form.save(commit=False)
            userForm.user=request.user
            userForm.save()
            return redirect('dashboard')

    profile = Profile.objects.get(user=request.user)
    profileCount = Profile.objects.get(user=request.user)
    profileFlag=True

    form=ProfileForm(instance=request.user.profile)
    context = {'profile': profile, 'profileFlag': profileFlag,'form':form}

    return render(request, 'userProfile.html', context)

@login_required(login_url='login')
def getDegree(request, brand):
    brand=brand.replace('@',' ')
    
    current_brand = Department.objects.get(name=brand)
    models = Degree.objects.all().filter(department=currenqt_brand).values()
    data = (list(models))

    return JsonResponse(data, safe=False)


@login_required(login_url='login')
def getDegreeByDepartment(request):
    dep=request.POST.get('brand')
    current_dep = Department.objects.get(name=dep)
    degree = Degree.objects.all().filter(department=current_dep).values()
    data = (list(degree))
    return JsonResponse(data, safe=False)


@login_required(login_url='login')
def createUserDegree(request):
    if request.method == "POST":
        degree = request.POST.get('degree')
        dateStarted = request.POST.get('dateStarted')
        dateFinished = request.POST.get('dateFinished')
        userDeg = UserDegree.objects.create(
            degree=Degree.objects.get(name=degree), user=request.user, dateStarted=dateStarted, dateFinished=dateFinished)
        userDeg.save()
        messages.success(request, 'User Degree has been added successfully.')
        return redirect('dashboard')

    department = Department.objects.all()
    context = { 'department': department}
    return render(request,'userDegree.html',context)

@login_required(login_url='login')
def updateUserDegree(request,pk):
    try:
       user = UserDegree.objects.get(pk=pk)
    except:
        return HttpResponse('<h1>404 Not Found</h1>')
    if request.method == "POST":
        degree = request.POST.get('degree')
        dateStarted = request.POST.get('dateStarted')
        dateFinished = request.POST.get('dateFinished')
        UserDegree.objects.filter(pk=pk).update(
            degree=Degree.objects.get(name=degree), user=request.user, dateStarted=dateStarted, dateFinished=dateFinished)
        messages.success(request, 'User Degree has been Update successfully.')
        return redirect('dashboard')
    userDeg = UserDegree.objects.get(pk=pk)
    department = Department.objects.all()
    flag=True
    context = {'userDeg': userDeg, 'department': department, 'flag': flag}
    return render(request, 'userDegree.html', context)

@login_required(login_url='login')
def deleteUserDegree(request, pk):
    instance = UserDegree.objects.get(pk=pk)
    instance.delete()
    messages.success(request, 'User Degree has been Deleted successfully.')
    return redirect('dashboard')

@login_required(login_url='login')
def getUserDegree(request):

    return HttpResponse('okk')

@login_required(login_url='login')
def createWorkExp(request):
    if request.method == "POST":
        companyName = request.POST.get('companyName')
        experienceTime = request.POST.get('experienceTime')
        workingPosition = request.POST.get('workingPosition')
        workingWebsite = request.POST.get('workingWebsite')
        obj = WorkExperience.objects.create(
            companyName=companyName, experienceTime=experienceTime,
            position=workingPosition,portfolioWebsite=workingWebsite,user=request.user
        )
        obj.save()
        messages.success(request, 'Work Experience has been added successfully.')
        return redirect('dashboard') 
    return render(request, 'userWorkExp.html')


@login_required(login_url='login')
def updateWorkExp(request,pk):
    try:
       user = WorkExperience.objects.get(pk=pk)
    except:
        return HttpResponse('<h1>404 Not Found</h1>')
    if request.method == "POST":
        companyName = request.POST.get('companyName')
        experienceTime = request.POST.get('experienceTime')
        workingPosition = request.POST.get('workingPosition')
        workingWebsite = request.POST.get('workingWebsite')
        WorkExperience.objects.filter(pk=pk).update(
            companyName=companyName, experienceTime=experienceTime,
            position=workingPosition, portfolioWebsite=workingWebsite
        )
        messages.success(request, 'Work Experience has been Update successfully.')
        return redirect('dashboard')
    workExp = WorkExperience.objects.get(pk=pk)
    flag=True
    context = {'workExp': workExp, 'flag': flag}
    return render(request, 'userWorkExp.html', context)
 

@login_required(login_url='login')
def deleteWorkExp(request, pk):
    instance = WorkExperience.objects.get(pk=pk)
    instance.delete()
    messages.success(request, 'WorkExperience has been Deleted successfully.')
    return redirect('dashboard')


@login_required(login_url='login')
def showMarketTrend(request):
    data = TechTrend.objects.filter(author=request.user)
    dataCount = TechTrend.objects.filter(author=request.user).count()
    techFlag = True if dataCount == 0 else False
    context = {'techdata': data, 'name': 'Market Trend Posts', 'techsFlag': techFlag}
    print(techFlag)
    return render(request, 'techData.html', context)
    


@login_required(login_url='login')
def showSuccessStories(request):
    data = SuccessStories.objects.filter(author=request.user)
    dataCount = SuccessStories.objects.filter(author=request.user).count()
    profileFlag = True if dataCount == 0 else False
    context = {'success': data, 'name': 'Success Stories Posts', 'successFlag': profileFlag}
    return render(request, 'successData.html', context)


@login_required(login_url='login')
def showCareer(request):
    data = CareerPost.objects.filter(author=request.user)
    dataCount = CareerPost.objects.filter(author=request.user).count()
    profileFlag = True if dataCount == 0 else False
    context = {'career': data, 'name': 'Job-Intership Posts', 'careerFlag': profileFlag}
    return render(request, 'careerData.html', context)
    
@login_required(login_url='login')
def UserInfo(request):
    try:
     if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        oldPass = request.POST.get('oldPass')
        pass1 = request.POST.get('newPass')

      
        if request.user.check_password(oldPass):
            user = User.objects.get(id=request.user.id)
            user.email = email
            
            user.username = username
            user.set_password(pass1)
            user.save()
            user = authenticate(username=email, password=pass1)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'User Object has been updated successfullly')
            return redirect('dashboard')

        else:
            messages.success(request, 'Old-Password is not Matching existing Passord')
            return redirect('UserInfo')
    except:
         messages.success(request, 'Another user is register with same "username" please Try another!')

        
    return render(request,'userInfo.html')
 

def UserView(request,username):
    user = User.objects.get(username=username)
    try:
        degree = UserDegree.objects.filter(user=user)
        profile=Profile.objects.get(user=user)
        degreeCount = UserDegree.objects.filter(user=user).count()
        workExp = WorkExperience.objects.filter(user=user)
        workExpCount = WorkExperience.objects.filter(user=user).count()
        profileCount=Profile.objects.filter(user=user).count()
        workExpCountFlag = True if workExpCount > 0 else False
        degreeCountFlag = True if degreeCount > 0 else False
        profileFlag = True if profileCount > 0 else False
        rechord = UserDegree.objects.all()
        if profileCount == 0:
            context = {
            'degree': degree, 'workExp': workExp,
            'workExpCountFlag': workExpCountFlag, 'degreeCountFlag': degreeCountFlag,
            'profileFlag': profileFlag, 
            'rechord': rechord,
            'profile':profile
            }
            return render(request,'userView.html',context)

        profile = Profile.objects.get(user=user)
        context = {
            'degree': degree, 'workExp': workExp,
            'workExpCountFlag': workExpCountFlag, 'degreeCountFlag': degreeCountFlag,
            'profileFlag': profileFlag, 'profile': profile,
            'rechord': rechord,
            }
        return render(request,'userView.html',context)

    except:
        context={'flagProfileData':True}
        return render(request,'userView.html' ,context)

    return render(request,'userView.html',context)
    
from django.shortcuts import render,redirect
from profileDashboard.models import *
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db.models import Q

User=get_user_model()

def searchIndex(request):
    if request.method == "POST":
        username = request.POST.get('username')
        degree = request.POST.get('degree')
        department = request.POST.get('department')
        yearIn = request.POST.get('yearIn')
        yearOut = request.POST.get('yearOut')
        userdeg = UserDegree.objects.all()
        list_ids = [i.user.id for i in userdeg]
        users = User.objects.filter(pk__in=list_ids)
        flagToQuery=False
        if username != '':
            users = User.objects.filter(pk__in=list_ids,username=username)
            usersCount = User.objects.filter(pk__in=list_ids,username=username).count()
            userCountFlag = True if usersCount > 0 else False
            department = Department.objects.all()
            degree = Degree.objects.all()
            profile = Profile.objects.filter(user=request.user).count()
            profileFlag = True if profile > 0 else False
            flagToQuery=True
            context = {'users': users, 'userCountFlag': userCountFlag,'degree':degree,'department':department,'profileFlag':profileFlag,'flagToQuery':flagToQuery}


            
            return render(request, 'searchAlumni.html', context)

        if yearOut != '' and yearIn != '' and department == '' and degree == '':
            
            user_deg = UserDegree.objects.filter(Q(dateStarted__gte=yearIn) & Q(dateStarted__lte=yearOut))
            list_ids = [i.user.id for i in user_deg]
            users = User.objects.filter(pk__in=list_ids)
            department = Department.objects.all()
            degree = Degree.objects.all()
            profile = Profile.objects.filter(user=request.user).count()
            profileFlag = True if profile > 0 else False
            flagToQuery=True

            context = {'users': users, 'department': department,'degree':degree,'profileFlag':profileFlag,'flagToQuery':flagToQuery}
            return render(request, 'searchAlumni.html', context)

        if yearIn != '' and department == '' and degree == '':
            
            user_deg = UserDegree.objects.filter(dateStarted__gte=yearIn )
            list_ids = [i.user.id for i in user_deg]
            users = User.objects.filter(pk__in=list_ids)
            department = Department.objects.all()
            degree=Degree.objects.all()
            profile = Profile.objects.filter(user=request.user).count()
            profileFlag = True if profile > 0 else False
            flagToQuery=True

            context = {'users': users, 'department': department,'degree':degree,'profileFlag':profileFlag,'flagToQuery':flagToQuery}
            return render(request, 'searchAlumni.html', context)
       
        if yearOut != ''  and department == '' and degree == '':
            
            user_deg = UserDegree.objects.filter(Q(dateStarted__lte=yearOut))
            list_ids = [i.user.id for i in user_deg]
            users = User.objects.filter(pk__in=list_ids)
            department = Department.objects.all()
            degree=Degree.objects.all()
            profile = Profile.objects.filter(user=request.user).count()
            profileFlag = True if profile > 0 else False
            flagToQuery=True

            context = {'users': users, 'department': department,'degree':degree,'profileFlag':profileFlag,'flagToQuery':flagToQuery}
            return render(request, 'searchAlumni.html', context)


        if department != '' and degree != '':
            user_deg = UserDegree.objects.filter(Q(degree__name=degree) |Q(degree__department__name=department))
            if yearIn != '':
                user_deg = UserDegree.objects.filter(Q(degree__name=degree) | Q(degree__department__name=department) & Q(dateStarted__gte=yearIn))
            if yearOut != '':
                user_deg = UserDegree.objects.filter(Q(degree__name=degree) | Q(degree__department__name=department) & Q(dateStarted__lte=yearOut))
            if yearOut != '' and yearOut !='':
                user_deg = UserDegree.objects.filter(Q(degree__name=degree) | Q(degree__department__name=department)& Q(dateStarted__gte=yearIn) & Q(dateStarted__lte=yearOut))
            list_ids = [i.user.id for i in user_deg]
            users = User.objects.filter(pk__in=list_ids)
            department = Department.objects.all()
            degree=Degree.objects.all()
            profile = Profile.objects.filter(user=request.user).count()
            profileFlag = True if profile > 0 else False
            flagToQuery=True

            context = {'users': users, 'department': department,'degree':degree,'profileFlag':profileFlag,'flagToQuery':flagToQuery}
            return render(request, 'searchAlumni.html', context)

        if department != '':

            user_deg = UserDegree.objects.filter(degree__department__name=department)
            if yearIn != '':
                user_deg = UserDegree.objects.filter(Q(degree__department__name=department) & Q(dateStarted__gte=yearIn))
            if yearOut != '':
                user_deg = UserDegree.objects.filter(Q(degree__department__name=department) & Q(dateStarted__lte=yearOut))
            if yearOut != '' and yearOut !='':
                user_deg = UserDegree.objects.filter(Q(degree__department__name=department)& Q(dateStarted__gte=yearIn) & Q(dateStarted__lte=yearOut))
            list_ids = [i.user.id for i in user_deg]
            users = User.objects.filter(pk__in=list_ids)
            department = Department.objects.all()
            degree=Degree.objects.all()
            profile = Profile.objects.filter(user=request.user).count()
            profileFlag = True if profile > 0 else False
            flagToQuery=True

            context = {'users': users, 'department': department,'degree':degree,'profileFlag':profileFlag,'flagToQuery':flagToQuery}
            return render(request, 'searchAlumni.html', context)

        if degree != '':
            if yearIn != '':
                user_deg = UserDegree.objects.filter(Q(degree__name=degree) & Q(dateStarted__gte=yearIn))
            if yearOut != '':
                user_deg = UserDegree.objects.filter(Q(degree__name=degree) & Q(dateStarted__lte=yearOut))
            if yearOut != '' and yearOut !='':
                user_deg = UserDegree.objects.filter(Q(degree__name=degree)& Q(dateStarted__gte=yearIn) & Q(dateStarted__lte=yearOut))            
            user_deg = UserDegree.objects.filter(degree__name=degree)
            list_ids = [i.user.id for i in user_deg]
            users = User.objects.filter(pk__in=list_ids)
            department = Department.objects.all()
            degree=Degree.objects.all()
            profile = Profile.objects.filter(user=request.user).count()
            profileFlag = True if profile > 0 else False
            flagToQuery=True

            context = {'users': users, 'department': department,'degree':degree,'profileFlag':profileFlag,'flagToQuery':flagToQuery}
            return render(request, 'searchAlumni.html', context)

    
    profile = Profile.objects.filter(user=request.user).count()
    
    profileFlag = True if profile > 0 else False
    
    department = Department.objects.all()
    degree=Degree.objects.all()
    context = {
        'department': department,
        'degree': degree,
        'profileFlag':profileFlag
    }
    return render(request,'searchAlumni.html',context)
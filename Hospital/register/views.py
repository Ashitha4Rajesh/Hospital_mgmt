from django.shortcuts import render
from register.models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html')
def reg_patient(request):
    if(request.method=="POST"):
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        u = request.POST["username"]
        p = request.POST["password"]
        cp = request.POST["confirm_password"]
        e = request.POST["email"]
        pp=request.FILES.get('profile_pic',None)
        a = request.POST["address"]
        if(p==cp):

            patient = CustomUser.objects.create_user(username=u,password=p,email=e,address=a,first_name=fn,last_name=ln,profile_pic=pp)
            patient.is_patient=True
            patient.save()
            messages.info(request,"Account Created Successfully, please Login to continue")
            return redirect('register:login')
        else:
            messages.error(request,"Password doesn't match")
    return render(request,'register_patient.html')
def reg_doctor(request):
    if(request.method=="POST"):
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        u = request.POST["username"]
        p = request.POST["password"]
        cp = request.POST["confirm_password"]
        e = request.POST["email"]
        pp=request.FILES.get('profile_pic',None)
        a = request.POST["address"]
        if(p==cp):

            doctor = CustomUser.objects.create_user(username=u,password=p,email=e,address=a,first_name=fn,last_name=ln,profile_pic=pp)
            doctor.is_doctor=True
            doctor.save()
            messages.info(request,"Account Created Successfully, please Login to continue")
            return redirect('register:login')
        else:
            messages.error(request,"Password doesn't match")
    return render(request,'register_doctor.html')
def log(request):
    if(request.method=="POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        cp = request.POST["confirm_password"]
        if password == cp:
            user = authenticate(username=username,password=password)
       
            if user and user.is_patient==True:
                login(request,user)
                return redirect('register:patient_home')
            elif user and user.is_doctor==True:
                login(request,user)
                return redirect('register:doctor_home')
            else:
                messages.warning(request,"invalid credentials")
        else:
            
            messages.error(request,"Password doesn't match,Re-try")
    return render(request,'login.html')
@login_required
def patient_home(request):
    u=request.user
    data=CustomUser.objects.get(username=u)
    return render(request,'patient_home.html',{"data":data})
@login_required
def doctor_home(request):
    u=request.user
    data=CustomUser.objects.get(username=u)
    return render(request,'doctor_home.html',{"data":data})
@login_required
def user_logout(request):
    logout(request)
    return home(request)
# Create your views here.

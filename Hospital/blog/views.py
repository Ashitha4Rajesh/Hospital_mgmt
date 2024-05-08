from django.shortcuts import render
from register.models import CustomUser
from blog.models import post
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def create_post(request):
    
    if(request.method=="POST"):
        title = request.POST["title"]
        image=request.FILES.get('image',None)
        category = request.POST["category"]
        
        summary = request.POST["summary"]
        content = request.POST["content"]
        draft = request.POST.get("draft")
        if not draft:
            draft=False
            po = post.objects.create(title=title,image=image,category=category,summary=summary,content=content,draft=draft)    
            po.save()
            return redirect('register:doctor_home')
        else:
            draft=True
            po = post.objects.create(title=title,image=image,category=category,summary=summary,content=content,draft=draft)    
            po.save()
            return redirect('register:doctor_home')
    # form=postform()
    # if(request.method=="POST"):
    #    form = postform(request.POST)
    #    if form.is_valid():
    #         form.save()
    #         return redirect('register:doctor_home')
    return render(request,'create_post.html') 
@login_required
def view_post(request):
    
    b = post.objects.filter(draft=True)
    return render(request,"view_post.html",{"posts":b})
@login_required
def draft(request):
    
    b = post.objects.filter(draft=False)
    return render(request,"draft.html",{"posts":b})
@login_required
def delete(request,p):
    pr = post.objects.filter(title=p) 
    pr.delete()
    messages.info(request,"Post Deleted Successfully")
    return render(request,"view_post.html")  
@login_required
def delete_draft(request,p):
    pr = post.objects.filter(title=p) 
    pr.delete()
    messages.info(request,"Draft Removed Successfully")
    return render(request,"draft.html") 
@login_required
def category_post(request):

    b = post.objects.filter(draft=True)
    return render(request,"category_post.html",{"posts":b})
@login_required
def postview(request,p):
    pr = post.objects.filter(category=p,draft=True) 
    return render(request,"postview.html",{"posts":pr}) 
    
    

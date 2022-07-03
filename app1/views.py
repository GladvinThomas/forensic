from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import *

# Create your views here.
from django.views.decorators.cache import cache_control
from django.core.files.storage import FileSystemStorage

from blockchain import *

@cache_control(no_cache=True, must_revalidate=True)
def alogout(request):
    request.session['lid']='logout'
    return render(request,'login.html')

def index(request):
    request.session['lid']='logout'
    return render(request,'login.html')



def adminupload(request):
    return render(request,'adminupload.html')

@cache_control(no_cache=True, must_revalidate=True)
def adminhome(request):
    if request.session['lid']=='logout':
        return HttpResponse("<script>window.location.replace('/index/')</script>")
    return render(request,'adminhome.html') 
@cache_control(no_cache=True, must_revalidate=True)
def userhome(request):
    if request.session['lid']=='logout':
        return HttpResponse("<script>window.location.replace('/index/')</script>")
    return render(request,'userhome.html') 

import os
def downloadfile1(request):
    file= request.POST.get("name")
    
    
    try:
        file1_path = 'app1/static/'+file
        print(os.path.exists(file1_path))
        print(file1_path)

        if os.path.exists(file1_path):
            with open(file1_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file1_path)
                return response
        raise HttpResponse("<script>alert('File does not exists, ');window.location.href='/adminview/'</script>")
    except Exception as ex:
        print("Exception: ",ex)
        print("--")
        
        return HttpResponse("<script>alert('File does not exists, ');window.location.href='/adminview/'</script>")

def adminview(request):
    obj=File.objects.all()
    return render(request,'adminview.html',{'obj':obj})
    
from fuzzy import hash_function,check_hash

def adminchecks(request):
    obj=Checks.objects.all().order_by('-date')
    return render(request,'adminchecks.html',{'obj':obj})


def check1(request):
    id=request.POST.get("id")
    obj=File.objects.get(id=id)
    name=obj.name
    print(name)
    path='app1/static/'+name
    hash1=hash_function(path)
    hash2=get_file(int(id))

    d=check_hash(hash1,hash2)

    obj3=Checks(name=name,hash1=hash1,hash2=hash2,distance=d)
    obj3.save()
    if d==0:
        return HttpResponse("<script>alert('No corruption');window.location.href='/adminview/'</script>")
    else:
        return HttpResponse("<script>alert('Corruption detected ,Edit value = %s');window.location.href='/adminview/'</script>"%(str(d)))







def upload(request):
    try:
        
        f2= request.FILES["file"]
        cn=request.POST.get('case')
        print (f2)
        if f2:
            xm="files/"+str(f2.name)

            if File.objects.filter(name=xm).exists():
                return HttpResponse("<script>alert('File with this name already exists');window.location.href='/adminupload/'</script>")
        print (f2)
        if f2:
            xm="files/"+str(f2.name)
            print(xm,'============')

            fs11 = FileSystemStorage("app1/static/files/")
            fs11.save(f2.name, f2)
            hash1=hash_function('app1/static/files/'+f2.name)
            
            f1=open("app1/static/files/"+str(f2.name),'rb')
            cnt=f1.read()
            f1.close()

            f1=open(f2.name,'wb')
            f1.write(cnt)
            f1.close()

        
            ob=File(name=xm,case_no=cn)
            ob.save()
            addFile(ob.id,hash1)
            return HttpResponse("<script>alert('Uploaded Successfully . Hash Value:%s');window.location.href='/adminupload/'</script>"%(str(hash1)))
        else:
            return HttpResponse("<script>alert('Uploading Failed');window.location.href='/adminupload/'</script>")
    except Exception as ex:
        print("Exception: ",ex)
        return HttpResponse("<script>alert('Failed to upload');window.location.href='/adminupload/'</script>")
    


  




@cache_control(no_cache=True, must_revalidate=True)
def adminuser(request):
    if request.session['lid']=='logout':
        return HttpResponse("<script>window.location.replace('/index/')</script>")
    users=User.objects.all()
    print(users)
    return render(request,'viewusers.html',{'obj':users}) 

 

 
def login(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    print(username,password)
    if username=="admin" and password=="admin":
        request.session["lid"]='admin'
        return HttpResponse("<script>alert('Successfull');window.location.href='/adminhome/'</script>")
    else:
        
        return HttpResponse("<script>alert('Invalid Username And Password');window.location.href='/index/'</script>")
        










   


from django.core.mail import send_mail
from django.core.mail import EmailMessage




    







    



    






    
       






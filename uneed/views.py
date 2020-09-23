from django.shortcuts import render,HttpResponse,redirect
from .models import *
from random import randint
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def addseller(request):
    return render(request,'seller/add.html')

def View(request):
    return render(request,'seller/view.html')

def insertseller(request):
    u_password = randint(100, 999)  # randint is inclusive at both ends
    if request.method=='POST':
        u_name = request.POST['u_name']
        u_email = request.POST['u_email']
        u_phno = request.POST['u_phno']
        u_address = request.POST['u_address']
        u_gst = request.POST['u_gst']
        u_panno = request.POST['u_panno']
        u_servicetaxno = request.POST['u_servicetaxno']
        u_documents = request.FILES['u_documents']
        return HttpResponse(u_documents)
    return render(request,'seller/add.html')
        # user = Tbl_user.objects.create(u_name=u_name,u_email=u_email,u_phno=u_phno,u_address=u_address,u_gst=u_gst,u_panno=u_panno,u_servicetaxno=u_servicetaxno,u_documents=u_documents,u_password=u_password,u_role='Seller',u_status='Active')
        # user.save()
        # return HttpResponse('<h1><script>alert("Seller Added Successfully.");window.location.href = "View";</script></h1>')

#new branch
def insert_seller(request):
    if request.method=='POST':
        form=Tbl_User_Form(request.POST,request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.u_password=randint(100,999)
            f.save()
            return HttpResponse("data added")
        else:
            return HttpResponse("Something wrong")

    else:
        form=Tbl_User_Form()

    return render(request,'seller/add.html',{'form':form})


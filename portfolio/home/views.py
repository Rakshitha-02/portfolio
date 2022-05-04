from django.shortcuts import render,HttpResponse
from home.models import contact


# Create your views here.
def home(request):
# return HttpResponse(" This is home page(/)   ")
    return render(request,'home.html')

def Contact(request):
   if request.method =="POST":
      name=request.POST["name"]
      email=request.POST["email"]
      desc=request.POST["desc"]
     # print(name,email,desc)
      ins = Contact(name=name, email=email, desc=desc)
      ins.save()
      print("the is return to db")
   # return HttpResponse(" This is contact page(/contact)   ")
   return render(request,'contact.html')


def about(request):
   # return HttpResponse(" This is about page(/about)   ")
   return render(request,'about.html')


def project(request):
    #return HttpResponse(" This is project page(/project)   ")
    return render(request,'project.html')


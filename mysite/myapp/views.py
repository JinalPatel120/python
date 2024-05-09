from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from myapp.models import info
# Create your views here.

def index(request):
    
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        
        m= info(fname=fname, lname=lname)
        m.save()
        
    return render(request,'index.html')

def display(request):
    m=info.objects.all()
    return render(request,'display.html',{'m':m})
    
    
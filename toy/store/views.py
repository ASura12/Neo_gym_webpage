from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import *
# Create your views here.
def test(request):
    return HttpResponse('<h1>This is test page</h1>')
def home2(request):
    return render(request,'home2.html')
def about1(request):
    return render(request,'about1.html')
def home3(request):
    return render(request,'home3.html')
def index(request):
    return render(request,'index.html')
def whyus(request):
    return render(request,'whyus.html')
def trainer(request):
    return render(request,'trainer.html')
def add(request):
    return render(request,'add.html')
def addcode(request):
    a = int(request.GET.get('a1', 0))
    b = int(request.GET.get('a2', 0))
    c = a + b
    return render(request, 'add.html',{'x':c})
def calculator(request):
    return render(request,'calculator.html')
def cal(request):

    a = int(request.GET.get('a1', 0))
    b = int(request.GET.get('a2', 1))
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    
    #return HttpResponse(c)
    return render(request,'calculator.html',{'w':c,'x':d,'y':e,'z':f})
def contact(request):
    return render(request,'contact.html')
def insert(request):
    return render(request,'insert.html')
def ins(request):
    u=user()
    u.fullname = request.GET.get('a1', '')
    u.email = request.GET.get('a2', '')
    u.password = request.GET.get('a3', '')
    u.phnno = request.GET.get('a4', '')
    u.save()
    return render(request,'insert.html')
def reg(request):
    return render(request,'reg.html')
def enter(request):
    v=user3()
    v.fullname=request.GET.get['fullname', '']
    v.username=request.GET.get['username', '']
    v.email=request.GET.get['email', '']
    v.password=request.GET.get['password', '']
    v.save()
    return render(request,'reg.html')
def contact(request):
    if request.method == 'POST':
        w = user6()
        w.name = request.POST.get('name', '')
        w.email = request.POST.get('email', '')
        w.phonenumber = request.POST.get('phone_number', '')
        w.message = request.POST.get('message', '')
        w.save()
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

def show(request):
    a = user3.objects.all()
    return render(request,'show.html',{'x':a})

def dele(request,id):
    d=user3.objects.get(id=id)
    d.delete()
    return redirect("../show")

def edit(request,id):
    d=user3.objects.get(id=id)
    return render(request,'edit.html',{'x':d})

def edcode(request,id):
    d=user3.objects.get(id=id)
    d.fullname = request.GET.get('fullname', d.fullname)
    d.username = request.GET.get('username', d.username)
    d.email = request.GET.get('email', d.email)
    d.password = request.GET.get('password', d.password)
    d.save()
    return redirect('../show')
def login(request):
    return render(request,'login.html')
def log2(request):
    a=request.GET.get['username', '']
    b=request.GET.get['password', '']
    if user3.objects.filter(username=a,password=b):
        return render(request,'index.html')
    else:
        return render(request,'login.html')
def logout(request):
    return render(request,'logout.html')
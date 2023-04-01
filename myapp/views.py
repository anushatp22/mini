from django.shortcuts import render, redirect
from myapp.models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
def register(request):
    return render(request, 'register.html')
def register_action(request):
    name = request.POST['name']
    address = request.POST['address']
    gender = request.POST['gender']
    phone = request.POST['phone']
    username = request.POST['username']
    password = request.POST['password']
    user = register_tb(Name=name, Address = address, Gender= gender, Phone= phone, Username= username, Password = password)
    user.save()
    messages.add_message(request, messages.INFO, 'Registration successful')
    return redirect('register')
def login(request):
    return render(request, 'login.html')
def login_action(request):
    username = request.POST['username']
    password = request.POST['password']
    user = register_tb.objects.filter(Username = username, Password = password)
    if user.count()>0:
        request.session['id'] = user[0].id
        messages.add_message(request, messages.INFO, 'Login successful')
        return render(request, 'home.html')
    else:
        return redirect('login')
def view_user(request):
    view=register_tb.objects.all()
    return render(request, 'view_user.html', {'user':view})
def delete(request, id):
    e = register_tb.objects.filter(id=id).delete()
    return redirect('view_user')
def edit(request, id):
    f = register_tb.objects.filter(id=id)
    return render(request, 'edit.html', {'user':f})
def edit_action(request):
    id=request.POST['id']
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    g=register_tb.objects.filter(id=id).update(Name=name,Address=address,Gender=gender,Phone=phone,Username=username,Password=password)
    messages.add_message(request, messages.INFO, 'updated')
    return redirect('view_user')
def image_upload(request):
    return render(request, 'image.html')
def upload_action(request):
    filename= request.POST['filename']
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image='no pic'
    p=image_tb(File=filename, Image=image)
    p.save()
    return redirect('image_upload')
def dropdownbinding(request):
    country=country_tb.objects.all()
    return render(request, 'dropdownbinding.html', {'coun':country})
def getstate(request):
    c=request.GET['count']
    state=state_tb.objects.filter(Countryid=c)
    return render(request, 'getstate.html', {'st':state})
def place_action(request):
    countryname=request.POST['country']
    print(countryname)
    statename=request.POST['state']
    print(statename)
    place=request.POST['place']
    print(place)
    po=place_tb(Country_id=countryname,State_id=statename,Place=place)
   
    po.save()
    return redirect('dropdownbinding')
def hide(request):
    return render(request,'hide.html')
def click(request):
    return render(request, 'click.html')

def jquery(request):
    return render(request, 'jquery.html')

def register1(request):
    use=reg.objects.all()
    return render(request, 'register2.html',{'r':use})

def Editmn(request, id):
    hi=reg.objects.filter(id=id)
    userstotal=reg.objects.all()
    return render(request, 'register2.html', {"u":hi,'r':userstotal})

def registeraction(request,id):
    m=reg.objects.filter(id=id)
    if len(hi) > 0:
        hz=reg.objects.filter(id=id)
        hi=request.POST['io']
        n=request.POST['name']
        u=request.POST['username']
        p=request.POST['password']
        h=reg.objects.filter(id=hz).update(name=n,user=u,pas=p)
        g=reg.objects.filter(id=hz)
    else:
        name=request.POST['name']
        user=request.POST['username']
        pas=request.POST['password']
        if len(name)>0:
            if len(user)>0:
                if len(pas)>0:
                    hu=reg(name=name,user=user,pas=pas)
                    hu.save()
    use=reg.objects.all()
    return render(request, 'register2.html', {'r':use,'g':m})
   
def login1(request):
    return render(request, 'login1.html')
def loginaction(request):
    username = request.POST['username']
    password = request.POST['password']
    user = reg.objects.filter(user = username, pas = password)
    if user.count()>0:
        request.session['id'] = user[0].id
        messages.add_message(request, messages.INFO, 'Login successful')
        return render(request, 'home1.html')
    else:
        return redirect('login1')
def deletemn(request,id):
    g=reg.objects.all()
    i=reg.objects.filter(id=id).delete()
    return render(request,'register2.html',{'r':g})


def file1(request):
    return render(request, 'file1.html')
def file1action(request):
    i=request.POST['im']
    if len(request.FILES)>0:
        image=request.FILES['file']
    else:
       image='no pic'
    f=file(n=i,f=image)
    f.save()
    return redirect('index')
        
# Create your views here.

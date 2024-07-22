from django.shortcuts import render
from myapp.models import Contact, Profile
from django.http import HttpResponse
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html')

def contact_us(request):
    context={}
    if request.method=="POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")

        obj = Contact(name=name, email=em, subject=sub, message=msz) 
        obj.save()
        context['message']=f"Dear {name}, Thanks for your time!"

    return render(request, 'contact.html', context)

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def all_dishes(request):
    return render(request, 'all_dishes.html')

def register(request):
    context={}
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        contact = request.POST.get('number')
        try:
            usr = User.objects.create_user(email, email, password)
            usr.first_name = name
            usr.save()
            
            profile = Profile(user=usr, contact_number = contact)
            profile.save()
            context['status'] = f"User {name} Registered Successfully"
        except:
            context['status'] = f"A User with this email already exists"

    return render(request,'register.html',context)

def signin(request):
    context={}
    if request.method=="POST":
        email = request.POST.get('email')
        passw = request.POST.get('password')

        check_user = authenticate(username=email, password=passw)
        if check_user:
            login(check_user)
            context.update({'message':'Login Successfully','class':'alert-success'})
        else:
            context.update({'message':'Invalid Login Details!','class':'alert-danger'})

    return render(request,'login.html',context)



from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.core.mail import send_mail 
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from .my_captcha import *

def index (request):
    return render(request,"index.html")


def about (request):
    return render(request,"about.html")

def contact (request):
    if request.method=='POST':
        name =request.POST['name']
        email =request.POST['email']
        subject =request.POST['subject']
        message =request.POST.get('message')

        subject = 'Thanks for Contacting FAH-Events.'
        message = f'Hi {name}, Thanks for Contacting FHS-events. \n Email: {email} \n Subject: {subject} \n Message : {message} \n Our team will contact you through email within 24hrs. \n Thanks for Registering \n Best regards, \n FAH-Team'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

        hr=Contact(name=name,email=email,subject=subject,message=message)
        hr.save()

    return render(request,"contact.html")

def services (request):
    return render(request,"services.html")

def team (request):
    return render(request,"team.html")

def gallery(request):
    return render(request,"gallery.html")
    
def faqs(request):
    return render(request,"faqs.html")

def terms(request):
    return render(request,"terms.html")

@login_required(login_url="signin")
def thanks(request):
    return render(request,"thanks.html")

def register(request):
    if request.method == 'POST':
        firstname =request.POST['firstname']
        lastname =request.POST['lastname']
        username =request.POST['username']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request,"username is exits")
            return redirect('/')
        
        if User.objects.filter(email=email):
            messages.error(request,"email is exits")
            return redirect('/')
        
        if password1 != password2:
            messages.error(request,"password not match")
            return redirect('/')
        if len(username)>12:
            messages.error(request,"username lessthan 12")
            return redirect('/')

        if not username.isalnum():
            messages.error(request,"only in alpha,numbric")
            return redirect('/')
    
            

        user=User.objects.create_user(username=username,email=email,password=password1,first_name=firstname,last_name=lastname)
        user.save()
        subject = 'Thanks for Creating account in FAH-events.'
        message = f'Hi {firstname} {lastname}, Thanks for Creating account in FAH-events. \n your  login details are \n Username: {username} \n Email: {email} \n Password: {password1} \n Dont share you login details to anyone. \n Thanks for Registering \n Best regards, \n FAH-Team'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list ) 

        messages.success(request,"Your account is register succesfully created")
        return redirect('signin')
        

    return render(request,"signup.html")
        

def signin(request):
    if request.method=='POST':
        captcha=FormWithCaptcha(request.POST)
        username =request.POST['username']
        password1 =request.POST['password1']

        user=authenticate(username=username,password=password1)

        if user is not None and captcha.is_valid():
            login(request,user)
            return render(request,"profile.html",)
        else:
            messages.error(request,"wrong details or captcha error")
            return redirect('/')
        
        

    return render(request,"registration/login.html",{"captcha":FormWithCaptcha})
    
@login_required(login_url="signin")
def signout(request):
    logout(request)
    
    return render(request,"registration/logout.html")


@login_required(login_url="signin")
def dashboard(request):
    if request.method=='POST':
        dashuser = User.objects.get(username=request.user.username)
        name =request.POST['name']
        email =request.POST['email']
        age =request.POST['age']
        phone =request.POST['phone']
        gender =request.POST.get('gender')
        state =request.POST['state']
        city =request.POST['city']
        event =request.POST.get('event')
        venues =request.POST.get('venues')
        acnonac =request.POST.get('acnonac')
        music =request.POST.get('music')
        decorations =request.POST.get('decorations')
        estimation =request.POST.get('estimation')
        food =request.POST.get('food')
        plate =request.POST.get('plate')
        doe= request.POST['doe']
        
        har=Book(dashuser=dashuser,name=name,email=email,phone=phone,gender=gender,age=age,event=event,venues=venues,state=state,city=city,acnonac=acnonac,music=music,food=food,plate=plate,doe=doe,decorations=decorations,estimation=estimation)
        har.save()

        subject = 'Thanks for booking the event in FAH events'
        message = f'Hi {name}, thank you for registering in FAH events. \n confrim your details are correct or Not \n Name: {name} \n Phone Number: {phone} \n Email: {email} \n Age: {age} \n Gender: {gender} \n  State: {state} \n City: {city} \n Event: {event} \n Venue: {venues} \n Ac or Non-Ac: {acnonac} \n Music: {music} \n Decoration: {decorations} \n Estimation: {estimation} \n Food: {food} \n Plate: {plate} \n Date of event: {doe} \n \n Thanks for Registering \n "** OUR TEAM WILL CONTACT YOU BY EMAIL OR PHONE **"  Best regards, \n FAH-Team'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        
        return render(request,"thanks.html")
    return render(request,"dashboard.html")

def new (request):
    if request.method=='POST':
        email=request.POST['email']

        if News.objects.filter(email=email):
            messages.error(request,"email is exits")
            return redirect('/')

        hr=News(email=email)
        hr.save()

        subject = 'Thanks for Subscribing FAH-Events.'
        message = f'Hi {email}, Thanks for Subscribing FAH-events. \n You will get mails on offers and updates of the FAH-Events \n Thanks for Registering \n Best regards, \n FAH-Team'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,"contact.html")

    return render(request,"index.html")


@login_required(login_url="signin")
def profile(request):
    if request.method=='POST':
        profileuser = User.objects.get(username=request.user.username)
        image = request.FILES['image']
        phone =request.POST['phone']
        ram=Profile(image=image,profileuser=profileuser,phone=phone)
        ram.save()
    return render(request,"profile.html")


#@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="signin")
def myevents(request):
    event_list = Book.objects.filter(dashuser=request.user)
    page = request.GET.get('page', 1)

    paginator = Paginator(event_list, 2)
    try:
        event_list = paginator.page(page)
    except PageNotAnInteger:
        event_list = paginator.page(1)
    except EmptyPage:
        event_list = paginator.page(paginator.num_pages)
    return render(request, "Myevents.html",{'event_list': event_list})
    
@login_required(login_url="signin")    
def delete(request,pk):   
        Book.objects.filter(id=pk).delete()
        return redirect('/myevents')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.Profile)  # request.FILES is show the selected image or file

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.Profile)
        args = {}
        # args.update(csrf(request))
        args['form'] = form
        args['profile_form'] = profile_form
        return render(request, 'profile.html', args)
from django.shortcuts import render
from home.models import Contact
# Create your views here.
from django.contrib import messages
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = Contact(name=name,email=email,password=password)
        contact.save()
        messages.success(request, 'Your Message has been sent')
    return render(request,'contact.html')

def knowus(request):
    return render(request,'knowus.html')

def services(request):
    return render(request,'services.html')

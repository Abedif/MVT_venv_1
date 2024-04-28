from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request ,'root/index.html')

def contact_us (request):
    return render(request ,'root/contact.html')

def about_us(request):
    return render(request ,'root/about.html')

def comment(request):
    return render(request ,'root/comment.html')

def help(request):
    return render(request ,'root/help.html')

def privacy(request):
    return render(request ,'root/privacy.html')







# Create your views here.

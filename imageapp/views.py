from django.http import HttpResponse 
from django.shortcuts import render, redirect 

  
# Create your views here. 
def index(request):
    from .models import User
    users = User.objects.all()
    p = users[len(users)-1].pic
    print(p)
    return render(request, 'index.html') 


def uploadImage(request):
    from .models import User
    print("request Handling............")
    p = request.FILES['uploadImage']
    User = User(pic = p)
    User.save()
    return render(request, 'index.html') 



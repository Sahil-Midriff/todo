from django.shortcuts import render,redirect
from . models import *
from django.views import View
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.db.models import Q
import json
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import model_to_dict
# Create your views here.


def Home(request):
    if request.method == "GET":
        return render(request,'home.html')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        photo = request.FILES['photo']
        password = make_password(request.POST.get('password'))
        print(request.POST)
        
        data = Signin.objects.create(first_name=first_name,
                                         last_name=last_name,
                                        phone=phone,
                                        email=email,
                                        photo=photo,
                                        password=password)
        data.save()
        return redirect ('profile')
        
        
def Search(request):
    if request.method == "POST":
        search_str= request.POST.get('suggestion')  
        title = list()
        expense = Signin.objects.filter(Q(first_name__icontains=search_str) | Q(last_name__icontains=search_str) | Q(email__icontains=search_str))
        #data = expense.values()
        if expense:
            my_list = [(i.id, i.first_name, i.last_name, i.email, i.phone) for i in expense ]
            my_list_convert = my_list
            
            for i in my_list_convert:
            
                x = '<tr border="2"> <th>First name</th> <th>Last name</th> <th>Phone_number</th> <th>Email</th> </tr>'
                x += "<tr>"
                x += "<td>" + str(i[1]) + "</td>"
                x += "<td>" + str(i[2]) + "</td>"
                x += "<td>" + str(i[3]) + "</td>"
                x += "<td>" + str(i[4]) + "</td>"
                x += "</tr>"     
                print('list converted',x)

            return JsonResponse(x, status=200,safe=False) 
        
            
        else:
            return JsonResponse(x, status=401,safe=False)
    
    
    
    
     
    # if request.method == "POST":
    #     print(request.POST)
    #     if 'try_search' in request.POST:
    #         print(request.POST)
    #         qs = Signin.objects.filter(Q(first_name__icontains=request.GET.get('try_search')) | Q(last_name__icontains=request.GET('try_search')))
    #         title = list()
        
    #         for prouduct in qs:
    #             title.append(f"{prouduct.first_name} {prouduct.last_name}")
    #             return JsonResponse(title,safe=False)
    #     else:
    #         print("this is else part")
    #         return HttpResponse("sucessfully")
    # else:
    #     print("this is else part 1")
    #     return HttpResponse("sucessfully")


    
              
    
def Profile(request):
    # if 'term' in request.GET:
    #     qs = Signin.objects.filter(Q(first_name__icontains=request.GET.get('term')) | Q(last_name__icontains=request.GET.get('term')) | Q(phone__icontains=request.GET.get('term')) | Q(email__icontains=request.GET.get('term')))
    #     print(qs)
    #     title = list()
      
    #     for prouduct in qs:
    #         title.append(f"{prouduct.first_name}  {prouduct.last_name}")
            
    #     return JsonResponse(title,safe=False)
    data = Signin.objects.all()
    return render(request,'profile.html',{'data':data})
    
def Showdetails(request,id):
    
        
    if request.method == "GET":
        data = Signin.objects.filter(id=id)
        return render(request,'showdetails.html',{'data':data})
    
    if request.method=='POST':
        print(request.POST,request.FILES)
        update_photo = Signin.objects.get(id=id)
        photo = request.FILES['photo']  
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        update_photo.first_name = first_name
        update_photo.last_name = last_name    
        update_photo.photo = photo
        update_photo.phone = phone
        update_photo.email=email
        update_photo.save()
        return redirect('profile')
        


def Delete(request,id):
    data = Signin.objects.get(id=id)
    data.delete()
    return redirect('profile')

def Update(request,id):
    return render(request,'showdetails.html')
    

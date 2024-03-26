from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(request):
    peoples= [
        {'name':'Abhijeet Gupta ','age':26},
        {'name':'rohan sharma ','age':23},
        {'name':'vicky kaushal  ','age':12},
        {'name':'deepanshu  chaurasiya  ','age':11},
        {'name':'Sandeep  Rai  ','age':63}

    ]

    for people in peoples:
        if people['age'] : 
            print("yes")

    

    return render (request,"home/index.html",context={'page':'Djanogo tutorial 2023','peoples' : peoples})

def about(request):
    context={'page':'About'}
    return render (request,"home/about.html",context)

def contact(request):
    context={'page':'Contact'}
    return render (request,"home/contact.html",context)

def success_page(request):
    
    return HttpResponse("<h1> this is success page</h1>")
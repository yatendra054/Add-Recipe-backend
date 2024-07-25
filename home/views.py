from django.shortcuts import render

from django.http import HttpResponse


peoples=[
    {'Name':"Raj Sharma",'Age':20},
    {'Name':"Harsh Singh",'Age':21},
    {'Name':"Nihal Patidar",'Age':18},
    {'Name':"Yatendra Dixit",'Age':28},
    {'Name':"Davita Roy",'Age':25},
    {'Name':"Tanu Upadhyay",'Age':17},
]
def home(request):
    return render(request,"index.html",context={'peoples':peoples})
# Create your views here.

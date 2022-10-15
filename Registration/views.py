from django.shortcuts import render
from django.http import HttpResponse
from Registration.models import Course,Batch,Student

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to Prime Intuit Registration page</h1>")
def Home(request):
    # return HttpResponse("<h1>Welcome to Prime Intuit Home page</h1>")
   #my_dict={'Insert_Me':"I am a text from registration/views.py from sub templates"}
    #batch_list=Batch.objects.order_by('batch_ID')
    data_dict={'access_record':batch_list,'Insert_Me':"I am a text from registration/views.py from sub templates"}
    #batch_list = Batch.objects.raw('select * from Registration_Batch where start_date >"2022-06-01"')
    batch_list = Batch.objects.raw('select * from Registration_Batch')
    return render(request,'Registration/index.html',context=data_dict)
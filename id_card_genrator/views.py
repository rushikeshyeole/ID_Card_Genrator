from django.shortcuts import render, HttpResponse
from id_card_genrator.models import studentinfo

# Create your views here.


def index(request):
    return render(request, 'index.html')

def save_stu_info(request):
    s_name = request.POST['name']
    s_age = request.POST['age']
    s_email = request.POST['email']
    s_address = request.POST['address']
    s_college_company = request.POST["college-company"]
    s_country = request.POST["country"]
  
    stu_id_obj = studentinfo.objects.all()
    stu_id_obj.delete()
    
    stu_obj = studentinfo(name = s_name, age = s_age, email = s_email, address = s_address, college = s_college_company, country = s_country)
    stu_obj.save()
    stu_id_obj = studentinfo.objects.all()
    return render(request, 'id_Card.html', {'stu_id_obj' : stu_id_obj})


def id_card(request):
    return render(request, 'id_Card.html')

def delete_rec(request):
    stu_id_obj_dlt = studentinfo.objects.all()
    stu_id_obj_dlt.delete()
    return render(request, 'index.html', {'msg':'All record deleted'})

def ic(request):
    return render(request, 'ic.html')





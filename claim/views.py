from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.forms import ModelForm
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from claim.models import Users

from claim.models import Claim


# Create your views here.
def home(request):
    users = Users.objects.all()
    context = {"users": users}
    return render(request, 'claim/home_claim.html',context)

"""
def about_us(request):
    users = Users.objects.all()
    context = {"users": users}
    return render(request, 'claim/about_us.html',context)
"""
def about_us(request):
    users = Users.objects.all()
    context = {"users": users}
    return render(request, 'claim/home_claim.html',context)
@login_required
def profile(request):
    users = Users.objects.all()
    context = {"users": users}
    return render(request, 'claim/profile.html',context)


def claim(request):
    claim = Claim.objects.all()
    if request.method == "POST":
        name = request.POST.get("firstname")
        surname = request.POST.get("lastname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")

        data = {
            "firstname": name,
            "lastname": surname,
            "email": email,
            "phone": phone,
            "subject": subject
        }
        message = """
            Subject: {}

            From: {}
            
            Phone: {}
            
            Name: {}
            
            Surname: {}
        """.format(data["subject"], data["email"], data["phone"], data["firstname"], data["lastname"])
        send_mail(data["subject"], message, "", ["djangotestest99999@gmail.com"])
        #return HttpResponse("Děkujeme - brzy Vás budeme kontaktovat. ")
        return  redirect("/")
    return render(request=request, template_name="claim/actual_offer.html", context={"claim": claim})


def claim_home(request):
    claim = Claim.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        data = {
            "name": name,
            "email": email,
            "message": message
        }
        message = """
            Message: {}

            Email: {}

            Name: {}

        """.format(data["message"], data["email"],  data["name"])
        send_mail(data["message"], message, "", ["djangotestest99999@gmail.com"])
        # return HttpResponse("Děkujeme - brzy Vás budeme kontaktovat. ")
        return redirect("/")
    return render(request=request,template_name="claim/actual_offer.html", context={"claim": claim})

def user(request):
    users = Users.objects.all()
    context = {"users": users}
    return render(request, 'actual_offer.html',{})



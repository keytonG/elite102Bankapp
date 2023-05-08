from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from string import punctuation

from .models import account

# Create your views here.
def index(request):
    template = loader.get_template("login/login.html")
    context = {}
    return HttpResponse(template.render(context,request))

def signupRedirect(request):
    context = {}
    return render(request, "login/signup.html", context)

def login(request):
    try:
        accountAttemptedForLogin = account.objects.get(username=request.POST["username"])
        print(accountAttemptedForLogin)
    except (KeyError, account.DoesNotExist):
        return render(
            request,
            "login/login.html",
            {
                "AccountDoesNotExist":True
            }
        )
    except:
        return render(request,"login/login.html",)
    
    if accountAttemptedForLogin.credential == request.POST['credential']:
        return HttpResponseRedirect(reverse("manage:index", kwargs={'account_id': accountAttemptedForLogin.id}))
    else:
        return HttpResponse("User not found or password incorrect.")

def signup(request):
    errors = {
        "alert_nameLengthInvalid":False,
        "alert_passwordComplexityInvalid":False,
        "alert_emailNotReal":False,
        "alert_accountAlreadyExists":False
    }

    if "@gmail.com" not in request.POST['email']:
        errors['alert_emailNotReal'] = True
        print("error: EmailNotReal")

    if any(char in request.POST['password'] for char in punctuation) == False or any(char in request.POST['password'] for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == False or any(char.isdigit() for char in request.POST['password']) == False or len(request.POST['password']) < 6:
        errors['alert_passwordComplexityInvalid'] = True
        print("error: passwordComplexityInvalid")

    if len(request.POST['fname']) < 2 or len(request.POST['lname']) < 2:
        errors['alert_nameLengthInvalid'] = True
        print("error: nameLengthInvalid")

    if account.objects.filter(holdername=f"{request.POST['fname']} {request.POST['lname']}"):
        errors['alert_accountAlreadyExists'] = True
        print("error: accountAlreadyExists")

    for i in errors.values():
        if i == True:
            return render(request,"login/signup.html",{"alert_nameLengthInvalid":errors["alert_nameLengthInvalid"],"alert_passwordComplexityInvalid":errors["alert_passwordComplexityInvalid"],"alert_emailNotReal":errors["alert_emailNotReal"],"alert_accountAlreadyExists":errors['alert_accountAlreadyExists'],"errors":True})

    try:
        a = account(username=f"{request.POST['fname']}{request.POST['lname']}",
        holdername=f"{request.POST['fname']} {request.POST['lname']}",
        email=request.POST['email'],
        dob=request.POST['dob'],
        credential=request.POST['password'],
        balance=0.00)
        a.save()
    except:
        return HttpResponseBadRequest()
    
    return HttpResponseRedirect(reverse("manage:index", kwargs={'account_id':a.id}))
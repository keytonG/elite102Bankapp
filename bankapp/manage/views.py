from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.utils import timezone
from decimal import Decimal

from login.models import account,transaction

# Create your views here.
def index(request, account_id):
    print(transaction.objects.filter(acctId_to=account_id))
    print(transaction.objects.filter(acctId_from=account_id))
    return HttpResponse(render(request,"manage/manage.html", {"transactions_outgoing":transaction.objects.filter(acctId_to=account_id), "transactions_incoming":transaction.objects.filter(acctId_from=account_id), "account":account.objects.filter(pk=account_id)[0]}))

def deposit(request):
    account_id = request.POST.get('account_id', None)
    amount = request.POST.get('amount', None)

    try:
        acctid = account.objects.get(pk=account_id)
        if acctid:
            acctid.balance += Decimal(amount)
            acctid.save()

            t = transaction(acctId_from=0,acctId_to=request.POST['account_id'],ammount=request.POST['amount'],date=timezone.now(),description=request.POST['description'])
            t.save()

            return HttpResponse(render(request,"manage/complete.html",))
        else:
            return HttpResponse(render(request,"manage/failed.html"))
    except account.DoesNotExist:
        return HttpResponse(render(request,"manage/failed.html"))

def withdrawal(request):
    account_id = request.POSt.get('account_id', None)
    amount = request.POSt.get('amount', None)

    try:
        acctid = account.objects.get(pk=account_id)
        if acctid:
            acctid.balance += Decimal(amount)
            acctid.save()

            t = transaction(acctId_from=request.POST['account_id'],acctId_to=0,ammount=request.POST['amount'],date=timezone.now(),description=request.POST['description'])
            t.save

            return HttpResponse(render(request,"manage/complete.html",))
        else:
            return HttpResponse(render(request,"manage/failed.html"))
    except account.DoesNotExist():
        return HttpResponse(render(request,"manage/failed.html"),{"DoesNotExist":True})
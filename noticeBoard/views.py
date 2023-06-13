from django.shortcuts import render, redirect, HttpResponseRedirect
from datetime import datetime
from noticeBoard.models import AdminNotice
from django.contrib import messages
from .forms import noticeaddition
from django.core.mail import send_mail


# Create your views here.
def broadcast(request, id):
    if request.method == "POST":
        pi = AdminNotice.objects.get(pk=id)
        subject = 'Broadcasting Notice'
        message = pi
        from_email = 'kk235964@gmail.com'
        recipient_list = ['kamal.20213003@mnnit.ac.in','kamal235964@gmail.com']
        
        for recipient in recipient_list:
            send_mail(subject, message, from_email, [recipient], fail_silently=False)
    return HttpResponseRedirect('/adminNotice')
    

def adminNotice(request):
   
    if request.method == "POST":
        notice = noticeaddition(request.POST)
        if notice.is_valid():
            con= notice.cleaned_data['notice']
            adminNotice = AdminNotice(notice=con, date=datetime.today())
            adminNotice.save() 
        
            messages.success(request, 'Notice has been posted!')
    else:
        notice = noticeaddition()
    content = AdminNotice.objects.all()
    return render(request, 'adminNotice.html', {'form' : notice , 'conts': content})

def update_data(request, id):
    if request.method == "POST":
        pi = AdminNotice.objects.get(pk=id)
        notice = noticeaddition(request.POST, instance=pi)
        if notice.is_valid():
            notice.save()
            messages.success(request, 'Notice has been Updated!')

    else:
        pi = AdminNotice.objects.get(pk=id)
        notice = noticeaddition(instance=pi)
    return render (request,'updateform.html',{ 'form':notice})

def delete_data(request,id):
    if request.method == "POST":
        pi = AdminNotice.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/adminNotice')
    





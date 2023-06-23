from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def submit(request):
    if request.method == 'POST':
        em = request.POST.get('email')
        me = request.POST.get('mess')
        
        # print(em)
        # print(me)
        subject="WAKANDA FOREVER"
        sender="aniketgade84421@gmail.com"
        send_mail(
                    subject,
                    me,
                    sender,
                    [em],
                    fail_silently=False,
        
                )
        
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
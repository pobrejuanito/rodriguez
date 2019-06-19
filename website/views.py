import pdb
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.core.mail import send_mail
from validate_email import validate_email
from django.conf import settings

# Create your views here.
def english(request):

    page_data = {}
    if request.method == 'POST':
        message = 'Appointment Request' + "\n"
        message += 'Name: ' + request.POST.get('name') + "\n"
        message += 'Phone: ' + request.POST.get('phone') + "\n"
        message += 'Email: ' + request.POST.get('email') + "\n"
        message += 'Time: ' + request.POST.get('time') + "\n"
        message += 'Message: ' + request.POST.get('message') + "\n\n"
        message += settings.EMAIL_SIGNATURE
        send_mail(settings.EMAIL_APPOINTMENT_SUBJECT, message,  settings.EMAIL_FROM, settings.EMAIL_TO, fail_silently=False)
        return JsonResponse({})

    page_data.update(csrf(request))


    return render_to_response('home-en.html', page_data)

def landing(request):

   page_data = {}
   if request.method == 'POST':
      if request.POST.get('fax_number') == '':
         message = 'Appointment Request' + "\n"
         message += 'Name: ' + request.POST.get('name') + "\n"
         message += 'Phone: ' + request.POST.get('phone') + "\n"
         message += 'Email: ' + request.POST.get('email') + "\n"
         message += 'Time: ' + request.POST.get('time') + "\n"
         message += 'Message: ' + request.POST.get('message') + "\n\n"
         message += settings.EMAIL_SIGNATURE
         send_mail(settings.EMAIL_APPOINTMENT_SUBJECT, message,  settings.EMAIL_FROM, settings.EMAIL_TO, fail_silently=False)
         return JsonResponse({})

   page_data.update(csrf(request))
   return render_to_response('landing-page.html', page_data)

def spanish(request):
   page_data = {}
   if request.method == 'POST':
      if request.POST.get('fax_number') == '':
         message = 'Appointment Request' + "\n"
         message += 'Name: ' + request.POST.get('name') + "\n"
         message += 'Phone: ' + request.POST.get('phone') + "\n"
         message += 'Email: ' + request.POST.get('email') + "\n"
         message += 'Time: ' + request.POST.get('time') + "\n"
         message += 'Message: ' + request.POST.get('message') + "\n\n"
         message += settings.EMAIL_SIGNATURE
         send_mail(settings.EMAIL_APPOINTMENT_SUBJECT, message,  settings.EMAIL_FROM, settings.EMAIL_TO, fail_silently=False)
         return JsonResponse({})

   page_data.update(csrf(request))
   return render_to_response('home-es.html', page_data)
   
def sendmessage(request):
   if request.method == 'POST':
      if request.POST.get('fax_number') == '':
         message = 'Message Details' + "\n"
         message += 'Name: ' + request.POST.get('fullname') + "\n"
         message += 'Phone: ' + request.POST.get('phone') + "\n"
         message += 'Email: ' + request.POST.get('email') + "\n"
         message += 'Message: ' + request.POST.get('message') + "\n\n"
         message += settings.EMAIL_SIGNATURE
         send_mail(settings.EMAIL_CONTACTUS_SUBJECT, message, settings.EMAIL_FROM, settings.EMAIL_TO, fail_silently=False)
   return JsonResponse({})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

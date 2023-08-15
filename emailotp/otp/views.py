
from django.shortcuts import render, redirect
from django.contrib import messages
import sib_api_v3_sdk 
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
import random
from django.http import HttpResponse






def otpgenarator():
    random_number = random.randrange(1000, 10000)  
    return random_number

def sendemail(request):
    code=otpgenarator()
    request.session['otp_code'] = code
    
    if request.method == "POST":
        sender = 'hay app team'
        toemail = request.POST.get('to')
        toname = "New user"
        fromemail = "<your email>"
        subject = "your otp verification code"
        message=str(code)
       
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = '<your api key>'
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        subject = subject
        html_content = message
        sender = {"name": sender, "email": fromemail}
        to = [{"email": toemail, "name": toname}]
        headers = {"Some-Custom-Name": "unique-id-1234"}
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers,html_content=html_content, sender=sender, subject=subject)
        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            pprint(api_response)
            messages.success(request, "otp code  send successfully")
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
    return render(request, 'email.html', locals())


def verifyotp(request):

    if request.method == "POST":
        otp = request.POST.get('otp')
        otp_code=request.session.get('otp_code')
        otp=int(otp)
        if otp_code != otp:
             return redirect('sendemail')
        
    return render(request, 'home.html', locals())          
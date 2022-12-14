from django.conf import settings
from django.core.mail import send_mail




def send_account_activation_email(email, email_token):
    subject = 'Activate your account in gharKiDukaanHai.com'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi, Please click on the link to activate your account  http://127.0.0.1:8000/accounts/activate/{email_token}'

    try:
        send_mail(subject, message, email_from, [email], fail_silently=False)
    except Exception as e:
        print(e)
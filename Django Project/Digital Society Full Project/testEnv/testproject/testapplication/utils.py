from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def mySendMail(subject,template,to,context):
    subject = 'Subject'
    template_str = 'testapplication/'+ template+'.html'
    html_message = render_to_string(template_str, {'data': context})
    plain_message = strip_tags(html_message)
    from_email = 'drashtiboricha@gmail.com'
    send_mail(subject, plain_message, from_email, to, html_message=html_message)
# accounts/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def send_email_to_client(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['Vinayakmishra9451@gmail.com']  # Replace with the recipient's email address

    send_mail(subject, message, from_email, recipient_list)
    return redirect('home')  # This redirects to the home page defined above

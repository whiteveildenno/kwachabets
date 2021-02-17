from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
# Create your views here.
def contacts(request):  
    if request.method == 'POST':
      print(request.POST)
      company_name = request.POST['company_name']
      email_address = request.POST['email_address']
      messager = request.POST['messager']

      contacts = Contact(company_name = company_name, email_address = email_address, messager = messager)

      contacts.save()

      messages.success(request,'Your message has been sent. One of our representatives will get back to you soon')
    
    return render(request,'contacts/contactus.html')
 
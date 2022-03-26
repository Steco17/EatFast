from django.http import HttpResponse
from  django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model

from .validations.forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        'title':'hello World',
        'content':'Welcome to the Home Page',
        'Premium_content': 'Yeaaaaj'
    }
    if request.user.is_authenticated:
        context['Premium_content'] =  'Yeaaaaj'


    return render(request, "home_page.html",context)
    

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title':'Contact our Restaurant',
        'content':'Welcome to the contact Page',
        'form' : contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #     print(request.POST.get('email'))
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('content'))


    return render(request, "contact/view.html",context)

def about_page(request):
    context = {
        "title":"About Restaurant",
        'content':'Welcome to the About Page'
    }


    return render(request, "home_page.html",context)
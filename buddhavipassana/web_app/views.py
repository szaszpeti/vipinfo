
from django.shortcuts import render, get_object_or_404
from .models import BuddhaRegister
from .forms import BuddhaRegisterForm

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse




# Create your views here.
def index(request):
    return render(request, 'baseIntro.html')

def intro_web(request):
    return render(request, 'web_app/buddhavipassana_intro.html')

def ajahn(request):
    return render(request, 'web_app/AjahnTong.html')


def rolunk(request):
    return render(request, 'web_app/rolunk.html')


def oktatok(request):
    return render(request, 'web_app/oktatok.html')

def tanfolyamok(request):
    return render(request, 'web_app/tanfolyamok.html')


def technikarol(request):
    return render(request, 'web_app/technikarol.html')

def gyik(request):
    return render(request, 'web_app/gyik.html')


def kapcsolat(request):

    if request.method == 'POST':

        form = BuddhaRegisterForm(request.POST)

        if form.is_valid():

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            print(last_name, first_name, email, phone, message)

            instance = BuddhaRegister(first_name=first_name, last_name=last_name, email=email, phone=phone, message=message)
            instance.save()

            return HttpResponseRedirect(reverse('web_app:valasz'))
    else:
        form = BuddhaRegisterForm()

    return render(request, 'web_app/kapcsolat.html', {'form': form})



def indexEng(request):
    return render(request, 'web_app/indexEng.html')

def ajahnEng(request):
    return render(request, 'web_app/ajahnEng.html')


def about(request):
    return render(request, 'web_app/about.html')


def teachers(request):
    return render(request, 'web_app/teachers.html')


def courses(request):
    return render(request, 'web_app/courses.html')


def technique(request):
    return render(request, 'web_app/technique.html')


def faq(request):
    return render(request, 'web_app/faq.html')

def answere(request):
    return render(request, 'web_app/answere.html')

def valasz(request):
    return render(request, 'web_app/valasz.html')

def contact(request):


    if request.method == 'POST':

        form = BuddhaRegisterForm(request.POST)
        if form.is_valid():

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            instance = BuddhaRegister(first_name=first_name, last_name=last_name, email=email, phone=phone, message=message)
            instance.save()

            return HttpResponseRedirect(reverse('web_app:answere'))

    else:
        form = BuddhaRegisterForm()

    return render(request, 'web_app/contact.html', {'form': form})


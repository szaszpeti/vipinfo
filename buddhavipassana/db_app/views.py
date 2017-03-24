from django.shortcuts import render
from db_app.forms import UserForm, Meditator
from django.shortcuts import render, get_object_or_404




# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

# def user_login(request):
#     return render(request,'db_app/login.html')
@login_required
def welcome_main(request):
    usern = request.user.username
    all_meditators = Meditator.objects.all()
    number = len(all_meditators)
    return render(request, 'db_app/welcome_main.html', {'username':usern, 'number':number})



@login_required
def find_meditator(request):
    usern = request.user.username
    return render(request, 'db_app/find_meditator.html', {'username':usern})

@login_required
def find_meditator_byname(request):

    print ("THis is the request from find", request)

    if request.method == 'POST':

        name = request.POST.get('nev')
        all_meditators = Meditator.objects.filter(name__contains=name)
        number = len(all_meditators)
        usern = request.user.username

    return render(request, 'db_app/query_result.html',{'nev':name, 'number':number, 'all_meditators':all_meditators, 'username':usern})

@login_required
def find_meditator_bycountry(request):

    print ("THis is the request from find", request)

    if request.method == 'POST':

        name = request.POST.get('orszag')
        all_meditators = Meditator.objects.filter(country__contains=name)
        number = len(all_meditators)
        usern = request.user.username

        return render(request, 'db_app/query_result.html',
                      {'nev': name, 'number': number, 'all_meditators': all_meditators, 'username': usern})


@login_required
def find_meditator_byborn(request):

    print ("THis is the request from find", request)

    if request.method == 'POST':

        name = request.POST.get('ev')
        all_meditators = Meditator.objects.filter(born__contains=name)
        number = len(all_meditators)
        usern = request.user.username

    return render(request, 'db_app/query_result.html',
                  {'nev': name, 'number': number, 'all_meditators': all_meditators, 'username': usern})


@login_required
def find_meditator_byprofession(request):

    print ("THis is the request from find", request)

    if request.method == 'POST':

        name = request.POST.get('foglalkozas')
        all_meditators = Meditator.objects.filter(profession__contains=name)
        number = len(all_meditators)
        usern = request.user.username

    return render(request, 'db_app/query_result.html',
                  {'nev': name, 'number': number, 'all_meditators': all_meditators, 'username': usern})


def detail(request, meditator_id):
    print("This is request for id", request, meditator_id)
    meditator = get_object_or_404(Meditator, id=meditator_id)

    fields = [f.name for f in Meditator._meta.get_fields()]

    usern = request.user.username

    return render(request, 'db_app/detail.html', {'meditator': meditator, 'fields':fields, 'username':usern})


@login_required
def add_meditator(request):
    usern = request.user.username

    if request.method == 'POST':

        meditator_form = Meditator(request.POST)

        name = request.POST.get('name')
        country = request.POST.get('country')
        born = request.POST.get('born')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profession = request.POST.get('profession')
        course = request.POST.get('course')
        course_date= request.POST.get('course_date')
        teacher = request.POST.get('teacher')
        remarks = request.POST.get('remarks')


        medit = Meditator.objects.get_or_create(name=name, country=country, born=born, gender=gender, email=email,
                                                    phone=phone, profession=profession, course=course,
                                                    course_date=course_date,
                                                    teacher=teacher, remarks=remarks)


    return render(request, 'db_app/add_meditator.html' , {'username':usern})






@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return render(request, 'db_app/login.html')

def register(request):
    usern = request.user.username

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)


        # Check to see  form is valid
        if user_form.is_valid():

            user = user_form.save()  # Save User Form to Databas
            user.set_password(user.password)  # Hash the password
            user.save() # Update with Hashed password
            registered = True # Registration Successful!

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'db_app/registration.html',
                          {'user_form':user_form,
                           'registered':registered,
                           'username':usern})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('db_app:welcome_main'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'db_app/login.html', {})
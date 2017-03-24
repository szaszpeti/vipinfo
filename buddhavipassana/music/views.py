from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album, Song
from .forms import UserForm


# list of object
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

    def get_queryset(self):
        return Song.objects.all()


#get details from one object
class DetailsView(generic.DetailView):
    model = Song
    template_name = 'music/details.html'



class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')




class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #if get = post or get etc.....but with class based views:

    #whenever they get request they will use this function
    def get(self, request):
        form = self.form_class(None) #use the user form, blank
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST) #jon az info a formarol

        if form.is_valid():
                # create object from the userinput, but not saving it!!!
            user = form.save(commit=False)

                #clean (normalized) data - properly formated data
                #makes the data ready to upload

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

                #if you want to change the password, must be like this, then hash created
            user.set_password(password)
            user.save()

                #check the username, password if they exist in the database
                #if ok, returns an object so user is not None
            user = authenticate(username=username, password=password)

            if user is not None:

                    #check if you activated the user, so nincs kizarva a csavo
                if user.is_active:
                    login(request, user)
                        #request.username if you later need your name
                    return redirect('music:index')

            #ha nincsen regisztralva, vagy le van tiltva akkor
        return render(request, self.template_name, {'form':form})




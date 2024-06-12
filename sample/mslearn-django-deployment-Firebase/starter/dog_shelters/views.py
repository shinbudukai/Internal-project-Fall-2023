from django.shortcuts import render, get_object_or_404
#from models import *
from . import models
from django.views import generic
#import pyrebase
import os


config = {
  'apiKey': "AIzaSyBylO6AA4dtPaAt4YPmHcUirSa6lOu1_1I",
  'authDomain': "sample-deployment-2034e.firebaseapp.com",
  'projectId': "sample-deployment-2034e",
  'storageBucket': "sample-deployment-2034e.appspot.com",
  'messagingSenderId': "1093152371486",
  'appId': "1:1093152371486:web:27e2bd0aecba7ddce70f0f",
  'measurementId': "G-MSSW6HYL3C",
  "databaseURL" : "https://sample-deployment-2034e-default-rtdb.firebaseio.com"
}
#intilize Firebase
#firebase = pyrebase.initialize_app(config)

# #firestore
# storage = firebase.storage()

# #realtime database
# auth = firebase.auth()
# db = firebase.database()

#Create your views here.
def shelter_list(request):
    shelters = models.Shelter.objects.all()
    context = {'shelters': shelters}
    return render(request, 'shelter_list.html', context)

def shelter_detail(request, pk):
    shelter = get_object_or_404(models.Shelter, pk=pk)
    context = {'shelter': shelter}
    return render(request, 'shelter_detail.html', context)

class DogDetailView(generic.DetailView):
    model = models.Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'

class DogCreateView(generic.CreateView):
    model = models.Dog
    template_name = 'dog_form.html'
    fields = ['shelter', 'name', 'description']

data = {

    'dog':'Casel',
    'cat':'Todo'
}

#db.child("Animal").push(data)
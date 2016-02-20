from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import Task
from django.shortcuts import render_to_response


def index(request):
    items = Task.objects.all() #ORM queries the database for all of the to-do entries.
 
    return render_to_response('index.html', {'items': items}) #Responds with passing the object items (contains info from the DB) to the template index
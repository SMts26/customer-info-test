from django.shortcuts import render, HttpResponse
from .models import InsertItem

# Create your views here.
def home(request):
    return render(request, "home.html")
    

def addItem(request):
    insert_item = InsertItem.objects.all() #This gets everything that is from that model title
    return render(request, "newEntry.html", {"items":  insert_item})
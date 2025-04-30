from django.shortcuts import render, HttpResponse
from .models import InsertItem

# Create your views here.
def home(response):
    return render(response, "home.html")
    

def addItem(response):
    response.user
    if response.method == "POST":

        insert_item = InsertItem.objects.all() #This gets everything that is from that model title
    return render(response, "newEntry.html", {"items":  insert_item})
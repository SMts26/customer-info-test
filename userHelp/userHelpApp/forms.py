from django import forms

class CreateNewEntry(forms.From):
    title = forms.CharField(label="Title", max_length=200)
    date = forms.DateField(label="Time")
    description= forms.CharField(label="Description", max_length=1000)
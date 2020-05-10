from django import forms

class SearchForm(forms.Form):
    date_month = forms.IntegerField()
    date_year = forms.IntegerField()

    
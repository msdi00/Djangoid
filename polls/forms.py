from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    ффф = forms.GenericIPAddressField()

from django import forms


class NewPhrasesForm(forms.Form):
    phrases = forms.CharField(label='Frase')

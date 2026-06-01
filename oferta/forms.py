from django import forms
from .models import Kategoria, Szkolenie, Rejestracja


class KategoriaForm(forms.ModelForm):
    class Meta:
        model = Kategoria
        fields = ['publikuj', 'kolejnosc', 'kategoria_nadrzedna', 'nazwa']


class SzkolenieForm(forms.ModelForm):
    class Meta:
        model = Szkolenie
        fields = ['kategoria', 'publikuj', 'kolejnosc', 'liczba_godzin', 'numer', 'cena', 'tytul', 'opis']


class RejestracjaForm(forms.ModelForm):
    class Meta:
        model = Rejestracja
        fields = ['szkolenie', 'zgoda_rodo', 'imie', 'nazwisko', 'telefon', 'email']
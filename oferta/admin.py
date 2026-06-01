from django.contrib import admin
from .models import Kategoria, Szkolenie, Rejestracja


@admin.register(Kategoria)
class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nazwa', 'publikuj', 'kolejnosc')
    list_filter = ('publikuj',)
    search_fields = ('nazwa',)


@admin.register(Szkolenie)
class SzkolenieAdmin(admin.ModelAdmin):
    list_display = ('id', 'tytul', 'kategoria', 'cena', 'liczba_godzin', 'publikuj')
    list_filter = ('publikuj', 'kategoria')
    search_fields = ('tytul', 'numer')


@admin.register(Rejestracja)
class RejestracjaAdmin(admin.ModelAdmin):
    list_display = ('id', 'imie', 'nazwisko', 'email', 'szkolenie', 'status', 'data_rejestracji')
    list_filter = ('status', 'szkolenie')
    search_fields = ('imie', 'nazwisko', 'email')
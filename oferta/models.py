from django.db import models


class Kategoria(models.Model):
    publikuj = models.BooleanField(default=True)
    kolejnosc = models.IntegerField(default=0)
    kategoria_nadrzedna = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa


class Szkolenie(models.Model):
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    publikuj = models.BooleanField(default=True)
    kolejnosc = models.IntegerField(default=0)
    liczba_godzin = models.IntegerField()
    numer = models.CharField(max_length=50)
    cena = models.DecimalField(max_digits=8, decimal_places=2)
    tytul = models.CharField(max_length=200)
    opis = models.TextField()

    def __str__(self):
        return self.tytul


class Rejestracja(models.Model):
    szkolenie = models.ForeignKey(Szkolenie, on_delete=models.CASCADE)
    zgoda_rodo = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='nowa')
    data_rejestracji = models.DateTimeField(auto_now_add=True)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
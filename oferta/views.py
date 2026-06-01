from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Kategoria, Szkolenie, Rejestracja
from .forms import KategoriaForm, SzkolenieForm, RejestracjaForm


def home(request):
    return render(request, 'oferta/home.html')


def offer(request):
    kategorie = Kategoria.objects.filter(publikuj=True).order_by('kolejnosc')
    return render(request, 'oferta/offer.html', {'kategorie': kategorie})


def offer_category(request, kategoria_id):
    kategoria = get_object_or_404(Kategoria, id=kategoria_id)
    szkolenia = Szkolenie.objects.filter(kategoria=kategoria, publikuj=True).order_by('kolejnosc')
    return render(request, 'oferta/offer_category.html', {
        'kategoria': kategoria,
        'szkolenia': szkolenia
    })


def course_detail(request, kategoria_id, course_id):
    szkolenie = get_object_or_404(Szkolenie, id=course_id)
    return render(request, 'oferta/course_detail.html', {'szkolenie': szkolenie})


def offer_mng(request):
    return render(request, 'oferta/offer_mng.html')


def categ_lst(request):
    kategorie = Kategoria.objects.all().order_by('kolejnosc')
    return render(request, 'oferta/categ_lst.html', {'kategorie': kategorie})


def course_lst(request):
    szkolenia = Szkolenie.objects.all().order_by('kolejnosc')
    return render(request, 'oferta/course_lst.html', {'szkolenia': szkolenia})


def categ_add(request):
    if request.method == 'POST':
        form = KategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categ_lst')
    else:
        form = KategoriaForm()

    return render(request, 'oferta/form.html', {
        'form': form,
        'title': 'Dodaj kategorię'
    })


def course_add(request):
    if request.method == 'POST':
        form = SzkolenieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_lst')
    else:
        form = SzkolenieForm()

    return render(request, 'oferta/form.html', {
        'form': form,
        'title': 'Dodaj szkolenie'
    })


def register(request, course_id):
    szkolenie = get_object_or_404(Szkolenie, id=course_id)

    if request.method == 'POST':
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('offer')
    else:
        form = RejestracjaForm(initial={'szkolenie': szkolenie})

    return render(request, 'oferta/form.html', {
        'form': form,
        'title': 'Rejestracja na szkolenie'
    })


def api_categories(request):
    data = list(Kategoria.objects.values())
    return JsonResponse(data, safe=False)


def api_courses(request):
    data = list(Szkolenie.objects.values())
    return JsonResponse(data, safe=False)


def api_registers(request):
    data = list(Rejestracja.objects.values())
    return JsonResponse(data, safe=False)


def api_register_detail(request, register_id):
    rejestracja = get_object_or_404(Rejestracja, id=register_id)

    data = {
        'id': rejestracja.id,
        'imie': rejestracja.imie,
        'nazwisko': rejestracja.nazwisko,
        'telefon': rejestracja.telefon,
        'email': rejestracja.email,
        'status': rejestracja.status,
        'szkolenie': rejestracja.szkolenie.tytul,
    }

    return JsonResponse(data)
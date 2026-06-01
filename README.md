# System szkoleń - Django

Projekt wykonany w ramach laboratorium z przedmiotu Nowoczesne Aplikacje Internetowe.

Aplikacja została przygotowana we frameworku Django i realizuje prosty system zarządzania ofertą szkoleń.

## Funkcjonalności projektu

Projekt zawiera:

- aplikację publiczną z listą kategorii i szkoleń,
- panel zarządzania ofertą,
- modele danych dla kategorii, szkoleń oraz rejestracji,
- formularze dodawania kategorii i szkoleń,
- panel administracyjny Django,
- endpointy API zwracające dane w formacie JSON.

## Wymagania

Do uruchomienia projektu potrzebne są:

- Python 3,
- Django,
- przeglądarka internetowa.

## Instalacja i uruchomienie projektu

### 1. Pobranie projektu

### 2. Utworzenie środowiska wirtualnego
python -m venv venv
### 3. Aktywacja środowiska wirtualnego

Windows:

venv\Scripts\activate
### 4. Instalacja Django
pip install django
### 5. Wykonanie migracji bazy danych
python manage.py makemigrations
python manage.py migrate
### 6. Utworzenie konta administratora
python manage.py createsuperuser
### 7. Uruchomienie serwera
python manage.py runserver

Po uruchomieniu aplikacja będzie dostępna pod adresem:

http://127.0.0.1:8000/
Najważniejsze adresy aplikacji

Strona główna:

http://127.0.0.1:8000/

Aplikacja publiczna - lista kategorii:

http://127.0.0.1:8000/offer/

Panel zarządzania ofertą:

http://127.0.0.1:8000/offer-mng/

Lista kategorii:

http://127.0.0.1:8000/offer-mng/categ-lst/

Lista szkoleń:

http://127.0.0.1:8000/offer-mng/course-lst/

Formularz dodawania kategorii:

http://127.0.0.1:8000/offer-mng/categ-add/

Formularz dodawania szkolenia:

http://127.0.0.1:8000/offer-mng/course-add/

Panel administracyjny Django:

http://127.0.0.1:8000/admin/
Endpointy API

Lista kategorii:

http://127.0.0.1:8000/api/categories/

Lista szkoleń:

http://127.0.0.1:8000/api/courses/

Lista rejestracji:

http://127.0.0.1:8000/api/registers/

Pojedyncza rejestracja:

http://127.0.0.1:8000/api/register/1/
Modele danych

W projekcie przygotowano następujące modele:

Kategoria

Model przechowuje informacje o kategoriach szkoleń, takie jak nazwa, kolejność, status publikacji oraz kategoria nadrzędna.

Szkolenie

Model przechowuje informacje o szkoleniach, takie jak tytuł, opis, cena, liczba godzin, numer, kolejność, status publikacji oraz przypisana kategoria.

Rejestracja

Model przechowuje dane osoby zapisującej się na szkolenie, takie jak imię, nazwisko, telefon, email, zgoda RODO, status oraz data rejestracji.
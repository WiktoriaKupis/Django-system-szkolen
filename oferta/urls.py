from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('offer/', views.offer, name='offer'),
    path('offer/<int:kategoria_id>/', views.offer_category, name='offer_category'),
    path('offer/<int:kategoria_id>/course/<int:course_id>/', views.course_detail, name='course_detail'),

    path('offer-mng/', views.offer_mng, name='offer_mng'),
    path('offer-mng/categ-lst/', views.categ_lst, name='categ_lst'),
    path('offer-mng/course-lst/', views.course_lst, name='course_lst'),
    path('offer-mng/categ-add/', views.categ_add, name='categ_add'),
    path('offer-mng/course-add/', views.course_add, name='course_add'),

    path('register/<int:course_id>/', views.register, name='register'),

    path('api/categories/', views.api_categories, name='api_categories'),
    path('api/courses/', views.api_courses, name='api_courses'),
    path('api/registers/', views.api_registers, name='api_registers'),
    path('api/register/<int:register_id>/', views.api_register_detail, name='api_register_detail'),
]
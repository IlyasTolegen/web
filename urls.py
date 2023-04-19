from django.urls import path
from .views import CompanyList, CompanyDetail, CompanyVacanciesList, VacancyList, VacancyDetail, TopTenVacanciesList

urlpatterns = [
    path('api/companies/', CompanyList.as_view(), name='company-list'),
    path('api/companies/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
    path('api/companies/<int:id>/vacancies/', CompanyVacanciesList.as_view(), name='company-vacancies'),
    path('api/vacancies/', VacancyList.as_view(), name='vacancy-list'),
]

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status

from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer
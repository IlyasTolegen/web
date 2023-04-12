from django.urls import path
from api.views import CompanyList, CompanyDetail, CompanyVacanciesList, VacancyList, VacancyDetail, TopTenVacanciesList

urlpatterns = [
    path('api/companies/', CompanyList.as_view(), name='company-list'),
    path('api/companies/<int:pk>/', CompanyDetail.as_view(),

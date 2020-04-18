from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import CompanySerializer, VacancySerializer
from api.models import Company, Vacancy


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated, )


class CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)


class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticated,)


class VacancyDetailAPIView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticated,)


class VacanciesByCompanyAPIView(generics.ListAPIView):
    def get_queryset(self):
        return Vacancy.objects.filter(company=self.kwargs.get('pk'))

    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticated,)


class TopTenVacanciesAPIView(generics.ListAPIView):
    def get_queryset(self):
        return Vacancy.objects.order_by('-salary')[:10]

    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticated,)
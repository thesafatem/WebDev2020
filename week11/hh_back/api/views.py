from django.db.models.functions import Coalesce
from django.http.response import JsonResponse
from api.models import Company, Vacancy


def company_list(request):
    companies = Company.objects.all()
    companies_json = [c.to_json() for c in companies]
    return JsonResponse(companies_json, safe=False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company.to_json(), safe=False)


def vacancies_by_company(request, company_id):
    vacancies = Vacancy.objects.filter(company=company_id)
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy.to_json(), safe=False)


def vacancy_top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')
    vacancies_top_ten = vacancies[:min(len(vacancies), 10)]
    vacancies_top_ten_json = [v.to_json() for v in vacancies_top_ten]
    return JsonResponse(vacancies_top_ten_json, safe=False)

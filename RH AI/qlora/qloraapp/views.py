from django.shortcuts import render

def index(request):
    return render(request, 'qloraapp/index.html')

def collect_jobs(request):
    return render(request, 'qloraapp/jobs.html')

def analyze_vacancies(request):
    return render(request, 'qloraapp/vacancies.html')

def analyze_project_data(request):
    return render(request, 'qloraapp/project_data.html')

def matrices_and_statistics(request):
    return render(request, 'qloraapp/statistics.html')
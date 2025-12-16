from django.shortcuts import render, redirect


def index(request):
    if request.method == "POST":
        for name in ("openai_key", "job_board_key", "analytics_key"):
            val = request.POST.get(name, "").strip()
            if val:
                request.session[name] = val
        print("openai_key:", request.session.get("openai_key"))
        print("job_board_key:", request.session.get("job_board_key"))
        print("analytics_key:", request.session.get("analytics_key"))
        request.session.modified = True
        return redirect(request.path)

    return render(request, 'qloraapp/index.html')

def collect_jobs(request):
    return render(request, 'qloraapp/jobs.html')

def analyze_vacancies(request):
    return render(request, 'qloraapp/vacancies.html')

def analyze_project_data(request):
    return render(request, 'qloraapp/project_data.html')

def matrices_and_statistics(request):
    return render(request, 'qloraapp/statistics.html')
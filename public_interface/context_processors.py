from datetime import datetime
from company.models import Blog


def company_total_year(request):
    years_elapsed = datetime.now().year - 1986
    return {"years_elapsed": years_elapsed}


def blogs(request):
    return {"all_blogs": Blog.objects.filter(status=True)}

from datetime import datetime


def company_total_year(request):
    years_elapsed = datetime.now().year - 1986
    return {"years_elapsed": years_elapsed}

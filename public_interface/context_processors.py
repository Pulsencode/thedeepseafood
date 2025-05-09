from datetime import datetime
from company.models import Blog, SEO


def global_context(request):
    years_elapsed = datetime.now().year - 1986
    return {
        "years_elapsed": years_elapsed,
        "all_blogs": Blog.objects.filter(status=True),
        "seo": SEO.objects.filter(page_name=request.path, status=True).first(),
    }

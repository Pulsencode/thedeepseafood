from django.shortcuts import render


def renderhelper(request, folder, htmlpage, context=None):
    if context is None:
        context = {}
    return render(request, f"superadmin/{folder}/{htmlpage}.html", context)


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"

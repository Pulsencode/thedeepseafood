"""for search filter & status filter to avoid Code repetition"""

from django.shortcuts import get_object_or_404, redirect

from django.contrib import messages


class SearchAndStatusFilterMixin:
    search_field = None  # Default search field, can override
    status_field = "status"  # Default status field

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        status_filter = self.request.GET.get("status_filter")

        if search: 
            queryset = queryset.filter(**{f"{self.search_field}__icontains": search})
            """**{ ... } → this unpacks the dictionary into keyword arguments when calling .filter"""

        if status_filter == "False":
            queryset = queryset.filter(**{self.status_field: False})
        else:
            queryset = queryset.filter(**{self.status_field: True})

        return queryset


"""for updating status in  list used to avoid code repetition"""


class StatusUpdateMixin:
    model = None

    def post(self, request, *args, **kwargs):
        status_id = request.POST.get("status_id")
        homepage_id = request.POST.get("homepage_id")

        status_value = request.POST.get("status", "")
        homepage_value = request.POST.get("homepage", "")

        if status_id:
            status_instance = get_object_or_404(self.model, id=status_id)
            status_instance.status = status_value == "on"
            status_instance.save()
            messages.success(request, "Status updated successfully")


        if homepage_id:
            homepage_instance = get_object_or_404(self.model, id=homepage_id)
            homepage_instance.homepage = homepage_value == "on"
            homepage_instance.save()
            messages.success(request, "Homepage Status updated successfully")


        return redirect(self.request.path)



    

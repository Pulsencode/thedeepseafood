"""for search filter & status filter to avoid Code repetition"""

from django.shortcuts import get_object_or_404, redirect


class SearchStatusMixin:
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


class StatusMixin:
    model = None

    def post(self, request, *args, **kwargs):
        object_id = request.POST.get("object_id")
        obj = get_object_or_404(self.model, id=object_id)
        status_value = request.POST.get("status", "")
        obj.status = status_value == "on"
        obj.save()
        return redirect(self.request.path)

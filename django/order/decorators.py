from django.http import HttpResponse


def allowed_user(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        return HttpResponse("You are not authorized to view this page")
    return wrapper_function

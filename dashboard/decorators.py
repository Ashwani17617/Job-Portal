from functools import wraps

from django.shortcuts import redirect


def role_required(required_role):

    def decorator(view_func):

        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if request.user.role != required_role:
                return redirect("login")

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
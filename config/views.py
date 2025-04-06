
from django.shortcuts import redirect
from django.utils.translation import activate


def set_language(request, language_code):
    activate(language_code)
    return redirect(request.GET.get('next', '/'))

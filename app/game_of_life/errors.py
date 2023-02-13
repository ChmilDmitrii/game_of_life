from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError


def errors_handler(func):
    def wrapper(request, *args, **kwargs):
        try:
            func_result = func(request, *args, **kwargs)
        except ObjectDoesNotExist as error:
            return render(request, 'errors.html', {'error': error})
        except ValidationError as error:
            return render(request, 'errors.html', {'error': error})
        return func_result
    return wrapper

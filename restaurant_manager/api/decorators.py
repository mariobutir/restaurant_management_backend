import functools

from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist
from django.core.paginator import EmptyPage
from django.db import transaction, DatabaseError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError


def _create_error_details(message):
    return {
        'error': message
    }


def _unauthorized_error():
    return Response(
        data=_create_error_details("Unauthorized."),
        status=status.HTTP_401_UNAUTHORIZED
    )


def _key_error(exception):
    return Response(
        data=_create_error_details(exception.args[0]),
        status=status.HTTP_404_NOT_FOUND
    )


def _validation_error(exception):
    return Response(
        data=_create_error_details(exception.get_full_details()),
        status=exception.status_code
    )


def _empty_page_error(exception):
    return Response(data=[], status=status.HTTP_200_OK)


def _object_does_not_exist_error(exception):
    return Response(
        data=_create_error_details(exception.args[0]),
        status=status.HTTP_404_NOT_FOUND
    )


def _field_does_not_exist_error(exception):
    return Response(
        data=_create_error_details(exception.args[0]),
        status=status.HTTP_400_BAD_REQUEST
    )


def _database_error(exception):
    return Response(
        data=_create_error_details(exception.args),
        status=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            # this is the function on which the decorator is used!
            response = func(request, *args, **kwargs)

        except KeyError as exception:
            return _key_error(exception)

        except ValidationError as exception:
            return _validation_error(exception)

        except EmptyPage as exception:
            return _empty_page_error(exception)

        except ObjectDoesNotExist as exception:
            return _object_does_not_exist_error(exception)

        except FieldDoesNotExist as exception:
            return _field_does_not_exist_error(exception)

        except DatabaseError as exception:
            return _database_error(exception)

        return response

    return wrapper


def use_transaction_atomic_and_handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            with transaction.atomic():
                # this is the function on which the decorator is used!
                response = func(request, *args, **kwargs)

        except KeyError as exception:
            return _key_error(exception)

        except ValidationError as exception:
            return _validation_error(exception)

        except EmptyPage as exception:
            return _empty_page_error(exception)

        except ObjectDoesNotExist as exception:
            return _object_does_not_exist_error(exception)

        except FieldDoesNotExist as exception:
            return _field_does_not_exist_error(exception)

        except DatabaseError as exception:
            return _database_error(exception)

        return response

    return wrapper


def allowed_users(allowed_roles):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            if request.request.user.groups.filter(name__in=allowed_roles).exists():
                return func(request, *args, **kwargs)
            else:
                return _unauthorized_error()

        return wrapper

    return decorator

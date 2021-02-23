from config.exceptions import InvalidEntityException, EntityDoesNotExistException, ConflictException, \
        ApiException, NoLoggedException, NoPermissionException
from config.serializers import ApiExceptionSerializer

exception_status_code_mapper = {
        InvalidEntityException: 422,
        EntityDoesNotExistException: 404,
        ConflictException: 409,
        NoLoggedException: 401,
        NoPermissionException: 403,
        }


def serialize_exceptions(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ApiException as e:
            body = ApiExceptionSerializer.serialize(e)
            status = exception_status_code_mapper[type(e)]
        return body, status
    return func_wrapper

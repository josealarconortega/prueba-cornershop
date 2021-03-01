class ApiException(Exception):

    def __init__(self, source, code, message):
        super().__init__(message)
        self._source = source
        self._code = code

    @property
    def source(self):
        return self._source

    @property
    def code(self):
        return self._code


class InvalidEntityException(ApiException):
    pass


class ConflictException(ApiException):
    pass


class NoLoggedException(ApiException):

    def __init__(self):
        super().__init__(source='authentication', code='required', message='Authentication required')


class EntityDoesNotExistException(ApiException):

    def __init__(self):
        super().__init__(source='entity', code='not_found', message='Entity not found')


class NoPermissionException(ApiException):

    def __init__(self):
        super().__init__(source='permission', code='denied', message='Permission denied')

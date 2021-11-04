from rest_framework.exceptions import APIException
from rest_framework import status


class UserAlreadyExistsError(APIException):
    # 409 is the most appropriate status code for this case
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Utilisateur existe déjà'
    default_code = 'UserExists'

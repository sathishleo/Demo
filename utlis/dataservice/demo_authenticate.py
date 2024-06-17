import rest_framework
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from rest_framework import authentication, exceptions
from rest_framework.authtoken.models import Token
from knox.auth import AuthToken,TokenAuthentication

# from userservice.models import Employee


class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = None
        user = None
        try:
            token = request.META['HTTP_AUTHORIZATION']
            token_arr = token.split()
            if not token_arr[0] == 'Token':
                raise exceptions.AuthenticationFailed(('No credentials provided.'))
            token = token_arr[1]
            print(token)

        except KeyError:
            try:
                token = request.META['HTTP_AUTHORIZATION']
                token_arr = token.split()
                if not token_arr[0] == 'Token':
                    raise exceptions.AuthenticationFailed(('No credentials provided.'))
                token = token_arr[1]
                tok = TokenAuthentication()
                token.encode("utf-8")
                tstr = token.encode("utf-8")
                token_obj = tok.authenticate_credentials(tstr)
                user = token_obj[0]
            except rest_framework.authtoken.models.Token.DoesNotExist:
                raise exceptions.AuthenticationFailed(('Invalid token.'))
            except:
                user = None

        if token is not None:
            print(token)
            tok = TokenAuthentication()
            token.encode("utf-8")
            tstr = token.encode("utf-8")
            token_obj = tok.authenticate_credentials(tstr)
            user = token_obj[0]

        else:
            user = None

        if user is None:
            token = request.GET.get('token', None)
            if token is not  None :
                tok = TokenAuthentication()
                token.encode("utf-8")
                tstr = token.encode("utf-8")
                token_obj = tok.authenticate_credentials(tstr)
                user = token_obj[0]

        return (user, None)
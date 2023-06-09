from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_framework.authtoken.models import Token
import datetime
class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'

    
    
    
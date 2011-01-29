# -*- mode: python; coding: utf-8; -*-
#from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class EmailModelBackend(ModelBackend):
    '''
      This is used so I can login using email instead of username. 
      This is used in conjunctions with changes in django-registration
      to change the login form to pass email
    '''
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email__exact=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
                return None

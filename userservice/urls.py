from django.urls import path
from usermodule.controller import devicecontroller, checksheet_controller, Maintaince_controller
from userservice.controller import auth_controller
# import usermodule.controller



urlpatterns=[
 path('signup', auth_controller.signup, name='signup'),
 path('auth_token', auth_controller.auth_token, name='auth_token'),
]
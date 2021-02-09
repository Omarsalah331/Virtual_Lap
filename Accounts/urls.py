from django.urls import path
from Accounts import views

app_name= 'Accounts'
urlpatterns=[
    path('signup/',views.register_view,name='signup'),
]

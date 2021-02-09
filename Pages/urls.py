from django.urls import path
from Pages import views

app_name= 'Pages'
urlpatterns=[
    path('',views.home_view,name='home'),
    path('blogs/',views.blog_view,name='blogs'),
    path('about/',views.about_view,name='about'),
    path('Virtual/',views.labs_view,name='virtual'),
    path('support/',views.support_view,name='support'),
]

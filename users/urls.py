from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^list', views.UserView.as_view(), name='user_list'),
]

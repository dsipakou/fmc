from django.conf.urls import url

from images import views

urlpatterns = [
    url(r'^images/?$', views.ImageView.as_view(), name='image_list')
]
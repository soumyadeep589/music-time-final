from django.urls import path

from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('add_post', views.add_post, name="add_post"),
    path('user/<username>', views.user, name="user"),
    path('follow/<username>', views.follow, name="follow"),
    path('unfollow/<username>', views.unfollow, name="unfollow"),
    path('followers/<username>', views.followers, name="followers"),
    path('studios', views.studios, name="studios"),
    path('addstudio', views.addstudio, name="addstudio"),
    path('studiodetails/<id>', views.studiodetails, name="studiodetails"),
    path('sendmail/<username>', views.sendmail, name="sendmail"),
    path('successmail', views.successmail, name="successmail")
]


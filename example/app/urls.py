from django.urls import re_path
from django.contrib.auth import logout as logoutview
from django.urls import reverse_lazy

from .views import home_view
from stravauth.views import StravaAuth


urlpatterns = [
    re_path(r'^$', home_view, name="home"),
    re_path(r'^login', StravaAuth.as_view(url=reverse_lazy("home")), kwargs={"approval_prompt": "force"}, name="login"),
    re_path(r'^logout$', logoutview, kwargs={'next_page': '/'}, name="logout"),
]
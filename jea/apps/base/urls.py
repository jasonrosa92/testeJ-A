from django.urls import re_path
from jea.apps.base.views import IndexView

from jea.configs.settings import DEBUG

app_name = 'base'
urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
]
